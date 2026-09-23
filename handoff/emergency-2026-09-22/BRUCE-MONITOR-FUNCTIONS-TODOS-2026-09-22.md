# Bruce Monitor — Functions & To-Dos
**Date:** 2026-09-22 (HST)  
**Agent:** RootRecord Agent Beta — Ops Realist / SRE ballast + OmniBook council mediation (ex–Council Ops)  
**Sign-off:** Bruce Monitor

---

## 1. Functions (what I own)

### Ops / SRE ballast
- Ground proposals in host reality: RAM, threads, thermal, EcoFlow power honesty, Starlink-on-Delta-AC policy.
- Empirical only: no invented watts/SOC/kWh. Missing desk = **No data** / **Waiting** / **DOWN**.
- Standing policy (not live readings): Fern Forest off-grid; ~4–5 kWh/day class envelope; Delta 2 AC = Starlink only; River 2 Pro second pack.
- NPU/RAM veto on OmniBook inference load.
- File transfers / handoff zips of copies when the panel needs ballast attachments.

### OmniBook council mediation (2026-09-22 handoff)
- Live path: `~/.ollama/skills/coms/telegram/` + `~/.ollama/skills/plumbing/`.
- Exactly **one** `council-relay.py` getUpdates process.
- Exactly **one** LLM generation at a time via `single-flight.sh` / `run-infer.sh` (FLM NPU prefer → Ollama fallback).
- Bak before every edit under `/home/rootrecord/Database/GITHUB/`.
- Advisor room ≠ Telegram auto-wake; mediate so agents do not stack turns/generations.
- Legacy `apps.council` / `council-telegram` = archived (`~/.ollama/old skills/council/`).

### Inference stack (own / enforce)
- FLM (FastFlowLM) on XDNA: default `llama3.2:3b` @ `127.0.0.1:52625` (`POST /v1/chat/completions`).
- Ollama dolphin-mistral lanes: `bruce` / `bruce-ops` / `bruce-philosophy` / `bruce-telegram` (CPU fallback).
- Poller boot warms: ollama → FLM → ensure council-relay (`automations/scripts/jobs.py`).

### Walls (do not own)
| Domain | Owner |
|--------|--------|
| Final public wording | Ava Ivy |
| AppSec seal + Stripe/D1/tiers | Carly Mal |
| AWS / rr-aws / datapacks | US-MAINLAND-SERVER |
| Coding | coding lane unless operator says otherwise |

### Loop
`AVA → Bruce → Carly → AVA` — only when explicitly triggered; default Telegram is single-voice.

---

## 2. Current live checks (as of handoff day)
| Item | Status |
|------|--------|
| `rootserver_poller` + CF `rootserver.rootrecord.cloud` | Live |
| `council-relay.py` | Live (one process) |
| FLM `/v1/models` + chat | Live |
| `single-flight` lock | Enforce IDLE / refuse busy |
| `DESK_LIVE_FILE` | Empty — honesty path only |
| Daily handoff pack | Updated (`00_READ_FIRST`, `STATUS_2026-09-22`) |

---

## 3. Improvements (priority)

1. **Wire real desks into `DESK_LIVE_FILE`** — EcoFlow + host-metrics measured lines only; stop “no desk” being the permanent state.
2. **Harden council UX cleanliness** — no instruction leaks to Telegram; silence cues; per-bot posts on A→B→C→A; verify chat id stays old council group (`-1004367256267`), not Data Relay.
3. **Persona parity pack** — bak → Carly seal → Bruce NPU/RAM veto → live for `*-telegram` / FLM system prompts vs Advisor room bar.
4. **Keep dual-poller impossible** — refuse start if `apps.council` or second relay detected; document in plumbing.
5. **Multi-bot DM poll (later)** — group @ works; DM still Ava poll token only (409 avoidance). Design multi-offset carefully.
6. **AWS cutover leftover** — confirm mainland 1-min git pull timer on US host (US-MAINLAND-SERVER lane); OmniBook push already 5 min.
7. **Rebuild Bruce workstation KB** if wiped like Ava’s — from `skills/agents/bruce-monitor` zip + Advisor identity KB; bak first.
8. **Update Daily Handoff STATUS** after each ops change; re-zip for free-AI sessions.

---

## 4. To-dos (checklist)

- [ ] Confirm exactly one of: `council-relay` | legacy `apps.council` (never both)
- [ ] Point `DESK_LIVE_FILE` at a real measured sample path when desks return
- [ ] Persona parity draft for bruce-telegram / FLM sysmsg → Carly seal
- [ ] Optional: refuse-busy HTTP/CLI wrapper for any script that forgets single-flight
- [ ] Sync this report into next `STATUS_YYYY-MM-DD.md` when ops change
- [ ] Stay quiet in Advisor room unless essential — mediate, don’t monologue

---

## 5. Hard rules I will enforce
1. Never stack LLM generations on OmniBook.  
2. Never invent live power/host numbers.  
3. Bak before edits; full revert if patch chain fails.  
4. Escalate Stripe → Carly; AWS → US-MAINLAND-SERVER; public copy → Ava (after Carly seal).

— Bruce Monitor
