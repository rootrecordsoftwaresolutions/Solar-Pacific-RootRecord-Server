---
name: github
description: >-
  Bidirectional desk↔GitHub sync for skills, website, mainland (repos.conf).
  Standing deploy: merge skills code → auto full poller stack reload + window.
---

# github

**MUST:** Never force-push. Never `reset --hard`. Never print tokens.

## HOW TO ADD A REPO

1. Edit `scripts/repos.conf` — copy the **TEMPLATE** line in SECTION: REPOS.
2. Fill id / enabled / mode / local_path / github_slug / remote_name (tabs).
3. Run `scripts/setup-all-remotes.sh` once if the worktree is new.
4. `github_sync_all` (poller, ~300s) picks it up — no parallel sync engine.

## Layout style (standing)

Keep SECTION banners and TEMPLATE lines in `repos.conf` and script headers.
If stripped, restore from git history. See `0-master-prompt/prompts/09-file-layout-style.md`.

## Paths

| What | Where |
|------|--------|
| Catalog | `scripts/repos.conf` |
| Sync all | `scripts/sync-all.sh` |
| One repo | `scripts/push-repo-once.sh` |
| Shared | `scripts/common.sh` |
| Baks / flags | `/home/rootrecord/Database/GITHUB/` |
