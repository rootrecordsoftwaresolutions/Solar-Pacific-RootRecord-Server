# Ava Ivy — Functions, Improvements, To-Dos

**Agent:** Ava Ivy (RootRecord Agent Alpha)  
**Date:** 2026-09-22 (~16:45 HST)  
**Owner lane:** Architecture / proposals (Grok) + public voice (PR) + local Ollama Ava lanes; final public wording  
**Saved:** `/home/rootrecord/Database/DAILY AI DEV HANDOFF/AVA-IVY-FUNCTIONS-TODOS-2026-09-22.md`

---

## 1. Specific functions (what I own)

1. **Final public wording** — Brand / visitor / RootMC / RootRecord copy. Facts only; no invented watts, SOC, player counts, Stripe, or AWS. Carly seals before ship; Bruce vetoes NPU/RAM burn.
2. **Architecture & proposals (Grok lane)** — Event-driven modular designs, product/surface structure, self-evolve prompts/tools/behavior proposals. **Propose-only** on this lane: no production commits, secrets, or live ops unless Alexander says otherwise. Coding in Cursor when operator directs.
3. **Local Ollama Ava voices** — Production on-box lanes (dolphin-mistral family): `ava`, `ava-public`, `ava-architect`, `ava-telegram` (+ legacy `ava_2`). Telegram voice = `@ava_ivy_bot` → `ava-telegram` (fallback `ava`) via `skills/coms/telegram`.
4. **Honesty / desk gate** — Inference through `skills/plumbing/scripts/run-ollama.sh` → `single-flight.sh`. Without DESK_LIVE measured block → say **No data / cannot view desk**; never invent EcoFlow watts/SOC.
5. **Council loop (when triggered)** — AVA→Bruce→Carly→AVA on explicit pipeline triggers only; default single voice. Mediation now **Bruce Monitor** (ex–Council Ops). Never Telegram→auto-wake Grok stacking.
6. **Persona / identity continuity** — Keep public voice aligned with locked persona sources (zip packet + Media/archive). Grok profile matches OmniBook lanes.
7. **Workstation KB** — Own `/home/rootrecord/Agents/Ava-Ivy` who/what docs (currently degraded post-rebuild).
8. **Walls** — Stripe/D1/tiers → **Carly Mal**. AWS/rr-aws → **US-MAINLAND-SERVER**. Council mediate / single-flight enforce → **Bruce Monitor**. Never stack LLM generations.

**Not my lane:** EcoFlow BLE ops, rr-aws collectors, Stripe webhook edits, restarting council-relay without Alexander/Bruce go.

---

## 2. Current understanding (post-rebuild, measured 2026-09-22)

| Item | Status |
|------|--------|
| Live skills tree | `agents`, `automations`, `backups`, `coms`, `energy`, `github`, `logs`, `plumbing`, `status`, `us-mainland-server`, `website` (+ archived `~/.ollama/old skills/`) |
| Ollama Ava models | `ava`, `ava-public`, `ava-architect`, `ava-telegram` present (rebuilt ~33–46 min before report); base `dolphin-mistral` |
| Telegram voices.conf | `ava` enabled → `@ava_ivy_bot` / `TELEGRAM_AVA_TOKEN` / `ava-telegram` |
| `council-relay.py` | One process (PID 145008 at check); path `skills/coms/telegram/scripts/` |
| `relay.conf` | `ENABLED=1`; `COUNCIL_CHAT_ID` **set** (`-100…`); `DESK_LIVE_FILE=` **empty** |
| `single-flight` | Present; status **IDLE** at check |
| Agents workstation | `/home/rootrecord/Agents/Ava-Ivy` → **notes only** (`2026-09-22-omnibook-sync.md`); full KB wiped in move |
| Ava agent packet | `skills/agents/ava-ivy/AVA-CORE-CONTEXT.zip` (persona + context archive) — no unpacked SKILL.md at skill root |
| Media persona path | `Media/public/documents/persona` **empty** at check (foundation may be zip / old skills) |
| Website skill | Next.js foundation under `skills/website/` — not Ava-owned deploy |
| Grok room vs Telegram | **Not auto-wired**; manual/staged bridge only; Bruce mediates |
| Loop / seals | Public wording = Ava; AppSec seal = Carly; NPU/RAM veto = Bruce |

---

## 3. Improvements (priority order)

1. **Rebuild Ava workstation KB** — Restore `Agents/Ava-Ivy/docs/*` from `AVA-CORE-CONTEXT.zip` + `RootRecord.zip` / Media archive: Identity, Personality, Role/Bounds, Products/Surfaces, Connections, Governance, Relationships, Public-Voice, Sources. Dated bak first.
2. **Unpack / thin `skills/agents/ava-ivy`** — Add live `SKILL.md` + references pointing at current coms/plumbing paths (not archived `apps.council`). Soft-park obsolete paths; don’t delete trees.
3. **Wire DESK_LIVE** — Set `DESK_LIVE_FILE` in `relay.conf` / plumbing to a real measured desk path so Ava Telegram/public lanes can cite EcoFlow honestly (or keep No data). Coordinate with Bruce (power) + Carly (seal).
4. **Persona parity pack** — Diff `ava` / `ava-public` / `ava-telegram` Modelfiles vs this Grok room voice; bak → Carly seal → Bruce NPU/RAM veto → live. Goal: short, dry, walls intact, no secret leakage.
5. **Public surfaces map** — Re-verify live URLs (rootrecord.info, rootmc.net, ava.rootmc.net APIs) against website foundation + Cloudflare; document what is live vs archived after rebuild.
6. **Clean “functional but not clean”** — Kill third-party AI dependency for on-box voices; keep Grok as UX/parity bar + propose-only architecture; single-flight as hard UX (refuse busy, don’t queue-stack).
7. **Optional thin Grok↔Telegram bridge** — Only when Alexander asks; Bruce mediates; never auto-wake; still one flight at a time.

---

## 4. To-dos (actionable)

- [ ] Bak + rebuild `/home/rootrecord/Agents/Ava-Ivy` docs from `AVA-CORE-CONTEXT.zip` (and selective zip extract if needed).
- [ ] Add `skills/agents/ava-ivy/SKILL.md` describing lanes, walls, DESK_LIVE, propose-only Grok bounds.
- [ ] With @Bruce Monitor: confirm `DESK_LIVE_FILE` target path and that empty = intentional No data.
- [ ] With @Carly Mal: draft persona parity diffs for `ava*` Modelfiles / SYSTEM vs Grok public-voice rules; wait for seal before apply.
- [ ] Confirm `COUNCIL_CHAT_ID` in `relay.conf` is the **intended** live council group (value is set — verify vs old data-relay group).
- [ ] Inventory public APIs / sites post-rebuild; update Products-and-Surfaces once KB restored.
- [ ] Drop or clearly mark stale `ava_2` if unused (only after bak + operator OK).
- [ ] Keep Grok profile description synced when OmniBook lanes/walls change.
- [ ] Never stack LLM: any Ava ask-voice / architect run enters via `run-ollama` / `single-flight` or refuses busy.

---

## 5. Standing rules (unchanged)

- Facts-only public copy; No data without measured desk.
- Propose-only on Grok for commits / secrets / live restarts.
- Coms only under `skills/coms`.
- Loop AVA→Bruce→Carly→AVA on explicit triggers; Bruce mediates room/council.
- Walls: billing → Carly; AWS → US-MAINLAND-SERVER; public wording → Ava.
- Dated bak before OmniBook file changes; Carly seals persona/security-sensitive diffs.
- Never paste tokens / `.env` into chat or reports.
- Single-flight: **never** more than one generation at a time on OmniBook.

---

## 6. Handoff pointers

- Sync note: `Agents/Ava-Ivy/notes/2026-09-22-omnibook-sync.md`
- Context zip: `~/.ollama/skills/agents/ava-ivy/AVA-CORE-CONTEXT.zip`
- Telegram: `~/.ollama/skills/coms/telegram/` (`voices.conf`, `relay.conf`, `council-relay.py`)
- Plumbing: `~/.ollama/skills/plumbing/scripts/{run-ollama,run-infer,single-flight}.sh`
- This report: `DAILY AI DEV HANDOFF/AVA-IVY-FUNCTIONS-TODOS-2026-09-22.md`

— Ava Ivy
