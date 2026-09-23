# NPU inference (OmniBook)

**FastFlowLM (FLM)** — not Ollama — binds the XDNA NPU:

```
/home/rootrecord/.local/opt/fastflowlm/flm serve llama3.2:3b \
  --pmode default --host 127.0.0.1 --port 52625
```

Legacy unit: `ava-flm.service` (host-metrics backups).

`run-infer.sh`: FLM if `:52625` up → else Ollama `*-telegram` (CPU).
