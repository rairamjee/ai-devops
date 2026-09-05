# Phase 07 — LLM Engineering

> Build a production-grade API on top of a large language model: prompting, sampling, streaming, structured outputs, tool calling, rate limits, retries and gateways.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–06.

## Overview

You now know what an LLM is. This phase teaches you to build with one responsibly. You will learn how foundation models are exposed through APIs, how prompting works, what temperature, top-k and top-p actually change, how to stream tokens to a client, how to force structured (JSON) output, how tool and function calling works, and how to make all of it robust: rate limits, retries with backoff, timeouts, and a model gateway that abstracts providers. Labs work against both a hosted model API and a locally served open model so nothing depends on a single vendor.

## Why a DevOps engineer needs this

LLM APIs fail in new ways: rate limits, context overflow, malformed structured output, slow streaming, silent quality regressions. The service patterns in this phase are what make an LLM feature operable, and the gateway is what makes it swappable when a provider changes price or behaviour.

## Learning objectives

- Describe LLM architecture and foundation models at the level needed to choose and operate them.
- Explain parameters, tokens and context windows as they appear in an API request and bill.
- Write effective prompts and explain sampling controls: temperature, top-k, top-p.
- Implement streaming responses end to end.
- Produce and validate structured outputs.
- Implement tool and function calling safely.
- Implement rate limiting, retries with backoff and timeouts; design a model gateway with provider abstraction.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | LLM architecture, foundation models and model APIs | 📋 |
| 02 | Prompting: system prompts, instructions, examples, context | 📋 |
| 03 | Sampling: temperature, top-k, top-p, and reproducibility | 📋 |
| 04 | Streaming and structured outputs | 📋 |
| 05 | Tool calling and function calling | 📋 |
| 06 | Robustness: rate limits, retries, timeouts, idempotency | 📋 |
| 07 | Model gateways and provider abstraction | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 7.1 — Call a model API and a locally served open model through one client interface; compare latency and cost | 🟢 | Local + model API | 📋 |
| 7.2 — Add streaming, structured JSON output with validation, and a tool call that hits the Phase 01 health API | 🟡 | Local, kind | 📋 |
| 7.3 — Inject rate-limit and timeout failures; implement retries with backoff; verify with tests | 🟡 | Local | 📋 |

## Phase project — Project 3: Production LLM API

A FastAPI service with streaming, structured outputs, tool calling, rate limiting, retries and timeouts, deployed to Kubernetes with Prometheus metrics for tokens, latency and errors, and a `.env.example` for provider keys. Full documentation set. This is the application layer for Projects 4, 5 and 6.

## Assessment

- **Knowledge check:** 15 questions.
- **Practical:** add a second provider behind the gateway without changing callers.
- **Troubleshooting:** structured output validation fails on 5% of requests; diagnose and fix.
- **Architecture:** design rate limiting and quotas for a multi-tenant LLM API.
- **Interview:** how do you make an LLM API reliable?

## Checkpoint

Move on to [Phase 08 — RAG](../08-rag/) when Project 3 streams, validates structured output, calls a tool, survives injected failures, and exposes metrics.
