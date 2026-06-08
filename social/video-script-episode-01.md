# Episode 1 — Video Script (Qwen3 1.7B)

> Word-for-word, first person, ~5 min speaking. On-screen cues in [brackets].

---

**[COLD OPEN — 0:00–0:10]**
"This laptop is six years old. It has a 4-gigabyte graphics card. Every guide online says it's too weak to run AI. So I made it teach me German — and what it got wrong is kind of incredible."

[on-screen: ❌ "TISCH IS NEUTER" — big red X over the wrong answer]

**[STORY INTRO — 0:10–0:50]**
"Quick context, because it matters for this whole series. I'm from Iran — Persian is my first language. I moved to Germany, and I'm learning German the hard way, every day. And I'm a little obsessed with one question:

Can free AI that runs *completely offline*, on a cheap laptop with no real GPU, actually help someone like me learn a language? No ChatGPT. No subscription. No internet. Nothing I type ever leaves this machine — which honestly matters, because when you're learning, you're typing your dumb mistakes, your personal notes, sometimes private stuff. I don't want that in someone's cloud.

Here's the part nobody else is doing: almost every AI benchmark online is in English, run on a three-thousand-dollar graphics card. Mine is the opposite — Persian and German, on a weak laptop. And because Persian is my mother tongue, I can catch errors a native English reviewer literally cannot see. Let me show you."

**[THE MACHINE — 0:50–1:05]**
[on-screen: Windows 'About' panel — specs highlighted]
"This is the machine. Intel i7 from 2019. 16 gigs of RAM. A GTX 1650 with 4GB of VRAM. The guides say this 'runs small models poorly.' Let's find out."

**[SETUP — 1:05–1:30]**
[screen recording: terminal]
"The whole setup is one line. `ollama pull qwen3:1.7b`. That's a model with 1.7 billion parameters — tiny by today's standards. It downloads once, then runs offline forever. I run my benchmark — same six tasks every model in this series will face — and the first surprise: it's fast. About 45 tokens a second on this old GPU. Okay. Promising. Then I read what it actually said."

**[TASK 1 — Translation FA→DE — 1:30–2:00]**
[on-screen: the German output]
"First, translate a Persian sentence into German. And... it's good. Natural German. A real person would say this. But — watch this — my sentence said I drink coffee every morning *before work*. It dropped 'morning' entirely. Small thing. But if you don't speak both languages, you'd never catch that the meaning quietly shifted. Four out of five."

**[TASK 2 — Translation DE→FA — 2:00–2:50]**
[on-screen: the broken Persian, with annotations]
"Now the reverse — German into Persian. This is where it falls apart. And this is the whole reason I'm making this series. To an English speaker, this Persian looks like Persian. It is not. It's word-salad. It invented a phrase about a 'hot day' that was never in the sentence. The verb conjugation isn't a real conjugation. It's confident, fluent-looking nonsense. As a native speaker, I can tell you a human would never write this. One out of five. An English-only reviewer would've scored this 'fine' and moved on."

**[TASK 3 — Grammar — 2:50–3:30]**
[on-screen: der/die/das, the wrong example circled]
"Test three: explain der, die, das to a beginner — the nightmare of German genders. And here's the most dangerous failure of the whole episode. It gives a confident, clear explanation... that's wrong. It says 'Tisch' — table — is neuter. It's not. It's *der* Tisch. Masculine. A beginner would memorize the wrong gender and trust it, *because it sounded so sure.* Confidently wrong is worse than 'I don't know.' Two out of five."

**[TASK 4 — Correction — 3:30–4:00]**
[on-screen: the broken sentence]
"Test four: I give it a German sentence with two real mistakes and ask it to fix them. It fixes neither — then tells me the sentence is now correct. For a learning tool, that's the worst possible outcome. You'd leave more confused than you started. One out of five."

**[TASKS 5 & 6 — quick — 4:00–4:25]**
"Quick on the last two: the bakery roleplay was actually okay — natural beginner German — except it answered *for* me, the customer, which is weird. Three out of five. And the vocab test: I asked for the German word for 'patience.' The answer is *die Geduld*. It invented a fake German word — 'der Sabr' — by just transliterating the Persian. One out of five."

**[VERDICT — 4:25–4:55]**
[on-screen: leaderboard, Qwen3 1.7B at ❌, average 2.0]
"So, verdict on Qwen3 1.7B as an offline German tutor: skip it. And here's the real lesson — it was fast, and it *sounded* fluent and confident the entire time. But fluency is not correctness. A tutor that's confidently wrong is more dangerous than no tutor at all. That's our baseline. Bottom of the leaderboard."

**[CLIFFHANGER — 4:55–5:05]**
"Next episode, I test Gemma 3 4B — the model the guides say is *actually* the right pick for a weak GPU like mine. Does bigger mean smarter? Subscribe, and let's build this leaderboard together. Everything's open on GitHub — same tests, same laptop — link below if you want to run it yourself."
