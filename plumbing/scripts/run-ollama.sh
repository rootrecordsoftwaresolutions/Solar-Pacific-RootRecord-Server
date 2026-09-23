#!/usr/bin/env bash
# ==============================================================================
# run-ollama.sh — ONLY supported ollama run entry (single-flight + DESK_LIVE)
# Usage:
#   run-ollama.sh <model> 'prompt'
#   DESK_LIVE_FILE=/path/to/block run-ollama.sh <model> 'prompt'
# ==============================================================================
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODEL="${1:?model}"
shift || true
JOB="ollama:$MODEL:$(date +%Y%m%d-%H%M%S)"

export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1
if [[ "${RR_ALLOW_IGPU:-0}" != "1" ]]; then
  unset OLLAMA_IGPU_ENABLE 2>/dev/null || true
fi

DESK_BLOCK="DESK_LIVE:
(none — no measured desk attached this turn)
RULE: For any watt/SOC/%/kWh/panel/host/NPU live claim → reply No data / I can't view that desk."

if [[ -n "${DESK_LIVE_FILE:-}" && -f "${DESK_LIVE_FILE}" ]]; then
  DESK_BLOCK="DESK_LIVE:
$(cat "$DESK_LIVE_FILE")"
fi

USER_PROMPT="${*:-}"
if [[ -z "$USER_PROMPT" ]]; then
  USER_PROMPT=$(cat)
fi

FULL="${DESK_BLOCK}

User request: ${USER_PROMPT}"

exec "$HERE/single-flight.sh" run "$JOB" -- ollama run "$MODEL" "$FULL"
