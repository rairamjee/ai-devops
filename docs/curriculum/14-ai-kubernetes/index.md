# Phase 14 — AI + Kubernetes

> Run AI workloads on Kubernetes the way you run everything else, plus the GPU-specific parts: device plugins, the GPU Operator, node pools, scheduling, model serving with vLLM, caching and autoscaling.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–13. Solid Kubernetes fundamentals.

## Overview

```text
Kubernetes Cluster
├── CPU Nodes
└── GPU Nodes
     ├── Model Server
     ├── AI Application
     └── Monitoring
```

You will make GPUs schedulable (device plugins, NVIDIA GPU Operator), isolate them (node pools, taints, tolerations, node affinity), request them correctly, deploy a model server (vLLM) with persistent storage and model caching, autoscale it, lock it down with network policies and monitor it. Model serving concepts (inference servers, batching, continuous batching, streaming, concurrency, replicas, quantisation) are taught before vLLM is introduced so you can evaluate alternatives.

## Why a DevOps engineer needs this

This is the job. Everything before it exists so that you can do this phase with understanding rather than by copying manifests.

## Learning objectives

- Explain how device plugins expose GPUs to the scheduler and what the GPU Operator installs.
- Design GPU node pools with taints, tolerations and affinity so only GPU workloads land there.
- Write correct resource requests and limits for GPU pods.
- Explain what an inference server does: model loading, batching, continuous batching, streaming, concurrency.
- Deploy vLLM with persistent model storage and caching; roll a new model version.
- Autoscale inference on a meaningful signal and set network policies.
- Monitor GPU nodes and the model server.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | GPU nodes, device plugins and the NVIDIA GPU Operator | 📋 |
| 02 | Node pools, taints, tolerations and node affinity | 📋 |
| 03 | Resource requests and limits for GPU workloads | 📋 |
| 04 | What an inference server does; deploying vLLM | 📋 |
| 05 | Persistent storage and model caching | 📋 |
| 06 | Autoscaling inference | 📋 |
| 07 | Network policies and GPU monitoring | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 14.1 — Simulate GPU scheduling in kind with a fake device plugin; use taints and tolerations to isolate a node | 🟡 | Local, kind | 📋 |
| 14.2 — Provision a GPU node pool with Terraform; install the GPU Operator; run a GPU smoke test; destroy | 🟠 | Cloud GPU (cost stated) | 📋 |
| 14.3 — Deploy vLLM with a cached model; stream from it; roll a model version; break it with a bad `max_model_len` and fix it | 🟠 | Cloud GPU (cost stated) | 📋 |
| 14.4 — Autoscale vLLM; load test; add network policies and GPU dashboards | 🟠 | Cloud GPU (cost stated) | 📋 |

## Phase project — Project 7: GPU Inference Platform

vLLM serving an open model on a GPU node pool: Terraform, GPU Operator, taints and tolerations, model cache on persistent storage, autoscaling, network policies, GPU monitoring, one deliberate GPU OOM incident with a write-up, full documentation including `COST.md` and `DISASTER-RECOVERY.md`. Ends with `terraform destroy`.

## Assessment

- **Knowledge check:** 15 questions.
- **Practical:** add a second model to the platform without disturbing the first.
- **Troubleshooting:** pods are `Pending` on a GPU node pool; diagnose across taints, requests, the device plugin and capacity.
- **Architecture:** design a multi-team GPU platform with quotas and isolation.
- **Interview:** how do you autoscale inference, and on what signal?

## Checkpoint

Move on to [Phase 15 — AI Security](../15-ai-security/) when Project 7 serves a model on a GPU node pool, autoscales, is monitored, has been destroyed and recreated from Terraform, and its cost is documented.
