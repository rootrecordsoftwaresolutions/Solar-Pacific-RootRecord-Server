# github-skill

Purpose: watch every subfolder under `/home/rootrecord/.ollama/skills` for
any change and push it to GitHub automatically, on a short poll interval,
without ever repeating the 14GB / `.gitignore`-not-sticking disaster from
before.

This is a MANUAL poller, not a systemd service. You start it yourself in a
terminal (or `tmux`/`screen` session) when you want it running, and stop it
with Ctrl+C. Nothing runs unless you launch it.

## Env var name (as requested)

Token lives at: `/home/rootrecord/master/master-key.env`

The scripts expect exactly one variable in that file:

```
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Use a **fine-grained GitHub personal access token**, scoped to only the
`Solar-Pacific-RootRecord-Server` repo, with `Contents: Read and write`
permission. Nothing else needed. Do not use a classic token with full repo
access if you can avoid it.

## One-time setup

```bash
bash scripts/setup-remote.sh
```

This reads `GITHUB_TOKEN` from the env file above and configures a second
git remote called `backup` (leaves your existing `origin` alone) pointed at:

```
https://x-access-token:<token>@github.com/rootrecordsoftwaresolutions/Solar-Pacific-RootRecord-Server.git
```

The token gets written into `.git/config` for this remote, same as any
git credential — that file is not itself pushed anywhere, but treat this
machine as needing the same security you'd give the token itself.

## Running it

```bash
bash scripts/poll-and-push.sh
```

Every 5 minutes (300 seconds) it will:
1. Check `git status --porcelain` under `/home/rootrecord/.ollama/skills`.
2. If nothing changed, sleep and check again.
3. If something changed, check every changed/new file's size first.
   - Any single file over 90MB is skipped and logged, never staged —
     this is what stops another 700MB `git-full-diff.txt` or 1.5GB log
     from ever getting committed by accident.
4. Stage everything else with `git add -A` (respects `.gitignore` as
   normal — untracked files are the only ones this can go wrong for,
   so the size guard in step 3 is the real safety net, not `.gitignore`
   alone).
5. Commit as `Auto-sync: <UTC timestamp>`.
6. Push to `backup` on the **currently checked-out branch** — it never
   assumes `main`, so whatever branch you're working on is what gets
   synced.

Every check, skip, commit, and push is logged to
`scripts/poll-and-push.log` (gitignored — logs never get committed into
the repo they're logging).

## Stopping it

Ctrl+C in the terminal it's running in. It's a plain foreground loop —
nothing lingers in the background after that.

## Files

- `scripts/setup-remote.sh` — one-time: wires up the `backup` remote with
  your token
- `scripts/poll-and-push.sh` — the loop you actually run
- `scripts/push-once.sh` — does exactly one check-stage-commit-push cycle,
  used internally by the loop but also callable by hand if you just want
  to force one sync right now
