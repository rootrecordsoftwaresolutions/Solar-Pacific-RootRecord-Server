# MIGRATED — do not run

| Field | Value |
| --- | --- |
| **Status** | Retired from G2 after G3 relay check PASS (process up, single instance, no 401/Unauthorized/Traceback) |
| **Date** | 2026-09-29 (HST) |
| **Old paths (removed)** | `/home/rootrecord/.ollama/skills/coms/telegram/scripts/council-relay.py`, `.../ensure-relay.sh` |
| **Canonical Pacific path** | `/home/rootrecord/RootRecord-Ecosystem/1 - Servers/1 - RootRecord-Pacific-Solar-Server/Communications/telegram/scripts/council-relay.py` + `ensure-relay.sh` (poller boot job `council_relay`) |
| **Evidence** | `2 - RootRecord-Database/Logs/Migration/g3-poller-realign-evidence-20260929T111731Z.md` |
| **Backup of removed files** | `/home/rootrecord/Database/GITHUB/g2-retire.bak-20260929-011731/.ollama/skills/coms/telegram/scripts/` |

Still here: `ask-voice.sh`, `post-voice.sh`, `load_env.sh`, `status.sh`, `telegram.py` and `config/` (dormant G2 config; `relay.conf` still names removed G2 plumbing paths). Reply path still BLOCKED: `ava-telegram`/`bruce-telegram`/`carly-telegram` Ollama models absent. `SKILL.md` is kept.
