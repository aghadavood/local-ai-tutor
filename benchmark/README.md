# Benchmark

A single, dependency-free Python script that runs a fixed set of Persian↔German tasks against any local [Ollama](https://ollama.com) model, measures real timing, and logs everything to CSV.

## Requirements
- [Ollama](https://ollama.com) installed and running (`ollama serve`)
- The model pulled, e.g. `ollama pull qwen3:1.7b`
- Python 3.8+ (standard library only — no `pip install` needed)

## Usage

```bash
# Run all 6 tasks against a model
python benchmark.py --model qwen3:1.7b --label "Qwen3 1.7B"

# Run a subset of tasks
python benchmark.py --model gemma3:4b --label "Gemma 3 4B" --tasks translation_fa_de,grammar

# See all task ids
python benchmark.py --help
```

## The 6 tasks
| id | what it tests |
|---|---|
| `translation_fa_de` | Persian → German, judged for naturalness |
| `translation_de_fa` | German → Persian, judged for fluency |
| `grammar` | explaining der/die/das to a beginner |
| `correction` | fixing + explaining a broken German sentence |
| `roleplay` | A2-level bakery conversation |
| `vocab` | word + article + plural + example sentence |
| `teach_from_chapter` | **the real job** — load the Herr Klaus persona + a chapter file and start a lesson (see below) |

## The `teach_from_chapter` task — the real job
This is the test that actually matters: can the model *be* Herr Klaus? It loads the
bot's `SOUL.md` + a chapter file and asks the model to start a lesson. Judge whether it
stayed in German and in character, taught **from the chapter** (not improvised),
presented one step at a time, and didn't hallucinate content.

By default it reads the files from the bot repo cloned next to this one:
```
../../german-teacher-openclaw/agent-files/SOUL.md
../../german-teacher-openclaw/curriculum/kapitel-00-sample.md
```
If your paths differ, pass them explicitly:
```bash
python benchmark.py --model gemma3:4b --label "Gemma 3 4B" \
  --soul /path/to/SOUL.md --chapter /path/to/chapter.md
```
If the files aren't found, this one task is skipped with a message and the others still run.

> ⚠️ This is a **single-shot approximation**. It catches the worst failures (ignoring the
> chapter, breaking character, dumping everything at once). The TRUE test is a live
> multi-turn lesson with the model plugged into the bot .

## Output
Results append to `results.csv` (one growing file across all episodes). Columns:
- timing: `wall_seconds`, `time_to_first_token_s`, `tokens`, `tokens_per_sec`
- `answer` — the full model output
- `judge_note` — what to look for
- `your_score_1to5` — **you fill this in** after watching. The numbers can't judge Persian quality; only you can.

Move the finished CSV into `../results/` and update `../results/LEADERBOARD.md`.

## Make it yours
Open `benchmark.py` and edit the `TASKS` list — swap in your own real German sentences, your own Persian text, your own A2 mistakes. Keep them identical across models so the comparison stays fair.