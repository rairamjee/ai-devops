#!/usr/bin/env python3
"""
Lab 0.1/0.2 — Inference only: load a saved model artifact and predict.

This is the "serving" half of train_and_predict.py on its own, the way it
runs inside a container or a Kubernetes Job: no training, no data generation,
just load the artifact and answer. It times the two things a production
service cares about at startup and per request.

Usage:
    python predict.py                                   # default artifact path
    MODEL_PATH=artifacts/pod-health-model-v2.joblib python predict.py
    python predict.py --pods pods.json                  # your own pods, JSON list of
                                                        #   {"name": ..., "features": [5 numbers]}
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

T_START = time.perf_counter()
import joblib   # noqa: E402  (imported here so import time is measured)
import numpy as np  # noqa: E402
T_IMPORT = time.perf_counter() - T_START

DEFAULT_MODEL = os.environ.get("MODEL_PATH", "artifacts/pod-health-model-v1.joblib")

SAMPLE_PODS = [
    # name                    restarts cpu%  mem%  err%  p95ms
    {"name": "api-7d9f-abcde",    "features": [0, 35.0, 48.0, 0.2,  180.0]},
    {"name": "worker-5c4b-fghij", "features": [4, 55.0, 61.0, 0.5,  220.0]},
    {"name": "cache-6b8a-klmno",  "features": [0, 20.0, 96.0, 0.1,  150.0]},
    {"name": "ingest-9e2d-pqrst", "features": [1, 70.0, 70.0, 8.5,  400.0]},
    {"name": "batch-3a1c-uvwxy",  "features": [0, 90.0, 40.0, 0.3, 1400.0]},
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", type=Path, default=Path(DEFAULT_MODEL),
                        help="path to the .joblib artifact (env MODEL_PATH also works)")
    parser.add_argument("--pods", type=Path, help="JSON file with a list of {name, features} objects")
    parser.add_argument("--threshold", type=float, default=0.5,
                        help="probability above which a pod is reported UNHEALTHY (default 0.5)")
    args = parser.parse_args()

    # ------------------------------------------------------------- 1. LOAD
    if not args.model.exists():
        print(f"[error]     model artifact not found: {args.model}", file=sys.stderr)
        print("            train one with train_and_predict.py, or set MODEL_PATH", file=sys.stderr)
        return 2
    t0 = time.perf_counter()
    bundle = joblib.load(args.model)
    load_ms = (time.perf_counter() - t0) * 1000
    model = bundle["model"]
    features = bundle["features"]
    print(f"[startup]   imports {T_IMPORT * 1000:.0f} ms, artifact load {load_ms:.0f} ms  "
          f"(model {bundle['version']}, {args.model.stat().st_size / 1024:,.0f} KB)")

    # ------------------------------------------------------------ 2. INPUT
    pods = SAMPLE_PODS
    if args.pods:
        pods = json.loads(args.pods.read_text())
    for pod in pods:  # validate before touching the model: bad input is the caller's fault, not a 500
        if len(pod.get("features", [])) != len(features):
            print(f"[error]     pod {pod.get('name')!r} has {len(pod.get('features', []))} features, "
                  f"expected {len(features)}: {features}", file=sys.stderr)
            return 2

    # ---------------------------------------------------------- 3. PREDICT
    print(f"[predict]   {'pod':<20} {'prediction':<11} {'p(unhealthy)':>12} {'latency':>9}")
    t_all = time.perf_counter()
    for pod in pods:
        row = np.array([pod["features"]], dtype=float)
        t0 = time.perf_counter()
        p_unhealthy = float(model.predict_proba(row)[0][1])
        latency_ms = (time.perf_counter() - t0) * 1000
        label = "UNHEALTHY" if p_unhealthy >= args.threshold else "healthy"
        print(f"            {pod['name']:<20} {label:<11} {p_unhealthy:>12.2f} {latency_ms:>7.2f}ms")
    total_ms = (time.perf_counter() - t_all) * 1000
    print(f"[done]      {len(pods)} predictions in {total_ms:.0f} ms; "
          f"process total {(time.perf_counter() - T_START) * 1000:.0f} ms")
    return 0


if __name__ == "__main__":
    sys.exit(main())
