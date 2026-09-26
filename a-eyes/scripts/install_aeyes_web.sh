#!/usr/bin/env bash
# Install /aeyes live web UI path through the poller proxy + restart cam server.
set -euo pipefail

SKILLS="${SKILLS:-/home/rootrecord/.ollama/skills}"
POLLER="$SKILLS/automations/scripts/rootserver_poller.py"
MASTER="/home/rootrecord/master/master-key.env"

echo "==> pull a-eyes scripts"
cd "$SKILLS"
git fetch origin
git checkout origin/main -- a-eyes/scripts/cam_server.py a-eyes/scripts/grab_frame.py a-eyes/scripts/install_aeyes_web.sh || true

echo "==> ensure AEYES_PUBLIC_PASSWORD in master-key.env"
if [[ -f "$MASTER" ]] && grep -q '^AEYES_PUBLIC_PASSWORD=' "$MASTER"; then
  echo "    AEYES_PUBLIC_PASSWORD already set"
else
  echo "    ADD this line to $MASTER:"
  echo "    AEYES_PUBLIC_PASSWORD=your-password-here"
fi

echo "==> inject /aeyes streaming reverse-proxy into rootserver_poller.py"
python3 - "$POLLER" <<'PY'
import sys
from pathlib import Path
p = Path(sys.argv[1])
t = p.read_text()

# Replace any existing proxy with the streaming-capable one.
if "_proxy_aeyes" in t:
    # Strip old method: from def _proxy_aeyes through the next def at same indent
    start = t.find("    def _proxy_aeyes")
    if start >= 0:
        # find next top-level method on Handler (4-space + def)
        rest = t[start + 4:]
        nxt = rest.find("\n    def ")
        if nxt > 0:
            t = t[:start] + rest[nxt + 1:]
            print("    removed old _proxy_aeyes")

method = '''
    def _proxy_aeyes(self) -> None:
        """Reverse-proxy /aeyes* to 127.0.0.1:8791 (streams MJPEG, does not buffer)."""
        import urllib.error
        import urllib.request
        target = f"http://127.0.0.1:8791{self.path}"
        headers = {}
        if self.headers.get("Cookie"):
            headers["Cookie"] = self.headers.get("Cookie")
        if self.headers.get("Content-Type"):
            headers["Content-Type"] = self.headers.get("Content-Type")
        body = None
        if self.command == "POST":
            length = int(self.headers.get("Content-Length") or 0)
            body = self.rfile.read(length) if length > 0 else b""
        timeout = 600 if ".mjpeg" in self.path else 45
        req = urllib.request.Request(target, data=body, headers=headers, method=self.command)
        try:
            resp = urllib.request.urlopen(req, timeout=timeout)
        except urllib.error.HTTPError as e:
            data = e.read()
            self.send_response(e.code)
            for key in ("Content-Type", "Set-Cookie", "Location"):
                val = e.headers.get(key) if e.headers else None
                if val:
                    self.send_header(key, val)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        except Exception as e:
            self._send(502, f"a-eyes proxy error: {type(e).__name__}\\n")
            return
        try:
            self.send_response(resp.status)
            for key in ("Content-Type", "Set-Cookie", "Location", "Cache-Control", "Pragma", "Connection"):
                val = resp.headers.get(key)
                if val:
                    self.send_header(key, val)
            is_stream = ".mjpeg" in self.path or "multipart" in (resp.headers.get("Content-Type") or "")
            if not is_stream:
                data = resp.read()
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            else:
                self.end_headers()
                while True:
                    chunk = resp.read(4096)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            try:
                resp.close()
            except Exception:
                pass

'''

marker = "    def do_GET(self) -> None:\n"
if marker not in t:
    raise SystemExit("do_GET not found")
t = t.replace(marker, method + marker, 1)

old = "    def do_GET(self) -> None:\n        with _lock:"
new = "    def do_GET(self) -> None:\n        if self.path.startswith(\"/aeyes\"):\n            self._proxy_aeyes()\n            return\n        with _lock:"
if "if self.path.startswith(\"/aeyes\")" not in t and "if self.path.startswith("/aeyes")" not in t:
    if old not in t:
        raise SystemExit("do_GET body pattern not found")
    t = t.replace(old, new, 1)
elif "if self.path.startswith("/aeyes")" not in t and 'if self.path.startswith("/aeyes")' not in t:
    # already has startswith from previous inject — leave it
    pass

if "def do_POST" not in t:
    at = t.find("\ndef _cloudflared_interesting")
    post = '''
    def do_POST(self) -> None:
        if self.path.startswith("/aeyes"):
            self._proxy_aeyes()
            return
        self._send(404, "not found\\n")

'''
    if at < 0:
        raise SystemExit("insert point for do_POST missing")
    t = t[:at] + post + t[at:]

p.write_text(t)
compile(t, str(p), "exec")
print("    streaming proxy OK")
PY

echo "==> restart a-eyes cam server"
pkill -f 'python3 cam_server.py' 2>/dev/null || true
sleep 0.5
bash "$SKILLS/a-eyes/scripts/ensure_cam_server.sh"
sleep 1

echo "==> local smoke test"
curl -sS -m 3 http://127.0.0.1:8791/health || true
echo
curl -sS -m 3 -o /dev/null -w "aeyes_html %{http_code}\n" http://127.0.0.1:8791/aeyes || true

echo
echo "Restart the poller stack so the streaming proxy is loaded:"
echo "  bash $SKILLS/automations/scripts/do-stack-reload.sh"
echo "Then:  https://rootserver.rootrecord.cloud/aeyes"
