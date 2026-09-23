---
name: github
description: >-
  Multi-repo auto-sync to GitHub (skills + website; mainland optional).
  Poller every 300s. Baks → /home/rootrecord/Database/GITHUB only.
---

# github

**Poller:** ON_BOOT `setup-all-remotes.sh` · EVERY_SECONDS 300 `sync-all.sh`  
Do not also run `poll-and-push.sh`.

**Registry:** `scripts/repos.conf`  
**Push one:** `scripts/push-repo-once.sh <id>`  
**Bak helper:** `scripts/bak-new.sh <tag> [paths…]` → `/home/rootrecord/Database/GITHUB/`

**Token:** `GITHUB_TOKEN` in `/home/rootrecord/master/master-key.env`  
**Logs:** `/home/rootrecord/Database/GITHUB/logs/`
