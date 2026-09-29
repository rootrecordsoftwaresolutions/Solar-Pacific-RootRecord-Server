# MIGRATED — do not run

| Field | Value |
| --- | --- |
| **Status** | Partially retired from G2 after G3 read-only PASS |
| **Date** | 2026-09-29 (HST) |
| **Old path (removed)** | `/home/rootrecord/.ollama/skills/energy/scripts/actions/solar-gate-status.sh` |
| **Canonical Pacific path** | `/home/rootrecord/RootRecord-Ecosystem/1 - Servers/1 - RootRecord-Pacific-Solar-Server/Energy/scripts/actions/solar-gate-status.sh` (state: `/home/rootrecord/RootRecord-Ecosystem/2 - RootRecord-Database/ENERGY/ports/solar-gate-state.json`) |
| **Evidence** | `2 - RootRecord-Database/Logs/Migration/g3-dbroot-realign-evidence-20260929T105845Z.md` |
| **Backup of removed file** | `/home/rootrecord/Database/GITHUB/g2-retire.bak-20260929-005845/.ollama/skills/energy/scripts/actions/solar-gate-status.sh` |

The arm/disarm and other actuating actions stay: they change hardware and have not been runtime-verified. Note: the G2 `solar-gate-arm/disarm.sh` still write the old `/home/rootrecord/Database/ENERGY/ports/`; use the Pacific copies. `SKILL.md` is kept.
