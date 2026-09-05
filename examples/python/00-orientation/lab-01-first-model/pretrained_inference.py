#!/usr/bin/env python3
"""
Lab 0.1 — Run Your First Model (Part B, optional): run a PRETRAINED model.

Part A trained a model from scratch in seconds. Most AI you will operate is
the opposite: someone else spent GPU-weeks training a model, published the
weights, and your job is to download, load and serve them.

This script downloads a small sentiment-classification transformer
(~268 MB on disk, ~67 million parameters), loads it on the CPU, and classifies
incident-channel messages. It times every step so you can see where a
production request's latency actually comes from.

Usage:
    python pretrained_inference.py
    HF_HOME=/data/hf-cache python pretrained_inference.py   # choose the cache location
"""
from __future__ import annotations

import os
import time

# A specific, pinned model. Never rely on a library's *default* model in
# production: defaults change between library versions, and so would your
# service's behaviour.
MODEL_ID = "distilbert-base-uncased-finetuned-sst-2-english"

MESSAGES = [
    "Deploy finished, all pods healthy, dashboards green.",
    "prod is down, 500s everywhere, customers screaming",
    "Rolled back to v1.4.2, error rate recovering.",
    "Node pool is out of GPU memory again and the job keeps crashing.",
    "Latency p95 back under 200ms after the cache fix.",
]


def main() -> None:
    # ------------------------------------------------------------- 0. IMPORTS
    # Importing the AI libraries is itself slow. In a container this is part
    # of your startup time, which matters for autoscaling and rollouts.
    t0 = time.perf_counter()
    import torch
    from transformers import pipeline
    import_s = time.perf_counter() - t0
    print(f"[import]    torch + transformers imported in {import_s:.2f}s  "
          f"(torch {torch.__version__}, CUDA available: {torch.cuda.is_available()})")

    # ------------------------------------------------------ 1. LOAD THE MODEL
    # First run: downloads weights + tokenizer into the Hugging Face cache
    # (~/.cache/huggingface by default; override with HF_HOME). Later runs
    # load from disk. In production this step is your pod's readiness delay.
    t0 = time.perf_counter()
    classifier = pipeline("sentiment-analysis", model=MODEL_ID, device="cpu")
    load_s = time.perf_counter() - t0
    n_params = sum(p.numel() for p in classifier.model.parameters())
    fp32_mb = n_params * 4 / 1024**2  # 4 bytes per parameter in 32-bit float
    print(f"[load]      model ready in {load_s:.2f}s  "
          f"({n_params / 1e6:.1f}M parameters, about {fp32_mb:.0f} MB of weights in fp32)")
    print(f"[cache]     weights cached under {os.environ.get('HF_HOME', '~/.cache/huggingface')}")

    # ----------------------------------------------------------- 2. WARM-UP
    # The very first inference is slower (lazy initialisation, memory
    # allocation). Serving systems send a warm-up request before taking traffic.
    t0 = time.perf_counter()
    classifier("warm-up")
    print(f"[warm-up]   first inference: {(time.perf_counter() - t0) * 1000:.0f} ms")

    # ---------------------------------------------------------- 3. INFERENCE
    print(f"[predict]   {'label':<9} {'score':>6} {'latency':>9}  message")
    for msg in MESSAGES:
        t0 = time.perf_counter()
        result = classifier(msg)[0]
        latency_ms = (time.perf_counter() - t0) * 1000
        print(f"            {result['label']:<9} {result['score']:>6.3f} {latency_ms:>7.0f}ms  {msg}")

    # -------------------------------------------------------------- 4. BATCH
    # One call with five inputs versus five calls with one input each.
    # Batching is the single most important lever for inference throughput.
    t0 = time.perf_counter()
    classifier(MESSAGES, batch_size=len(MESSAGES))
    batch_ms = (time.perf_counter() - t0) * 1000
    print(f"[batch]     all {len(MESSAGES)} messages in one call: {batch_ms:.0f} ms total, "
          f"{batch_ms / len(MESSAGES):.0f} ms per message")


if __name__ == "__main__":
    main()
