#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/river2pro-ac-always-on-off.sh - River2Pro AC always-on OFF
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "river2pro" --method "enable_ac_always_on" --want "off" --label "River2Pro AC always-on OFF"
