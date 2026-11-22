#!/usr/bin/env bash
set -euo pipefail

ENV_FILE="${HOME}/.openclaw/.env"
# shellcheck disable=SC1090
set -a; . "$ENV_FILE"; set +a

OUT="${TMPDIR:-/tmp}/cerebras-access.json"
code=$(curl -sS -o "$OUT" -w '%{http_code}' \
  https://api.cerebras.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${CEREBRAS_API_KEY}" \
  -d '{"model":"moonshotai-kimi-k3.1-pro-trial","messages":[{"role":"user","content":"Reply with exactly: pong"}],"max_completion_tokens":32}')

echo "HTTP $code"
cat "$OUT"
echo
