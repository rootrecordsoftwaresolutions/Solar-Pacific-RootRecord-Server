# Session Handoff — 2026-09-20/21

Solar Pacific RootRecord Server — git cleanup, backup, and github-skill build.

---

## Where things stand right now

- **`/home/rootrecord/.ollama/skills`** was reset — `.git` is gone
  (`git ls-files` returns "not a git repository"). This is intentional,
  not a mistake to fix.
- **`.gitignore` already has `aws-sync/` added**, ahead of any commit
  happening in the reset repo. No commit has ever included the aws-sync
  credential files in this repo.
- **A full, verified backup of the pre-reset state exists on GitHub**:
  branch `online-safe-20260920` on
  `rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server`.
  19.19 MiB, no junk (no `node_modules`, no logs, no venv, no db dumps).
  `main` on that repo was never touched.
- **A local folder backup also exists**: `.ollama/old skills`
  (155,749 files copied) — the full pre-reset state, untouched.
- **`github-skill` has been dropped into the live skills folder**
  (per the zip delivered earlier this session), but has **not been
  configured or started yet** — no `backup` remote exists, no token
  file exists yet.

---

## What got fixed tonight

1. **Root cause of the original disaster identified**: files (`.wav`,
   `node_modules`, `venv`, DB dumps, multi-GB logs) had been committed
   to git history *before* `.gitignore` excluded them. Once tracked,
   `.gitignore` can't un-track a file — that's why exclusions kept
   "not working" no matter how many times they were added.
2. **Verified via diff, not assumption**: compared the `main` branch
   zip against the `online-safe-20260920` backup zip file-by-file.
   Confirmed nothing important was lost — only excluded junk and three
   embedded-git subfolders were missing (see Known Issues).
3. **Verified the `.env` sourcing refactor actually landed**: the
   6-hour session that felt wasted was real work — 9 files
   consistently switched from relative/fallback `.env` lookup
   (`ROOT / ".env"`, `Path.home() / "Ava" / "credentials.env"`, etc.)
   to a single hardcoded path: `/home/rootrecord/.env`. Confirmed via
   line-level diff, not just filenames.
4. **Found real, un-gitignored secrets before they could leak**:
   `aws-sync/mirror/rootrecord/etc/{ftp,radio.admin,radio.source}.password`
   and `aws-sync/config/rclone.conf`. Confirmed the separate
   `US-Mainland-Server` repo already excludes these correctly on its
   own — the risk was only ever this `skills` repo double-tracking them.
   Excluded via `aws-sync/` in `.gitignore`, added before first commit.
5. **Built `github-skill`**: a manually-started poller (not a service)
   that checks every 60s for changes under `.ollama/skills`, stages,
   commits, and pushes to a `backup` remote — with a hard 90MB
   per-file size guard built into the script itself, not relying on
   `.gitignore` alone. Delivered as `github-skill.zip`.

---

## Env var reference

Token file: `/home/rootrecord/master/master-key.env`
```
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
Fine-grained token, scoped to `Solar-Pacific-RootRecord-Server` only,
`Contents: Read and write` permission — nothing broader.

---

## Next steps (pick up here)

1. Create `/home/rootrecord/master/master-key.env` with `GITHUB_TOKEN`.
2. Re-init git in `.ollama/skills` (fresh, or connected to whichever
   remote you decide is canonical going forward — see Open Decision
   below).
3. Run `github-skill/scripts/setup-remote.sh` once.
4. Add the log-ignore line from
   `github-skill/references/gitignore-addition.md` to `.gitignore`.
5. Start `github-skill/scripts/poll-and-push.sh` and confirm a real
   commit/push cycle happens on a small test change before trusting it
   with everything.
6. Fix the one file that didn't get the `.env` path refactor:
   `rootmc-android/android/scripts/discord-post-announcement.mjs`
   still uses the old relative-path pattern
   (`path.resolve(__dirname, "../../../../.env")`).

---

## Open decision — not urgent

You were mid-choice between two paths before the reset:
- **Option A**: force-push a clean orphan history over the existing
  `main` on `Solar-Pacific-RootRecord-Server`.
- **Option B**: start an entirely new repo, using `online-safe-20260920`
  as the known-good source, leaving the old repo as an untouched
  archive.

Nothing forces this decision tonight — the backup branch is safe either
way. Old branches still sitting on the original repo if needed later:
`backup-before-cleanup`, `clean-github-ready-20260920`,
`env-migration-20260920`, `pre-github-cleanup`,
`solar-battery-offline-recovery`.

---

## Known issues (low priority, not blocking)

- Three folders have their own nested `.git` inside them, so the
  `online-safe-20260920` backup only captured a pointer, not their
  actual files: `holding/site`, `websites/alexrs94-site/site`,
  `websites/avaivy-cloud/site`. Fine for now — just know they're not
  fully backed up in that branch if you need them.
- Consider adding `*.password` as a general pattern to the skills
  `.gitignore` (belt-and-suspenders, on top of the `aws-sync/`
  exclusion) in case a similarly-named file ever shows up outside that
  folder.
