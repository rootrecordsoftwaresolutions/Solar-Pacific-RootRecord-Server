#!/usr/bin/env bash
# ============================================================================
# plumbing/scripts/flm-warmup.sh — start FastFlowLM on NPU if binary present
# ----------------------------------------------------------------------------
# WHAT: flm serve llama3.2:3b on 127.0.0.1:52625; no-op if binary missing.
# Layout style (standing): keep this header.
# ============================================================================
set -euo pipefail

# ====================================================
# SECTION: CONFIG
# ====================================================
PORT=52625
FLM_MODEL="${FLM_MODEL:-llama3.2:3b}"
LOG="/home/rootrecord/Database/GITHUB/logs/flm.log"
mkdir -p "$(dirname "$LOG")"

# ====================================================
# SECTION: FIND BINARY
# ====================================================
FLM_BIN=""
for c in "$HOME/.local/bin/flm" /usr/local/bin/flm flm; do
  if command -v "$c" >/dev/null 2>&1 || [[ -x "$c" ]]; then
    FLM_BIN=$(command -v "$c" 2>/dev/null || echo "$c")
    break
  fi
done
if [[ -z "$FLM_BIN" || ! -x "$FLM_BIN" ]]; then
  echo "[skip] FLM binary not found (NPU path optional; Ollama remains fallback)"
  exit 0
fi

# ====================================================
# SECTION: START IF NEEDED
# ====================================================
if curl -sf -m 1 "http://127.0.0.1:$PORT/v1/models" >/dev/null 2>&1; then
  echo "[ok] FLM already up"
  exit 0
fi
pkill -f "flm serve" 2>/dev/null || true
sleep 1
nohup "$FLM_BIN" serve "$FLM_MODEL" --pmode default --host 127.0.0.1 --port "$PORT" >>"$LOG" 2>&1 &
echo "[ok] FLM starting pid=$! → $LOG"
for i in 1 2 3 4 5 6 7 8 9 10; do
  sleep 2
  if curl -sf -m 1 "http://127.0.0.1:$PORT/v1/models" >/dev/null 2>&1; then
    echo "[ok] FLM ready"
    exit 0
  fi
done
echo "[warn] FLM not ready yet — check $LOG"
exit 0
