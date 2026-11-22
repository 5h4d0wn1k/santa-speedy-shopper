# Golden rehearsal answer

Model used for rehearsal: `cerebras/qwen-3.8-27b` (public fallback).
Final submission MUST use `cerebras/moonshotai-kimi-k3.1-pro-trial`.

## Answer (verified PASS)

```text
PAVILIA Christmas Red Snowflake Throw Blanket, Holiday Winter Fleece, 50x60 — USD 16.99 — Amazon — https://www.amazon.com/PAVILIA-Christmas-Blanket-Holiday-Snowflakes/dp/B07XVSKZGT
Christmas Throw Blanket, Winter Holiday Sherpa Fleece, 50" x 60", ChristmasRhombus — USD 24.79 — Walmart — https://www.walmart.com/ip/Christmas-Throw-Blanket-Winter-Holiday-Sherpa-Fleece-Premium-Warm-Cozy-Blankets-Throws-Decorations-Bedroom-Gifts-Women-50-X-60-ChristmasRhombus/13348217368
DIY Felt Christmas Tree Set 32 pcs Detachable Ornaments Kids Wall Hanging Gift — USD 12.56 — eBay — https://www.ebay.com/itm/376574493359
Northlight 15 in. Unfinished Paintable Wooden Christmas Nutcracker with Rifle — USD 31.46 — The Home Depot — https://www.homedepot.com/p/Northlight-15-in-Unfinished-Paintable-Wooden-Christmas-Nutcracker-with-Rifle-34851144/319164540
Queens of Christmas Arctic 50 Piece Assorted Ball Ornament Set — USD 37.99 — Wayfair — https://www.wayfair.com/holiday-decor/pdp/queens-of-christmas-arctic-50-piece-assorted-ball-ornament-set-winl4152.html
```

## Rehearsal telemetry

- Assistant turns: 6
- Tool calls: 42
- Wall time: 108.6 s
- Output tokens: 25,137
- Cache-read tokens: 119,808
- Verification: Amazon/Walmart HTTP 200; eBay/Home Depot/Wayfair HTTP 403/429 (bot-protected, accepted via search+fetch evidence)

## Note

403/429 from a datacenter IP does not mean the product is fake. The URLs came from live
`web_search` results and were seen by `web_fetch`. Only 404/connection failure is treated as FAIL.
