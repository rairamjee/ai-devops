# Phase 13 — GPU Infrastructure

> What a GPU is, why AI needs it, how to size it, how to read it, and how it runs out of memory.

**Status:** 📋 planned · **Estimated effort:** 1–2 weeks · **Prerequisites:** Phases 00–12. A local NVIDIA GPU is useful but not required; a cloud GPU path is provided and its cost stated.

## Overview

You will learn GPU architecture at the level an infrastructure engineer needs: VRAM, memory bandwidth, tensor cores, CUDA, drivers and the container toolkit. Then the operational half: GPU scheduling and sharing, reading utilisation and memory pressure, diagnosing GPU OOM, and estimating a model's memory requirements so you can pick the right GPU before you rent it.

## Why a DevOps engineer needs this

GPUs are the most expensive line on the bill and the hardest resource to schedule. A GPU sitting at 15% utilisation because of a batching misconfiguration costs real money every hour. This phase makes GPU behaviour legible.

## Learning objectives

- Describe GPU architecture: cores, VRAM, memory bandwidth, tensor cores.
- Explain CUDA, NVIDIA drivers, the CUDA toolkit and the NVIDIA Container Toolkit, and how their versions must align.
- Read `nvidia-smi` and GPU metrics: utilisation, memory, temperature, power.
- Diagnose GPU memory pressure and GPU OOM.
- Estimate a model's GPU memory requirement and choose an instance size.
- Explain GPU scheduling and sharing options.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | GPU architecture: VRAM, memory bandwidth, tensor cores | 📋 |
| 02 | CUDA, drivers, toolkit and containers: the version matrix | 📋 |
| 03 | Model memory requirements and GPU sizing | 📋 |
| 04 | GPU utilisation, memory pressure and OOM | 📋 |
| 05 | GPU scheduling and sharing: time-slicing and MIG, conceptually | 📋 |
| 06 | Cloud GPU instances and their cost | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 13.1 — Read `nvidia-smi`; run a PyTorch workload in a GPU container; watch utilisation and memory | 🟠 | Local GPU or cloud GPU | 📋 |
| 13.2 — Provision one cloud GPU instance with Terraform; state the cost; run the same workload; destroy it | 🟠 | Cloud GPU (cost stated) | 📋 |
| 13.3 — Induce GPU OOM by loading too large a model or context; diagnose from logs and metrics; fix by quantisation or sizing | 🟠 | Local GPU or cloud GPU | 📋 |

## Mini project — GPU sizing guide

A short guide, backed by your estimator from Phases 02 and 06 and measurements from these labs, that maps model sizes and context lengths to GPU memory sizes and instance types, with a section on what to check when a workload OOMs.

## Assessment

- **Knowledge check:** 12 questions.
- **Practical:** choose the smallest GPU instance for a named model and concurrency, and justify it.
- **Troubleshooting:** a container cannot see the GPU; walk through driver, toolkit and runtime checks.
- **Architecture:** decide between one large GPU and several small ones for a given workload.
- **Interview:** why does GPU memory matter more than GPU compute for LLM serving?

## Checkpoint

Move on to [Phase 14 — AI + Kubernetes](../14-ai-kubernetes/) when you can read `nvidia-smi`, explain a GPU OOM, size a GPU for a model, and have provisioned and destroyed a cloud GPU with the cost written down.
