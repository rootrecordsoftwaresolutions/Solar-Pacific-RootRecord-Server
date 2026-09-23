#!/usr/bin/env bash
set -euo pipefail
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST=/home/rootrecord/.ollama/skills/plumbing
AG=/home/rootrecord/.ollama/agents/vision
TS=$(date +%Y%m%d-%H%M%S)
BAK=/home/rootrecord/Database/GITHUB/plumbing.bak-$TS
mkdir -p "$BAK" /home/rootrecord/Database/intake
if [[ -d "$DEST" ]]; then cp -a "$DEST"/. "$BAK/" || true; fi
mkdir -p "$DEST"
rsync -a --exclude INSTALL.sh "$SRC"/ "$DEST"/
chmod +x "$DEST/scripts/"*.sh
mkdir -p "$AG"
# vision from sibling if present
if [[ -d "$(dirname "$SRC")/vision-agent" ]]; then
  cp -a "$(dirname "$SRC")/vision-agent/"*.Modelfile "$(dirname "$SRC")/vision-agent/README.md" "$AG/" 2>/dev/null || true
fi
# also copy from pack root vision-agent
VF=/home/rootrecord/Database/GITHUB/plumbing-pack/vision-agent
[[ -d "$VF" ]] && cp -a "$VF/"* "$AG/" || true
echo "[ok] plumbing → $DEST"
echo "[ok] vision staged → $AG (create later: ollama create vision-reader -f $AG/vision-reader.Modelfile)"
echo "Test lock: bash $DEST/scripts/single-flight.sh status"
