# Pipeline: vision / image-reader (STAGED — not runnable yet)

Goal: image understanding on **NPU only** when an EP exists; never invent captions from thin air.

```
image path / desk still
  → single-flight acquire (job=vision:…)
  → prefer NPU EP (ONNX/XRT)  [TODO: wire runtime]
  → fallback: refuse or queue — do NOT silently use iGPU unless RR_ALLOW_IGPU=1
  → emit short caption JSON { "caption", "objects?", "source": "npu|waiting" }
  → release
  → optional handoff to carly-energy / bruce-ops for desk interpretation
```

Ollama multimodal (`vision-reader` Modelfile) is a **staging** brain only; production path should be NPU EP once packaged.
