"""Telegram Bot API helpers for report DMs + /subscribe.

Ported from communications/telegram/scripts/telegram.py. Token now loads
from the single master env file instead of the old multi-candidate scan
in apps/core/config.py.
"""
from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

import httpx

log = logging.getLogger("ava.telegram")

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


def telegram_bot_token() -> str:
    _load_master_env()
    return (os.environ.get("AVA_TELEGRAM_BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN") or "").strip()


def _base() -> str:
    token = telegram_bot_token()
    return f"https://api.telegram.org/bot{token}" if token else ""


async def send_message(
    chat_id: str | int,
    text: str,
    *,
    question: str = "",
    source: str = "",
) -> dict | None:
    if not _base() or not str(chat_id).strip() or not str(text or "").strip():
        return None
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.post(
            f"{_base()}/sendMessage",
            json={
                "chat_id": str(chat_id),
                "text": str(text)[:3900],
                "disable_web_page_preview": True,
            },
        )
    body = {}
    try:
        body = r.json()
    except Exception:
        body = {}
    if r.status_code >= 400 or not body.get("ok"):
        log.warning("Telegram send failed chat=%s: %s", chat_id, str(body)[:200])
        return None
    result = body.get("result")
    # Optional legacy hook — no-ops if apps.core.services isn't present in this
    # skill's environment. Left as-is from the original (already self-guarded).
    if isinstance(result, dict) and result.get("message_id") is not None:
        try:
            from apps.core.services import reply_feedback

            q = str(question or "").strip()
            if not q:
                q = reply_feedback.guess_question_for_chat(chat_id)
            reply_feedback.note_outbound(
                surface="telegram",
                chat_id=chat_id,
                message_id=result.get("message_id"),
                answer=str(text)[:3900],
                question=q,
                source=source or "telegram_send",
            )
        except Exception as e:
            log.debug("outbound register: %s", e)
    return result


async def get_me() -> dict:
    if not _base():
        return {}
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.get(f"{_base()}/getMe")
        body = r.json()
        if body.get("ok") and isinstance(body.get("result"), dict):
            return body["result"]
    except Exception as e:
        log.debug("Telegram getMe: %s", e)
    return {}


async def get_updates(offset: int | None = None, timeout: int = 20) -> list[dict[str, Any]]:
    if not _base():
        return []
    payload: dict[str, Any] = {
        "timeout": timeout,
        "allowed_updates": ["message", "message_reaction"],
    }
    if offset:
        payload["offset"] = offset
    try:
        async with httpx.AsyncClient(timeout=timeout + 10) as client:
            r = await client.post(f"{_base()}/getUpdates", json=payload)
        body = r.json()
        if body.get("ok"):
            return list(body.get("result") or [])
        log.warning("Telegram getUpdates: %s", str(body)[:200])
    except Exception as e:
        log.debug("Telegram getUpdates: %s", e)
    return []
