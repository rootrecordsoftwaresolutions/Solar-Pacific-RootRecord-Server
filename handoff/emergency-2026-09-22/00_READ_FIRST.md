# READ FIRST — Daily AI Dev Handoff

**As of:** 2026-09-22 end of day (Hawaiʻi / HST)  
**Operator:** Alexander Storey (Alexrs94) — Fern Forest, Big Island, 100% off-grid  
**Purpose:** Brief external / coverage AIs while panel agents rest (weekly usage ~80%).

## Primary entry (do not skip)
1. **`MASTER-HANDOFF-FOR-EXTERNAL-AIS-2026-09-22.md`** — THE combined long handoff. Start here.
2. `STATUS_2026-09-22.md` / `STATUS_LATEST.md` — live stack + end-of-day truth
3. Per-agent `*-STOPPING-POINT-2026-09-22.md` for the lane you touch
4. `*-FULL-RESUME-*` / `*-EMERGENCY-STATE-*` only as needed
5. `AGENT_Current_Understanding.md` — longer history; **master + STATUS win** on conflicts
6. Topic folders only as needed: `US-MAINLAND-SERVER/`, connect docs, `staging area/`

## Hard rules for any AI using this pack
- **Empirical only.** Missing live desk = `No data` / `Waiting` / `DOWN`. Never invent watts, SOC, kWh/day, player counts, or coords as current readings.
- Standing site envelope (~4–5 kWh/day gen, ~2 kWh storage; Delta 2 AC = Starlink only; River 2 Pro second pack) is **policy**, not a live measurement.
- **Do not print tokens** from `master-key.env` or `~/.config/ava-council/secrets.env`.
- **One getUpdates poller** for council Telegram. Dual pollers → HTTP 409.
- **One inference at a time** on OmniBook (`skills/plumbing` single-flight).
- Prefer **NPU via FastFlowLM** when up; Ollama is CPU fallback for persona Modelfiles.
- Outside-world I/O lives under `~/.ollama/skills/coms/` (not scattered).
- Coding stays in the **coding lane** unless the operator says otherwise.
- Gate: **bak → Carly seal → Bruce veto**; working code only — no archive import.
- Remotes **SSH-only**; fail-closed purge; **no vendor product names** in docs.
- Panel ↔ Telegram stays **manual** (ops room ≠ auto-wake).

## Machines (short)
| Role | What |
|------|------|
| OmniBook (Solar Pacific RootRecord Server) | Live skills, poller, FLM/NPU, council relay, Starlink/solar site |
| US-Mainland-Server (AWS) | Always-on collectors / globe / radio — own GitHub; OmniBook pushes, AWS should pull |
| Advisor panel | Ava Ivy / Bruce Monitor / Carly Mal / US-MAINLAND / Advisor — manual Advisor↔Telegram bridge only |

## Agent loop
`AVA → Bruce → Carly → AVA`  
Ava = public/architect · Bruce = ops ballast · Carly = AppSec seal (never Clara).

## End-of-day snapshot (2026-09-22)
- `collect_locations` live; **Telegram-only** packs short-term; AWS disk ~90%
- DESK_LIVE `WAITING`; council-relay may be down; NETWORK writers incomplete; EcoFlow writers not shipped
- Vendor scrub done; **panel agents on break** — external coverage

When finished a work session: update `STATUS_YYYY-MM-DD.md` (and master if material) and re-zip this folder.
