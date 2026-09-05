# Phase 12 — AI Observability

> Metrics, logs and traces you already know, plus the signals AI adds: tokens, GPU utilisation, model and prompt versions, retrieval quality, generation quality and cost.

**Status:** 📋 planned · **Estimated effort:** 1–2 weeks · **Prerequisites:** Phases 00–11. Prior Prometheus and Grafana experience helps.

## Overview

Traditional observability tells you a service is up and fast. AI observability must also tell you it is answering well, what it costs, and whether the GPU is earning its keep. You will instrument an AI service with Prometheus and Grafana, add OpenTelemetry traces across RAG and agent steps, use Loki for logs where useful, and define SLIs and SLOs that include quality and cost.

```text
Traditional: Metrics · Logs · Traces
AI adds:     Tokens · Latency · Throughput · GPU utilisation · GPU memory
             Model version · Prompt version · Retrieval quality · Generation quality · Cost
```

## Why a DevOps engineer needs this

You will be the one paged. If the dashboards only show HTTP 200s while the model has been answering nonsense for an hour, that is an observability gap you own.

## Learning objectives

- Instrument an AI service with Prometheus metrics for tokens, latency, throughput, errors, model and prompt version.
- Collect GPU utilisation and memory metrics.
- Trace a request across gateway, retrieval, tools and generation with OpenTelemetry.
- Ship structured logs to Loki and correlate them with traces.
- Build Grafana dashboards for an AI service.
- Define SLIs and SLOs for an AI service, including quality and cost, and configure alerts.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Metrics, logs and traces: a fast recap for AI services | 📋 |
| 02 | The AI signals: tokens, GPU, versions, quality, cost | 📋 |
| 03 | Prometheus and Grafana for AI services | 📋 |
| 04 | OpenTelemetry tracing across RAG and agents | 📋 |
| 05 | Logs with Loki | 📋 |
| 06 | SLIs, SLOs and alerting for AI services | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 12.1 — Add Prometheus metrics to Project 3; build a Grafana dashboard | 🟡 | Local, Docker | 📋 |
| 12.2 — Add OpenTelemetry tracing to Project 4 and 5; find a slow retrieval step from the trace | 🟡 | Local, Docker | 📋 |
| 12.3 — Define SLOs; inject latency, token spikes and quality regressions; verify the alerts fire | 🟠 | Local, Docker | 📋 |

## Phase project — Observable AI service

Project 3 (or 4) fully instrumented: metrics, traces, logs, dashboards, `SLO.md` and `RUNBOOK.md`, with alerts that fire on latency, error, token and quality regressions.

## Assessment

- **Knowledge check:** 12 questions.
- **Practical:** add a cost-per-request panel to the dashboard.
- **Troubleshooting:** latency doubled but CPU is flat; find the cause using traces and GPU metrics.
- **Architecture:** define SLIs and SLOs for an incident-response assistant.
- **Interview:** what do you monitor for an LLM service that you would not monitor for a web service?

## Checkpoint

Move on to [Phase 13 — GPU Infrastructure](../13-gpu-infrastructure/) when your service has dashboards, traces and SLO alerts, and you have used them to find an injected fault.
