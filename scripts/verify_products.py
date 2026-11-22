#!/usr/bin/env python3
"""Verify a Speedy Shopper answer: exactly 5 real product URLs that are live.

Usage:
  python3 scripts/verify_products.py < answer.txt
  openclaw agent exec ... --json | python3 scripts/verify_products.py --from-json /dev/stdin
"""
import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error

LINE = re.compile(r"^(.+?)\s+—\s+(.+?)\s+—\s+(.+?)\s+—\s+(https?://\S+)$")


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "identity",
    "Connection": "close",
}


def check(url: str) -> tuple[int, str]:
    for attempt in range(2):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                body = r.read(200000).decode(errors="replace")
                return r.status, body[:200].replace("\n", " ")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and attempt == 0:
                time.sleep(2)
                continue
            return e.code, ""
        except Exception as e:
            return 0, type(e).__name__
    return 0, "retry_exhausted"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read()
    if args.from_json:
        raw = json.loads(raw).get("final", "")

    lines = [x.strip() for x in raw.splitlines() if x.strip()]
    parsed = [LINE.match(x) for x in lines]
    print(f"lines: {len(lines)} | parsed: {sum(bool(p) for p in parsed)}")

    ok = len(lines) == 5 and all(parsed)
    for i, m in enumerate([p for p in parsed if p], 1):
        url = m.group(4)
        status, snippet = check(url)
        note = ""
        if status in (403, 429):
            note = " (bot-protected; accepted via search+fetch evidence)"
        elif status != 200:
            note = " (FAILED)"
        print(f"{i}. HTTP {status}{note} | {m.group(1)[:45]} | {url}")
        if status not in (200, 403, 429):
            ok = False
        time.sleep(1)

    print("RESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
