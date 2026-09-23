---
name: plumbing
description: >-
  Inference pipelines for RootRecord: NPU-first (FLM) when available, hard
  single-flight (one model/agent run at a time), DESK_LIVE honesty. Not a coms
  skill — wires how brains run.
---

# ==============================================================================
# # INFO — MUST HAVE (operators / future agents)
# ------------------------------------------------------------------------------
# What: single-flight lock + FLM/NPU infer + Ollama fallback + DESK_LIVE gate
# Paths: scripts/{single-flight,run-infer,run-ollama}.sh · state/ · references/
# Bak: /home/rootrecord/Database/GITHUB/   Intake desk: Database/intake/desk-live.txt
# Style bar: automations/scripts/jobs.py (banners + HOW TO ADD)
# Walls: mediate/NPU-RAM → Bruce · billing → Carly · AWS → US-MAINLAND · public → Ava
# ==============================================================================

# plumbing

| Piece | Path | Role |
|-------|------|------|
| Single-flight lock | `scripts/single-flight.sh` | `flock` — **one** inference job on this host |
| FLM/NPU + fallback | `scripts/run-infer.sh` | Prefer FLM `:52625`; Ollama on fail |
| Ollama wrapper | `scripts/run-ollama.sh` | Always takes the lock; attaches DESK_LIVE when set |
| NPU policy | `references/NPU-FIRST.md` | Prefer NPU; honesty on Ollama |
| Pipelines | `pipelines/*.md` | Staged runbooks |
| Desk file | `DESK_LIVE_FILE` (relay.conf) | Measured lines only; missing → No data |

**MUST:** never start a second model/agent run while one holds the inference lock.
**MUST:** every `ava*` / `bruce*` / `carly*` entry uses these scripts or **refuse busy**.

State dir: `/home/rootrecord/.ollama/skills/plumbing/state/`

# ------------------------------------------------------------------------------
# SECTION: HOW TO ADD an inference entrypoint
# ------------------------------------------------------------------------------
# 1) Call `scripts/run-infer.sh <voice|model> 'prompt'` (preferred) or `run-ollama.sh`.
# 2) Do **not** call `ollama run` / FLM curl directly from a skill — skips lock + desk.
# 3) If single-flight is busy → exit non-zero / refuse busy (do not queue-stack gens).
# 4) Bak under Database/GITHUB/ before editing these scripts.

# ------------------------------------------------------------------------------
# SECTION: HOW TO ADD a warmup
# ------------------------------------------------------------------------------
# 1) One owner path only (flm-warmup.sh **or** ollama-warmup.sh — Bruce clears dual).
# 2) Add a labeled job in automations/scripts/jobs.py — never a second silent loop.
# 3) Warmup must not hold the inference lock longer than needed.
