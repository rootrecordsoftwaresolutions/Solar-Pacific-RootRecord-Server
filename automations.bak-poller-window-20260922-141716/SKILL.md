---
name: automations
description: >-
  RootRecord on-box automations desk. Boot poller heartbeat every 5s and
  optional Cloudflare tunnel for rootserver.rootrecord.cloud. Use when asked
  about the poller, rootserver hostname, or automations systemd unit.
---

# automations

This folder **is** the desk.

## Poller

- Script: `scripts/rootserver_poller.py`
- Runner: `scripts/run-poller.sh`
- Binary: `bin/cloudflared`
- systemd (user): `rr-rootserver-poller.service`
- Log: `~/.ollama/skills/logs/store/rootserver-poller.log`
- Local HTTP: `http://127.0.0.1:8799/` (open access on bind)
- Heartbeat every 5s: `<FULLTIMESTAMP>Poller is online.`

## Tunnel

Token file (never commit / never print): `~/.cloudflared/origin.token`

Public hostname target: `rootserver.rootrecord.cloud`

Hostname + ingress are configured in **Cloudflare Zero Trust** for the token
tunnel. Local process only runs `cloudflared tunnel run --token …`.

If DNS or public hostname is missing, set them in Cloudflare (zone
`rootrecord.cloud`) or provide a CF API token with Tunnel + DNS edit, then
re-run setup documented in `references/cloudflare-setup.md`.

## Do not

- Invent live tunnel status — check the log or curl localhost.
- Put tokens in the unit file or SKILL.md.
- Expose the poller on `0.0.0.0` unless the operator asks (default is loopback;
  Cloudflare tunnel is the public door).
