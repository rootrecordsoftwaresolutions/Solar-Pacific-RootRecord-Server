# github-skill

Purpose: watch every subfolder under `/home/rootrecord/.ollama/skills` for
any change and push it to GitHub automatically, without repeating the
14GB / `.gitignore`-not-sticking disaster.

## How it runs now

Driven by the **automations poller** (`jobs.py`):

- **ON_BOOT p2** `github_backup_remote` — `scripts/setup-remote.sh`
- **EVERY_SECONDS 300** `github_autopush` — `scripts/push-once.sh`

Do **not** also run `scripts/poll-and-push.sh` in a terminal (double push).
Ctrl-C on the rootserver poller window stops the whole stack, including this.

Manual one-shot still works:

```bash
bash /home/rootrecord/.ollama/skills/github/scripts/push-once.sh
```

## Env

Token: `/home/rootrecord/master/master-key.env` → `GITHUB_TOKEN=…`
Fine-grained PAT scoped to `Solar-Pacific-RootRecord-Server` (Contents R/W).

## Safety

- 90MB per-file size guard in `push-once.sh`
- Log path gitignored: `github/scripts/poll-and-push.log`
- Pushes to remote `backup` on the current branch

## Files

- `scripts/setup-remote.sh` — one-time / boot: wire `backup` remote
- `scripts/push-once.sh` — one check-stage-commit-push cycle
- `scripts/poll-and-push.sh` — legacy foreground loop (prefer poller job)
