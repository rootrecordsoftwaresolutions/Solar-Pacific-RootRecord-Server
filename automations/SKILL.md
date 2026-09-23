---
name: automations
description: >-
  Boot poller + Cloudflare tunnel + jobs.py (incl. github_sync_all every 300s).
---

# automations

**MUST:** Ctrl-C / `rootserver-poller stop` kills poller + cloudflared + unit.

| | |
|--|--|
| Jobs | `scripts/jobs.py` |
| CLI | `/home/rootrecord/rootserver-poller` |
| Public | `https://rootserver.rootrecord.cloud/` |
| GitHub sync | `github_sync_all` → skills + website + mainland |
| Data | `/home/rootrecord/Database/` (intake + GITHUB baks) |

`ON_BOOT` p0 self → p1 tunnel → p2 `github_setup_remotes` → schedules.
