#!/usr/bin/env python3
"""Internet connectivity gate for poller net services (tunnel, GitHub, Telegram)."""
from __future__ import annotations

import socket
import time
from typing import Callable

LogFn = Callable[[str], None]


def internet_ok(timeout: float = 2.5) -> bool:
    """TCP reachability to public endpoints — does not use local DNS stub."""
    for host, port in (("1.1.1.1", 443), ("8.8.8.8", 53), ("1.0.0.1", 443)):
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except OSError:
            continue
    return False
