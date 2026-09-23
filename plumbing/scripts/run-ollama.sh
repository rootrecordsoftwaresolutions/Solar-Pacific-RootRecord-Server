#!/usr/bin/env bash
# ==============================================================================
# run-ollama.sh — ONLY supported way to invoke ollama run on OmniBook
# Always single-flight. Never background a second agent.
# Usage: run-ollama.sh <model> [prompt…]
#        run-ollama.sh <model> <<EOF … EOF
# ==============================================================================
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODEL="${1:?model name (ava|bruce|carly|…)}"
shift || true
JOB="ollama:$MODEL:$(date +%Y%m%d-%H%M%S)"

# NPU-first honesty: Ollama path is CPU (see references/NPU-FIRST.md)
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1
# Do NOT set OLLAMA_IGPU_ENABLE unless RR_ALLOW_IGPU=1
if [[ "${RR_ALLOW_IGPU:-0}" != "1" ]]; then
  unset OLLAMA_IGPU_ENABLE || true
fi

if [[ $# -gt 0 ]]; then
  exec "$HERE/single-flight.sh" run "$JOB" -- ollama run "$MODEL" "$*"
else
  # stdin prompt
  tmp=$(mktemp)
  cat > "$tmp"
  exec "$HERE/single-flight.sh" run "$JOB" -- bash -c "ollama run \"$MODEL\" \"\$(cat \"$tmp\")\"; rm -f \"$tmp\""
fi
