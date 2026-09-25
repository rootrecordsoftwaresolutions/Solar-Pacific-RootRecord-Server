---
name: a-eyes
description: Solar panel and desk camera skill — stills, power session, path-secret gateway on 8791. Use for solar-cam, panel stills, cam gateway, current.jpg, power-on power-off. Honest WAITING when offline. No invented frames.
---

# a-eyes

Play on A.I. eyes. Thin desk camera skill restored from legacy panels-cam.

## INFO — MUST HAVE

- Never invent a frame or caption. No stream means WAITING / No data.
- Secrets only in store/secrets.env or master-key.env — never in SKILL or git.
- Gateway is light: health, one JPEG still, power on/off. Heavy GIF stays on AWS when live.
- Data samples go under /home/rootrecord/Database/A-EYES/
- NPU vision captions are staged in plumbing vision-npu.md

## Layout

- Scripts: scripts/cam_gateway.py, panels_grab.py, cam_power_session.py, solar_origin_mux.py
- Secrets: store/secrets.env (mode 600)
- Connection: store/CONNECTION.json
- Frames (skill): store/frames/
- Frames (database): /home/rootrecord/Database/A-EYES/frames/
- Unit: ~/.config/systemd/user/rr-solar-cam-gateway.service

## Gateway API (path secret)

- GET /secret/health
- GET /secret/current.jpg
- POST /secret/power-on
- POST /secret/power-off

Listen from RR_SOLAR_LISTEN (historically port 8791).

## Operator

- systemctl --user status rr-solar-cam-gateway.service
- systemctl --user restart rr-solar-cam-gateway.service
