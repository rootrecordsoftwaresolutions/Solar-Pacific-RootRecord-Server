#!/usr/bin/env bash
echo 'target is not on this desk. Do not start a local website.' >&2; exit 1
set -euo pipefail
cd "$(dirname "$0")/../site"
npm install
npm run dev
