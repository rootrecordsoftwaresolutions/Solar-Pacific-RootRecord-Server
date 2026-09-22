---
name: ssh
description: SSH/rsync relay between RootRecord and AWS Mainland for network-globe telemetry data packs. Pull-based — RootRecord rsyncs zips from AWS out/, verifies, confirms over SSH to trigger remote wipe. Replaced the old Telegram push (rr-packer). Use for starting/stopping/checking the relay or troubleshooting SSH/relay failures.
---

Part of `coms/` (see `coms/README.md`) — loads independently of `telegram/`,
`discord/`, `slack/`. Runtime path: `/home/rootrecord/.ollama/skills/coms/ssh`.

Flow: local collector → SSH relay → AWS Mainland `out/` → RootRecord pull
(verify + confirm) → Network Globe backend.

## Commands

- Start: `./run.sh`
- Stop: `pkill -f ssh-relay`
- Status: `./scripts/health-check.sh`
- Logs: `./logs/`

## Rules

- Never delete `backups/` or `context/` — historical implementations stay as reference
- No runtime data committed; no secrets in the skill package
- Verify SSH connectivity before relay startup

## Troubleshooting

- SSH failure → check key, host, permissions
- Relay failure → check outbox, network connectivity
