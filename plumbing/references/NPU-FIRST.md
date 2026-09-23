# NPU-first policy (OmniBook)

## Live facts (do not invent metrics)
- Device: `/dev/accel/accel0` (AMD XDNA class via accel)
- Packages seen: `libxrt-npu2`, `libxrt-utils-npu`, `libze1`, `linux-firmware-amd-misc`, `python3-xrt`
- iGPU also present: AMD Radeon 840M (`/dev/dri/renderD128`) — **not** preferred when NPU can do the job

## Rule
1. If a workload has an NPU path (XRT / Vitis AI / ONNX Runtime EP that binds accel / vendor NPU EP) → **use NPU only**.
2. If the workload **cannot** bind NPU (today: stock **Ollama** llama.cpp path does not target XDNA) → run **CPU**, single-flight. Do **not** enable iGPU/`OLLAMA_IGPU_ENABLE` as a substitute for NPU unless the operator explicitly overrides for a named experiment.
3. Never claim "running on NPU" without a live desk check (accel busy / XRT session). Else **No data**.

## What belongs on NPU (stage targets)
- Vision / image-reader ONNX or vendor EP
- Embedding / small classifier graphs already compiled for XDNA
- Any prior Kokoro/FLM/OpenVINO pipelines that historically used accel (re-verify before claiming)

## What stays on Ollama (CPU for now)
- `ava` / `bruce` / `carly` (+ lane tags) — dolphin-mistral via Ollama
- Until an NPU-capable LLM runtime is wired in `pipelines/npu-llm.md`, chat agents are CPU + single-flight

## Override
Operator may set `RR_ALLOW_IGPU=1` for a one-off Vulkan experiment. Default unset.
