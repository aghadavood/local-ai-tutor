#!/usr/bin/env python3
"""
local_ai_benchmark.py
---------------------
A dead-simple benchmark runner for your Persian <-> German local-AI series.

What it does:
  - Sends a fixed set of test prompts to a local Ollama model
  - Measures real timing: time-to-first-token and tokens/second
  - Logs every answer + the numbers to a CSV you can use on screen / in a leaderboard
  - Works fully offline once the model is pulled (the whole point of the series)

Requirements:
  - Ollama installed and running (https://ollama.com) -- `ollama serve` in the background
  - The model already pulled, e.g.:  ollama pull qwen3:1.7b
  - Python 3.8+  (no pip installs needed -- uses only the standard library)

Usage:
  python local_ai_benchmark.py --model qwen3:1.7b
  python local_ai_benchmark.py --model gemma3:4b --label "Gemma 3 4B"
  python local_ai_benchmark.py --model llama3.2:3b --tasks translation,grammar

Then open results.csv. Each run appends rows, so you build one growing
leaderboard file across every episode.
"""

import argparse
import csv
import json
import os
import sys
import time
import urllib.request
import urllib.error

OLLAMA_URL = "http://localhost:11434/api/generate"
RESULTS_FILE = "results.csv"

# ---------------------------------------------------------------------------
# THE TEST SUITE
# Each task = one comparable, repeatable test every model takes identically.
# Edit freely: add your own real German sentences, your own Persian text, etc.
# The "id" is what you pass to --tasks to run a subset.
# ---------------------------------------------------------------------------
TASKS = [
    {
        "id": "translation_fa_de",
        "category": "Translation FA->DE",
        "prompt": "Translate this Persian sentence into natural, correct German. "
                  "Give ONLY the German translation, nothing else:\n\n"
                  "من هر روز صبح قبل از کار قهوه می‌خورم و کمی آلمانی تمرین می‌کنم.",
        "judge_note": "Native check: is the German natural? Is the meaning fully preserved?",
    },
    {
        "id": "translation_de_fa",
        "category": "Translation DE->FA",
        "prompt": "Translate this German sentence into natural, correct Persian. "
                  "Give ONLY the Persian translation, nothing else:\n\n"
                  "Ich muss morgen früh zum Bürgeramt, weil ich meine Adresse ummelden möchte.",
        "judge_note": "Native check: is the Persian fluent or robotic/word-salad?",
    },
    {
        "id": "grammar",
        "category": "Grammar tutor",
        "prompt": "I am an A2-level German learner whose native language is Persian. "
                  "Explain simply, in English, when to use 'der', 'die', and 'das', "
                  "and give one memory trick. Keep it under 120 words.",
        "judge_note": "Is the explanation correct AND actually helpful to a beginner?",
    },
    {
        "id": "correction",
        "category": "Correct my German",
        "prompt": "I am learning German. Correct the following sentence, then explain "
                  "the mistakes briefly in English:\n\n"
                  "'Ich habe gestern in die Schule gegangen und habe gesehen meine Freund.'",
        "judge_note": "Did it fix BOTH errors (auxiliary 'bin', word order) correctly?",
    },
    {
        "id": "roleplay",
        "category": "Conversation practice",
        "prompt": "Let's roleplay in simple German (A2 level). You are a baker at a German "
                  "Bäckerei. I am a customer. Start by greeting me and asking what I want. "
                  "Keep your reply to 2 short sentences.",
        "judge_note": "Natural beginner German? Right difficulty? Does it stay in character?",
    },
    {
        "id": "vocab",
        "category": "Vocab + example",
        "prompt": "Give me the German word for the Persian 'صبر' (patience), its article, "
                  "plural if any, and one simple example sentence with English translation.",
        "judge_note": "Correct article/word? Is the example sentence actually correct German?",
    },
]


def list_task_ids():
    return [t["id"] for t in TASKS]


def call_ollama(model, prompt, timeout=300):
    """Call the local Ollama generate endpoint (non-streaming) and return timing + text."""
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}
    )

    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        return {"error": f"Could not reach Ollama at {OLLAMA_URL}. Is it running? ({e})"}
    elapsed = time.time() - start

    # Ollama returns nanosecond timing fields when available.
    eval_count = data.get("eval_count")          # tokens generated
    eval_duration = data.get("eval_duration")    # ns spent generating
    prompt_eval_duration = data.get("prompt_eval_duration")  # ns spent on prompt

    tok_per_sec = None
    if eval_count and eval_duration:
        tok_per_sec = eval_count / (eval_duration / 1e9)

    ttft = None
    if prompt_eval_duration is not None:
        ttft = prompt_eval_duration / 1e9

    return {
        "text": data.get("response", "").strip(),
        "wall_seconds": round(elapsed, 2),
        "tokens": eval_count,
        "tokens_per_sec": round(tok_per_sec, 2) if tok_per_sec else None,
        "time_to_first_token_s": round(ttft, 2) if ttft else None,
    }


def run(model, label, task_ids):
    selected = [t for t in TASKS if not task_ids or t["id"] in task_ids]
    if not selected:
        print(f"No matching tasks. Available: {', '.join(list_task_ids())}")
        sys.exit(1)

    print(f"\n=== Benchmarking: {label or model} ===")
    print(f"Running {len(selected)} task(s). Make sure Ollama is running and the model is pulled.\n")

    new_file = not os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow([
                "model_label", "model_id", "task_id", "category",
                "wall_seconds", "time_to_first_token_s", "tokens", "tokens_per_sec",
                "answer", "judge_note", "your_score_1to5"
            ])

        for t in selected:
            print(f"--- {t['category']} ({t['id']}) ---")
            result = call_ollama(model, t["prompt"])
            if "error" in result:
                print("  ERROR:", result["error"])
                sys.exit(1)

            print(f"  speed: {result['tokens_per_sec']} tok/s | "
                  f"first token: {result['time_to_first_token_s']}s | "
                  f"wall: {result['wall_seconds']}s")
            preview = result["text"].replace("\n", " ")
            print(f"  answer: {preview[:160]}{'...' if len(preview) > 160 else ''}")
            print(f"  >> JUDGE: {t['judge_note']}\n")

            writer.writerow([
                label or model, model, t["id"], t["category"],
                result["wall_seconds"], result["time_to_first_token_s"],
                result["tokens"], result["tokens_per_sec"],
                result["text"], t["judge_note"], ""  # you fill score in after watching
            ])

    print(f"Done. Results appended to {RESULTS_FILE}")
    print("Open it, watch each answer, and fill in 'your_score_1to5' yourself.")
    print("That human column is your show -- the numbers can't judge Persian quality, only you can.\n")


def main():
    p = argparse.ArgumentParser(description="Benchmark local Ollama models for the FA<->DE series.")
    p.add_argument("--model", required=True, help="Ollama model id, e.g. qwen3:1.7b")
    p.add_argument("--label", default="", help="Friendly name for the leaderboard, e.g. 'Qwen3 1.7B'")
    p.add_argument("--tasks", default="", help="Comma-separated task ids to run a subset. "
                                               f"Available: {', '.join(list_task_ids())}")
    args = p.parse_args()
    task_ids = [x.strip() for x in args.tasks.split(",") if x.strip()]
    run(args.model, args.label, task_ids)


if __name__ == "__main__":
    main()
