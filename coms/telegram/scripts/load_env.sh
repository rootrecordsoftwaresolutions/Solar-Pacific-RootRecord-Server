#!/usr/bin/env bash
set -euo pipefail
for f in "$@"; do
  [[ -f "$f" ]] || continue
  set -a
  # shellcheck disable=SC1090
  source "$f"
  set +a
done
