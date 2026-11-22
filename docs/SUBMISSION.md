# Submission templates

All posts must go out before **Sun 22 Nov, 10:00 AM PT (23:30 IST)**. X is the required official submission.

## X (required)

Tags and hashtag are mandatory: `@Cerebras @Kimi_Moonshot #KimiOnCerebras`

```text
Project: Santa's Speedy Shopper
Team: @nikhilnagpure_
This OpenClaw agent finds 5 real Christmas gifts with verified retail links in SECONDS using Kimi K3.1 Pro on Cerebras. Same prompt: GPU ~XXs vs Cerebras ~XXs (median of 3). 60s demo + code: github.com/YOU/REPO
#KimiOnCerebras @Cerebras @Kimi_Moonshot
```

Self-reply thread:
1. Stack: OpenClaw + `moonshotai-kimi-k3.1-pro-trial` on `https://api.cerebras.ai/v1`, standard API key.
2. Measurement: median of 3, same prompt/temperature, no speed patch in this public demo.
3. One honest limitation.
4. Repo + one-command quickstart.

Never ask for likes/retweets. Organic only.

## Reddit (optional, for the Reddit prize)

Subreddit: **r/cerebras** · Flair: **Kimi K3.1 Pro Hackathon**

Title:
```text
[Santa's Speedy Shopper] OpenClaw agent finds 5 real gifts in XXs on Kimi K3.1 Pro / Cerebras (60s demo)
```

Body:
```text
Project Name: Santa's Speedy Shopper
Team Members: u/YOU (@YOU on X)
Project Description: An OpenClaw agent that finds five real Christmas gift products from real retail sites, verifies each product page is live, and returns name/price/retailer/link. Kimi K3.1 Pro on Cerebras is the central model across the search-and-verify tool loop. Median end-to-end time was XXs vs XXs on a GPU provider (N=3, standard OpenClaw, no speed patch). The 60s demo shows both lanes and the final five links.
GitHub Repository: https://github.com/YOU/REPO
Demo Video: attached / YouTube: LINK

Measurement details and limitations are in the README. Feedback welcome — especially on whether the comparison is fair.
```

## Discord Speed Bounty entry

Channel: `#share-your-demo`

```text
Speed Bounty entry: 1234 TPS

Project: Santa's Speedy Shopper
Model: moonshotai-kimi-k3.1-pro-trial on Cerebras, OpenClaw harness
Video shows the top TPS readout and all 5 real products with their product-page links.
```

Rules: video ≤60s, TPS visible in video **and** written in the message. Never share the speed patch.

## Teammate post (`#hackathon-chat`)

```text
Building Santa's Speedy Shopper for the Speed Bounty: OpenClaw + Kimi K3.1 Pro on Cerebras. Harness, native skill, TPS benchmark and demo plan are already set up. Looking for 1 teammate — ideally someone with approved Cerebras access or demo-video skills. DM me or reply here!
```
