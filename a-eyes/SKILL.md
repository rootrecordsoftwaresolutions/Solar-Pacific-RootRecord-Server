---
name: a-eyes
description: Camera views only. Local server serves live stills from the DVR channels; grab_frame.py writes them to the Database. Use for cam stills, current.jpg, health check.
---

# a-eyes

Simple version. Cameras only — no automations, no power sessions, no solar logic.

## INFO — MUST HAVE

- Never invent a frame. No stream means an error response, not a fake image.
- Real DVR credentials go in `store/CONNECTION.json` (never in git).
- Frames are written ONLY to `/home/rootrecord/Database/A-EYES/frames/` —
  no local skill-store mirror, no second copy anywhere.
- `cam_server.py` binds `127.0.0.1:8791` and should be the ONLY process
  serving camera views on this box. If something else is listening on a
  camera/gateway port, it's a leftover from the old setup — find and stop it.

## Layout

- `scripts/grab_frame.py` — grabs one JPEG for a channel, saves to Database. Does nothing else.
- `scripts/cam_server.py` — local HTTP server that broadcasts the current stills.
- `store/CONNECTION.json` — DVR IP / RTSP credentials.
- `references/CAMERAS.md` — how the cameras work.

## Run

```bash
python3 scripts/cam_server.py
```

Then:
- `curl http://127.0.0.1:8791/health`
- `curl http://127.0.0.1:8791/current.jpg -o test.jpg`
