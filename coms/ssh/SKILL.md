---
name: ssh
description: >-
  SSH/rsync pull relay RootRecord↔AWS Mainland (network-globe packs).
  Replaced Telegram rr-packer. Start/stop/health or SSH/relay debug.
---

# ssh

Under `coms/` (independent of telegram/discord/slack). Path: `coms/ssh`.

Flow: collector → SSH → AWS `out/` → RootRecord pull (verify+confirm) → Globe.

- Start `./run.sh` · Stop `pkill -f ssh-relay` · Health `./scripts/health-check.sh` · Logs `./logs/`

**Rules:** keep `backups/`+`context/`; no secrets/runtime data in package; verify SSH before start.
