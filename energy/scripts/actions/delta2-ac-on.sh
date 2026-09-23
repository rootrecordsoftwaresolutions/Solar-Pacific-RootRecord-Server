#!/usr/bin/env bash
# Delta2 AC ON (Starlink)
# Bruce Monitor — atomic EcoFlow action. Exits non-zero on WAITING/No data.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" \
  --device "delta2" \
  --method "enable_ac_ports" \
  --want "on" \
  --label "Delta2 AC ON (Starlink)"
