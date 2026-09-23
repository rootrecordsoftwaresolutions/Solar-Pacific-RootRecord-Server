# BLE boot (user systemd)

Unit: `~/.config/systemd/user/ava-ecoflow-ble.service`  
Owner script: `../ble/ble-owner.py` (thin heartbeat — **one** owner, no pack scan loops)

## Enable on login/boot (lingering recommended for headless)

```bash
loginctl enable-linger rootrecord   # once, if not already
systemctl --user daemon-reload
systemctl --user enable --now ava-ecoflow-ble.service
~/.ollama/skills/energy/scripts/ble/ble-status.sh
```

Or: `./enable-ble-boot.sh`

Do **not** start a second poller/getUpdates-style owner. Poll buckets stay stubbed.
