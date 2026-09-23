#!/usr/bin/env bash
# Ensure ollama serve is up; touch lane models (load lightly / list).
set -euo pipefail
if ! ollama list >/dev/null 2>&1; then
  nohup ollama serve >>/home/rootrecord/Database/GITHUB/logs/ollama-serve.log 2>&1 &
  sleep 3
fi
ollama list >/dev/null
# warm one small call under single-flight (optional skip if FLM preferred)
echo "[ok] ollama up"
