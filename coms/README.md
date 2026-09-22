# coms/

Parent folder grouping every communications/relay protocol RootRecord uses.
This folder itself is **not** a skill (no metadata entry, nothing to
discover) — it's purely organizational. Each subfolder below it is its own
independently-loadable skill with its own `SKILL.md`, so activating one
never pulls the others' instructions into context. That matters on
NPU-constrained inference: cheap to keep several around (each metadata
entry is ~50-100 tokens), expensive to merge them into one skill that loads
everything at once on activation.

| Skill | Status | Purpose |
|---|---|---|
| `ssh/` | **Live** | Data-pack pull + verify + remote-wipe-confirm between RootRecord and AWS Mainland. Replaced the old Telegram-based `rr-packer` relay. |
| `telegram/` | **Live** (functions) | `send_message`/`get_me`/`get_updates`. Separate from the still-running AWS `chat_poll.py` trigger poller — see `telegram/references/aws-chat-poll.md`. |
| `discord/` | **Live** (functions) | Post/pin/forward/read messages, DMs, guild channels. Persona reply logic (`discord_chat.py`) intentionally not ported. |
| `slack/` | **Live** (functions) | `post_message`/`history`/`auth_test`. Replies only, never deletes history. |

All three protocol skills load their bot token from a single file:
`/home/rootrecord/master/master-key.env` — `AVA_TELEGRAM_BOT_TOKEN`,
`AVA_DISCORD_BOT_TOKEN` (+ fallbacks), `AVA_SLACK_BOT_TOKEN`. `ssh/` doesn't
use this — its credential is the SSH key file itself, referenced directly.

## Adding a new protocol later

Copy the shape of `ssh/` or `telegram/`: a `SKILL.md` describing what it
does and how to invoke it, `scripts/` for anything it runs, `references/`
for anything it needs to look up but shouldn't load by default. Keep each
skill's `SKILL.md` body reasonably lean (rough guideline: under ~5000
tokens) — if a protocol's instructions get big, push the bulk into
`references/` and have `SKILL.md` point at it rather than inlining
everything.

###
All three are now real, working function libraries — not stubs — all pointed at /home/rootrecord/master/master-key.env:

coms/telegram — send_message, get_me, get_updates, ported from communications/telegram/scripts/telegram.py. This is a different, simpler script than the AWS chat_poll.py trigger poller — that one's still running as-is on AWS and is now documented separately in telegram/references/aws-chat-poll.md so the two don't get conflated.
coms/discord — full set: post (with file attachments, auto-splitting long messages), pin, forward, read history, DMs, list guild channels. Left out discord_chat.py (the Ava-persona reply generator) and discord_september.py (legacy migration script) — those are a different, much bigger thing than "discord functions."
coms/slack — updated in place. Also fixed something while I was in there: the token env-var name I'd guessed earlier (SLACK_BOT_TOKEN) was wrong — found the real one (AVA_SLACK_BOT_TOKEN) while reading config.py for Discord/Telegram's token functions, so that's corrected now too.

One thing worth flagging: since these are all async def functions (matching the originals), whatever calls them — an Ollama agent, a script — needs to run them through asyncio.run(...) or an existing event loop. Not a problem, just something to know going in rather than hit as a surprise.

I did not touch coms/ssh for the master-key.env change — it doesn't have a bot-token-style secret, the SSH key file itself is the credential and it's already referenced directly by path, so there was nothing there to point at master-key.env.
