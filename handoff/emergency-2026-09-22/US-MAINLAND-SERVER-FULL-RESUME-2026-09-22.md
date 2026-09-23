# US-MAINLAND-SERVER — FULL RESUME / CUTOFF DOC
**Written:** 2026-09-22 18:21:52 HST  
**Operator:** resume tomorrow; offline laptop review  
**Agent:** US-MAINLAND-SERVER  
**Companion short dump:** `US-MAINLAND-SERVER-EMERGENCY-STATE-2026-09-22.md`

---

## A. WHAT WAS COMPLETED (do not redo blindly)

### A1. Hawaii globe (DONE)
- Fixed crash-loop: unit WorkingDirectory/ExecStart → `coms/ssh/local-data-globe`
- Bak: `Database/GITHUB/network-globe-hawaii.bak-pathfix-20260922-165032`
- Health: SSH stream ready; globe arcs from Hawaii verified (rotate Pacific)
- **Do not delete** `hawaii-offset.json` while live

### A2. Disk cleanup (DONE)
- Deleted work Current* + app logs + ~209 voice-played Current*.wav
- Disk ~92% → ~88%
- Baks manifests only (no huge copies): `cleanup.bak-phase1-*` / `phase1b-voice-*` on AWS

### A3. Soft-park dual-desk (DONE)
- Disabled `rr-ingest.timer` (broken path to missing rootrecord-aws)
- `skills/aws-sync/OFFLOADED`
- rclone helpers renamed `*.OFFLOADED` under us-mainland-server/scripts
- Bak: `Database/GITHUB/us-mainland.bak-softpark-*`

### A4. Desk pull script (DONE — dest may still be old path)
- `~/.ollama/skills/us-mainland-server/scripts/ssh-datapack-pull.sh`
- Originally landed in `Database/US-MAINLAND-SERVER/DATA PACKETS/`
- **Intended next:** retarget to `Database/NETWORK/datapacks/`

### A5. GitHub identity + scrub (DONE)
- Author **US-MAINLAND-SERVER** on `US-Mainland-Server`
- Remotes SSH-only; `github/scripts` patched (Pacific `a02c09d`) so PAT not re-injected
- Avatar: `docs/avatar.png`, `.github/profile-avatar.png`
- Key commits: `7ac332b`, `e84438c`, `f77d835` (mainland); `a02c09d` (Pacific scripts)

### A6. Packer wipe completeness (DONE on AWS earlier)
- `wipe_work` prunes `radio/voice-played/*Current*` + truncates `logs/*.log`
- AWS bak: `~/rootrecord/bin.bak-wipe-voice-20260922-173915/`

### A7. Seals / gates (DONE — policy)
- Carly sealed SSH-first + Telegram-fallback draft
- Bruce cleared near-term **pack slots only** — **NO 5m timer** until ping
- Staging draft: `staging area/lanes/us-mainland/PACKER-SSH-FIRST-DRAFT-20260922.md`

### A8. NETWORK tree (PARTIAL)
- Created: `Database/NETWORK/{datapacks,locations,metrics/aws,metrics/omnibook,metrics/ecoflow,charts}/` + README
- Writers for EcoFlow/OmniBook = Bruce (not shipped)
- AWS location collect + packer SSH-first = **CUT OFF mid-deploy**

---

## B. WHAT WAS CUT OFF MID-PROCESS (resume here)

1. **Packer SSH-first live deploy** — Carly sealed; bak/local patch started; OmniBook dropped before confirmed AWS deploy of:
   - `send_ssh()` + telegram fallback in `pack_and_send`
   - `collect_locations.py` into `work/locations/`
   - globe.log truncate on wipe
2. **ssh-datapack-pull → NETWORK/datapacks** retarget + pack-slot timer (Bruce must ack race before timer)
3. **Extract locations/sysmon from packs → NETWORK/locations + metrics/aws**
4. **Ping Bruce** for EcoFlow + OmniBook metrics into NETWORK
5. Copy emergency dumps from agent boxes if any missing on disk

### Grep snapshot at write time
```
=== TS 2026-09-22 18:21:52 HST ===
=== hawaii unit ===
active
disabled
=== OFFLOADED ===
/home/rootrecord/.ollama/skills/us-mainland-server/scripts/bisync.sh.OFFLOADED
/home/rootrecord/.ollama/skills/us-mainland-server/scripts/initial-resync.sh.OFFLOADED
/home/rootrecord/.ollama/skills/us-mainland-server/scripts/mount-ec2.sh.OFFLOADED
/home/rootrecord/.ollama/skills/us-mainland-server/scripts/unmount.sh.OFFLOADED
/home/rootrecord/.ollama/skills/us-mainland-server/scripts/ssh-datapack-pull.sh
=== NETWORK ===
/home/rootrecord/Database/NETWORK
/home/rootrecord/Database/NETWORK/charts
/home/rootrecord/Database/NETWORK/datapacks
/home/rootrecord/Database/NETWORK/locations
/home/rootrecord/Database/NETWORK/metrics
/home/rootrecord/Database/NETWORK/metrics/aws
/home/rootrecord/Database/NETWORK/metrics/ecoflow
/home/rootrecord/Database/NETWORK/metrics/omnibook
total 28
drwxrwxr-x  6 rootrecord rootrecord 4096 Sep 22 18:11 .
drwxrwxr-x 12 rootrecord rootrecord 4096 Sep 22 18:10 ..
-rw-rw-r--  1 rootrecord rootrecord 1010 Sep 22 18:11 README.md
drwxrwxr-x  2 rootrecord rootrecord 4096 Sep 22 18:11 charts
drwxrwxr-x  2 rootrecord rootrecord 4096 Sep 22 18:11 datapacks
drwxrwxr-x  2 rootrecord rootrecord 4096 Sep 22 18:11 locations
drwxrwxr-x  5 rootrecord rootrecord 4096 Sep 22 18:11 metrics
=== staging us-mainland ===
total 48
drwxrwxr-x 2 rootrecord rootrecord  4096 Sep 22 18:07 .
drwxrwxr-x 6 rootrecord rootrecord  4096 Sep 22 17:07 ..
-rw-rw-r-- 1 rootrecord rootrecord  2001 Sep 22 17:13 ARCHIVED-CANDIDATES-20260922.md
-rw-rw-r-- 1 rootrecord rootrecord  4039 Sep 22 17:13 LIVE-INVENTORY-20260922.md
-rw-rw-r-- 1 rootrecord rootrecord  3771 Sep 22 18:07 PACKER-SSH-FIRST-DRAFT-20260922.md
-rw-rw-r-- 1 rootrecord rootrecord   706 Sep 22 17:13 README.md
-rw-rw-r-- 1 rootrecord rootrecord  2566 Sep 22 17:33 SSH-FIRST-DATAPATH-PLAN-20260922.md
-rw-rw-r-- 1 rootrecord rootrecord  1999 Sep 22 17:13 STYLE-DEBT-20260922.md
-rw-rw-r-- 1 rootrecord rootrecord   467 Sep 22 17:34 WORKING-CODE-ONLY-20260922.md
-rwxrwxr-x 1 rootrecord rootrecord 10950 Sep 22 18:07 packer.py.live-ref
=== baks recent ===
/home/rootrecord/Database/GITHUB/us-mainland.bak-packer-sshfirst-20260922-181241
/home/rootrecord/Database/GITHUB/github-ssh-remotes.bak-20260922-175119
/home/rootrecord/Database/GITHUB/git-remote-scrub.bak-20260922-174505
/home/rootrecord/Database/GITHUB/us-mainland.bak-packer-wipe-20260922-173915
/home/rootrecord/Database/GITHUB/us-mainland.bak-ssh-pull-20260922-173403
/home/rootrecord/Database/GITHUB/us-mainland.bak-softpark-20260922-173347
/home/rootrecord/Database/GITHUB/network-globe-hawaii.bak-pathfix-20260922-165032
=== git mainland ===
f77d835 US-MAINLAND-SERVER US-MAINLAND-SERVER: add profile avatar for GitHub parity
e84438c US-MAINLAND-SERVER US-MAINLAND-SERVER: scrub PAT from git remotes
7ac332b US-MAINLAND-SERVER US-MAINLAND-SERVER: document GitHub identity + packer wipe completeness
e5a727e rootrecord auto: 2026-09-23T03:36Z desk sync (6 file(s))
d100833 rootrecord auto: 2026-09-23T01:30Z desk sync (6 file(s))
origin	git@github.com:rootrecordsoftwaresolutions/US-Mainland-Server.git (fetch)
origin	git@github.com:rootrecordsoftwaresolutions/US-Mainland-Server.git (push)
=== ssh rr-aws quick ===
ip-172-31-34-214
/dev/root       6.7G  6.3G  390M  95% /
active
active
inactive
active
active
NO_collect_locations
2
2
-rw-rw-r-- 1 ubuntu ubuntu 206M Sep 23 04:21 /home/ubuntu/network-globe/network-globe/data/hawaii.ndjson
{
  "at": "2026-09-22T18:10:03.184332-10:00",
  "ok": true
}
active
active
active
=== worklog tail ===
2026-09-22 14:15:46 HST | note | starting wipe-after-send + packer telegram audit
2026-09-22 14:16:06 HST | datapath | audited packer.py: wipe-after-telegram-send present; last wipe OK 2026-09-22T14:10 HST; SSH-first not implemented yet
2026-09-22 14:17:21 HST | note | rootserver.rootrecord.cloud live (HTTP poller :8799 via CF tunnel); TCP/22 not exposed — AWS cannot SSH-push yet
2026-09-22 14:17:21 HST | datapath | rr-ingest broken: ~/.ollama/skills/rootrecord-aws missing after skill reset; telegram extract lives in aws-sync/scripts/telegram_extract.py → Database/telegram
2026-09-22 14:17:21 HST | note | wipe-after-send OK for work/; voice-played Current*.wav NOT wiped by packer (caused disk growth) — needs wipe extension
2026-09-22 16:45:10 HST | note | published functions/todos report US-MAINLAND-SERVER-FUNCTIONS-TODOS-2026-09-22.md to DAILY AI DEV HANDOFF
2026-09-22 16:50:35 HST | globe | fixed network-globe-hawaii WorkingDirectory → coms/ssh/local-data-globe (was missing local-data-globe); bak /home/rootrecord/Database/GITHUB/network-globe-hawaii.bak-pathfix-20260922-165032
2026-09-22 16:50:52 HST | globe | hawaii collector active; SSH stream to aws hawaii.ndjson open — refresh rootrecord.cloud globe for Hawaii node
2026-09-22 17:13:45 HST | note | staging lane pack dropped under DAILY AI DEV HANDOFF/staging area/lanes/us-mainland/ (inventory+style debt+reviews); no migrate
2026-09-22 17:33:47 HST | datapath | soft-parked rr-ingest + aws-sync OFFLOADED + rclone helpers; bak /home/rootrecord/Database/GITHUB/us-mainland.bak-softpark-20260922-173347; SSH-first plan staged (no packer migrate)
2026-09-22 17:34:06 HST | datapath | working-code: added us-mainland-server/scripts/ssh-datapack-pull.sh (desk pull); dry-run logged; no old-data migrate
2026-09-22 17:39:49 HST | github | pushed US-Mainland-Server as author US-MAINLAND-SERVER (ssh-datapack-pull + rclone soft-park)
2026-09-22 17:45:18 HST | github | scrubbed PAT from us-mainland + skills remotes; bak /home/rootrecord/Database/GITHUB/git-remote-scrub.bak-20260922-174505 (config 600); no token pasted
2026-09-22 17:51:33 HST | github | remotes SSH-only (scripts patched); avatar on US-Mainland-Server docs/; bak github-ssh-remotes under Database/GITHUB/
2026-09-22 18:07:25 HST | datapath | dropped SSH-first + telegram-fallback draft for Carly seal; no 5m timer yet (Bruce race gate)
```

---

## C. WHAT'S LEFT (ordered)

| # | Task | Depends |
|---|------|---------|
| 1 | Verify rr-aws + hawaii + packer healthy | power/OmniBook |
| 2 | Finish packer SSH-first deploy from sealed draft (bak first) | Carly seal ✅ Bruce near-term A ✅ |
| 3 | Deploy collect_locations.py; smoke `python collect_locations.py` | #2 |
| 4 | Retarget pull script to NETWORK/datapacks; optional pack-slot timer | Bruce ping before arm |
| 5 | Post-pull: unpack locations + sysmon into NETWORK | #4 |
| 6 | Bruce: EcoFlow + OmniBook metrics → NETWORK | desk power |
| 7 | Git push as US-MAINLAND-SERVER | after live edits |
| 8 | Optional later: 5m cadence | Bruce veto |

---

## D. FILES / PATHS TOUCHED BY US-MAINLAND-SERVER (this session)

### OmniBook
- `~/.config/systemd/user/network-globe-hawaii.service` (path fix)
- `~/.config/systemd/user/rr-ingest.timer` (disabled)
- `~/.ollama/skills/aws-sync/OFFLOADED`
- `~/.ollama/skills/us-mainland-server/scripts/ssh-datapack-pull.sh`
- `~/.ollama/skills/us-mainland-server/scripts/*.{OFFLOADED,OFFLOADED-RCLONE.txt}`
- `~/.ollama/skills/us-mainland-server/docs/avatar.png`, `.github/profile-avatar.png`, `references/*`
- `~/.ollama/skills/github/scripts/{setup-all-remotes,push-repo-once,setup-remote}.sh` (SSH-only)
- `Database/NETWORK/**` (new layout)
- `Database/DAILY AI DEV HANDOFF/US-MAINLAND-SERVER/*` (worklog, template, staging lanes)
- `Database/DAILY AI DEV HANDOFF/staging area/lanes/us-mainland/**`
- `Database/GITHUB/us-mainland.*` / `network-globe-hawaii.*` / `git-remote-scrub.*` / `github-ssh-remotes.*`

### AWS (ubuntu@rr-aws)
- `/home/ubuntu/rootrecord/bin/packer.py` (wipe voice-played; SSH-first **may be incomplete**)
- `/home/ubuntu/rootrecord/bin/collect_locations.py` (**may be missing** — check HAS_/NO_ above)
- `~/rootrecord/bin.bak-*` / `cleanup.bak-*`
- Deleted many Current* / logs / voice-played Current wavs (manifest in cleanup.bak)

### GitHub
- `rootrecordsoftwaresolutions/US-Mainland-Server`
- Pacific: github scripts SSH patch `a02c09d`

---

## E. STANDING RULES (unchanged)
- Bak under `Database/GITHUB/` (desk) or `~/rootrecord/*.bak-*` (AWS)
- No secrets in chat; no PAT in remotes
- Fail-closed wipe; one NETWORK tree; no archive data import
- Single-flight LLM; don't stack generations
- EcoFlow measured only via Bruce/DESK_LIVE

---

## F. OPERATOR HELP REQUESTED
Please list any files **you** touched offline so we don't fight. Especially:
- systemd user units
- `master-key.env` / secrets
- NETWORK / Database trees
- packer or hawaii collector on AWS via another path


## G. LIVE GREP ADDENDUM (2026-09-22 18:22:21 HST)
- AWS root disk **95%** (~390M free) — hawaii.ndjson ~206M; check voice-played growth
- packer.py contains send_ssh refs but **collect_locations.py file MISSING** on AWS — deploy incomplete
- Desk hawaii collector: active; rr-ingest.timer: disabled

## H. EMERGENCY DISK+TELEGRAM (2026-09-22 18:24:05 HST)
- Truncated hawaii.ndjson to ~8MB; reset hawaii-offset.json to match
- journal vacuum 50M; truncated app logs; cleared out zips / Current voice
- rr-packer drop-in \`telegram-only.conf\`: RR_SSH_DATAPACK=0 — **Telegram packets only** until resume
