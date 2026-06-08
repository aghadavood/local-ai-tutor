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

## Output
Results append to `results.csv` (one growing file across all episodes). Columns:
- timing: `wall_seconds`, `time_to_first_token_s`, `tokens`, `tokens_per_sec`
- `answer` — the full model output
- `judge_note` — what to look for
- `your_score_1to5` — **you fill this in** after watching. The numbers can't judge Persian quality; only you can.

Move the finished CSV into `../results/` and update `../results/LEADERBOARD.md`.

## Make it yours
Open `benchmark.py` and edit the `TASKS` list — swap in your own real German sentences, your own Persian text, your own A2 mistakes. Keep them identical across models so the comparison stays fair.
