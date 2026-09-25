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
- `scripts/timelapse_engine.py` — compiles `frames/` into an hourly `video_chunks/hour_HH.mp4`,
  stitches the day into `final_output/master_stitched_timelapse.mp4` + a web GIF, and
  catches up on boot if the poller wasn't running when a trigger fired. All paths are
  derived from `grab_frame.DB_FRAMES` — nothing is re-typed by hand.
- `scripts/timelapse_hourly.sh` / `timelapse_daily.sh` / `timelapse_catchup.sh` — thin
  wrappers `jobs.py` calls (EVERY_HOUR, ON_AT 22:01, ON_BOOT).
- `store/CONNECTION.json` — DVR IP / RTSP credentials.
- `references/CAMERAS.md` — how the cameras work.

## Timelapse layout

```
Database/A-EYES/
├── frames/          # grab_frame.py writes here (already timestamped — no staging step needed)
├── video_chunks/    # hour_05.mp4 ... hour_21.mp4
├── final_output/    # master_stitched_timelapse.mp4, optimized_web_timelapse.gif
└── _archive/YYYYMMDD/hour_HH/   # frames moved here after a successful hourly compile (not deleted)
```

Window 05:00–22:00 HST, ch1, target 3 min / 68 fps master, 30 fps GIF — all overridable
via `A_EYES_TIMELAPSE_*` env vars in `jobs.py`'s job `env` field. See
`scripts/timelapse_engine.py` docstring for the full list.

## Run

```bash
python3 scripts/cam_server.py
```

Then:
- `curl http://127.0.0.1:8791/health`
- `curl http://127.0.0.1:8791/current.jpg -o test.jpg`
