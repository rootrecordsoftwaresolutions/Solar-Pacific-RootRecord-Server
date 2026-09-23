#!/usr/bin/env bash
# Start FastFlowLM llama3.2:3b on XDNA NPU if binary exists and not already up.
set -euo pipefail
FLM_BIN="${FLM_BIN:-/home/rootrecord/.local/opt/fastflowlm/flm}"
FLM_MODEL="${FLM_MODEL:-llama3.2:3b}"
PORT="${FLM_PORT:-52625}"
LOG="${FLM_LOG:-/home/rootrecord/Database/GITHUB/logs/flm.log}"
mkdir -p "$(dirname "$LOG")"
if curl -sf -m 1 "http://127.0.0.1:$PORT/v1/models" >/dev/null 2>&1; then
  echo "[ok] FLM already up :$PORT"
  exit 0
fi
if [[ ! -x "$FLM_BIN" ]]; then
  echo "[skip] FLM binary missing: $FLM_BIN (Ollama remains fallback)"
  exit 0
fi
# stop stale
pkill -f "flm serve" 2>/dev/null || true
sleep 1
nohup "$FLM_BIN" serve "$FLM_MODEL" --pmode default --host 127.0.0.1 --port "$PORT" >>"$LOG" 2>&1 &
echo "[ok] FLM starting pid=$! → $LOG"
# wait briefly
for i in 1 2 3 4 5 6 7 8 9 10; do
  sleep 2
  if curl -sf -m 1 "http://127.0.0.1:$PORT/v1/models" >/dev/null 2>&1; then
    echo "[ok] FLM ready"
    exit 0
  fi
done
echo "[warn] FLM not ready yet — check $LOG"
exit 0
