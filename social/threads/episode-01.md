# Episode 1 — X thread (Qwen3 1.7B) — REAL RESULTS

> One idea per tweet. Screenshots where noted. No link until the final reply.

---

**1/**
The internet says my 6-year-old laptop is too weak for AI.

2019 ultrabook. 4GB GPU. The 2026 guides literally say this "runs small models poorly."

So I ran a tiny offline AI anyway — and asked it to teach me German.

As a native Persian speaker, I caught things an English reviewer never could 🧵

**2/**
Setup is one command, fully offline, nothing leaves my laptop:

`ollama pull qwen3:1.7b`

1.7 billion parameters. It ran at ~45 tokens/sec on my weak GPU — genuinely fast. So far, impressive.

Then I gave it 6 real tasks. [screenshot: terminal]

**3/**
Test 1 — Persian → German. ✅ mostly good.

It produced natural German... but quietly DROPPED the word "morning" from my sentence. Small meaning loss you'd never notice if you don't speak both languages. 4/5.

**4/**
Test 2 — German → Persian. ❌ this is where it fell apart.

The Persian was word-salad. Invented words, broken grammar, a hallucinated "hot day" that was never in the sentence.

A native speaker spots this instantly. An English reviewer would've called it "fine." 1/5. [screenshot]

**5/**
Test 3 — explain German grammar (der/die/das).

It sounded confident and helpful... and was WRONG. It claimed "Tisch" (table) is neuter. It's *der* Tisch — masculine.

Confidently wrong is the most dangerous kind of tutor. 2/5.

**6/**
Test 4 — fix my broken German sentence.

There were two real errors. It fixed NEITHER, then declared the sentence correct. 1/5.

A beginner would walk away more confused than before.

**7/**
Verdict on Qwen3 1.7B as an offline German tutor: ❌

Fast and fluent — but broken Persian, invented grammar, and it can't fix mistakes. Fluency ≠ correctness.

Next episode: Gemma 3 4B, the model the guides say is actually the best for weak GPUs. Follow to watch the leaderboard build 👇

---

**Final reply (with links):**

Everything is open & reproducible — same prompts, same weak laptop, run it yourself:

🔗 github.com/aghadavood/local-ai-tutor

Full video: [link]
