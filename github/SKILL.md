---
name: github
description: >-
  Auto-sync ~/.ollama/skills → GitHub backup remote (90MB guard). Driven by
  automations jobs.py; token GITHUB_TOKEN in master-key.env.
---

# github

**Poller-owned** (do not also run `poll-and-push.sh`):
- ON_BOOT p2 `github_backup_remote` → `scripts/setup-remote.sh`
- EVERY_SECONDS 300 `github_autopush` → `scripts/push-once.sh`

Manual: `bash scripts/push-once.sh`

**Token:** `/home/rootrecord/master/master-key.env` → `GITHUB_TOKEN` (fine-grained, `Solar-Pacific-RootRecord-Server` Contents R/W). Remote name: `backup`. Log gitignored: `scripts/poll-and-push.log`.
