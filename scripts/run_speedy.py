#!/usr/bin/env python3
"""Run the Speedy Shopper task through OpenClaw and verify the result.

Primary model is Kimi K3.1 Pro on Cerebras. Use --model qwen-3.8-27b only for
rehearsals; public demos and submissions must use the Kimi model.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASK = os.path.join(ROOT, "speedy-shopper-task.txt")
OUT = os.path.join(ROOT, "out")
LINE = re.compile(r"^(.+?)\s+—\s+(.+?)\s+—\s+(.+?)\s+—\s+(https?://\S+)$")


def parse_lines(text: str):
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    parsed = [LINE.match(x) for x in lines]
    return lines, parsed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--model",
        default="cerebras/moonshotai-kimi-k3.1-pro-trial",
        help="OpenClaw model ref",
    )
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--thinking", default="off", help="OpenClaw thinking level, e.g. off/low/medium")
    ap.add_argument("--locked", action="store_true", help="Apply the strict tool allowlist (experimental)")
    args = ap.parse_args()

    os.makedirs(OUT, exist_ok=True)
    locked_policy = {
        "tools": {
            "allow": ["web_search", "web_fetch", "tool_search", "dispatch_action"],
            "deny": ["exec", "process", "code_execution", "bash", "read"],
            "toolSearch": True,
            "codeMode": {"enabled": False},
            "exec": {"mode": "deny"},
            "elevated": {"enabled": False},
            "loopDetection": {"enabled": True},
        }
    }

    cmd = [
        "openclaw", "agent", "exec",
        "--model", args.model,
        "--cwd", ROOT,
        "--thinking", args.thinking,
        "--timeout", str(args.timeout),
        "--message-file", TASK,
        "--json",
    ]
    if args.locked:
        cmd.extend(["--config-override", json.dumps(locked_policy)])

    started = time.perf_counter()
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    wall = time.perf_counter() - started

    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError:
        print("Failed to parse OpenClaw JSON output", file=sys.stderr)
        print(proc.stdout[:2000], file=sys.stderr)
        print(proc.stderr[:2000], file=sys.stderr)
        sys.exit(1)

    final = result.get("final", "")
    lines, parsed = parse_lines(final)
    usage = result.get("usage", {})

    summary = {
        "model": args.model,
        "ok": result.get("ok"),
        "status": result.get("status"),
        "assistant_turns": result.get("assistantTurns"),
        "tool_calls": result.get("toolSummary", {}).get("calls"),
        "wall_time_s": round(wall, 2),
        "output_tokens": usage.get("output"),
        "cache_read_tokens": usage.get("cacheRead"),
        "lines": len(lines),
        "parsed_lines": sum(bool(p) for p in parsed),
    }

    with open(os.path.join(OUT, "last-run.json"), "w") as f:
        json.dump({"summary": summary, "raw": result}, f, indent=2)
    with open(os.path.join(OUT, "last-answer.txt"), "w") as f:
        f.write(final)

    print(json.dumps(summary, indent=2))
    print("\n--- ANSWER ---")
    print(final)

    if not result.get("ok") or summary["lines"] != 5 or summary["parsed_lines"] != 5:
        print("\nRESULT: FAIL — inspect out/last-run.json", file=sys.stderr)
        sys.exit(1)
    print("\nRESULT: FORMAT OK — run scripts/verify_products.py next")


if __name__ == "__main__":
    main()
