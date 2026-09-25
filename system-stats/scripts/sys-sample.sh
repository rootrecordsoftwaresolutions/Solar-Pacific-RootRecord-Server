#!/usr/bin/env bash
# system-stats sample — one host snapshot (CPU / load / mem)
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/system-stats"
export PYTHONPATH="$ROOT/lib${PYTHONPATH:+:$PYTHONPATH}"
exec python3 "$ROOT/lib/sample.py"
