#!/usr/bin/env bash
# River2Pro energy backup OFF
# Bruce Monitor — atomic EcoFlow action. Exits non-zero on WAITING/No data.
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" \
  --device "river2pro" \
  --method "enable_energy_backup" \
  --want "off" \
  --label "River2Pro energy backup OFF"
