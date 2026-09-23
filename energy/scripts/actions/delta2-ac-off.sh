#!/usr/bin/env bash
# Delta2 AC OFF (Starlink drops)
# Bruce Monitor — atomic EcoFlow action. Exits non-zero on WAITING/No data.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec python3 "$ROOT/lib/action_runner.py" \
  --device "delta2" \
  --method "enable_ac_ports" \
  --want "off" \
  --label "Delta2 AC OFF (Starlink drops)"
