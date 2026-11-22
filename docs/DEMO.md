# 60-second demo plan

Record with **standard OpenClaw only** — never the speed patch. Max 60 seconds.

## Privacy before recording

- Desktop notifications off / Do Not Disturb.
- Clean browser profile: no saved tabs, passwords, email, DMs.
- No `.env`, terminal history, or API keys visible. Use `env` values, never raw keys on screen.
- Use dummy data only.

## Storyboard

| Time | Shot | On-screen text |
|---|---|---|
| 0–3s | Hook card | `Santa's Speedy Shopper — Xs vs Ys. Kimi K3.1 Pro / Cerebras / OpenClaw.` |
| 3–8s | Prompt typed into OpenClaw | Full task visible; badge `Standard OpenClaw — no speed patch` |
| 8–20s | Cerebras lane, real-time | Streaming output + search/fetch tool calls; overlay `TTFT`, `tok/s` |
| 20–34s | GPU lane, same task | Honest timer. If fast-forwarded, label `GPU shown at 5x; real time on timer` |
| 34–44s | Split-screen result | `Cerebras DONE Xs` / `GPU DONE Ys`, real artifact: 5 live product links |
| 44–53s | Project value montage | 2–3 quick cuts, 4-word captions |
| 53–60s | Lockup | Repo URL, `moonshotai-kimi-k3.1-pro-trial`, handles, `#KimiOnCerebras` |

## Honest numbers

- Compute tok/s from Cerebras `usage.completion_tokens / time_info.completion_time`.
- Also report end-to-end wall clock (keystroke → final artifact).
- Same prompt, repo, settings, machine, network; no warm-cache advantage for one lane.
- Median of 3 runs. State model used on each side; if the GPU lane uses a different model, say so.

## Verification before posting

1. All 5 URLs return HTTP 200: `python3 scripts/verify_products.py < answer.txt`
2. Video ≤60s, first frame is the result card.
3. TPS not shown in public X/Reddit demo (patch is Discord-only).
4. Tags/hashtag and flair correct (see `docs/SUBMISSION.md`).
