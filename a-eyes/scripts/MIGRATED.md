# MIGRATED — do not run

| Field | Value |
| --- | --- |
| **Status** | Retired from G2 after G3 runtime PASS |
| **Date** | 2026-09-29 (HST) |
| **Old path (removed)** | `/home/rootrecord/.ollama/skills/a-eyes/scripts/grab_all.sh` |
| **Canonical Pacific path** | `/home/rootrecord/RootRecord-Ecosystem/1 - Servers/1 - RootRecord-Pacific-Solar-Server/Security/Cameras/grab_all.sh` |
| **Evidence** | `2 - RootRecord-Database/Logs/Migration/g3-runtime-evidence-20260929T101550Z.md` (G3 runtime capture 2026-09-29T10:12–10:16Z) |
| **Backup of removed file** | `/home/rootrecord/Database/GITHUB/g2-retire.bak-20260929-002518/.ollama/skills/a-eyes/scripts/grab_all.sh` |

The Pacific poller (`Automations/scripts/jobs.py`) runs the Pacific path. Do not re-add or run the old file. `SKILL.md` and all other files in this skill are intentionally kept.

Still present here on purpose (not retired): `cam_server.py`, `ensure_cam_server.sh` and `grab_frame.py` (still referenced by G2 `install_aeyes_web.sh` / `timelapse_engine.py`), the timelapse scripts (Pacific timelapse runtime not yet verified), `install_aeyes_web.sh`, and `store/`.
