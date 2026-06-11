# 🏆 Leaderboard — Best Offline Persian→German Tutor

Scored on the test machine (i7-10510U · 16GB RAM · GTX 1650 4GB VRAM).
Scores are 1–5, judged natively. Speed is average tokens/sec across the tasks.
**Season complete — 6 models tested.**

| Rank | Model | Size | Speed (tok/s) | Translation | Grammar | Conversation | Overall | Verdict |
|---|---|---|---|---|---|---|---|---|
| 🥇 1 | Gemma 3 4B | 4B | ~14.5 | 5 | 4 | 4 | **4.0** | ✅ keep — WINNER |
| 2 | Phi-4-mini | 3.8B | ~8.7 | 2.5 | 4 | 3 | **3.0** | ⚠️ okay in a pinch |
| 3 | Mistral 7B Q4 | 7B | ~3.5 | 2.5 | 1 | 3 | **2.3** | ❌ skip (as tutor) |
| 4 | Llama 3.2 3B | 3B | ~12.1 | 2 | 2 | 4 | **2.1** | ❌ skip (as tutor) |
| 5 | Qwen3 1.7B | 1.7B | ~45 | 2.5 | 2 | 3 | **2.0** | ❌ skip (as tutor) |
| 6 | TinyLlama | 1.1B | ~35.7 | 1 | 1 | 1 | **1.0** | ❌ skip (as tutor) |

**Verdict key:** ✅ keep · ⚠️ okay in a pinch · ❌ skip

## 🏆 Winner: Gemma 3 4B
The only model that could actually run the tutor. On a laptop the 2026 guides said was too weak,
a mid-sized 4B model came out *trustworthy*: natural German, fluent Persian, correct grammar,
real vocabulary, and held character on the live-teaching job. Not the fastest, not the biggest —
the **sweet spot.** Bigger (Mistral) was slower and dumber; smaller (TinyLlama) was incoherent.
Gemma in the middle was the one that worked.

**The season's lesson:** on weak hardware, neither biggest nor fastest wins. The middle does.

---

### Gemma 3 4B — notes ✅ WINNER
Natural FA→DE, genuinely fluent DE→FA Persian where rivals produced word-salad, correct
der/die/das, kept character in the bakery roleplay, *die Geduld* right for صبر. Minor slips on
the correction explanation and chapter format. ~14.5 tok/s — slow but correct. The one keeper.

### Phi-4-mini — notes ⚠️
Smartest in English: best grammar (correctly called *der Tisch* masculine), best vocab. But DE→FA
came out a three-language salad (Persian + Indonesian + Russian), and on the real job it scripted
a fake student ("John Smith") and played both sides. Slow (~8.7 tok/s). Brilliant in English,
lost in the actual job.

### Mistral 7B Q4 — notes ❌
The biggest model — and it lost. Didn't fit the 4GB card, crawled at ~3.5 tok/s (chapter task:
75s to first token). Hallucinated a fake grammar rule ("consonant vs vowel sound"), and on
correction made the sentence *worse* ("gegangen"→"gegeben"). One bright spot: vocab. Proof that
bigger isn't better on weak hardware.

### Llama 3.2 3B — notes ❌
Answered a Persian translation request in **Thai** — wrong language entirely. Strong only on
roleplay (a 4). ~12 tok/s. Disqualifying for a Persian tutor.

### Qwen3 1.7B — notes ❌
Fast (~45 tok/s) but dangerous: word-salad Persian, confidently-wrong grammar (called *Tisch*
neuter), failed the correction, invented "der Sabr" for صبر. Not trustworthy.

### TinyLlama 1.1B — notes ❌ (lowest score)
The smallest and fastest (~35.7 tok/s) — and a clean sweep of 1s. Hallucinated "the towers of
Ankara" into a coffee sentence, produced word-salad Persian, invented a grammar rule, and on the
real job **leaked its own system prompt** instead of teaching. Fastest and least usable — the
proof that speed means nothing without quality.

> Season complete. Re-post the final table as an image on X — it's the thread people followed the series for.