# MIGRATED — do not run

| Field | Value |
| --- | --- |
| **Status** | Retired from G2 after operator-approved G3 cutover PASS |
| **Date** | 2026-09-29 (HST) |
| **Old path (removed)** | `/home/rootrecord/.ollama/skills/energy/scripts/ble/ble-owner.py` |
| **Canonical Pacific path** | `/home/rootrecord/RootRecord-Ecosystem/1 - Servers/1 - RootRecord-Pacific-Solar-Server/Energy/scripts/ble/ble-owner.py` |
| **Runs as** | `ava-ecoflow-ble.service` (systemd user), repointed to Pacific 2026-09-29 00:35 HST |
| **Log / pid now** | `/home/rootrecord/Database/Logs/Energy/ava-ecoflow-ble.log` / `/home/rootrecord/Database/ENERGY/state/ava-ecoflow-ble.pid` |
| **Evidence** | `2 - RootRecord-Database/Logs/Migration/g3-cutover-evidence-20260929T103720Z.md` |
| **Backup of removed file** | `/home/rootrecord/Database/GITHUB/g2-retire.bak-20260929-003720/.ollama/skills/energy/scripts/ble/ble-owner.py` |

`ble-start.sh`, `ble-stop.sh`, `ble-status.sh` and `ble-log-watch.sh` stay (they act on the unit, not on this file). G2 `energy/config/devices.conf` still names the old path; it is dormant G2 config. `SKILL.md` is kept.
