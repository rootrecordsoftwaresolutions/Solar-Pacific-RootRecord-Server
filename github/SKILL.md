---
name: github
description: >-
  Auto-sync three GitHub repos (skills, website, US-Mainland-Server). Poller
  every 300s. Baks → /home/rootrecord/Database/GITHUB only.
---

# github

**Repos** `scripts/repos.conf` — all three enabled:
- `skills` → Solar-Pacific-RootRecord-Server (`~/.ollama/skills`)
- `website` → RootRecord-Website (mirror from `skills/website/site`)
- `mainland` → US-Mainland-Server (`Database/GITHUB/worktrees/mainland`)

**Poller:** boot `setup-all-remotes.sh` · every 300s `sync-all.sh`  
**Bak:** `scripts/bak-new.sh <tag> [paths…]` → `/home/rootrecord/Database/GITHUB/`  
**Token:** `GITHUB_TOKEN` in `master-key.env` · **Logs:** `Database/GITHUB/logs/`
