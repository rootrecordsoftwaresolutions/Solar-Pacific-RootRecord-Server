---
name: github
description: >-
  Auto-sync skills + website + us-mainland-server to their GitHub repos
  every 300s. Intake/baks under /home/rootrecord/Database/.
---

# github

**repos.conf**
- `skills` → Solar-Pacific-RootRecord-Server (`~/.ollama/skills`)
- `website` → RootRecord-Website (mirror `skills/website/site`)
- `mainland` → US-Mainland-Server (`skills/us-mainland-server`)

**Poller:** boot `setup-all-remotes.sh` · 300s `sync-all.sh`  
**Data:** `/home/rootrecord/Database/intake/` · **Baks/logs:** `Database/GITHUB/`  
**Ignore on Pacific:** `website/` · `us-mainland-server/` · `aws-sync/`
