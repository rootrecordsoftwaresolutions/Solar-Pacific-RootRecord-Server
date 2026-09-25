from pathlib import Path
SKILL_ROOT = Path("/home/rootrecord/.ollama/skills/root-status")
STATUS_DIR = SKILL_ROOT / "status"
ENERGY_STATUS = Path("/home/rootrecord/Database/ROOTRECORD/status/energy-status.json")  # future
SYSTEM_STATUS = Path("/home/rootrecord/Database/SYSTEM/status/system-status.json")
MERGED = STATUS_DIR / "root-status-5min.json"
def ensure_dirs():
    STATUS_DIR.mkdir(parents=True, exist_ok=True)
