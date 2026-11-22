---
name: speedy-shopper
description: Find five real Christmas gift products with live retail product-page URLs, then return a strict 5-line answer. Use for the Santa's Speedy Shopper speed bounty.
---

# Santa's Speedy Shopper

Use this skill for the Speed Bounty task or whenever asked to find real Christmas gifts.
The project must run on OpenClaw with `cerebras/moonshotai-kimi-k3.1-pro-trial` as the primary model.

## Goal

Return **exactly 5 real products** that exist on the internet, each with a **real product-page URL**
from a **real retail site**. Invented, placeholder, hard-coded, cached, or category-page results
are disqualified.

## Procedure

1. Use the available **web search tool** — never shell or `exec` for search. If the exact tool id
   is unknown, discover it with `tool_search` first. Issue 5 site-filtered queries in **one
   parallel tool block**: `site:amazon.com`, `site:walmart.com`, `site:ebay.com`,
   `site:homedepot.com`, `site:wayfair.com`.
2. Do NOT fetch retailer search pages or homepages directly. Use the available **fetch tool** on
   exactly 5 product URLs returned by search, in **one parallel tool block**. Accept HTTP 200 with a
   product title, or 403/429 if the search result showed a title and USD price (bot-protected).
   Reject only 404s and connection failures.
3. Keep tool results compact — only `{title, price, retailer, url}`. Never paste full HTML.
4. Then produce the final answer. **Maximum 3 model turns total. No loops, no re-searching.**
5. Do not pad output with filler. Do not include reasoning in the final answer.

## Final answer format (exact, 5 lines)

```text
Product name — price — retailer — product page URL
Product name — price — retailer — product page URL
Product name — price — retailer — product page URL
Product name — price — retailer — product page URL
Product name — price — retailer — product page URL
```

## Speed discipline

- Keep the system prompt and tool schemas unchanged between runs so Cerebras prefix caching works.
- Prefer one planning response with parallel tool calls, then one final formatted response.
- Do not change the reasoning level mid-session (thinking is off by default on the trial endpoint;
  set `reasoning_effort` only if you need it).
- Never share or use the speed patch in public X/Reddit demos. Record those with standard OpenClaw.
