# Phase 02 — AI Fundamentals

> The vocabulary of AI, explained from zero and tied to the infrastructure each word implies.

**Status:** 📋 planned · **Estimated effort:** 1 week · **Prerequisites:** Phases 00–01.

## Overview

This phase makes you fluent. You will be able to explain AI, machine learning, deep learning, generative AI, foundation models and LLMs; models, parameters and hyperparameters; datasets, features and labels; training and inference; tokens, embeddings and context windows. Not by memorising definitions, but by connecting each term to something you can measure: bytes of memory, seconds of latency, dollars of cost.

## Why a DevOps engineer needs this

When a team says "the 8B model needs a context of 32k", you need to hear "roughly 16 GB of weights in fp16 plus a KV cache that grows with every token, so plan GPU memory accordingly". This phase gives you that translation layer.

## Learning objectives

- Explain how AI, ML, deep learning, generative AI, foundation models and LLMs relate.
- Explain what a model is, what parameters and hyperparameters are, and how they differ.
- Explain datasets, features and labels with an infrastructure example.
- Explain training versus inference in terms of compute, duration, frequency and failure modes.
- Explain tokens, embeddings and context windows and what each costs at inference time.
- Estimate a model's memory footprint from its parameter count and numeric precision.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | AI, ML, deep learning, generative AI: what nests inside what | 📋 |
| 02 | Models, parameters, hyperparameters, weights: what a model physically is | 📋 |
| 03 | Data: datasets, features, labels, and why data quality is an ops problem | 📋 |
| 04 | Training versus inference: two very different workloads | 📋 |
| 05 | Tokens, embeddings and context windows | 📋 |
| 06 | Reading an AI architecture diagram: from user to GPU | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 2.1 — Tokenise real log lines and prompts with a Hugging Face tokenizer; count tokens, observe how they vary | 🟢 | Local | 📋 |
| 2.2 — Inspect a downloaded model: files, sizes, config, parameter count; compute memory in fp32, fp16 and int8 | 🟢 | Local | 📋 |

## Mini project — Model resource estimator

A small CLI that takes a parameter count, precision and context length and prints estimated weight memory, a rough KV-cache estimate and a recommendation of the smallest common GPU memory size that fits. You will use it in Phases 06, 13 and 14.

## Assessment

- **Knowledge check:** 15 questions across all terms.
- **Practical:** given a Hugging Face model card, estimate its memory footprint and defend the number.
- **Troubleshooting:** a request is rejected for exceeding the context window; explain why and propose two fixes.
- **Architecture:** label a supplied architecture diagram with where training, inference, embeddings and tokens appear.
- **Interview:** what is a token, why does it matter for cost and latency?

## Checkpoint

Move on to [Phase 03 — Math for AI](../03-math-for-ai/) when you can explain every term in section 14 of the design specification without notes and estimate a model's memory from its parameter count.
