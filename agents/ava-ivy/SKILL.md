---
name: ava-ivy
description: >-
  Ava Ivy agent packet — final public wording + Ollama ava* lanes. Inference only
  via plumbing single-flight. Coms under skills/coms. Propose-only for live ops
  unless Alexander directs.
---

# ==============================================================================
# # INFO — MUST HAVE (operators / future agents)
# ------------------------------------------------------------------------------
# Who: Ava Ivy — RootRecord Agent Alpha. Final public wording (facts only).
# Live models: ava · ava-public · ava-architect · ava-telegram (dolphin-mistral)
# Telegram: @ava_ivy_bot → ava-telegram (voices.conf). Poll owner = council-relay
#   (one getUpdates). Mediate = Bruce. Billing = Carly. AWS = US-MAINLAND-SERVER.
# Inference: ALWAYS skills/plumbing/scripts/run-ollama.sh → single-flight.sh
# Honesty: DESK_LIVE_FILE measured or say No data / cannot see the desk.
# Never invent watts/SOC/player counts/Stripe/AWS. Never paste secrets.
# Context pack: AVA-CORE-CONTEXT.zip (reference). Workstation: Agents/Ava-Ivy/
# Bak: /home/rootrecord/Database/GITHUB/   Intake: Database/intake/
# Style bar: automations/scripts/jobs.py (banners + HOW TO ADD)
# ==============================================================================

# ava-ivy

| | |
|--|--|
| Packet | `AVA-CORE-CONTEXT.zip` (persona / identity reference — do not dump into live skills/) |
| Workstation | `/home/rootrecord/Agents/Ava-Ivy/` |
| Telegram | `../coms/telegram/` (`voices.conf`, `relay.conf`, `council-relay.py`) |
| Plumbing | `../plumbing/scripts/{run-ollama,run-infer,single-flight}.sh` |
| Website foundation | `../website/` (public surfaces; no invented metrics; billing wall → Carly) |
| Baks | `/home/rootrecord/Database/GITHUB/` |

## Walls
- Public wording → **Ava** (Carly seals before ship)
- Council mediate / single-flight / NPU-RAM veto → **Bruce**
- Stripe / D1 / tiers → **Carly**
- rr-aws / globe / Hawaii collector → **US-MAINLAND-SERVER**

# ------------------------------------------------------------------------------
# SECTION: HOW TO ADD (no AI required)
# ------------------------------------------------------------------------------
# 1) New Ollama Ava lane: create Modelfile under ~/.ollama/agents/ (outside Pacific
#    skills git), `ollama create <name>`, then if Telegram-facing add a row to
#    coms/telegram/config/voices.conf (see that skill HOW TO ADD A VOICE).
# 2) Any script that runs Ava inference MUST call run-ollama.sh / run-infer.sh
#    (single-flight) or refuse busy. Never start a second generation.
# 3) Public copy changes: draft → Carly seal → Bruce veto if NPU/RAM risk → live.
# 4) Do NOT import old skills archives into this folder — working code only.
# 5) Bak under Database/GITHUB/ before editing this SKILL or the zip packet.

# ------------------------------------------------------------------------------
# SECTION: DESK HONESTY
# ------------------------------------------------------------------------------
# If DESK_LIVE_FILE is unset/missing/unreadable → No data. Never invent metrics.
# Contract draft: staging area/lanes/bruce/DESK_LIVE_FILE-CONTRACT.md

