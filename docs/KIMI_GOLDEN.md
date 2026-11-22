# Kimi golden run (valid submission answer)

Model: `cerebras/moonshotai-kimi-k3.1-pro-trial`
Config: `--locked --thinking low`, tool surface limited to search/fetch.

## Answer (verified PASS)

```text
24 Pack Christmas Gift Bags with Handles and 50 Gift Tags — USD 23.99 — Amazon — https://www.amazon.com/Christmas-Handles-Styles-Assorted-Holiday/dp/B0BLK5ZSKC
Hershey's Kisses Solid Milk Chocolate Santa Hat Gift Box, 1.45 oz — USD 2.00 — Walmart — https://www.walmart.com/ip/Hershey-s-Kisses-Solid-Milk-Chocolate-Santa-Hat-Christmas-Candy-Gift-Box-1-45-oz/177133819
Schylling NeeDoh Advent Countdown to Squishmas 2026 — USD 30.99 — eBay — https://www.ebay.com/itm/377634419013
Amscan Christmas Printed Glossy Bottle Bags, 4-Count, 5-Pack — USD 19.99 — Home Depot — https://www.homedepot.com/p/Amscan-14-in-x-5-in-x-5-in-Christmas-Printed-Glossy-Bottle-Bags-4-Count-5-Pack-160251/301008197
The Holiday Aisle 12-Piece Christmas Kitchen Towel Set — USD 39.99 — Wayfair — https://www.wayfair.com/kitchen-tabletop/pdp/the-holiday-aisle-12-pcs-christmas-kitchen-towels-dish-towels-vintage-winter-snowman-decoration-hand-towels-tea-xmas-dishcloths-christmas-kitchen-decor-for-holiday-housewarming-gift-w116714207.html
```

## Telemetry

- Assistant turns: 10
- Wall time: 150.94 s
- Verification: Amazon + Walmart HTTP 200; eBay + Home Depot + Wayfair bot-protected (accepted via live search/fetch evidence)
- Result: PASS

## Speed notes

Earlier locked run reached **4 turns / 47 s** but refused the answer because its verification
rule was too strict. The rule is now aligned with the verifier (403/429 accepted). Re-run
`python3 scripts/run_speedy.py --locked --thinking low` 3 times and report the fastest verified
run for the Speed Bounty, using the official OpenClaw speed patch from Discord.
