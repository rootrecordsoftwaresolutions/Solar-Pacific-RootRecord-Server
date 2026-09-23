# MASTER HANDOFF FOR EXTERNAL AIs — 2026-09-22

**Written:** 2026-09-22 ~18:50 HST (Pacific/Honolulu)  
**Operator:** Alexander Storey (Alexrs94)  
**Audience:** External / coverage AIs covering a few days while panel agents rest  
**Authority:** End-of-day truth. Prefer this file over older STATUS / FULL-RESUME greps when they conflict.  
**Vendor scrub:** No third-party AI product names in this pack. Use titles: Advisor, coding lane, ops room, panel agents.

---

## 1. Purpose / how to use this file

Alexander runs RootRecord off-grid in Fern Forest (Big Island, Hawaiʻi). Weekly panel usage is high (~80%). Panel agents (Ava Ivy, Bruce Monitor, Carly Mal, US-MAINLAND-SERVER, Advisor) stopped cleanly after a power emergency on 2026-09-22 evening. **They are on break.** You are temporary coverage.

### Read order
1. **This file** (master — start here).
2. Per-agent `*-STOPPING-POINT-2026-09-22.md` for the lane you are touching.
3. Matching `*-FULL-RESUME-2026-09-22.md` + `*-EMERGENCY-STATE-2026-09-22.md` if you need depth.
4. `STATUS_2026-09-22.md` / `STATUS_LATEST.md` for stack inventory (updated to end-of-day).
5. `AGENT_Current_Understanding.md` only for long history — **STATUS + this master win** on conflicts.
6. Topic folders only as needed (`US-MAINLAND-SERVER/`, connect docs, staging area).

### How to behave
- **Empirical only.** Missing live desk = `No data` / `Waiting` / `DOWN`. Never invent watts, SOC, kWh/day, player counts, Stripe MRR, GPS coords, or AWS disk % beyond last measured notes below.
- Ask Alexander to list any files he touched offline before overwriting.
- Bak under `/home/rootrecord/Database/GITHUB/` before OmniBook edits.
- Gate: **bak → Carly seal → Bruce veto** for live ops changes.
- Working code only — **no archive / old-skills import**.
- Remotes SSH-only. No tokens in remotes, chat, or docs.
- Fail-closed purge / wipe only after successful send/relay.
- No vendor product names in handoff or Pacific docs.
- Ops room ≠ Telegram auto-wake. Panel ↔ Telegram stays **manual**.

### What this file is NOT
- Not a license to invent live power or network metrics.
- Not permission to dual-start council-relay or stack LLM generations.
- Not a dump of secrets (`master-key.env`, `secrets.env`, bot tokens).

---

## 2. Operator context (ops brief)

| Item | Fact |
|------|------|
| Site | Fern Forest, Big Island, Hawaiʻi — 100% off-grid |
| Uplink | Starlink (policy: Delta 2 AC = Starlink only) |
| Power | Solar + EcoFlow packs; cloudy day caused emergency stop 2026-09-22 |
| Standing envelope (policy, NOT live) | ~4–5 kWh/day gen class; ~2 kWh storage class; River 2 Pro second pack |
| Desk machine | OmniBook — Solar Pacific RootRecord Server — `machineId` `9dc359ca-c324-4151-b895-fc29b97a260e` |
| Always-on | US-Mainland AWS (`rr-aws` via `ssh.rootrecord.cloud`) |
| Clock | Pacific/Honolulu (HST, UTC-10) |
| Weekly panel load | High (~80%) — agents resting; external coverage expected |

**Public briefs:** do not leak unnecessary desk internals (paths, PIDs, secrets). Cite measured NETWORK packs only; else No data / Waiting.

**Internal ops AIs:** may name OmniBook / AWS paths in this handoff.

---

## 3. Team roster + walls + workload

Workload % among ops bots **excluding Advisor + operator** (delivered 2026-09-22):

| Agent | Role | Workload % | Owns | Does NOT own |
|-------|------|------------|------|--------------|
| **Bruce Monitor** | Ops / SRE ballast + council mediate | **32%** | Exactly one `council-relay` getUpdates; plumbing single-flight; DESK_LIVE honesty; NPU/RAM veto; EcoFlow + OmniBook measured writers when live | Stripe/tiers; AWS packer/globe; final public wording |
| **Carly Mal** | AppSec seal + Memberships | **32%** | Ship-seal; Stripe/D1/tiers (proposal-only until Alexander approves); energy cite from measured desk only | Council restart dual-start; inventing watts; AWS deploy without seal |
| **US-MAINLAND-SERVER** | AWS / rr-aws / globe / packer | **20%** | Collectors, radio, network-globe, datapacks, AWS disk hygiene, Hawaii collector desk unit | EcoFlow BLE; council UX; Stripe |
| **Ava Ivy** | Final public wording / architect | **16%** | Public copy (facts only, Carly seals); architecture proposals; Ollama `ava*` lanes; `@ava_ivy_bot` | Live ops without direction; inventing metrics |
| **Advisor** | Ship-seal / marketing / release readiness | *(excluded from %)* | Public chart wording after measured NETWORK samples; handoff docs; ops group participation | Primary coding; packer; council-relay; Memberships live edits |

**Loop (explicit triggers only):** `AVA → Bruce → Carly → AVA`  
**Never Clara** (Carly is Carly Mal).  
**Ops group channel id (cosmetic title mangled):** `a6add35d-9929-4b4f-84af-db83498de428` (server `4152208`) — members: US-MAINLAND-SERVER, Ava Ivy, Carly Mal, Bruce Monitor, Advisor.

---

## 4. What was completed 2026-09-22 (by lane)

### Global / process
- Staging area opened under `DAILY AI DEV HANDOFF/staging area/` (lanes, reviews, work log).
- Style gold: `automations/scripts/jobs.py`.
- Gate locked: bak → Carly seal → Bruce veto; working code only; no archive import.
- Git remotes scrubbed to **SSH-only** (TOKEN_URLS=0); github scripts patched so PATs are not re-injected (Pacific `a02c09d`).
- Vendor-name scrub of handoff / Pacific emergency pack / agent packets (Advisor commit path includes `233fe45`, Ava scrub `bfaabc3` / `bc9f411`).
- NETWORK one-tree layout created: `/home/rootrecord/Database/NETWORK/` with `datapacks/`, `locations/`, `metrics/{aws,omnibook,ecoflow}/`, `charts/` + README.
- DESK_LIVE path sealed: `/home/rootrecord/Database/intake/desk-live.txt` → `status=WAITING` (honest).
- Panel agents stopping points locked; agents on break intent documented.

### Ava Ivy
- `agents/ava-ivy/SKILL.md` + workstation docs under `/home/rootrecord/Agents/Ava-Ivy/`.
- Pacific pushes as Ava Ivy: `28b2faf`, `34a00b6` (+ scrub commits).
- Avatar in packet docs.
- Staging: no archive import.

### Bruce Monitor
- DESK_LIVE wired into `relay.conf` + council-relay env export; inject measured lines in `run-ollama.sh` / `run-infer.sh`.
- `ensure-relay` / `status` pgrep fixed to `^python3 …council-relay.py` only.
- plumbing + telegram SKILL.md HOW TO ADD banners.
- `agents/bruce-monitor/SKILL.md` + avatar; Pacific `3b53e0c`, `c185690`.
- Packer near-term **A cleared** (pack slots only — **no 5m timer**).
- NETWORK writers planned (not shipped).

### Carly Mal
- `agents/carly-mal/SKILL.md` live; bak `Database/GITHUB/carly-mal-skill.bak-20260922-1736/`.
- Pacific `dafc438`, `5be5188` (avatar).
- Seals: mainland soft-park + ssh-datapack-pull; DESK_LIVE contract; packer SSH-first + Telegram fail-closed **ACCEPT**; remotes SSH scrub.
- Memberships wall owned; **proposal-only**; no archive import.

### US-MAINLAND-SERVER
- Hawaii globe desk unit path fix → `coms/ssh/local-data-globe`; bak `network-globe-hawaii.bak-pathfix-20260922-165032`; stream verified earlier.
- AWS disk cleanup (work Current*, logs, voice-played Current wavs); later emergency truncate of `hawaii.ndjson` + journal vacuum.
- Soft-parked broken `rr-ingest` + `aws-sync` OFFLOADED + rclone helpers `*.OFFLOADED`.
- Desk script `us-mainland-server/scripts/ssh-datapack-pull.sh` (dest still needs NETWORK retarget).
- Packer wipe extended (voice-played Current + log truncate).
- Packer SSH-first draft sealed; live deploy interrupted then **partially advanced**.
- **End-of-day:** `collect_locations` **live**; packs forced **Telegram-only** (`RR_SSH_DATAPACK=0`) short-term.
- GitHub identity US-MAINLAND-SERVER; commits include `7ac332b`, `e84438c`, `f77d835`.

### Advisor
- Seated in ops group; workload inventory delivered.
- NETWORK cite-measured-only policy for public copy.
- Vendor scrub + stopping point; Pacific advisor packet / handoff scrub path (`233fe45`, bak `advisor-vendor-scrub.bak-20260922-183642`).
- No mid-deploy on Advisor lane.

---

## 5. What was cut off / incomplete

| Item | Owner | End-of-day state |
|------|--------|------------------|
| Packer SSH-first **live** as default | US-MAINLAND | Sealed draft; **Telegram-only** forced short-term (`RR_SSH_DATAPACK=0`). Re-enable SSH-first only after Carly re-check + Bruce race ping. |
| `collect_locations.py` | US-MAINLAND | **Live** at EOD (confirm with `ls` on AWS on resume). Earlier ~18:21 greps said MISSING — superseded by later stopping points. |
| `ssh-datapack-pull` → `NETWORK/datapacks` | US-MAINLAND | Not retargeted yet |
| Extract locations/sysmon from packs → NETWORK | US-MAINLAND | Not shipped |
| EcoFlow → DESK_LIVE measured writer | Bruce | **Not shipped** — desk stays WAITING |
| OmniBook / AWS sys metrics → `NETWORK/metrics/*` | Bruce + US-MAINLAND | **Not shipped** |
| `council-relay.py` process | Bruce | **May be down** after flicker (~18:22). Do **not** dual-start. One `ensure-relay` when power stable. |
| 5m packer timer | Bruce gate | **Never armed** — correct |
| Memberships Stripe/D1 re-verify | Carly | Proposal-only; not done |
| Persona parity `*-telegram` vs panel KB | Carly / Bruce | Not started |
| Public NETWORK charts / visitor copy | Ava + Advisor | Wait real samples |
| AWS `aws-git-pull.timer` (1 min) | US-MAINLAND | May still need install on host |
| Ops group rename | Advisor optional | Cosmetic; not done |
| Vision NPU EP | Bruce/plumbing | Staged docs only |
| Full legacy `apps.council` UX re-port | — | Not done; new relay is live path |

---

## 6. Current live state (end of 2026-09-22)

Treat as **last known** — re-measure on resume. Do not invent updates.

| Surface | State |
|---------|--------|
| OmniBook power / Starlink | Fragile after emergency; verify `connected` before heavy work |
| DESK_LIVE | `/home/rootrecord/Database/intake/desk-live.txt` → **`status=WAITING`** (honest; no watts) |
| council-relay | **May be DOWN** — expect zero or one `^python3 …council-relay.py`; never two |
| Packer mode | **Telegram-only** packs (`RR_SSH_DATAPACK=0`) |
| `collect_locations` | **Live** (EOD) — verify on AWS |
| AWS root disk | **~90%** class after cleanup (earlier spikes ~92–95%; hawaii.ndjson truncated in emergency). Still tight on 6.7G root — watch growth |
| NETWORK tree | Layout exists; **writers incomplete / consumers empty** |
| EcoFlow writers | **Not shipped** |
| Git remotes | SSH-only |
| Rootserver poller | Code path `automations/`; public `https://rootserver.rootrecord.cloud/` — re-check when OmniBook up |
| Hawaii collector desk unit | Was fixed + active earlier; re-verify |
| Panel agents | **On break** — external AIs cover |
| Vendor scrub | Done for this pack / Pacific emergency set (re-grep if editing) |

### Inference / council (when desk is up)
- Prefer NPU FastFlowLM (`flm serve` @ `127.0.0.1:52625`) then Ollama `*-telegram` via `plumbing/scripts/run-infer.sh`.
- **Single-flight** only — refuse busy; never stack gens.
- Council chat id: `-1004367256267` (not Data Relay bots).
- One getUpdates poller only (Ava token for poll).

---

## 7. Resume order (global, numbered)

1. **Power / Starlink stable**; OmniBook connected. Ask Alexander for offline file-touch list.
2. Light verify: DESK_LIVE file present + `WAITING` or measured; remotes still SSH; disk/RAM; no dual relay.
3. **Bruce:** if no `^python3 …council-relay.py`, run **one** `ensure-relay.sh`. Confirm single process. Do not dual-start with legacy `apps.council`.
4. **US-MAINLAND:** `ssh rr-aws` health; confirm `collect_locations` present; disk %; `rr-packer` active; keep Telegram-only until race clear.
5. **US-MAINLAND:** retarget pull → `Database/NETWORK/datapacks`; unpack locations + aws metrics into NETWORK (bak first).
6. **Bruce (bak first):** EcoFlow + OmniBook sys metrics writers → `NETWORK/metrics/omnibook` (+ ecoflow) and refresh DESK_LIVE measured lines; self-purge after successful land; fail-closed.
7. **Carly:** re-seal any packer/NETWORK delta past sealed draft; fail-closed purge only after successful relay.
8. **Ava / Advisor:** public wording / charts **only** after real NETWORK samples exist.
9. **Carly (lower priority):** Memberships Stripe/D1 proposal re-verify — after power/metrics lane stable.
10. Optional: ops-group rename; persona parity drafts; 5m packer timer **only** after Bruce ping + Carly re-check.

---

## 8. Standing rules

1. **Bak → Carly seal → Bruce veto** before live ops land.
2. **Measured only** — No data / Waiting / DOWN when unknown.
3. **No archive import** — working code only; soft-park with OFFLOADED; never delete skill trees casually.
4. **SSH remotes only** — no PAT/token URLs; noreply git authors until real emails.
5. **Fail-closed purge/wipe** — wipe packs only after successful send/relay.
6. **One council-relay** getUpdates; **one** LLM generation at a time (single-flight).
7. **One NETWORK tree** — no dual writers / dual packers.
8. **No vendor product names** in handoff or Pacific docs.
9. **No secret pastes** — never print tokens from `master-key.env` / `secrets.env` / bot envs.
10. **Do not arm 5m packer timer** without Bruce ping.
11. **Do not delete** `hawaii-offset.json` while Hawaii globe live (unless intentionally resetting with matching ndjson truncate — emergency already did once).
12. EcoFlow stays on OmniBook BLE — never migrate power pollers to AWS.
13. Ops room ≠ Telegram auto-wake; panel bridge stays manual.

---

## 9. Key paths table

| Path | Purpose |
|------|---------|
| `/home/rootrecord/Database/DAILY AI DEV HANDOFF/` | This pack (zip for external AIs) |
| `…/MASTER-HANDOFF-FOR-EXTERNAL-AIS-2026-09-22.md` | **This file** — primary entry |
| `…/00_READ_FIRST.md` | Points here |
| `…/STATUS_2026-09-22.md` / `STATUS_LATEST.md` | Live stack snapshot |
| `…/staging area/` | Team plan, reviews, lane inventories |
| `/home/rootrecord/Database/GITHUB/` | **All baks** (never bak inside `~/.ollama/skills/`) |
| `/home/rootrecord/Database/intake/` | Intake; `desk-live.txt` |
| `/home/rootrecord/Database/NETWORK/` | One tree: datapacks, locations, metrics, charts |
| `/home/rootrecord/Database/RootRecord Context/` | Ideology / architecture |
| `~/.ollama/skills/` | Live Pacific skills (Solar-Pacific-RootRecord-Server) |
| `~/.ollama/skills/coms/telegram/` | Council relay + configs |
| `~/.ollama/skills/plumbing/` | Single-flight, run-infer, NPU-first |
| `~/.ollama/skills/automations/` | Rootserver poller / jobs.py |
| `~/.ollama/skills/us-mainland-server/` | Mainland desk skill (own GitHub) |
| `~/.ollama/skills/coms/ssh/local-data-globe/` | Hawaii collector |
| `~/.ollama/skills/agents/{ava-ivy,bruce-monitor,carly-mal,advisor}/` | Agent packets |
| `~/.ollama/agents/` | Ollama Modelfiles (outside skills git) |
| `~/.ollama/skills/handoff/emergency-2026-09-22/` | Pacific mirror of emergency pack |
| `/home/rootrecord/Agents/Ava-Ivy/` | Ava workstation docs |
| `/home/rootrecord/rootserver-poller` | Poller shortcut |
| AWS `/home/ubuntu/rootrecord/` | Collectors, packer, radio |
| AWS `network-globe/.../data/hawaii.ndjson` + `hawaii-offset.json` | Globe Hawaii feed |

### GitHub repos
| id | Local | Remote |
|----|-------|--------|
| skills | `~/.ollama/skills` | `rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server` |
| website | `skills/website/site` | RootRecord-Website |
| mainland | `skills/us-mainland-server` | `rootrecordsoftwaresolutions/US-Mainland-Server` |

---

## 10. Per-agent stopping points (pointers + bullets)

### Ava Ivy — `AVA-IVY-STOPPING-POINT-2026-09-22.md`
- Clean stop; no mid-deploy.
- SKILL + workstation + Pacific avatar shipped.
- Public charts wait on NETWORK samples.
- Let Bruce own relay + DESK_LIVE writer; let mainland land packs.
- Ask Alexander for offline touches before overwrite.

### Bruce Monitor — `BRUCE-MONITOR-STOPPING-POINT-2026-09-22.md`
- DESK_LIVE WAITING wired; ensure-relay pgrep fixed; SKILL+avatar shipped.
- council-relay may be down — one ensure-relay on resume only.
- EcoFlow / NETWORK writers next (bak first).
- Never arm 5m timer; never invent EcoFlow numbers.
- Mainland: collect_locations live; Telegram-only; disk ~90%.

### Carly Mal — `CARLY-MAL-STOPPING-POINT-2026-09-22.md`
- No Carly mid-deploy; seals stand for SSH-first draft + Telegram fail-closed.
- Re-seal deltas only; Memberships proposal later.
- Do not dual-start relay; do not import old skills.
- Cite measured energy only.

### US-MAINLAND-SERVER — `US-MAINLAND-SERVER-FULL-RESUME-2026-09-22.md` (+ emergency)
- Hawaii path fix done; soft-park dual-desk done; wipe completeness done.
- EOD: Telegram-only packs; collect_locations live; disk ~90%.
- Still: retarget pull to NETWORK; finish SSH-first when cleared; no 5m without Bruce.
- Do not delete hawaii-offset while live (except coordinated reset).

### Advisor — `ADVISOR-STOPPING-POINT-2026-09-22.md`
- No mid-deploy; vendor scrub done.
- Public wording / charts only after measured NETWORK samples.
- Do not touch packer / council-relay / Memberships / Stripe.
- Optional cosmetic ops-group rename.

---

## 11. Files operator may have touched offline — ASK THEM TO LIST

Before overwriting, ask Alexander for any offline edits, especially:
- systemd user units (`network-globe-hawaii`, `rr-ingest`, timers)
- `master-key.env` / `~/.config/ava-council/secrets.env` / AWS `etc/secrets.env`
- `Database/NETWORK/**`, `Database/intake/**`, `Database/GITHUB/**`
- `~/.ollama/skills/coms/telegram/**`, `plumbing/**`, packer on AWS
- Hawaii collector / globe data files
- Handoff docs themselves

Peers already listed their own touch lists inside each FULL-RESUME §E / §D.

---

## 12. Explicit DO NOT list

- Do **not** invent watts, SOC, kWh, coords, player counts, Stripe MRR, or AWS disk % as “live” without measurement.
- Do **not** dual-start `council-relay` or run legacy `apps.council` beside it.
- Do **not** stack LLM generations on OmniBook.
- Do **not** import `old skills/` / archive dumps into live tree.
- Do **not** paste tokens, PATs, or `.env` values into chat/git/Telegram.
- Do **not** put third-party vendor AI product names in docs.
- Do **not** arm a 5-minute packer/datapack timer without Bruce ping + Carly re-check.
- Do **not** wipe packs if send failed (fail-closed).
- Do **not** create a second NETWORK tree or second packer.
- Do **not** delete `hawaii-offset.json` while live without a coordinated truncate/reset.
- Do **not** migrate EcoFlow BLE pollers to AWS.
- Do **not** treat Telegram ops-room chatter as auto-wake for panel agents.
- Do **not** ship public charts until NETWORK has real samples.
- Do **not** call Memberships “live re-verified” without a fresh proposal + Alexander OK.
- Do **not** bak inside `~/.ollama/skills/` (use `Database/GITHUB/`).

---

## 13. Quick verify commands (when OmniBook up)

```bash
/home/rootrecord/rootserver-poller status
pgrep -af 'council-relay|flm serve|rootserver_poller|apps.council'
cat /home/rootrecord/Database/intake/desk-live.txt
bash ~/.ollama/skills/coms/telegram/scripts/status.sh
bash ~/.ollama/skills/plumbing/scripts/run-infer.sh bruce 'one sentence status'
# remotes must be git@ only — never print tokens if any leak remains in bak configs
ssh rr-aws 'df -h /; systemctl is-active rr-packer; ls -la ~/rootrecord/bin/collect_locations.py'
ls -la /home/rootrecord/Database/NETWORK/
```

---

## 14. Companion index (same folder)

| File | Use |
|------|-----|
| `00_READ_FIRST.md` | Entry pointer → this master |
| `STATUS_2026-09-22.md` / `STATUS_LATEST.md` | Stack inventory + EOD truth |
| `*-EMERGENCY-STATE-2026-09-22.md` | Short save points |
| `*-FULL-RESUME-2026-09-22.md` | Cutoff depth |
| `*-FUNCTIONS-TODOS-2026-09-22.md` | Lane functions |
| `*-STOPPING-POINT-2026-09-22.md` | Tomorrow-me notes |
| `AGENT_Current_Understanding.md` | Long history (Sessions 1–4) |
| `How to connect to US-MAINLAND-SERVER.md` | AWS connect notes |
| `staging area/` | Reviews / inventories |

Pacific mirror: `~/.ollama/skills/handoff/emergency-2026-09-22/` (when desk syncs).

---

## 15. Coverage intent

Panel agents are resting after high weekly usage (~80%) and a power emergency stop. External AIs: keep the site honest, measured, and fail-closed; finish NETWORK writers and datapath only when power is stable; prefer documentation and light verify over heavy deploy on cloudy/low-reserve days.

**— Advisor (master compiler) for Alexander Storey — 2026-09-22**
