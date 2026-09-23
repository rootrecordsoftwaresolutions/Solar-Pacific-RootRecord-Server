#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
VOICE="${1:?voice}"; shift
PROMPT="${*:?prompt}"
MODEL=$(awk -F'\t' -v v="$VOICE" '$1==v && $2=="1" {print $5; exit}' "$ROOT/config/voices.conf")
FALLBACK=$(awk -F'\t' -v v="$VOICE" '$1==v && $2=="1" {print $6; exit}' "$ROOT/config/voices.conf")
RUN=$(grep -E '^RUN_OLLAMA=' "$ROOT/config/relay.conf" | cut -d= -f2-)
DESK=$(grep -E '^DESK_LIVE_FILE=' "$ROOT/config/relay.conf" | cut -d= -f2-)
[[ -x "$RUN" ]] || { echo "No data: RUN_OLLAMA missing" >&2; exit 2; }
[[ -n "$DESK" ]] && export DESK_LIVE_FILE="$DESK" || unset DESK_LIVE_FILE || true
out=$("$RUN" "$MODEL" "$PROMPT" 2>&1) || out=$("$RUN" "$FALLBACK" "$PROMPT" 2>&1) || true
echo "$out" | grep -v '^\[ok\] single-flight' || true
