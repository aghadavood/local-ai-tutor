# 🧠 Local AI as a Private Persian → German Tutor

**Can free, offline AI actually teach a Persian speaker German — on a laptop with no real GPU?**

No cloud. No subscriptions. Nothing leaves the machine. If it runs on my laptop, it runs on yours.

This repo is the open, reproducible home of the series: every model tested, every prompt used, every score recorded. Watch the videos, then run the exact same benchmark yourself.

---

## 🎯 Why this exists

Almost every local-AI benchmark online is English-only and run on a $3,000 GPU. This one is different:

- **Multilingual-first** — judged by a native Persian speaker who is also a real German learner.
- **Weak-hardware-first** — a 2019 ultrabook with a 4GB GPU. The machine most people actually own.
- **Privacy-first** — the whole point of local AI: your language mistakes, notes, and journal never touch a server.

## 💻 The test machine

| Component | Spec |
|---|---|
| CPU | Intel i7-10510U (2019 ultrabook) |
| RAM | 16 GB |
| GPU | NVIDIA GTX 1650 Max-Q — **4 GB VRAM** |
| OS | Windows 11, 64-bit |

The 2026 guides say 4GB VRAM "runs small models poorly." This series finds out what actually works anyway.

## 🏆 The leaderboard

Live scores across every episode live in [`results/LEADERBOARD.md`](results/LEADERBOARD.md).

## 🚀 Run the benchmark yourself

```bash
# 1. Install Ollama:  https://ollama.com
# 2. Pull a small model
ollama pull qwen3:1.7b

# 3. Run the benchmark
cd benchmark
python benchmark.py --model qwen3:1.7b --label "Qwen3 1.7B"

# 4. Open results.csv, watch each answer, fill in your own 1–5 scores
```

Full instructions: [`benchmark/README.md`](benchmark/README.md).

## 📺 The episodes

Each episode has notes, the models tested, and links in [`episodes/`](episodes/).
Companion X threads live in [`social/`](social/).

## 📂 Repo structure

```
local-ai-tutor/
├── README.md            ← you are here
├── benchmark/           ← the benchmark script + how to run it
├── results/            ← CSV data + the running leaderboard
├── episodes/           ← per-episode notes & scripts
├── social/             ← X threads + posting playbook
├── docs/               ← the full series plan
└── assets/             ← thumbnails, leaderboard images
```

## 🤝 Contributing

Got a weak laptop too? Run the benchmark and open a PR with your `results.csv` — let's map what *actually* runs on normal hardware, in every language.

## 📜 License

MIT — see [LICENSE](LICENSE). Use it, fork it, remix it.
