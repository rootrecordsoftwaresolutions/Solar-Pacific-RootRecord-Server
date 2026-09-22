# Telegram Skill (coms/telegram) — STUB, not yet migrated

## Status: placeholder

This folder exists so `coms/` has its final shape now. The real
implementation still lives at its original location and has **not** been
moved or modified yet:

    rootrecord-aws/aws/bin/chat_poll.py   (runs on AWS Mainland)

## Why this one stays on Telegram (design decision, confirmed)

Unlike `rr-packer` (already swapped to `coms/ssh`), the chat/trigger poller
stays on Telegram intentionally. Telegram's `getUpdates`/`sendMessage` are
both outbound-only calls — that's what lets a NAT'd home box (RootRecord)
and a public cloud box (AWS) both reach the same chat without either one
needing an inbound tunnel or exposed port. This was a deliberate design
choice, not a leftover.

## What it actually does today (from the current source)

- Polls Telegram every ~1s for two chats: `RR_CONTROL_CHAT_ID` (trigger
  source) and watches for wake-words (`ava`, `bruce`, `carly`, `/ask`,
  `@ava` etc.) addressing the RootRecord agents.
- Logs every message to `work/chatlogs/Current.jsonl` (rides along in the
  regular SSH-based data pack now — see `coms/ssh`).
- On a radar-related message, shells out to `radar_post_once.py` and posts
  the GIF back to the same chat.
- On a wake-word trigger, writes `work/triggers/Current.json` and posts a
  quiet `RR_TRIGGER ...` notice to the control chat so RootRecord (polling
  independently) can pick it up fast, without waiting for the next data-pack
  cycle.
- Does **not** run any LLM inference itself — that stays on AVA-CORE
  (RootRecord's NPU side).
- Uses two separate bot tokens (`RR_TELEGRAM_BOT_TOKEN` / trigger watch vs.
  the old `RR_DATAPACK_RECV_BOT_TOKEN` / now-retired) so concurrent
  `getUpdates` calls don't collide (Telegram 409).
- `RR_PUBLISH_CHAT_ID` — a separate broadcast/report destination, a second
  chat distinct from the control chat.

## To actually migrate this into a skill (not done yet)

1. Bring in `chat_poll.py` and `radar_post_once.py` source (not in any zip
   provided so far — only the systemd unit was included in
   `US-Mainland-Server-main.zip`; the actual script came from the
   skills-rebuild upload).
2. Bring in `common.py` (shared WORK/append_jsonl/etc. helpers it imports).
3. Decide whether this stays AWS-only (current) or gets a RootRecord-side
   counterpart that also polls `RR_CONTROL_CHAT_ID` directly for the
   reply-now path — worth confirming against how AVA-CORE currently
   actually picks up `RR_TRIGGER` notices before assuming anything here.
4. `references/OPERATOR.md` (in the original repo) has the full token/chat-id
   table — bring that in as `coms/telegram/references/`.

## scripts/

Empty — nothing ported yet.
