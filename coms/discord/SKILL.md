---
name: discord
description: Discord REST API functions — post/edit messages (with file attachments), pin, forward, read channel/DM history, list guild channels. Token from /home/rootrecord/master/master-key.env (AVA_DISCORD_BOT_TOKEN). Functions only, not the Ava-persona reply logic.
---

`scripts/discord.py` — ported from `communications/discord/scripts/discord.py`
(itself ported from `discordApi.mjs`).

## Functions

- `post_message(channel_id, content, ref_id=None)` — auto-splits long content
- `post_message_with_files(channel_id, content, file_paths)`
- `pin_message(channel_id, message_id)`
- `forward_message(dest_channel_id, source_channel_id, message_id)`
- `get_messages(channel_id, limit=50)` — backs off on 404/5xx per channel
- `send_dm(user_id, content)`
- `list_guild_channels(guild_id)`
- `get_me()`
- `list_private_channels()`

## Not ported (out of scope — functions only, not persona logic)

- `discord_chat.py` — Ava-persona reply generation, depends on
  `apps.core.services.ollama`/`persona`/`people`. Separate, much larger
  system — not a messaging function.
- `discord_september.py` — legacy Windows migration script.
