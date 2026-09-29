# MIGRATED — do not run

| Field | Value |
| --- | --- |
| **Status** | Partially retired from G2 after G3 runtime PASS (Plumbing non-NPU) |
| **Date** | 2026-09-29 (HST) |
| **Old path (removed)** | `/home/rootrecord/.ollama/skills/plumbing/scripts/ollama-warmup.sh` |
| **Canonical Pacific path** | `/home/rootrecord/RootRecord-Ecosystem/1 - Servers/1 - RootRecord-Pacific-Solar-Server/System/scripts/plumbing/ollama-warmup.sh` (poller job `ollama_warmup`) |
| **Evidence** | `2 - RootRecord-Database/Logs/Migration/g3-dbroot-realign-evidence-20260929T105845Z.md` |
| **Backup of removed file** | `/home/rootrecord/Database/GITHUB/g2-retire.bak-20260929-005845/.ollama/skills/plumbing/scripts/ollama-warmup.sh` |

**2026-09-29 01:17 HST update:** `run-ollama.sh` and `run-infer.sh` also removed (G2 Telegram relay retired after G3 relay PASS; zero live references). Backup: `/home/rootrecord/Database/GITHUB/g2-retire.bak-20260929-011731/.ollama/skills/plumbing/scripts/`. Evidence: `2 - RootRecord-Database/Logs/Migration/g3-poller-realign-evidence-20260929T111731Z.md`. Canonical: Pacific `System/scripts/plumbing/`.

Still here on purpose: `single-flight.sh` (G2 `npu-status.sh` still calls it), `flm-warmup.sh` (NPU BLOCKED), `npu-status.sh`. `SKILL.md` is kept.
