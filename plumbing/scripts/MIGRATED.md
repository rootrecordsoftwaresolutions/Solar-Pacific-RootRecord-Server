# MIGRATED — do not run

| Field | Value |
| --- | --- |
| **Status** | Partially retired from G2 after G3 runtime PASS |
| **Date** | 2026-09-29 (HST) |
| **Old path (removed)** | `/home/rootrecord/.ollama/skills/plumbing/scripts/ollama-warmup.sh` |
| **Canonical Pacific path** | `/home/rootrecord/RootRecord-Ecosystem/1 - Servers/1 - RootRecord-Pacific-Solar-Server/System/scripts/plumbing/ollama-warmup.sh` (poller job `ollama_warmup`) |
| **Evidence** | `2 - RootRecord-Database/Logs/Migration/g3-runtime-evidence-20260929T101550Z.md` (warmup) and `2 - RootRecord-Database/Logs/Migration/g3-energy-plumbing-evidence-20260929T104618Z.md` (single-flight) |
| **Backup of removed file** | `/home/rootrecord/Database/GITHUB/g2-retire.bak-20260929-004619/.ollama/skills/plumbing/scripts/ollama-warmup.sh` |

Still here on purpose: `single-flight.sh`, `run-ollama.sh`, `run-infer.sh` (the retained G2 Telegram relay and its `relay.conf` still point at them; Telegram has not passed G3), `flm-warmup.sh` (NPU gate BLOCKED), `npu-status.sh` (no Pacific counterpart). `SKILL.md` is kept.
