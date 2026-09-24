#!/usr/bin/env bash
# =============================================================================
# energy/scripts/actions/river2pro-ac-always-on-on.sh - River2Pro AC always-on ON
# =============================================================================
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy"
exec "$ROOT/lib/py" "$ROOT/lib/action_runner.py" --device "river2pro" --method "enable_ac_always_on" --want "on" --label "River2Pro AC always-on ON"
