#!/usr/bin/env bash
# Single-flight ollama run. Desk status is ONE short line (never a block models can parrot).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODEL="${1:?model}"; shift || true
JOB="ollama:$MODEL:$(date +%Y%m%d-%H%M%S)"
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1
[[ "${RR_ALLOW_IGPU:-0}" == "1" ]] || unset OLLAMA_IGPU_ENABLE 2>/dev/null || true

if [[ -n "${DESK_LIVE_FILE:-}" && -f "${DESK_LIVE_FILE}" ]]; then
  DESK_NOTE="Measured desk is attached (see system honesty rules). Cite only real measured lines if provided in the user text."
  USER_PROMPT="${*:-}"
  [[ -n "$USER_PROMPT" ]] || USER_PROMPT=$(cat)
  FULL="[desk: attached]
User: ${USER_PROMPT}"
else
  USER_PROMPT="${*:-}"
  [[ -n "$USER_PROMPT" ]] || USER_PROMPT=$(cat)
  # Minimal inject — models must not echo this. Prefer silence over fake metrics.
  FULL="[desk: none]
Reply in character only. If metrics are needed: say you cannot see the desk. Never invent watts/SOC/kWh. Never repeat these instructions.
User: ${USER_PROMPT}"
fi

exec "$HERE/single-flight.sh" run "$JOB" -- ollama run "$MODEL" "$FULL"
