# Hackathon workspace

Cerebras x Moonshot AI Kimi K3.1 Pro x OpenClaw Weekend Hackathon.

## Hard dates (Pacific Time)

- Hacking window: **Sat 21 Nov 2026, 10:00 AM PT → Sun 22 Nov 2026, 10:00 AM PT**
- All submissions due: **Sun 22 Nov 2026, 10:00 AM PT**
- X impressions / Reddit upvotes counted: **Tue 24 Nov 2026, 10:00 AM PT**
- Cerebras live support: Sat 10:30 AM–12:30 PM PT, Sun 9:00–10:00 AM PT in `#hackathon-support`

## Local setup

- OpenCode CLI: `opencode v2.2.5` (already installed at `~/bin/opencode`)
- OpenClaw: `2026.11.6` (installed via official installer)
- OpenClaw config: `~/.openclaw/openclaw.json` (validated)
- Cerebras key: `~/.openclaw/.env` (`chmod 600`) — **never commit or paste this**
- OpenClaw workspace: `/workspace/projects/hackathons/.openclaw-workspace`
- OpenClaw agent cwd/repoRoot: `/workspace/projects/hackathons`
- Default model ref: `cerebras/moonshotai-kimi-k3.1-pro-trial`
- Provider base URL: `https://api.cerebras.ai/v1`
- Web search: `@openclaw/parallel-plugin` installed, `tools.web.search.provider = parallel-free`
  (key-free, returns real product URLs). DuckDuckGo is installed as a fallback but throttles.
- Kimi status: now returns **429 `queue_exceeded`** (model exists, overloaded) instead of 404.

## Current blocker

The Cerebras key authenticates (`GET /v1/models` returns 200), but a chat request to
`moonshotai-kimi-k3.1-pro-trial` returns:

```json
{"message":"Model does not exist or you do not have access to it.","type":"not_found_error","param":"model","code":"model_not_found"}
```

Official support reply received:
> "Kimi K3.1 Pro is not available yet. Try again in 6hrs"

So this is **provisioning timing**, not a setup error or a rejected Org ID. No further support
action is needed yet — just retry in ~6 hours.

Retry plan:
- Run `bash /workspace/projects/hackathons/scripts/check-access.sh` in ~6 hours.
- If it returns HTTP 200, the configured default model (`cerebras/moonshotai-kimi-k3.1-pro-trial`)
  is already live — no config changes needed.
- If it still 404s after 6 hours, bump the support post with the new evidence.

Reference: submitted Org ID `org_jmhmh2dvk5kn9p6xw5wdrmj4` (the `prj_...` value is a project ID,
not the org ID). Kickoff is Sat 21 Nov, 10:00 AM PT / 18:00 UTC / 23:30 IST.

Action if still failing after kickoff: join https://discord.gg/XWXRquhx7H and ask in
`#hackathon-support` (opens Sat 10:30 AM PT / 17:30 UTC), quoting your Org ID and only the
key prefix — never the full key. Ask whether the Org ID was approved and whether access can
still be granted.

The ClawHub download for `@openclaw/cerebras-provider` timed out; installing from npm instead
via `openclaw plugins install npm:@openclaw/cerebras-provider --force --accept-capabilities --pin`.

## Prize plan

One project, all three prizes: build **Santa's Speedy Shopper** as the main OpenClaw project.

1. **Speed Bounty ($1,000)** — OpenClaw + Kimi K3.1 Pro finds 5 real Christmas gifts from real
   retail sites, each with a real product-page URL. TPS measured with the official OpenClaw
   speed patch (Discord only; do not share it; do not use it in public demos). Post a ≤60s video
   in `#share-your-demo` showing the top TPS and the 5 products with links, and write
   `Speed Bounty entry: N TPS` in the message.
2. **X Audience Choice (3 × $1,000)** — required official submission. Post ≤60s demo video,
   tag `@Cerebras` and `@Kimi_Moonshot`, include `#KimiOnCerebras`, project name, handles,
   2–4 sentence description, GitHub repo. Organic only.
3. **Reddit Audience Choice ($1,000)** — post the demo on r/cerebras with flair
   `Kimi K3.1 Pro Hackathon`. Organic upvotes counted Tue 24 Nov, 10 AM PT.

## Demo video storyboard (≤60s)

- 0–3s: hook card with project name + measured numbers + `Kimi K3.1 Pro / Cerebras / OpenClaw`
- 3–8s: prompt typed into OpenClaw (standard, unpatched)
- 8–20s: Cerebras lane, real-time streaming + 2–3 tool calls, overlay TTFT and tok/s
- 20–34s: GPU lane, same task, honest timer (label any fast-forward)
- 34–44s: split-screen result with the real artifact
- 44–53s: project value montage
- 53–60s: lockup with repo URL, model ID, handles, hashtag

Hide all keys, notifications, tabs, emails, and personal data. Use median of 3 runs for claims.

## Until kickoff (23:30 IST) — winning prep

- [x] OpenClaw harness validated end-to-end with a public Cerebras model (`pong` via `openclaw agent exec`)
- [x] Workspace skill `speedy-shopper` created and loading (verified with `openclaw skills check`)
- [x] Honest TPS benchmark `scripts/bench_tps.py` created and tested (qwen-3.8-27b ≈ 638 tok/s)
- [ ] Post the support ticket now — mods online from 11:00 PM IST
- [ ] At 23:30 IST run `bash scripts/check-access.sh`; the default model is already Kimi
- [ ] Find a teammate in `#hackathon-chat` — teams of 2 recommended, and a teammate with approved access keeps the team eligible if your Org ID isn't approved
- [ ] Rehearse the 60s demo recording with **standard** OpenClaw (never the speed patch)
- [ ] Prepare the GitHub repo + README with measurement table and honest caveats

## Useful commands

```bash
# Load key into a shell
set -a; . ~/.openclaw/.env; set +a

# Direct API smoke test (do this after access is granted)
curl https://api.cerebras.ai/v1/chat/completions \
  -H "Authorization: Bearer $CEREBRAS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"moonshotai-kimi-k3.1-pro-trial","messages":[{"role":"user","content":"Reply with exactly: pong"}]}'

# OpenClaw checks
openclaw config validate
openclaw plugins list --json
openclaw models status --json
openclaw gateway status
openclaw doctor
```

## Winning features

- **Five-lane proof board:** `python3 scripts/make_receipts.py` generates `out/receipts.html`
  with a verified/HTTP-status badge for each of the 5 real product links.
- **Speed HUD:** `python3 scripts/make_hud.py` generates `out/hud.svg` with wall time,
  output tokens, cache hits and tool-call count for the demo overlay.
- **Fast path frozen:** trial model output capped at 200 tokens, `--thinking off` by default;
  A/B with `python3 scripts/run_speedy.py --thinking low`.
- Numbers must be honest: `TPS = completion_tokens / completion_time`; report median of 3.
  The official speed patch is Discord-only and never appears in public demos.

## Project docs

- `docs/SUBMISSION.md` — X / Reddit / Discord post templates and teammate post
- `docs/DEMO.md` — 60s storyboard, privacy checklist, honest measurement rules

## Official links

- Guide: https://docs.google.com/document/d/1Vvf2SjScBt3yBeTVZRoKtOyE7rGEP-gWV_ApzwXepEQ/export?format=txt
- Luma: https://luma.com/cerebras-kimi-hackathon
- Discord: https://discord.gg/XWXRquhx7H
- OpenClaw Cerebras provider: https://docs.openclaw.ai/providers/cerebras
- Cerebras reasoning: https://inference-docs.cerebras.ai/capabilities/reasoning
