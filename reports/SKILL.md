---
name: Offline work auto-doc
description: >-
  Use when documenting Alexander’s offline OmniBook work for agents — file and
  folder create/modify/delete audit only (no keystrokes, clipboard, or mouse).
  Logs live under Database/WORKLOG only; never in this skill or any git repo.
---

# Offline work auto-doc

## What it records
While the **poller** is running (every ~60s):
- **NEW_FILE** — first time a path appears under a watched root
- **MOD_FILE** — same path, different size and/or mtime
- **NEW_DIR** — new directory under a watched root
- **DELETED** — a recently tracked path that no longer exists

Each line is **path + size + mtime** (dirs: path + mtime). **Not** file contents.

## What it does NOT record
Keystrokes, mouse, clipboard copy/paste, screen, window titles, or typed secrets.
USB/network transfer *protocols* are not logged — but a file that **lands** in a
watched folder (copy, download, move, extract) shows up as **NEW_FILE** / **NEW_DIR**.

## Paths (data stays out of skill/git)
| Role | Path |
|------|------|
| Current log | `/home/rootrecord/Database/WORKLOG/worklog_current.md` |
| Hourly archives | `/home/rootrecord/Database/WORKLOG/<START>-<END>.md` |
| Scrub list | `/home/rootrecord/master/master-key.env` → `*_KEYLOG_DELETE=` / `*_WORKLOG_DELETE=` (+ long KEY/TOKEN/SECRET/PASS values) |

## Watched roots
`DAILY AI DEV HANDOFF`, `NETWORK`, `Documents`, `Desktop`, `Downloads`, `.ollama/skills`

Skipped: `WORKLOG`, `KEYLOGGER`, `GITHUB`, `.git`, `node_modules`, `*.log`

## Commands
```bash
bash /home/rootrecord/.ollama/skills/reports/scripts/worklog_poller.sh   # start
bash /home/rootrecord/.ollama/skills/reports/scripts/worklog_once.sh     # one scan
kill "$(cat /home/rootrecord/Database/WORKLOG/.poller.pid)"             # stop
```
