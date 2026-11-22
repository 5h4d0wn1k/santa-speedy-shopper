#!/usr/bin/env python3
"""Measure tokens/second on the Cerebras Inference API using its own timing data.

This is an honest local benchmark for tuning and for the README. It is NOT the
official OpenClaw speed patch required by the Speed Bounty.
"""
import argparse
import json
import os
import time
import urllib.request

ENV_FILE = os.path.expanduser("~/.openclaw/.env")
URL = "https://api.cerebras.ai/v1/chat/completions"


def load_key() -> str:
    if os.path.exists(ENV_FILE):
        for line in open(ENV_FILE, encoding="utf-8"):
            if line.startswith("CEREBRAS_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return os.environ.get("CEREBRAS_API_KEY", "")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen-3.8-27b")
    ap.add_argument("--prompt", default="Write a short paragraph about fast inference.")
    ap.add_argument("--max-tokens", type=int, default=256)
    ap.add_argument("--reasoning-effort", default=None)
    args = ap.parse_args()

    key = load_key()
    if not key or key.startswith("csk-REPLACE"):
        raise SystemExit("CEREBRAS_API_KEY is missing or still a placeholder")

    body = {
        "model": args.model,
        "messages": [{"role": "user", "content": args.prompt}],
        "max_completion_tokens": args.max_tokens,
    }
    if args.reasoning_effort:
        body["reasoning_effort"] = args.reasoning_effort

    req = urllib.request.Request(
        URL,
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    start = time.perf_counter()
    with urllib.request.urlopen(req, timeout=90) as resp:
        payload = json.loads(resp.read().decode())
    wall = time.perf_counter() - start

    usage = payload.get("usage", {})
    timing = payload.get("time_info", {})
    completion_time = timing.get("completion_time") or wall
    out_tokens = usage.get("completion_tokens", 0)

    result = {
        "model": args.model,
        "completion_tokens": out_tokens,
        "completion_time_s": round(completion_time, 4),
        "wall_time_s": round(wall, 4),
        "tokens_per_second": round(out_tokens / completion_time, 1) if completion_time else None,
        "reasoning_tokens": usage.get("completion_tokens_details", {}).get("reasoning_tokens"),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
