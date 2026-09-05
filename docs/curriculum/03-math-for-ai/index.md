# Phase 03 — Math for AI

> Only the mathematics you need to understand why AI systems behave the way they do in production. No proofs.

**Status:** 📋 planned · **Estimated effort:** 1 week · **Prerequisites:** Phases 00–02. High-school algebra.

## Overview

Three small toolkits: linear algebra (scalars, vectors, matrices, tensors, dot products, matrix multiplication), statistics (mean, median, variance, standard deviation, probability, distributions, correlation), and optimisation (derivative, gradient, loss, gradient descent). Each is taught with NumPy, tied directly to a production question, and stops as soon as it has answered it.

## Why a DevOps engineer needs this

Matrix multiplication is *why* GPUs exist in your cluster. Percentiles and distributions are how you already read latency dashboards; here they also explain model evaluation. Gradient descent is what a training job is doing for those eight hours on the GPU node, and why it can diverge and waste them.

## Learning objectives

- Describe scalars, vectors, matrices and tensors and recognise them in model shapes.
- Compute a dot product and a matrix multiplication by hand for tiny cases and with NumPy for large ones.
- Explain why matrix multiplication parallelises well and what that implies for GPUs.
- Use mean, median, variance, standard deviation and percentiles to describe latency and model outputs.
- Explain probability and distributions well enough to read a model's confidence scores.
- Explain derivative, gradient, loss and gradient descent, and implement gradient descent in a few lines.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Scalars, vectors, matrices, tensors: reading model shapes | 📋 |
| 02 | Dot products and matrix multiplication: why GPUs exist | 📋 |
| 03 | Statistics you already use: mean, median, variance, percentiles, and p95 latency | 📋 |
| 04 | Probability and distributions: what a confidence score means | 📋 |
| 05 | Derivatives, gradients, loss and gradient descent: what a training job is doing | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 3.1 — Benchmark matrix multiplication in pure Python vs NumPy vs PyTorch on CPU (and GPU if available); plot time vs size | 🟢 | Local | 📋 |
| 3.2 — Implement gradient descent from scratch to fit a line; break it with a bad learning rate and watch it diverge | 🟢 | Local | 📋 |

## Mini project — Matrix-multiply benchmark report

A short report with a chart: time versus matrix size for pure Python, NumPy and PyTorch, with a paragraph explaining the result in terms of parallelism and memory bandwidth. This is your first performance-engineering artifact for the portfolio.

## Assessment

- **Knowledge check:** 10 questions.
- **Practical:** compute the output shape of a matrix multiplication chain and the memory it needs.
- **Troubleshooting:** a training loss goes to `NaN`; name the two most likely causes.
- **Architecture:** explain to a stakeholder why a CPU-only node is fine for a 100 MB classical model but not for a 14 GB LLM.
- **Interview:** why are GPUs good at deep learning?

## Checkpoint

Move on to [Phase 04 — Machine Learning](../04-machine-learning/) when you can explain matrix multiplication, percentiles and gradient descent with a whiteboard sketch and a NumPy snippet.
