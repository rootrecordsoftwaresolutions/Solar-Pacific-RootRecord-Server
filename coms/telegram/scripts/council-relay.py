#!/usr/bin/env python3
"""council-relay.py — one getUpdates; single-voice by default; A→B→C→A only on triggers.
Each hop posts with that voice's bot token."""
from __future__ import annotations
import json, os, re, subprocess, sys, time, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONF = ROOT / "config" / "relay.conf"
VOICES = ROOT / "config" / "voices.conf"
PIPELINE_ORDER = ("ava", "bruce", "carly", "ava")  # A→B→C→A

def load_kv(path: Path) -> dict:
    out = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        out[k.strip()] = v.strip()
    return out

def load_secrets(paths):
    for p in paths:
        fp = Path(p)
        if not fp.is_file():
            continue
        for line in fp.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip("'").strip('"')
            if k and k not in os.environ:
                os.environ[k] = v

def load_voices():
    voices = {}
    for line in VOICES.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 6:
            continue
        vid, enabled, user, token_env, model, fallback = parts[:6]
        if enabled != "1":
            continue
        voices[vid] = {"user": user, "token_env": token_env, "model": model, "fallback": fallback}
    return voices

def token_for(voice):
    t = (os.environ.get(voice["token_env"]) or "").strip()
    if t:
        return t
    if "AVA" in voice["token_env"]:
        return (os.environ.get("AVA_TELEGRAM_BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN") or "").strip()
    return ""

def api(token, method, payload=None):
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"} if data else {},
        method="POST" if data else "GET",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        body = json.load(r)
    if not body.get("ok"):
        raise RuntimeError(f"{method} failed: {body}")
    return body

def wants_pipeline(text: str, triggers: list[str]) -> bool:
    t = text.lower()
    for trig in triggers:
        trig = trig.strip().lower()
        if trig and trig in t:
            return True
    if re.search(r"\ba\s*>\s*b\s*>\s*c\b", t):
        return True
    return False

def mentioned_voice(text: str, voices: dict, entities=None) -> str | None:
    """Single-voice if a specific bot/@name is addressed. DM handled by chat type."""
    t = text.lower()
    # username mentions
    for vid, v in voices.items():
        user = (v.get("user") or "").lower()
        if user and f"@{user}".lower() in t:
            return vid
    if re.search(r"(^|\s)@?ava(\s|$|[,:])|@ava_ivy_bot|@avaivy_bot", t) and not re.search(r"\b(bruce|carly)\b", t):
        return "ava"
    if re.search(r"(^|\s)@?bruce(\s|$|[,:])|@brucemonitor_bot", t) and not re.search(r"\b(ava|carly)\b", t):
        return "bruce"
    if re.search(r"(^|\s)@?carly(\s|$|[,:])|@carlymal_bot", t) and not re.search(r"\b(ava|bruce)\b", t):
        return "carly"
    # multiple names without pipeline trigger → still single? prefer first mentioned
    hits = []
    if re.search(r"\bava\b|@ava", t):
        hits.append("ava")
    if re.search(r"\bbruce\b|@bruce", t):
        hits.append("bruce")
    if re.search(r"\bcarly\b|@carly", t):
        hits.append("carly")
    if len(hits) == 1:
        return hits[0]
    return None

def run_ollama(cfg, voice, voices, prompt, prior=""):
    run = cfg.get("RUN_OLLAMA", "")
    env = os.environ.copy()
    desk = cfg.get("DESK_LIVE_FILE", "")
    if desk:
        env["DESK_LIVE_FILE"] = desk
    else:
        env.pop("DESK_LIVE_FILE", None)
    full = prompt if not prior else f"Prior council turns:\n{prior}\n\nYour turn as {voice}. User:\n{prompt}"
    def once(m):
        p = subprocess.run([run, m, full], capture_output=True, text=True, env=env, timeout=600)
        out = p.stdout or ""
        return "\n".join(ln for ln in out.splitlines() if not ln.startswith("[ok] single-flight")).strip()
    text = ""
    try:
        text = once(voices[voice]["model"])
    except Exception:
        text = ""
    if not text:
        try:
            text = once(voices[voice]["fallback"])
        except Exception:
            text = "No data — inference failed."
    return text or "No data — inference failed."

def post_as(voice_id, voices, chat_id, text, max_text):
    tok = token_for(voices[voice_id])
    if not tok:
        print(f"[fail] no token for {voice_id}", file=sys.stderr)
        return False
    api(tok, "sendMessage", {
        "chat_id": chat_id,
        "text": text[:max_text],
        "disable_web_page_preview": True,
    })
    print(f"[ok] posted as {voice_id}")
    return True

def main():
    cfg = load_kv(CONF)
    if cfg.get("ENABLED", "1") != "1":
        print("[skip] ENABLED=0"); return 0
    load_secrets([cfg.get("SECRETS_1", ""), cfg.get("SECRETS_2", "")])
    voices = load_voices()
    if not voices:
        print("No data: no enabled voices", file=sys.stderr); return 2
    poll_voice = cfg.get("POLL_VOICE", "ava")
    if poll_voice not in voices:
        poll_voice = next(iter(voices))
    token = token_for(voices[poll_voice])
    if not token:
        print(f"No data: token for poll voice {poll_voice}", file=sys.stderr); return 3
    chat_id = cfg.get("COUNCIL_CHAT_ID", "").strip()
    if not chat_id:
        print("No data: COUNCIL_CHAT_ID empty", file=sys.stderr); return 4
    triggers = [x.strip() for x in cfg.get("PIPELINE_TRIGGERS", "").split(",") if x.strip()]
    default_voice = cfg.get("DEFAULT_SINGLE_VOICE", "ava")
    max_text = int(cfg.get("MAX_TEXT", "3900") or 3900)
    state_dir = Path(cfg.get("STATE_DIR", "/home/rootrecord/Database/intake/council-relay"))
    state_dir.mkdir(parents=True, exist_ok=True)
    offset_file = state_dir / "offset.txt"
    offset = int(offset_file.read_text().strip() or "0") if offset_file.is_file() else 0
    timeout = int(cfg.get("POLL_TIMEOUT", "20") or "20")
    print(f"[ok] relay chat={chat_id} poll={poll_voice} pipeline_triggers={len(triggers)}")

    while True:
        try:
            body = api(token, "getUpdates", {"timeout": timeout, "offset": offset, "allowed_updates": ["message"]})
        except urllib.error.HTTPError as e:
            if e.code == 409:
                print("[fail] 409 — another getUpdates poller running", file=sys.stderr)
                return 409
            raise
        for upd in body.get("result") or []:
            offset = int(upd["update_id"]) + 1
            offset_file.write_text(str(offset))
            msg = upd.get("message") or {}
            text = (msg.get("text") or "").strip()
            if not text:
                continue
            chat = msg.get("chat") or {}
            ch = str(chat.get("id", ""))
            is_private = chat.get("type") == "private"
            # Group: only council chat. Private: allow (DM to whichever bot received — we only poll AVA token though)
            if not is_private and ch != str(chat_id):
                continue
            # DMs to Ava bot only while POLL_VOICE=ava; document limitation
            if is_private:
                voice = poll_voice
                reply = run_ollama(cfg, voice, voices, text)
                post_as(voice, voices, ch, reply, max_text)
                continue

            if wants_pipeline(text, triggers):
                prior = ""
                for hop in PIPELINE_ORDER:
                    if hop not in voices:
                        continue
                    label = hop
                    reply = run_ollama(cfg, hop, voices, text, prior=prior)
                    post_as(hop, voices, chat_id, reply, max_text)
                    prior += f"\n[{hop}]: {reply}\n"
                    # single-flight already serializes ollama; brief pause between posts
                    time.sleep(0.5)
                print("[ok] pipeline A>B>C>A done")
                continue

            voice = mentioned_voice(text, voices) or default_voice
            if voice not in voices:
                voice = default_voice
            reply = run_ollama(cfg, voice, voices, text)
            post_as(voice, voices, chat_id, reply, max_text)
        time.sleep(0.2)

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("[ok] stopped"); raise SystemExit(0)
