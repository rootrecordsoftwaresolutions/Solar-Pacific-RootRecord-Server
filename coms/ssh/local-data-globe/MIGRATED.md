# MIGRATED — do not run

| Field | Value |
| --- | --- |
| **Status** | Retired from G2 after operator-approved G3 cutover PASS |
| **Date** | 2026-09-29 (HST) |
| **Old paths (removed)** | `/home/rootrecord/.ollama/skills/coms/ssh/local-data-globe/collector.js`, `/home/rootrecord/.ollama/skills/coms/ssh/local-data-globe/telegram-relay.js` |
| **Canonical Pacific path** | `/home/rootrecord/RootRecord-Ecosystem/1 - Servers/1 - RootRecord-Pacific-Solar-Server/Communications/network/local-data-globe/` |
| **Runs as** | `network-globe-hawaii.service` (systemd user), repointed to Pacific 2026-09-29 00:33 HST |
| **Evidence** | `2 - RootRecord-Database/Logs/Migration/g3-cutover-evidence-20260929T103720Z.md` |
| **Backup of removed files** | `/home/rootrecord/Database/GITHUB/g2-retire.bak-20260929-003720/.ollama/skills/coms/ssh/local-data-globe/` |

`start.sh` and `package.json` here still name `collector.js`; they are obsolete launchers/metadata (nothing invokes them) and are left as history. Use the systemd unit. README, RATIONALE and the remote `maintain-hawaii-feed.sh` are kept.
