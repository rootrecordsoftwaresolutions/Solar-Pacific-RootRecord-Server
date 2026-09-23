# RootRecord status — 2026-09-22 (HST) — END OF DAY

Authoritative “what is live **now**” after OmniBook rebuild day **and** evening power-emergency stop.  
Supersedes older session blockers and mid-evening FULL-RESUME greps where they conflict.  
Companion master: `MASTER-HANDOFF-FOR-EXTERNAL-AIS-2026-09-22.md`.

**Panel agents:** on break / rest after high weekly usage (~80%). External AIs provide coverage.

---

## 0. End-of-day truth (read this first)

| Item | State |
|------|--------|
| `collect_locations` | **Live** (confirm on AWS resume) |
| Packer datapath | **Telegram-only** (`RR_SSH_DATAPACK=0`) short-term |
| AWS root disk | **~90%** class after emergency cleanup (still tight) |
| DESK_LIVE | `Database/intake/desk-live.txt` → **`status=WAITING`** |
| council-relay | **May be down** after flicker — Bruce: one ensure-relay when stable; never dual-start |
| NETWORK writers | **Incomplete** — layout exists; EcoFlow / OmniBook writers **not shipped** |
| Vendor scrub | **Done** for handoff / Pacific emergency pack |
| Agents | **Break intent** — coverage AIs active |

---

## 1. OmniBook live stack

### Rootserver poller + Cloudflare
- Public: `https://rootserver.rootrecord.cloud/`
- Code: `~/.ollama/skills/automations/` (`rootserver_poller.py`, `jobs.py`, `poller-watch.py`)
- Shortcut: `/home/rootrecord/rootserver-poller` (`restart|stop|start|window|status`)
- **MUST:** Ctrl-C / stop kills poller + cloudflared + unit (not window-only)
- Local HTTP heartbeat: `http://127.0.0.1:8799/`
- Re-verify when OmniBook returns after power emergency.

### `jobs.py` boot order (priority)
0. self / status terminal  
1. Cloudflare tunnel  
2. GitHub `setup-all-remotes`  
3. `ollama_warmup`  
4. `flm_npu_warmup` (FastFlowLM)  
5. `council_relay` ensure (skips if legacy `apps.council` still running)

### Recurring
- Heartbeat every 5s  
- `github_sync_all` every 300s → `skills` + `website` + `mainland`

---

## 2. Data layout
| Path | Purpose |
|------|---------|
| `/home/rootrecord/Database/intake/` | Data we take in (`desk-live.txt`) |
| `/home/rootrecord/Database/GITHUB/` | Baks, logs, cutover scripts, worktrees |
| `/home/rootrecord/Database/NETWORK/` | One tree: datapacks / locations / metrics / charts |
| `/home/rootrecord/Database/RootRecord Context/` | Ideology / architecture docs |
| `/home/rootrecord/Database/DAILY AI DEV HANDOFF/` | **This pack** — zip for external AIs |

Never dump baks into `~/.ollama/skills/` (floods git autopush).

---

## 3. GitHub (three repos)
Configured in `~/.ollama/skills/github/scripts/repos.conf`:

| id | Mode | Local | GitHub |
|----|------|-------|--------|
| skills | inplace | `~/.ollama/skills` | Solar-Pacific-RootRecord-Server |
| website | mirror | `skills/website/site` | RootRecord-Website |
| mainland | inplace | `skills/us-mainland-server` | US-Mainland-Server |

Remotes: **SSH-only** (TOKEN_URLS=0).  
Pacific `.gitignore` excludes: `website/`, `us-mainland-server/`, `aws-sync/`, `plumbing/state/`, …  
`aws-sync` / rclone retired (GitHub push/pull model). AWS 1‑min pull timer may still need install on the mainland host.

---

## 4. Agents — Ollama + FLM (NPU)

### Ollama (CPU fallback) — `dolphin-mistral:latest` lanes
Desk: `~/.ollama/agents/` · registry `lanes.conf` · `create-all.sh`  
Models: `ava` / `ava-public` / `ava-architect` / `ava-telegram` · `bruce` / `bruce-ops` / `bruce-philosophy` / `bruce-telegram` · `carly` / `carly-appsec` / `carly-energy` / `carly-telegram` · `vision-reader` (staged)

**Honesty:** without measured desk → say cannot see desk / No data. Standing envelopes ≠ live readings.

### FastFlowLM (NPU) — preferred infer
- `flm serve … --host 127.0.0.1 --port 52625`
- Default chat model in plumbing: **`llama3.2:3b`**
- Entry: `~/.ollama/skills/plumbing/scripts/run-infer.sh` → FLM if up, else Ollama `*-telegram` → always `single-flight.sh`

### Plumbing
`~/.ollama/skills/plumbing/` — NPU-first policy, single-flight lock, warmup, pipelines (vision NPU still staged).

---

## 5. Telegram council (rebuilt)

**Not** the Data Relay (`@rootreceiver_bot` / `@rootsender_bot`).  
**Council group** chat id: `-1004367256267`

Live path: `~/.ollama/skills/coms/telegram/`
- `scripts/council-relay.py` — **one** getUpdates (poll token = Ava)
- Routing: `@one` → that bot only; pipeline phrases → A→B→C→A; silence cues → no post
- DESK_LIVE / HARD RULES must not leak outbound

Tokens as env names only: `TELEGRAM_AVA_TOKEN`, `TELEGRAM_BRUCE_TOKEN`, `TELEGRAM_CARLY_TOKEN` (never print values).

Advisor panel lane stays **manual** — no auto Telegram→Advisor.

**EOD:** council-relay process may be **down** — resume with one ensure-relay only.

---

## 6. Coms layout
Parent: `~/.ollama/skills/coms/`  
Children: `telegram/`, `discord/`, `slack/`, `ssh/` (+ staged `council/` notes).  
SSH skill = data-pack / AWS path (distinct from council).

---

## 7. Website
Skill desk: `~/.ollama/skills/website/` (Next.js foundation).  
GitHub: RootRecord-Website. Foundation only — status page No data/Waiting style.

---

## 8. US-MAINLAND / NETWORK (EOD)

- Hawaii collector path fixed earlier; re-verify active.
- Soft-park: `rr-ingest` disabled; `aws-sync` OFFLOADED; rclone helpers OFFLOADED.
- Packer: wipe-after-successful-send; voice-played Current prune added earlier.
- **Telegram-only** packs until SSH-first re-enabled with seals + Bruce ping.
- `collect_locations` **live**.
- NETWORK layout present; **writers incomplete**.
- AWS disk **~90%** — keep watching `hawaii.ndjson` / voice-played / logs.

---

## 9. Explicitly NOT done / Waiting
- Live EcoFlow / host-metrics wired into `DESK_LIVE_FILE` for infer (**Bruce**)
- NETWORK metric writers populated (**Bruce** + **US-MAINLAND**)
- Packer SSH-first as default path (sealed; Telegram-only temporary)
- AWS host systemd `aws-git-pull.timer` (1 min) — prepare locally; install when ready
- Vision NPU EP (staged docs only)
- Multi-bot DM long-poll (group @ works; DM poll Ava token only)
- Full legacy `apps.council` UX re-port
- Memberships live Stripe/D1 re-verify (**Carly**, proposal-only)
- Public NETWORK charts (**Ava** / **Advisor** after samples)
- Re-port of pre-reset skills from `Old-online-safe` zip (historical only unless operator names a module)

---

## 10. Team workload (excl. Advisor)
Bruce 32% · Carly 32% · US-MAINLAND 20% · Ava 16%

---

## 11. Quick operator commands
```bash
/home/rootrecord/rootserver-poller status|restart|window
bash ~/.ollama/skills/plumbing/scripts/run-infer.sh bruce 'one sentence status'
bash ~/.ollama/skills/coms/telegram/scripts/status.sh
pgrep -af 'council-relay|flm serve|rootserver_poller|apps.council'
bash ~/.ollama/skills/github/scripts/sync-all.sh
ssh rr-aws 'df -h /; systemctl is-active rr-packer; test -f ~/rootrecord/bin/collect_locations.py && echo HAS_collect_locations || echo NO_collect_locations'
```

---

## 12. Panel agents (context synced 2026-09-22)
Profiles mention Ollama lanes, plumbing single-flight, DESK_LIVE honesty, coms telegram relay, NPU-prefer FLM. Stopping points locked evening 2026-09-22. **Agents resting — use master handoff for coverage.**
