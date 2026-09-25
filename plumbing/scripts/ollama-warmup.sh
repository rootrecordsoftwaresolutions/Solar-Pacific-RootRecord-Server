#!/usr/bin/env bash
# ============================================================================
# plumbing/scripts/ollama-warmup.sh — ensure ollama serve is up
# ----------------------------------------------------------------------------
# WHAT: Start ollama if down; used by poller ON_BOOT (local, no internet required).
# Layout style (standing): keep this header.
# ============================================================================
set -euo pipefail
if curl -sf -m 2 http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
  echo "[ok] ollama up"
  exit 0
fi
if command -v ollama >/dev/null 2>&1; then
  nohup ollama serve >>/tmp/ollama-serve.log 2>&1 &
  sleep 2
fi
if curl -sf -m 2 http://127.0.0.1:11434/api/tags >/dev/null 2>&1; then
  echo "[ok] ollama up"
  exit 0
fi
echo "[warn] ollama not ready"
exit 0
