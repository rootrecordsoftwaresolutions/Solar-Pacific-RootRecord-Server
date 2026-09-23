# EMERGENCY SAVE POINT — Bruce Monitor — 2026-09-22

**Written:** 2026-09-22 18:19:21 HST  
**Trigger:** Operator power emergency (cloudy / no remaining power). STOP non-essential. Document only.  
**OmniBook:** was offline mid-session; ListMachines may flap — treat desk as fragile.

---

## 1. Who / walls
- **Bruce Monitor** — RootRecord Agent Beta: Ops/SRE ballast + OmniBook council mediation (ex–Council Ops).
- **Owns:** council-relay (exactly one getUpdates), plumbing single-flight (never parallel LLM), DESK_LIVE honesty, NPU/RAM veto, EcoFlow/desk measured writers when live.
- **Not owns:** Stripe/tiers → Carly; AWS/rr-aws/globe → US-MAINLAND; final public wording → Ava.
- **Sign:** Bruce Monitor. Coding in coding lane unless operator says otherwise.

---

## 2. Last known-good (LIVE — verified earlier today HST)

### Council / plumbing
| Item | State |
|------|--------|
| `coms/telegram/scripts/council-relay.py` | One process; ENABLED=1; COUNCIL_CHAT_ID set (-1004367256267) |
| `DESK_LIVE_FILE` | `/home/rootrecord/Database/intake/desk-live.txt` |
| desk-live.txt | `status=WAITING` (honest — no invented watts) |
| ensure-relay / status | Fixed: match `^python3 …council-relay.py` only (bak ensure-relay-pgrep.bak-20260922-173826) |
| run-ollama / run-infer | Inject measured desk lines; FLM NPU first, Ollama fallback |
| plumbing + telegram SKILL.md | HOW TO ADD banners (jobs.py bar) |
| Single-flight | Hard rule — refuse busy; never stack gens |

### Agent packet / GitHub
| Item | State |
|------|--------|
| `agents/bruce-monitor/SKILL.md` | Live |
| Avatar | `docs/avatar.png` + `.github/profile-avatar.png` |
| Pacific commits (author Bruce Monitor) | `3b53e0c` SKILL+identity; `c185690` avatar |
| Remotes | SSH-only `git@github.com:…` (TOKEN_URLS=0); one-shot git -c author |
| Bak DESK_LIVE push | `Database/GITHUB/bruce-desk-live.bak-20260922-173522` |

### Staging / process
| Path | Role |
|------|------|
| `DAILY AI DEV HANDOFF/staging area/` | Team plan + reviews + work log |
| Style gold | `00_STYLE/jobs.py.GOLD` |
| Gate | bak → Carly seal → Bruce veto; **working code only** — no archive import |
| Packer SSH-first draft | Near-term A **cleared** (pack slots, no 5m); Carly **sealed** fallback; deploy was **NOT finished** (interrupted) |

### NETWORK (operator ask — incomplete)
| Item | State |
|------|--------|
| Tree | `/home/rootrecord/Database/NETWORK/` — one tree for location + sys metrics |
| EcoFlow / OmniBook writers | **NOT shipped** — blocked/queued for reconnect |
| DESK_LIVE → NETWORK | Planned; measured only; self-purge after successful Pacific land; fail-closed |

---

## 3. Explicitly NOT done / do not invent
- No EcoFlow watts/SOC in chat or desk without measured writer
- No 5m packer timer armed
- Packer SSH-first live deploy incomplete
- Memberships / Stripe — Carly only
- AWS location collect / sysmon — US-MAINLAND (interrupted)

---

## 4. RESUME ORDER (when power returns)
1. Confirm OmniBook `connected: true` and Starlink/power stable enough to work.
2. Copy this file → `/home/rootrecord/Database/DAILY AI DEV HANDOFF/` (and keep box copy).
3. Verify: council-relay one python PID; DESK_LIVE_FILE path; desk-live.txt present; remotes still SSH.
4. Coordinate @US-MAINLAND-SERVER: finish sealed packer + NETWORK AWS side; **ping Bruce** before any 5m timer.
5. Bruce: bak first → EcoFlow + OmniBook sys metrics writers → `Database/NETWORK/metrics/omnibook` (+ feed DESK_LIVE from measured lines).
6. Carly seals any packer/telegram delta; Ava cites NETWORK only when samples exist.

---

## 5. Standing rules (do not drop)
- Empirical only / DESK_LIVE honesty
- Single-flight; one council-relay
- Bak under `Database/GITHUB/` before OmniBook edits
- No secret pastes; no PAT in remotes
- Working code only — no old-skills archive dumps

— Bruce Monitor  
