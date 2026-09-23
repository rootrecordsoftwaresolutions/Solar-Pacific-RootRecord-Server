---
name: automations
description: >-
  RootRecord on-box automations desk. Boot poller heartbeat every 5s and
  Cloudflare tunnel for rootserver.rootrecord.cloud. Use when asked about the
  poller, rootserver hostname, or automations systemd unit.
---

# automations

This folder **is** the desk.

## Poller

- Script: `scripts/rootserver_poller.py`
- Runner: `scripts/run-poller.sh`
- Window: `scripts/open-poller-window.sh` (autostart desktop)
- Binary: `bin/cloudflared`
- systemd (user): `rr-rootserver-poller.service` — owns the process
- Log: `~/.ollama/skills/logs/store/rootserver-poller.log`
- Local HTTP: `http://127.0.0.1:8799/` (open access on bind)
- Public: `https://rootserver.rootrecord.cloud/`
- Heartbeat every 5s: `<FULLTIMESTAMP>Poller is online.`

## Boot order (inside the poller)

1. Start `cloudflared tunnel run` (token from file)
2. Wait for first `Registered tunnel connection` (or timeout)
3. Bind HTTP + start heartbeat polling

## Tunnel

Token file (never commit / never print): `~/.cloudflared/rootserver.token`
(from `ROOTSERVER_TUNNEL_TOKEN` in `/home/rootrecord/master/master-key.env`)

Public hostname + ingress: Cloudflare Zero Trust for tunnel **rootserver**.

## Visible window

Autostart: `~/.config/autostart/rr-rootserver-poller-window.desktop`
Opens a titled terminal tailing the log. Closing the window does **not** stop
the service. To stop the stack: `systemctl --user stop rr-rootserver-poller`.

## Do not

- Invent live tunnel status — check the window, the log, or curl localhost / public URL.
- Put tokens in the unit file or SKILL.md.
- Expose the poller on `0.0.0.0` unless the operator asks (default is loopback;
  Cloudflare tunnel is the public door).
- Run a second poller in the status window (port clash).
