# Phase 06 — Transformers

> How the architecture behind every modern LLM works, and exactly what each part costs in compute, memory, latency and throughput at inference time.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–05.

## Overview

Transformers get thorough treatment because they are what you will serve for the rest of your career. You will learn tokenisation, embeddings, attention and self-attention, query, key and value, multi-head attention, positional information, encoders and decoders, and how transformer blocks stack. Every concept is immediately tied to an operational consequence: why attention cost grows with sequence length, why the KV cache eats GPU memory, what decides time-to-first-token versus tokens-per-second, and why batching helps throughput.

## Why a DevOps engineer needs this

Without this phase, inference-server tuning is guesswork. With it, `max_model_len`, batch size, KV-cache memory and GPU utilisation become dials you understand. It is also the phase that makes GPU sizing (Phase 13) a calculation rather than a shrug.

## Learning objectives

- Explain tokenisation and embeddings and how they turn text into tensors.
- Explain attention, self-attention and query/key/value at the level of "what is being compared with what".
- Explain multi-head attention, positional information, encoder and decoder roles, and a transformer block.
- Connect sequence length to compute and memory, and explain the KV cache.
- Explain the two phases of LLM inference (prefill and decode) and what they mean for latency and throughput.
- Measure latency versus sequence length and batch size on a real model.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Tokenisation: from text to integers | 📋 |
| 02 | Embeddings: from integers to vectors | 📋 |
| 03 | Attention and self-attention: query, key, value | 📋 |
| 04 | Multi-head attention and positional information | 📋 |
| 05 | Encoders, decoders and the transformer block | 📋 |
| 06 | What it costs: compute, memory, the KV cache, prefill vs decode, latency and throughput | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 6.1 — Explore a tokenizer: tokens per word across languages and code; count parameters and memory of a small model | 🟢 | Local | 📋 |
| 6.2 — Run a small open model with Hugging Face Transformers; measure time-to-first-token and tokens-per-second vs prompt length | 🟡 | Local (GPU optional) | 📋 |
| 6.3 — Batch requests and observe throughput vs latency; hit an out-of-memory error by raising context length and explain it | 🟡 | Local GPU or cloud GPU | 📋 |

## Mini project — Inference cost calculator

Extend the Phase 02 estimator to include KV-cache memory for a given context length and batch size, and a rough tokens-per-second estimate from memory bandwidth. Validate it against your own measurements from Lab 6.2.

## Assessment

- **Knowledge check:** 15 questions.
- **Practical:** estimate the GPU memory needed to serve a named model at a given context length and concurrency, then test the estimate.
- **Troubleshooting:** time-to-first-token is fine but tokens-per-second collapses under load; explain the likely cause.
- **Architecture:** decide whether a given workload is latency-bound or throughput-bound and justify a serving configuration.
- **Interview:** what is the KV cache and why does it matter for serving?

## Checkpoint

Move on to [Phase 07 — LLM Engineering](../07-llm-engineering/) when you can explain attention with a sketch, explain prefill versus decode, and estimate a model's serving memory including KV cache.
