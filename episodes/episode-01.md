# Episode 1 — "The guides say my laptop can't do this"

**Model tested:** Qwen3 1.7B
**Status:** ✅ recorded data in, scored

## Verdict: ❌ skip as a tutor (avg 2.0 / 5)
Fast (~45 tok/s) and fluent-looking, but broken Persian, confidently-wrong grammar,
and failed the correction task. Fluency ≠ correctness. This is the series baseline.

## My scores
| Task | Speed (tok/s) | Score | Note |
|---|---|---|---|
| translation_fa_de | 45.83 | 4 | natural German, dropped "morning" |
| translation_de_fa | 45.53 | 1 | broken Persian word-salad, hallucinated "hot day" |
| grammar | 46.83 | 2 | confident but wrong — said Tisch is neuter (it's der) |
| correction | 44.88 | 1 | missed both errors (bin, word order) |
| roleplay | 46.69 | 3 | natural but answered for the customer |
| vocab | 44.19 | 1 | invented "der Sabr"; correct is die Geduld |

## Deliverables
- Raw data: ../results/results_qwen3-1.7b.csv
- Video script: ../social/video-script-episode-01.md
- X thread: ../social/threads/episode-01.md
- LinkedIn: ../social/linkedin-episode-01.md
- Leaderboard: ../results/LEADERBOARD.md

## Links (fill after upload)
- Video: _tbd_
