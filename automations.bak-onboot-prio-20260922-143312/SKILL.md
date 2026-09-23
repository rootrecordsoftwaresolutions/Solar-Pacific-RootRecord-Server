---
name: automations
description: >-
  RootRecord on-box automations desk. Boot poller + Cloudflare tunnel for
  rootserver.rootrecord.cloud, scheduled jobs in jobs.py, status window.
---

# automations

## # INFO — MUST HAVE

Ctrl-C in the poller window (or `/home/rootrecord/rootserver-poller stop`)
**must** stop every related process: `rootserver_poller.py`, `cloudflared`,
and `rr-rootserver-poller.service`. See `scripts/stop-poller-stack.sh` and the
header in `scripts/jobs.py`.

## Operator paths

| What | Where |
|------|--------|
| Jobs / templates (edit here) | `scripts/jobs.py` |
| Engine | `scripts/rootserver_poller.py` |
| Stop all | `scripts/stop-poller-stack.sh` |
| Status window | `scripts/open-poller-window.sh` |
| Home shortcut | `/home/rootrecord/rootserver-poller` |
| systemd unit | `rr-rootserver-poller.service` |
| Log | `~/.ollama/skills/logs/store/rootserver-poller.log` |
| Public | `https://rootserver.rootrecord.cloud/` |

## Job sections in `jobs.py`

- `EVERY_SECONDS` — repeating interval (`interval_sec`)
- `EVERY_MINUTE` — on wall-clock minute change (`only_at_minutes` optional)
- `EVERY_HOUR` — on wall-clock hour change (`only_at_hours` optional)
- `ONCE_AT_START` — one-shot after tunnel READY

Copy the blank TEMPLATE inside the section you need; keep key order identical.

## Shortcut

```bash
/home/rootrecord/rootserver-poller restart
/home/rootrecord/rootserver-poller stop
/home/rootrecord/rootserver-poller status
```
