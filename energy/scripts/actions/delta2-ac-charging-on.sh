#!/usr/bin/env bash
# Delta2 AC charging ON
# Bruce Monitor — atomic EcoFlow action. Exits non-zero on WAITING/No data.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec python3 "$ROOT/lib/action_runner.py" \
  --device "delta2" \
  --method "enable_ac_charging" \
  --want "on" \
  --label "Delta2 AC charging ON"
