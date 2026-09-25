#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/river2pro-energy-backup-off.sh - River2Pro energy backup OFF
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "river2pro" --method "enable_energy_backup" --want "off" --label "River2Pro energy backup OFF"
