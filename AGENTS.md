# Hackathon agent instructions

You are working on a Cerebras x Kimi K3.1 Pro x OpenClaw hackathon entry.

## Required stack

- Harness: OpenClaw. The final project must use the OpenClaw harness.
- Model: `moonshotai-kimi-k3.1-pro-trial` on `https://api.cerebras.ai/v1` with the standard
  Cerebras API key from `~/.openclaw/.env`. No separate preview endpoint.
- Read the key from the environment (`CEREBRAS_API_KEY`). Never print, commit, or echo it.
- On the trial endpoint, thinking is off by default; set `reasoning_effort` only when needed.

## Main task: Santa's Speedy Shopper

Build an OpenClaw agent that finds **5 real Christmas gift products** on real retail sites,
each with a real product-page URL. Requirements:

- Products and links must be real and verifiable. Made-up, placeholder, or hard-coded results
  are disqualified.
- Keep the model in the loop: real discovery through OpenClaw tools, not a pre-baked list.
- Keep tool results small (title, price, retailer, canonical URL) and minimize tool round trips.
- Keep a static system prompt/tool schema prefix so Cerebras prompt caching can work.
- Final output: exactly 5 lines of `Product name — price — retailer — product page URL`.

## Compliance

- Demo videos must be ≤60 seconds and must show Cerebras speed.
- Never use the Speed Bounty speed patch in public X/Reddit demos. Never share the patch.
- Hide keys, notifications, browser tabs, emails, and personal data in any recording.
- X post must tag `@Cerebras` and `@Kimi_Moonshot` and include `#KimiOnCerebras`.
- Reddit post goes to r/cerebras with flair `Kimi K3.1 Pro Hackathon`.
- Organic reach only: no bots, paid promotion, vote exchanges, or engagement farming.

## Status

The configured key currently gets `model_not_found` for the trial model. Do not keep
retrying blindly; check with the organizers in `#hackathon-support` until private-preview
access is confirmed for the Org ID.
