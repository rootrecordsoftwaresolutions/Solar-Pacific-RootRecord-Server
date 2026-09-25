#!/usr/bin/env bash
# Leap-frog: every ~5s call → alternate Delta2 / River2Pro (each pack ~10s)
set -euo pipefail
ROOT="/home/rootrecord/.ollama/skills/energy/scripts/read"
# slot = floor(epoch/5); even → delta2, odd → river2pro
slot=$(( $(date +%s) / 5 ))
if (( slot % 2 == 0 )); then
  exec bash "$ROOT/delta2-read.sh"
else
  exec bash "$ROOT/river2pro-read.sh"
fi
