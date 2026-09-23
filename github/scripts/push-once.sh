#!/usr/bin/env bash
# Legacy alias: skills repo only. Prefer sync-all.sh / push-repo-once.sh.
exec "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/push-repo-once.sh" skills
