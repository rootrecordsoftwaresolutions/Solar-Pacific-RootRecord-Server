---
name: automations
description: >-
  Boot poller + Cloudflare tunnel (rootserver.rootrecord.cloud) + jobs.py
  scheduler/status window. Use for poller, tunnel, or jobs.
---

# automations

**MUST:** Ctrl-C on poller window or `rootserver-poller stop` kills poller + cloudflared + `rr-rootserver-poller.service` (`scripts/stop-poller-stack.sh`).

| | |
|--|--|
| Jobs | `scripts/jobs.py` |
| Engine | `scripts/rootserver_poller.py` |
| Stop | `scripts/stop-poller-stack.sh` |
| Window | `scripts/open-poller-window.sh` |
| CLI | `/home/rootrecord/rootserver-poller` `{restart\|stop\|status\|window}` |
| Unit | `rr-rootserver-poller.service` |
| Log | `~/.ollama/skills/logs/store/rootserver-poller.log` |
| Public | `https://rootserver.rootrecord.cloud/` |

**jobs.py:** `ON_BOOT` (prio↑ later; p0 `self_terminal`, p1 `cloudflare_tunnel`, p2 `github_backup_remote`) → `ONCE_AT_START` → `EVERY_SECONDS` (incl. `heartbeat` 5s, `github_autopush` 300s) / `EVERY_MINUTE` / `EVERY_HOUR`. Copy section TEMPLATEs; keep key order.

**Bak:** `/home/rootrecord/Database/GITHUB/` only — never `automations.bak-*` under `skills/`.
