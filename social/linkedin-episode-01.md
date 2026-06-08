# Episode 1 — LinkedIn Post (Qwen3 1.7B)

> Professional but personal. Line breaks kept for readability. Adapt the voice to yours.

---

Everyone says you need an expensive GPU and a cloud subscription to use AI.

I decided to test that — on a 6-year-old laptop with a 4GB graphics card. The kind of machine most people in the world actually own.

Some context: I'm a native Persian speaker. I moved to Germany, and I'm learning German the hard way — every single day.

So I asked a simple question:

Can free AI, running 100% offline on a weak laptop, actually teach me a language? No ChatGPT. No subscription. No internet. Nothing I type ever leaves my machine.

That last part matters more than people admit. When you're learning, you type your mistakes, your notes, sometimes personal things. Not everyone is comfortable sending that to a server in another country.

Here's what makes this experiment different from every "best local AI" article online:

Those are written in English, tested on $3,000 GPUs.

Mine is Persian and German, on a laptop the guides literally call "too weak."

And because Persian is my mother tongue, I can catch errors a native English reviewer simply cannot see.

The first model I tested — Qwen3, 1.7 billion parameters — was a perfect example.

It was fast. It produced fluent-looking German. On the surface, impressive.

But:

→ Its Persian translation was word-salad — it even invented phrases that were never in the original. An English reviewer would have scored it "fine."

→ It explained German grammar confidently... and incorrectly, teaching the wrong gender for a basic noun.

→ Asked to fix a sentence with two clear mistakes, it fixed neither — then declared it correct.

The lesson isn't "this model is bad."

The lesson is: fluency is not correctness. A tool that is confidently wrong is more dangerous than one that admits it doesn't know — especially for a beginner who can't tell the difference yet.

This is episode one of an open, reproducible series. Same tests, same weak laptop, every model. A public leaderboard. All of it on GitHub so anyone can rerun it — in any language, on any old machine.

Because local AI shouldn't only work for English speakers with expensive hardware.

If you're learning a language, building on a budget, or you just care about AI that respects your privacy — follow along. The failures are the most interesting part.

🔗 github.com/aghadavood/local-ai-tutor

#LocalAI #LanguageLearning #BuildInPublic #Privacy #AI
