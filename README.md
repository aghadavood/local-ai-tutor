# 🧠 Local AI as an Offline German Tutor — the search for a brain that runs anywhere

**Which free, offline AI model can run a real German tutor — on a weak laptop, with no API, for people who can't get one?**

No cloud. No subscription. Nothing leaves the machine. If it runs on my laptop, it runs on yours.

---

## Why this exists

I built a working German tutor: a Telegram bot called **Herr Klaus** that teaches from a real B2 textbook, tracks progress, and drills my weak spots. → **[See the bot here](https://github.com/aghadavood/german-teacher-openclaw)**

It works — but it runs on a paid AI API. And that's the problem.

Many of my friends in Iran can't get an API key: sanctions, the dollar/payment barrier, and long stretches without stable internet. The people who'd benefit most from a free, private tutor are exactly the ones a cloud tool locks out. I keep getting messages asking how to get around it.

So this repo asks a concrete question: **which local model could replace the API brain in Herr Klaus** — running offline, free, on hardware people actually own?

## What makes this benchmark different

- **It's tied to a real product.** Every model is judged on whether it could *be* the tutor's offline engine — not abstract scores.
- **Multilingual-first.** Judged by a native Persian speaker who is also a real German learner. Persian quality is something English-only reviewers literally cannot assess.
- **Weak-hardware-first.** A 2019 ultrabook with 4GB VRAM — the machine the 2026 guides call "too weak."
- **Privacy-first.** Language mistakes, notes, personal context — none of it should need the cloud.

## The test machine

| Component | Spec |
|---|---|
| CPU | Intel i7-10510U (2019 ultrabook) |
| RAM | 16 GB |
| GPU | NVIDIA GTX 1650 Max-Q — **4 GB VRAM** |
| OS | Windows 11 |

## The bar a model must clear

To actually run Herr Klaus offline, a model has to: stay in character across a long stateful session, follow mode-switching commands, **read a ~15k-token German chapter file and teach from it**, correct German precisely, and explain in Persian without falling apart. That's a heavy ask for a small model — which is exactly what we're measuring.

## The leaderboard

Live scores across every episode: [`results/LEADERBOARD.md`](results/LEADERBOARD.md).

## Run the benchmark yourself

```bash
# 1. Install Ollama:  https://ollama.com
ollama pull qwen3:1.7b
cd benchmark
python benchmark.py --model qwen3:1.7b --label "Qwen3 1.7B"
# Open results.csv, watch each answer, fill in your own 1–5 scores
```

Details: [`benchmark/README.md`](benchmark/README.md).

## Repo structure

```
benchmark/   ← the benchmark script + how to run it
results/     ← CSV data + the running leaderboard
episodes/    ← per-episode notes & scripts
social/      ← X threads, video scripts, LinkedIn posts + playbook
docs/        ← series plan + the reusable evaluation prompt
assets/      ← thumbnails, leaderboard images
```

## Sister project

🔗 **[german-teacher-openclaw](https://github.com/aghadavood/german-teacher-openclaw)** — the actual Telegram tutor this benchmark is trying to set free from the API.

## Contributing

Got a weak laptop too? Run the benchmark and open a PR with your `results.csv` — let's map what *actually* runs on normal hardware, in every language.

## License

MIT — see [LICENSE](LICENSE).
