#!/usr/bin/env bash
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/root-status"
export PYTHONPATH="$ROOT/lib${PYTHONPATH:+:$PYTHONPATH}"
exec python3 -c "from merge import merge; p=merge(); print(f'OK wrote {p}')"
