# Phase 05 — Deep Learning

> Neural networks and PyTorch, with a constant eye on the hardware: what runs on the CPU, what needs a GPU, and why training jobs run out of memory.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–04.

## Overview

You will learn what a neural network is made of (neurons, layers, weights, bias, activations), how it computes (forward propagation), how it learns (loss, backpropagation, optimisers, epochs, batches), and how to write all of that in PyTorch. Then you will run the same training loop on CPU and, if you have one, GPU, and look at where the time and memory go, including CUDA basics and mixed precision. CNNs, RNNs and LSTMs are covered for conceptual understanding only; transformers get their own phase.

## Why a DevOps engineer needs this

Training jobs are the most resource-hungry workloads you will schedule. Batch size decides memory, epochs decide duration, and mixed precision can halve both. When a training pod is OOMKilled at 3 a.m., the fix is in this phase.

## Learning objectives

- Describe neurons, layers, weights, bias and activation functions.
- Explain forward propagation, loss, backpropagation and optimisers in plain language.
- Explain epochs and batches and how they drive runtime and memory.
- Write and run a PyTorch training loop.
- Compare CPU and GPU execution; explain what CUDA is and how PyTorch uses it.
- Explain mixed precision and when to use it.
- Package a training job as a container and run it as a Kubernetes Job.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Neurons, layers, weights, bias and activations | 📋 |
| 02 | Forward propagation and loss: how a network makes a guess and gets scored | 📋 |
| 03 | Backpropagation and optimisers: how it learns | 📋 |
| 04 | Epochs, batches and the PyTorch training loop | 📋 |
| 05 | CPU vs GPU, CUDA basics and mixed precision | 📋 |
| 06 | CNNs, RNNs and LSTMs: the shapes of networks you will meet | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 5.1 — Train a small network in PyTorch on CPU; time each epoch; vary batch size | 🟢 | Local | 📋 |
| 5.2 — Run the same training on GPU if available; enable mixed precision; compare time and memory | 🟡 | Local GPU or cloud GPU | 📋 |
| 5.3 — Package training as a Kubernetes Job with resource limits; force an OOMKill by raising batch size; diagnose and fix | 🟡 | Local, kind (GPU optional) | 📋 |

## Phase project — Containerised training job on Kubernetes

A reproducible PyTorch training job: Dockerfile, Kubernetes Job manifest with requests and limits, persistent volume for the output artifact, and a `TROUBLESHOOTING.md` covering OOMKill, slow epochs and missing CUDA.

## Assessment

- **Knowledge check:** 12 questions.
- **Practical:** reduce the memory footprint of a given training job by 40% without changing the model.
- **Troubleshooting:** a Job is `OOMKilled`; find the cause from the manifest and training config.
- **Architecture:** design where training artifacts and checkpoints should live and how they are versioned.
- **Interview:** what is the difference between training and inference hardware requirements?

## Checkpoint

Move on to [Phase 06 — Transformers](../06-transformers/) when you can run a training job on Kubernetes, explain what each epoch does, and predict the effect of doubling the batch size on memory and runtime.
