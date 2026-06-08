# Episode 1 — X thread

> Draft. One idea per tweet. Screenshots where noted. No link until the final reply.

---

**1/**
The internet says my laptop is too weak to run AI.

2019 ultrabook. 4GB GPU. The 2026 guides literally say this "runs small models poorly."

So I ran the smallest decent model anyway — and tested if it can teach me German.

Here's what happened 🧵

**2/**
The setup is one command. That's the whole install:

`ollama pull qwen3:1.7b`

1.7 billion parameters. Tiny. Runs fully offline. Nothing I type ever leaves the laptop — which matters when you're sharing your bad German and personal notes.

[screenshot: terminal pull]

**3/**
Test 1 — Persian → German translation.

I gave it an everyday Persian sentence. As a native speaker I can tell instantly if the German is natural or robotic.

Result: [your verdict + screenshot]

**4/**
Test 2 — the grammar tutor.

"Explain der/die/das to a beginner." This is where most tools either oversimplify or confuse you.

[your verdict + screenshot]

**5/**
Test 3 — correct my broken German.

I fed it a sentence with two classic learner mistakes. Did a 1.7B model catch both?

[your verdict + screenshot]

**6/**
Speed on a 4GB GPU: [X tokens/sec].

For a model this small on hardware this old — [honest take: usable? painful?].

**7/**
Verdict on Qwen3 1.7B as an offline German tutor: [✅/⚠️/❌]

Next episode I test Gemma 3 4B — the one the guides say is actually the best pick for weak GPUs. Follow so you don't miss the leaderboard building up.

---

**Final reply (with link):**

Same prompts, same weak laptop — run the exact test yourself:

🔗 [your GitHub repo link]
