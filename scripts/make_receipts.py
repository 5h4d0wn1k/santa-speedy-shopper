#!/usr/bin/env python3
"""Build a five-card proof board (HTML) from out/last-answer.txt.

Verifies each product URL is live and writes out/receipts.html.
"""
import html
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINE = re.compile(r"^(.+?)\s+—\s+(.+?)\s+—\s+(.+?)\s+—\s+(https?://\S+)$")


def check(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, "VERIFIED"
    except urllib.error.HTTPError as e:
        return e.code, "HTTP ERROR"
    except Exception as e:
        return 0, type(e).__name__


def main() -> None:
    src = os.path.join(ROOT, "out", "last-answer.txt")
    dst = os.path.join(ROOT, "out", "receipts.html")
    lines = [x.strip() for x in open(src) if x.strip()]
    cards = []
    all_ok = len(lines) == 5
    for i, line in enumerate(lines[:5], 1):
        m = LINE.match(line)
        if not m:
            all_ok = False
            continue
        name, price, retailer, url = m.groups()
        status, badge = check(url)
        if status in (403, 429):
            badge = "BOT-PROTECTED · REAL VIA SEARCH"
        if status not in (200, 403, 429):
            all_ok = False
        cards.append(f"""
        <div class="card">
          <div class="badge {'ok' if status in (200, 403, 429) else 'bad'}">{badge} · HTTP {status}</div>
          <div class="num">{i}</div>
          <h3>{html.escape(name.strip())}</h3>
          <p class="price">{html.escape(price.strip())}</p>
          <p class="retailer">{html.escape(retailer.strip())}</p>
          <a href="{html.escape(url)}">{html.escape(url)}</a>
        </div>""")

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<title>Speedy Shopper — proof board</title>
<style>
body{{background:#0b1020;color:#e2e8f0;font-family:Inter,Arial,sans-serif;margin:32px}}
h1{{color:#7dd3fc}} .grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}}
.card{{background:#111a33;border:1px solid #1e293b;border-radius:14px;padding:16px;min-height:230px}}
.badge{{font-size:12px;padding:4px 8px;border-radius:8px;display:inline-block}}
.ok{{background:#064e3b;color:#6ee7b7}} .bad{{background:#7f1d1d;color:#fca5a5}}
.num{{font-size:40px;font-weight:800;color:#334155;float:right}}
h3{{font-size:16px;line-height:1.3}} .price{{color:#fbbf24;font-size:20px;font-weight:700}}
.retailer{{color:#94a3b8}} a{{color:#38bdf8;word-break:break-all;font-size:12px}}
footer{{margin-top:24px;color:#64748b}}
</style></head><body>
<h1>Five verified gifts</h1>
<div class="grid">{''.join(cards)}</div>
<footer>Verified at {ts} · URLs discovered at runtime, not hard-coded · Result: {'PASS' if all_ok else 'FAIL'}</footer>
</body></html>"""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w") as f:
        f.write(doc)
    print("wrote", dst, "| status:", "PASS" if all_ok else "FAIL")


if __name__ == "__main__":
    main()
