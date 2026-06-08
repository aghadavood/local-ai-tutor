# Episode 1 — "The guides say my laptop can't do this"

**Model tested:** Qwen3 1.7B
**Status:** ⏳ not recorded yet

## Goal
Set up the whole series: show the machine, install Ollama, run the smallest model, establish the leaderboard. The hook is the tension — the 2026 guides say 4GB VRAM is too weak, so let's find out.

## Setup shown on screen
```bash
ollama pull qwen3:1.7b
cd benchmark
python benchmark.py --model qwen3:1.7b --label "Qwen3 1.7B"
```

## The 6 tasks (same every episode)
1. Translate FA→DE — judge German naturalness
2. Translate DE→FA — judge Persian fluency
3. Grammar tutor — der/die/das explanation
4. Correct my German — fix + explain
5. Conversation practice — bakery roleplay
6. Vocab + example

## My scores (fill in after recording)
| Task | Speed (tok/s) | Score 1–5 | Notes |
|---|---|---|---|
| translation_fa_de | | | |
| translation_de_fa | | | |
| grammar | | | |
| correction | | | |
| roleplay | | | |
| vocab | | | |

## Verdict
_tbd_ — ✅ / ⚠️ / ❌

## Links
- Video: _tbd_
- Companion X thread: ../social/threads/episode-01.md
