"""Slack Web API — replies only. Never delete history.

Token loads from the single master env file (matches telegram.py/discord.py).
Corrected token var name to AVA_SLACK_BOT_TOKEN to match the real config.py
convention discovered when porting discord/telegram (previous version of
this file used a made-up SLACK_BOT_TOKEN name — fixed here).
"""
from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

import httpx

log = logging.getLogger("ava.slack")
API = "https://slack.com/api"
MASTER_ENV = Path("/home/rootrecord/master/master-key.env")


def _load_master_env() -> None:
    if not MASTER_ENV.is_file():
        return
    for line in MASTER_ENV.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip("'").strip('"')
        if k and k not in os.environ:
            os.environ[k] = v


def _token() -> str:
    _load_master_env()
    return (os.environ.get("AVA_SLACK_BOT_TOKEN") or "").strip()


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {_token()}",
        "Content-Type": "application/json; charset=utf-8",
    }


async def api(method: str, payload: dict[str, Any] | None = None, *, params: dict | None = None) -> dict:
    if not _token():
        return {"ok": False, "error": "no_token"}
    async with httpx.AsyncClient(timeout=20) as client:
        if payload is None:
            r = await client.get(f"{API}/{method}", headers=_headers(), params=params or {})
        else:
            r = await client.post(f"{API}/{method}", headers=_headers(), json=payload)
    try:
        data = r.json()
    except Exception:
        return {"ok": False, "error": f"http_{r.status_code}"}
    return data if isinstance(data, dict) else {"ok": False}


async def auth_test() -> dict:
    return await api("auth.test", {})


async def post_message(channel: str, text: str) -> dict:
    return await api(
        "chat.postMessage",
        {"channel": channel, "text": text[:3500], "unfurl_links": False},
    )


async def history(channel: str, *, limit: int = 12) -> list[dict]:
    data = await api("conversations.history", params={"channel": channel, "limit": str(limit)})
    if not data.get("ok"):
        return []
    return list(data.get("messages") or [])
