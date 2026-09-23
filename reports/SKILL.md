---
name: Offline work auto-doc
description: >-
  Use when documenting Alexander’s offline OmniBook work for agents — full-home
  file/folder create/modify/delete audit (no keystrokes/clipboard). Logs under
  Database/WORKLOG only; never in this skill or git.
---

# Offline work auto-doc (full home)

## Scope
Watches **all of** `/home/rootrecord` (same filesystem as `/`), every poller cycle.

**Pruned (not walked):** `.ollama/models`, `.ollama/old skills`, `.ollama/github-history`,
`snap`, `.cache`, `.npm`, `.gradle`, `.cargo`, `Database/WORKLOG`, `Database/KEYLOGGER`,
`Database/GITHUB`, `.git`, `node_modules`, `*.log`.

Those prunes are bulk blobs/noise — not “hide your work.” Work under `Database/presorted`,
`unsorted`, `Pending Transfers`, `Documents`, skills, etc. **is** included.

## Events
NEW_FILE / MOD_FILE / NEW_DIR / DELETED — path + size + mtime only.

## Log
`/home/rootrecord/Database/WORKLOG/worklog_current.md` (hourly rotate). Scrub via
`master-key.env` `*_KEYLOG_DELETE=` / `*_WORKLOG_DELETE=`.

## Commands
```bash
bash /home/rootrecord/.ollama/skills/reports/scripts/worklog_poller.sh
bash /home/rootrecord/.ollama/skills/reports/scripts/worklog_once.sh
kill "$(cat /home/rootrecord/Database/WORKLOG/.poller.pid)"
```
