# Phase 11 — LLMOps

> LLM applications need an operational lifecycle like any other production system: versioned prompts, evaluation against golden datasets, regression tests, tracing, token accounting and routing.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–10.

## Overview

A prompt change is a deploy. A model upgrade is a dependency bump that can silently change behaviour. This phase gives you the lifecycle to manage that: prompt versioning, golden datasets, evaluation and regression testing, tracing across RAG and agent steps, token accounting, model routing and provider abstraction, and quality, cost and latency monitoring.

## Why a DevOps engineer needs this

You would never ship a code change without tests and a rollback plan. LLM applications are shipped that way constantly, and they break in ways no health check catches. This phase gives you the equivalent of CI, monitoring and rollback for prompts and models.

## Learning objectives

- Version prompts and tie every response to a prompt version and model version.
- Build a golden dataset and an evaluation harness; run it as a regression test in CI.
- Trace a request across gateway, retrieval, tool calls and generation.
- Account for tokens and cost per request, per feature and per tenant.
- Route between models and providers by cost, latency or capability.
- Monitor quality, cost and latency and alert on regressions.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Why LLM applications need an operational lifecycle | 📋 |
| 02 | Prompt versioning | 📋 |
| 03 | Evaluation and golden datasets | 📋 |
| 04 | Regression testing in CI | 📋 |
| 05 | Tracing and token accounting | 📋 |
| 06 | Model routing and provider abstraction | 📋 |
| 07 | Quality, cost and latency monitoring | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 11.1 — Version the prompts in Project 3 and stamp every response with prompt and model version | 🟢 | Local | 📋 |
| 11.2 — Build a golden dataset for Project 4; run evaluation in CI; make a prompt change that fails it | 🟡 | Local | 📋 |
| 11.3 — Add tracing and per-request token and cost accounting; route cheap queries to a smaller model | 🟡 | Local | 📋 |

## Phase project — Project 6: LLMOps Platform

A model gateway with provider abstraction and routing, prompt management with versioning, a golden-dataset evaluation harness wired into CI, tracing, token accounting and cost reporting. Projects 3, 4 and 5 are re-pointed through it.

## Assessment

- **Knowledge check:** 12 questions.
- **Practical:** add a routing rule and prove it with traces.
- **Troubleshooting:** answer quality dropped after a provider's model update; find it using evaluation history.
- **Architecture:** design prompt promotion from staging to production with rollback.
- **Interview:** how do you test an LLM application?

## Checkpoint

Move on to [Phase 12 — AI Observability](../12-ai-observability/) when a prompt change can fail CI, every response carries prompt and model versions, and you can report cost per request.
