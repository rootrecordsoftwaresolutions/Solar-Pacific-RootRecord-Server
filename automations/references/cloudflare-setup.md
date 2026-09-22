# Cloudflare setup for rootserver.rootrecord.cloud

## Need from operator (if not already done)

1. Zone `rootrecord.cloud` is already on Cloudflare NS (confirmed).
2. Create **Public hostname** on the existing tunnel (token in
   `~/.cloudflared/origin.token`, tunnel id `0f16a586-8791-4711-8347-a162c264110d`):
   - Hostname: `rootserver.rootrecord.cloud`
   - Service: `http://127.0.0.1:8799`
3. DNS: CNAME `rootserver` → `<tunnel-id>.cfargotunnel.com` (proxied), or let
   Zero Trust “Create DNS record” do it.

## Or provide API token

Scoped: Account Cloudflare Tunnel Edit + Zone DNS Edit for `rootrecord.cloud`.
Put as `CLOUDFLARE_API_TOKEN=…` in a secrets file Bruce/ops can read (never chat).

## Quick test (local)

```bash
curl -sS http://127.0.0.1:8799/
journalctl --user -u rr-rootserver-poller -n 20 --no-pager
```
