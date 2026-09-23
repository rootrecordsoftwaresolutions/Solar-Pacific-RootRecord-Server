---
name: Offline work auto-doc
description: >-
  Use when documenting Alexander’s offline OmniBook work for agents — file
  create/modify audit only (no keystrokes, clipboard, or mouse). Logs live under
  Database/WORKLOG only; never in this skill or any git repo.
---

# Offline work auto-doc

## What it is
A **file-change worklog** for agent handoff of offline work. Records new and
modified files under watched roots. **Does not** capture keystrokes, mouse,
clipboard, screen, or typed secrets.

## Paths (data stays out of skill/git)
| Role | Path |
|------|------|
| Current log | `/home/rootrecord/Database/WORKLOG/worklog_current.md` |
| Hourly archives | `/home/rootrecord/Database/WORKLOG/<START>-<END>.md` |
| Scrub list | `/home/rootrecord/master/master-key.env` keys `*_KEYLOG_DELETE=` / `*_WORKLOG_DELETE=` (and other env VALUES length ≥ 12) |
| Poller PID | `/home/rootrecord/Database/WORKLOG/.poller.pid` |

## Run (only while poller is active)
```bash
# start (1-minute scan + scrub + hourly rotate)
bash /home/rootrecord/.ollama/skills/reports/scripts/worklog_poller.sh

# one-shot verify
bash /home/rootrecord/.ollama/skills/reports/scripts/worklog_once.sh

# stop
kill "$(cat /home/rootrecord/Database/WORKLOG/.poller.pid)"
```

## Safety
1. Logs are **paths + size + mtime only** — not file contents.
2. Scrub runs every minute against `master-key.env`; matching substrings in the log are replaced with `[REDACTED]`.
3. Never commit `Database/WORKLOG/` or put log text inside this skill.
4. Stop the poller when power is thin; logging only runs while the poller process is up.
