# a-eyes — how the cameras work

## Hardware
- Night Owl DVR on the LAN, 4 channels (ch1–ch4).
- Connect over RTSP using `store/CONNECTION.json` (IP + RTSP user/password).

## Scripts
- `scripts/grab_frame.py` — pulls one JPEG per channel via ffmpeg/RTSP and
  writes it straight to `/home/rootrecord/Database/A-EYES/frames/`. That's
  the only thing it does — no serving, no power control, no mirroring.
- `scripts/cam_server.py` — the one local server that hosts the camera
  views. Binds `127.0.0.1:8791`. Calls `grab_frame.grab_jpeg()` on request
  and returns the JPEG. If another server is found running the old routes
  somewhere else, it's leftover and should be stopped/removed.

## Storage
- Single source of truth: `/home/rootrecord/Database/A-EYES/frames/`
- No local `store/frames/` — that mirror was removed.

## Rules
- Never invent a frame or caption — no stream means an error, not a fake image.
- Secrets only in `store/CONNECTION.json` (or a secrets file you add) — never in git.
