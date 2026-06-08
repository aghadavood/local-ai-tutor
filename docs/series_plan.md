# Local AI as a Private Persian→German Tutor — Series Plan

**The one-liner (your channel bio / pinned post):**
> Testing whether free, offline AI can actually teach a Persian speaker German — on a laptop with no real GPU. No cloud, no subscriptions, nothing leaves my machine. If it runs on my laptop, it runs on yours.

**Why this works:** you stack three under-served audiences — Persian speakers, immigrants learning a language, and the local-AI/privacy crowd — and you have judgment nobody else has: a native Persian ear + real German-learner pain. English captions = global reach.

**Your honest constraint, stated as the hook:** the 2026 guides literally say 4GB VRAM "runs small models poorly." Your show is: *let's find out what actually works anyway.* That tension is your thumbnail.

---

## Your hardware reality (state it on screen, episode 1)
- Intel i7-10510U (2019 ultrabook CPU, weak) · 16GB RAM · GTX 1650 Max-Q **4GB VRAM**
- 4GB VRAM is the real ceiling. Workable: 1B–4B models. 7B Q4 runs but crawls (great "struggle" content).

## Model lineup (all current as of 2026)
| Model | Size | Role in series |
|---|---|---|
| Qwen3 1.7B | tiny | The multilingual surprise — best small option for 100+ languages |
| Gemma 3 4B | small | Best pick for ≤6GB VRAM; likely your daily-driver winner |
| Llama 3.2 3B | small | The popular baseline everyone knows |
| Phi-4-mini 3.8B | small | The "viable on weak machines" contender |
| Mistral 7B Q4 | medium | The "watch my laptop suffer" episode |
| TinyLlama 1.1B | tiny | The "how bad can it get" comic-relief episode |

> Note: model rankings move fast. Re-check the Ollama library before each episode; swap in whatever's newest.

---

## Repeatable video structure (same every episode — this is what makes it bingeable)
1. **Cold open (10s):** the verdict teaser. "Can a 1.7B model survive ordering bread in German? Let's see."
2. **The machine (10s):** flash the specs. Reinforce the "weak laptop" identity every time.
3. **Setup (30s):** one command — `ollama pull <model>` — and how much it downloaded.
4. **The tests (core):** run the same 6 fixed tasks (below). Show the answer live.
5. **The native judgment:** *you* react to Persian/German quality. This is the irreplaceable part.
6. **The scoreboard:** speed + your 1–5 scores fill in the running leaderboard.
7. **Verdict + cliffhanger:** ✅/⚠️/❌ and tease the next model.

## The 6 fixed tasks (identical for every model = fair + comparable)
These match the benchmark script exactly, so your on-screen numbers come straight from `results.csv`:
1. **Translate FA→DE** — a real daily sentence. You judge German naturalness natively.
2. **Translate DE→FA** — a Bürgeramt sentence. You judge Persian fluency natively.
3. **Grammar tutor** — explain der/die/das to a beginner. Correct AND helpful?
4. **Correct my German** — fix a broken sentence + explain. Did it catch every error?
5. **Conversation practice** — roleplay at a bakery. Right difficulty, stays in character?
6. **Vocab + example** — word, article, plural, example sentence. Is the example actually correct?

---

## Episode list (Season 1)
1. **"The guides say my laptop can't do this."** — intro, specs, install Ollama, run the smallest model (Qwen3 1.7B). Set the leaderboard up.
2. **Gemma 3 4B** — the likely champion. Probably your "this is the one to actually use" episode.
3. **Llama 3.2 3B** — the famous baseline. Does fame = quality in Persian? (Often: no.)
4. **Phi-4-mini** — the efficiency contender.
5. **Mistral 7B Q4 — "I pushed my 4GB GPU too far."** The struggle episode; find the limit.
6. **TinyLlama — "the worst German tutor in the world."** Comedy + a real lesson on size.
7. **The RAG payoff: "I built a private offline tutor that only knows MY German textbook."** Feed it a grammar PDF / your notes; it answers only from that. Big build-in-public moment.
8. **Season finale: the leaderboard.** Crown the best offline Persian→German tutor. Recap every score.

## Later / spin-off episodes
- RAG over your **Medium posts** (the original idea — keep it, as a vibecoding-flavored standalone).
- "Local vs ChatGPT for Persian" — privacy + quality face-off.
- Fine-tuning experiment (if you ever upgrade hardware).

---

## Companion posts on X (turn each video into a week of text content)
- Day the video drops: a **thread** = the 6 tasks + screenshots + the verdict. Video link in a *reply*, not the main post.
- Mid-week: one **"surprising failure"** clip (e.g., a model inventing fake Persian). Most shareable format.
- A **running leaderboard image** you re-post each episode — that's the thing people follow the series for.
- Reply daily to bigger local-AI / language-learning accounts. Early on this beats your own posts for reach.

## Practical cadence (solo, realistic)
- 1 video/week, 1 thread/week, short posts most days. Consistency > volume. Don't burn out.
