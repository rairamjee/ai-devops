#!/usr/bin/env python3
"""
Lab 0.1 — Run Your First Model (Part A): train, save, load, predict.

What this script demonstrates, in DevOps terms:

    training   ~ a build step   -> produces an artifact (the model file)
    the model  ~ an artifact    -> has a size, a version, a checksum
    inference  ~ serving        -> loads the artifact and answers requests, fast

The problem: predict whether a Kubernetes pod is UNHEALTHY from five metrics.
The data is synthetic (generated below) so the lab needs no external files.

Usage:
    python train_and_predict.py                       # defaults: v1, 10k rows
    python train_and_predict.py --version v2 --threshold 2.0
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# The five signals the model sees for each pod, in this order.
FEATURES = ["restart_count", "cpu_pct", "mem_pct", "error_rate_pct", "p95_latency_ms"]


def generate_pod_telemetry(n: int, seed: int, error_rate_threshold: float) -> tuple[np.ndarray, np.ndarray]:
    """Synthesise pod metrics and a ground-truth label.

    In the real world these rows would come from Prometheus and the label from
    incident records. Here a hidden rule plus noise stands in for reality; the
    model's job is to rediscover that rule from the data alone.
    """
    rng = np.random.default_rng(seed)
    restart_count = rng.poisson(0.7, n)
    cpu_pct = rng.uniform(0, 100, n)
    mem_pct = rng.uniform(0, 100, n)
    error_rate_pct = rng.exponential(1.5, n).clip(0, 100)
    p95_latency_ms = rng.gamma(2.0, 120.0, n)

    # Hidden truth: a pod is unhealthy if it restarts a lot, or is starved of
    # memory, or throws many errors, or is very slow.
    unhealthy = (
        (restart_count >= 3)
        | (mem_pct > 92)
        | (error_rate_pct > error_rate_threshold)
        | (p95_latency_ms > 900)
    )
    # Flip ~4% of labels to mimic noisy real-world incident data.
    noise = rng.random(n) < 0.04
    y = np.where(noise, ~unhealthy, unhealthy).astype(int)

    X = np.column_stack([restart_count, cpu_pct, mem_pct, error_rate_pct, p95_latency_ms])
    return X, y


def sha256_of(path: Path) -> str:
    """Checksum the artifact so we can prove which file is in production."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--samples", type=int, default=10_000, help="rows of synthetic telemetry (default 10000)")
    parser.add_argument("--seed", type=int, default=42, help="random seed, so runs are reproducible")
    parser.add_argument("--threshold", type=float, default=5.0,
                        help="error-rate %% above which a pod is labelled unhealthy (default 5.0)")
    parser.add_argument("--version", default="v1", help="model version tag used in the artifact name")
    parser.add_argument("--out", type=Path, default=Path("artifacts"), help="directory for model artifacts")
    args = parser.parse_args()

    # ------------------------------------------------------------------ 1. DATA
    X, y = generate_pod_telemetry(args.samples, args.seed, args.threshold)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=args.seed, stratify=y
    )
    print(f"[data]      {len(X_train):>6} training rows, {len(X_test):>5} test rows, "
          f"{y.mean():.1%} labelled unhealthy")

    # -------------------------------------------------------------- 2. TRAINING
    # 100 decision trees vote on each pod. You do not need to understand how a
    # random forest works yet (Phase 04); watch what it costs and what it produces.
    model = RandomForestClassifier(n_estimators=100, random_state=args.seed, n_jobs=-1)
    t0 = time.perf_counter()
    model.fit(X_train, y_train)
    train_s = time.perf_counter() - t0
    print(f"[train]     RandomForest(100 trees) fitted in {train_s:.2f}s")

    # ------------------------------------------------------------ 3. EVALUATION
    # Always score on data the model did NOT see during training.
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"[evaluate]  accuracy on held-out test data: {acc:.1%}")
    print(classification_report(y_test, predictions, target_names=["healthy", "unhealthy"], digits=3))

    # --------------------------------------------------------- 4. THE ARTIFACT
    # Everything the model learned is now numbers inside `model`. Serialise it,
    # together with metadata a serving system will need, into ONE file.
    args.out.mkdir(parents=True, exist_ok=True)
    model_path = args.out / f"pod-health-model-{args.version}.joblib"
    bundle = {
        "model": model,
        "features": FEATURES,
        "version": args.version,
        "trained_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "label_threshold_error_rate_pct": args.threshold,
        "test_accuracy": round(acc, 4),
    }
    joblib.dump(bundle, model_path)
    size_kb = model_path.stat().st_size / 1024
    digest = sha256_of(model_path)
    (args.out / f"pod-health-model-{args.version}.sha256").write_text(f"{digest}  {model_path.name}\n")
    print(f"[artifact]  {model_path}  ({size_kb:,.0f} KB)  sha256={digest[:16]}...")

    # -------------------------------------------------------------- 5. INFERENCE
    # In production this part runs in a different process, on a different
    # machine, possibly months later. All it needs is the artifact.
    del model
    t0 = time.perf_counter()
    loaded = joblib.load(model_path)
    load_ms = (time.perf_counter() - t0) * 1000
    served = loaded["model"]
    print(f"[load]      artifact {loaded['version']} loaded in {load_ms:.1f} ms")

    sample_pods = {
        # name                 restarts cpu%  mem%  err%  p95ms
        "api-7d9f-abcde":     [0,      35.0, 48.0, 0.2,  180.0],
        "worker-5c4b-fghij":  [4,      55.0, 61.0, 0.5,  220.0],
        "cache-6b8a-klmno":   [0,      20.0, 96.0, 0.1,  150.0],
        "ingest-9e2d-pqrst":  [1,      70.0, 70.0, 8.5,  400.0],
        "batch-3a1c-uvwxy":   [0,      90.0, 40.0, 0.3, 1400.0],
    }
    print(f"[predict]   {'pod':<20} {'prediction':<11} {'p(unhealthy)':>12} {'latency':>9}")
    for name, features in sample_pods.items():
        row = np.array([features])
        t0 = time.perf_counter()
        p_unhealthy = served.predict_proba(row)[0][1]
        latency_ms = (time.perf_counter() - t0) * 1000
        label = "UNHEALTHY" if p_unhealthy >= 0.5 else "healthy"
        print(f"            {name:<20} {label:<11} {p_unhealthy:>12.2f} {latency_ms:>7.2f}ms")

    # One call with all five pods versus five calls with one pod each. Most of
    # the per-call time above is fixed overhead, not work; batching amortises it.
    all_rows = np.array(list(sample_pods.values()))
    t0 = time.perf_counter()
    served.predict_proba(all_rows)
    batch_ms = (time.perf_counter() - t0) * 1000
    print(f"[batch]     all {len(all_rows)} pods in one call: {batch_ms:.2f} ms total, "
          f"{batch_ms / len(all_rows):.2f} ms per pod")

    # ---------------------------------------------------------------- 6. SUMMARY
    summary = {
        "version": args.version,
        "test_accuracy": round(acc, 4),
        "train_seconds": round(train_s, 2),
        "artifact_kb": round(size_kb),
        "sha256": digest,
        "load_ms": round(load_ms, 1),
    }
    print("[summary]  ", json.dumps(summary))


if __name__ == "__main__":
    main()
