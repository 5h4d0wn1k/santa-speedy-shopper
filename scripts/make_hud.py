#!/usr/bin/env python3
"""Generate a speed-HUD SVG from out/last-run.json for the demo overlay.

Usage: python3 scripts/make_hud.py
Writes: out/hud.svg
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "out", "last-run.json")
DST = os.path.join(ROOT, "out", "hud.svg")


def main() -> None:
    data = json.load(open(SRC))
    s = data["summary"]
    tokens = s.get("output_tokens") or 0
    wall = s.get("wall_time_s") or 0
    tps = tokens / wall if wall else 0

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="220" viewBox="0 0 900 220">
  <rect width="900" height="220" rx="18" fill="#0b1020" fill-opacity="0.88"/>
  <g font-family="Inter, Arial, sans-serif" fill="#e2e8f0">
    <text x="28" y="46" font-size="24" fill="#7dd3fc">SPEED HUD</text>
    <text x="28" y="112" font-size="58" font-weight="800">{tps:.0f}</text>
    <text x="150" y="112" font-size="28" fill="#94a3b8">tok/s (wall estimate)</text>
    <text x="28" y="166" font-size="26">wall {wall:.2f}s</text>
    <text x="230" y="166" font-size="26">out {tokens} tok</text>
    <text x="430" y="166" font-size="26">cacheRead {s.get('cache_read_tokens') or 0}</text>
    <text x="700" y="166" font-size="26">tools {s.get('tool_calls') or 0}</text>
  </g>
</svg>
"""
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w") as f:
        f.write(svg)
    print("wrote", DST)


if __name__ == "__main__":
    main()
