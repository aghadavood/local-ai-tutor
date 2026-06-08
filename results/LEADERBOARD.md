# 🏆 Leaderboard — Best Offline Persian→German Tutor

Scored on the test machine (i7-10510U · 16GB RAM · GTX 1650 4GB VRAM).
Scores are 1–5, judged natively. Speed is average tokens/sec across the 6 tasks.

| Rank | Model | Size | Speed (tok/s) | Translation | Grammar | Conversation | Overall | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Qwen3 1.7B | 1.7B | ~45 | 2.5 | 2 | 3 | **2.0** | ❌ skip (as tutor) |
| — | _Gemma 3 4B_ | 4B | _tbd_ | _tbd_ | _tbd_ | _tbd_ | _tbd_ | ⏳ ep.2 |
| — | _Llama 3.2 3B_ | 3B | _tbd_ | _tbd_ | _tbd_ | _tbd_ | _tbd_ | ⏳ ep.3 |
| — | _Phi-4-mini_ | 3.8B | _tbd_ | _tbd_ | _tbd_ | _tbd_ | _tbd_ | ⏳ ep.4 |
| — | _Mistral 7B Q4_ | 7B | _tbd_ | _tbd_ | _tbd_ | _tbd_ | _tbd_ | ⏳ ep.5 |
| — | _TinyLlama_ | 1.1B | _tbd_ | _tbd_ | _tbd_ | _tbd_ | _tbd_ | ⏳ ep.6 |

**Verdict key:** ✅ keep · ⚠️ okay in a pinch · ❌ skip · ⏳ not tested yet

### Qwen3 1.7B — notes
Surprisingly competent at *producing* German, but a dangerous tutor: broken/hallucinated
Persian (DE->FA was word-salad), confidently-wrong grammar (claimed *Tisch* is neuter — it's
*der Tisch*), failed the correction task (missed both "bin" and word-order fixes), and invented
"der Sabr" for صبر instead of the correct *die Geduld*. Fast (~45 tok/s) but not trustworthy for learning.

> Update this after each episode. Re-post the table as an image on X — it's the thread people follow the series for.
