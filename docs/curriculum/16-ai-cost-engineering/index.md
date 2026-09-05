# Phase 16 — AI Cost Engineering

> Where AI money goes, how to measure it per request and per token, and the levers that reduce it: utilisation, batching, caching, model selection, quantisation, autoscaling and capacity planning.

**Status:** 📋 planned · **Estimated effort:** 1 week · **Prerequisites:** Phases 00–15.

## Overview

```text
AI Cost
├── GPU
├── CPU
├── Storage
├── Network
├── API calls
└── Tokens
```

You will build a cost model for an AI system, instrument cost per request and per token, and then work through the optimisation levers one by one, measuring each. The phase ends with a cost dashboard and an optimisation report you could hand to a finance partner.

## Why a DevOps engineer needs this

AI is often the fastest-growing line on the cloud bill, and the most opaque. Being the engineer who can say "this feature costs 0.4 cents per request, here is why, and here are three ways to halve it" is a career-defining skill.

## Learning objectives

- Break down the cost of an AI system into GPU, CPU, storage, network, API calls and tokens.
- Measure cost per request and cost per token.
- Raise GPU utilisation through batching and right-sizing.
- Apply caching (responses, embeddings, KV) and model selection or routing to cut cost.
- Explain quantisation and its quality trade-offs.
- Autoscale and capacity-plan for cost.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | The anatomy of AI cost | 📋 |
| 02 | Cost per request and cost per token | 📋 |
| 03 | GPU utilisation and batching | 📋 |
| 04 | Caching and model selection | 📋 |
| 05 | Quantisation | 📋 |
| 06 | Autoscaling and capacity planning | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 16.1 — Instrument cost per request in Project 6; build a cost dashboard from token and GPU metrics | 🟠 | Local + billing data | 📋 |
| 16.2 — Apply caching, routing and quantisation to a workload; measure cost and quality before and after | 🟠 | Local or cloud GPU (cost stated) | 📋 |

## Phase project — AI cost dashboard and optimisation report

A Grafana dashboard for cost per request, per token, per feature and per tenant, and a written report with measured savings from at least three levers and the quality impact of each.

## Assessment

- **Knowledge check:** 10 questions.
- **Practical:** estimate the monthly cost of a described workload and identify the biggest lever.
- **Troubleshooting:** the bill doubled with no traffic change; find the cause.
- **Architecture:** design capacity planning for a spiky inference workload.
- **Interview:** how do you reduce inference cost?

## Checkpoint

Move on to [Phase 17 — AI-SRE Capstone](../17-capstone-ai-sre/) when you can state your platform's cost per request and show measured savings from three levers.
