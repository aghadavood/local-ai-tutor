# Reusable Evaluation Prompt

Paste this entire file into a fresh Claude chat for **every model** you test.
Swap the CSV at the bottom for that model's `results.csv`. It carries the full
story, hardware, scoring rules, and deliverables so each chat is consistent.

---

## ROLE
You are my content + evaluation partner for an ongoing open-source video/Twitter/LinkedIn series. Read this entire brief, then evaluate the CSV results I paste at the bottom and produce all the deliverables listed. Be honest and specific — failures are the point of this series, not something to soften.

## THE STORY BEHIND THIS EXPERIMENT (use for the intro/narrative every time)
I'm a native Persian (Farsi) speaker, learning German, living in Germany. I vibecode (light coding, not a hardcore engineer).

I already BUILT a working German tutor: a Telegram bot called "Herr Klaus" (using OpenClaw) that teaches from a real B2 textbook chapter by chapter, tracks my progress, corrects me in a fixed gentle format, and runs a 45-minute speaking drill. It's a stateful teacher with a curriculum and memory — not a generic chatbot. It currently runs on a PAID AI API.

That's the problem, and the real reason for this benchmark: many of my friends in Iran CAN'T get an API key — sanctions, the dollar/payment barrier, and long stretches with no stable internet. The people who'd benefit most from a free private tutor are locked out by a cloud-dependent tool. So I'm hunting for a LOCAL model that could run Herr Klaus OFFLINE, free, on a weak laptop.

The test machine (deliberately weak):
- CPU: Intel i7-10510U (2019 ultrabook chip) · RAM: 16 GB · GPU: GTX 1650 Max-Q, only 4 GB VRAM · OS: Windows 11
The 2026 guides literally say 4GB VRAM "runs small models poorly." That tension IS the show.

Core question:
**"Which free, offline model can run my German tutor — on a laptop with no real GPU, for people who can't get an API? No cloud, no subscription, nothing leaves the machine."**

Why this is unique (lean into it):
- Almost every local-AI benchmark online is English-only on a $3,000 GPU. Mine is multilingual-first, weak-hardware-first, and tied to a REAL product.
- I can NATIVELY judge Persian quality — English-only reviewers cannot. I FEEL German-learner pain because I live it.
- Privacy + access are real here, not theoretical. Local = it works for people the cloud leaves behind.

Framing note: lead with the tech and the universal idea (offline AI for real people on real hardware). Mention the Iran/sanctions reality as the human stakes, but don't make it the headline.

Two linked repos: the benchmark (this) and the bot (github.com/aghadavood/german-teacher-openclaw). A running leaderboard crowns the best offline model to run the tutor.

## THE 6 FIXED TASKS (identical for every model)
1. translation_fa_de — Persian→German. Judge: natural German AND full meaning preserved (watch dropped words)?
2. translation_de_fa — German→Persian. Judge: fluent Persian, or robotic/word-salad/hallucinated? (judged natively — watch invented words / broken conjugation.)
3. grammar — explain der/die/das to a beginner. Judge: CORRECT (not just fluent)? Check the example nouns' real genders. Confident-but-wrong is the worst outcome.
4. correction — fix "Ich habe gestern in die Schule gegangen und habe gesehen meine Freund" and explain. The two REAL errors: (a) auxiliary should be "bin" not "habe" (movement verb → sein), (b) word order should be "habe meinen Freund gesehen". Did it fix BOTH?
5. roleplay — A2 bakery conversation. Judge: natural beginner German, right difficulty, in character, doesn't answer for the customer.
6. vocab — German for Persian "صبر" (patience). Correct = "die Geduld". Judge: correct word + article + plural + a genuinely correct example. Watch transliteration hallucinations (e.g. inventing "der Sabr").

> KEY FUTURE TASK (the one that really matters): the tutor works by reading a ~15k-token German textbook *chapter file* and teaching from it while staying in the Herr Klaus persona and following commands. The ultimate test of any model is: can it read a chapter and teach from it without losing the thread, breaking character, or hallucinating content? When I add this task, weight it heavily — it's literally the job.

## SCORING
Score each task 1–5 (5 = a native speaker/real learner would be happy; 1 = wrong/unusable). Give an average and verdict:
- ✅ keep (avg ≳ 3.5) · ⚠️ okay in a pinch (≈ 2.5–3.5) · ❌ skip as a tutor (< 2.5)
Be specific about WHY — quote the model's actual output, name the exact error (wrong gender, invented word, missing word, bad word order).

## WHAT TO PRODUCE (in order, clearly sectioned)
1. Task-by-task evaluation — per task: verdict, specific error/win, 1–5 score. End with average + ✅/⚠️/❌.
2. Updated leaderboard row — a markdown row to paste into results/LEADERBOARD.md:
   `| [model] | [size] | [avg tok/s] | [translation] | [grammar] | [conversation] | [overall] | [verdict] |`
   Restate the full current leaderboard if I paste previous rows below.
3. Hook tweets — 5–7 standalone hooks about THIS model. Punchy, specific, no links. At least one centers the most shareable failure. First line stops the scroll.
4. Full video transcript/script — word-for-word, on camera: cold-open hook (10s); the story intro written fresh; the 6 tasks with live reactions; on-screen cues in [brackets]; verdict + cliffhanger to next model. Natural, spoken, first-person, ~4–7 min.
5. Viral LinkedIn post — longer, professional but personal. Lead with the story, make it about the big idea (local AI for real people on real hardware, not GPU-rich English speakers), use results as proof, end with takeaway + soft CTA. Line breaks for readability, 3–5 hashtags max.

## TONE
Honest, specific, a little contrarian, warm. Never hype. Failures are content. A non-expert immigrant learner gets it; a developer respects it.

## THE DATA
Here are the CSV results for this model. Evaluate and produce everything above:

[PASTE YOUR results.csv CONTENT HERE]
