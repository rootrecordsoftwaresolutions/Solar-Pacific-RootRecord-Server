#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# This file is copied over plumbing run-ollama.sh
PLUMB="$(dirname "$(readlink -f "$0" 2>/dev/null || echo "$0")")"
# when installed to plumbing/scripts:
SINGLE="$(cd "$(dirname "$0")" && pwd)/single-flight.sh"
MODEL="${1:?model}"; shift || true
JOB="ollama:$MODEL:$(date +%Y%m%d-%H%M%S)"
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1
[[ "${RR_ALLOW_IGPU:-0}" == "1" ]] || unset OLLAMA_IGPU_ENABLE 2>/dev/null || true

DESK_BLOCK="DESK_LIVE:
(none — no measured desk attached this turn)

HARD RULES FOR THIS TURN:
- Do NOT state watts, SOC, kWh/day, pack online/offline, panel status, or host load.
- Do NOT restate standing envelopes (~4–5 kWh/day, Delta 2, River 2 Pro, Starlink) as if they were live readings.
- If asked for status: one short line that you are the named agent + \"No live desk data attached.\" Nothing else about power/hardware."

if [[ -n "${DESK_LIVE_FILE:-}" && -f "${DESK_LIVE_FILE}" ]]; then
  DESK_BLOCK="DESK_LIVE:
$(cat "$DESK_LIVE_FILE")

Cite ONLY lines inside DESK_LIVE for measurements. Standing policy is not a live reading."
fi

USER_PROMPT="${*:-}"
[[ -n "$USER_PROMPT" ]] || USER_PROMPT=$(cat)
FULL="${DESK_BLOCK}

User request: ${USER_PROMPT}"
exec "$SINGLE" run "$JOB" -- ollama run "$MODEL" "$FULL"
