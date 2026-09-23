# READ FIRST — Daily AI Dev Handoff

**As of:** 2026-09-22 (Hawaiʻi / HST)  
**Operator:** Alexander Storey (Alexrs94) — Fern Forest, Big Island, 100% off-grid  
**Purpose of this folder:** zip + hand to free AI accounts so they understand the ecosystem, workflows, and **current** status without inventing state.

## Read order (do not skip)
1. **This file**
2. `STATUS_2026-09-22.md` — live stack after today’s work (authoritative for “what runs now”)
3. `AGENT_Current_Understanding.md` — longer checkpoint history (Sessions 1–4); correct anything that conflicts with STATUS
4. `RootRecord Context/` — ideologies / agent framework foundation (v0.03)
5. Topic folders only as needed: `US-MAINLAND-SERVER/`, `How to connect to US-MAINLAND-SERVER.md`, `INSTALL-hawaii-collector.md`, `Github Copies/`

## Hard rules for any AI using this pack
- **Empirical only.** Missing live desk = `No data` / `Waiting` / `DOWN`. Never invent watts, SOC, kWh/day as current readings.
- Standing site envelope (~4–5 kWh/day gen, ~2 kWh storage; Delta 2 AC = Starlink only; River 2 Pro second pack) is **policy**, not a live measurement.
- **Do not print tokens** from `master-key.env` or `~/.config/ava-council/secrets.env`.
- **One getUpdates poller** for council Telegram. Dual pollers → HTTP 409.
- **One inference at a time** on OmniBook (`skills/plumbing` single-flight).
- Prefer **NPU via FastFlowLM** when up; Ollama is CPU fallback for persona Modelfiles.
- Outside-world I/O lives under `~/.ollama/skills/coms/` (not scattered).
- Coding stays in **Cursor** unless the operator says otherwise.

## Machines (short)
| Role | What |
|------|------|
| OmniBook (Solar Pacific RootRecord Server) | Live skills, poller, FLM/NPU, council relay, Starlink/solar site |
| US-Mainland-Server (AWS) | Always-on collectors / globe / radio — own GitHub; OmniBook pushes, AWS should pull |
| Grok Bot panel | Ava Ivy / Bruce Monitor / Carly Mal — manual Grok↔Telegram bridge only |

## Agent loop
`AVA → Bruce → Carly → AVA`  
Ava = public/architect · Bruce = ops ballast · Carly = AppSec seal (never Clara).

When finished a work session: update `STATUS_YYYY-MM-DD.md` (or append a SESSION block) and re-zip this folder.
