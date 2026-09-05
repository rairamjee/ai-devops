# Projects

Eight projects, each more realistic than the last, culminating in an AI-SRE platform. Every project is a portfolio piece: it lives in its own repository (or directory) with real engineering documentation.

## Required documentation for every project

```text
README.md            what it is, how to run it
ARCHITECTURE.md      components, data flow, decisions and trade-offs
SETUP.md             reproducible setup from a clean machine
OPERATIONS.md        how to run it day to day: deploy, scale, upgrade, roll back
TROUBLESHOOTING.md   known failure modes and how to diagnose them
SECURITY.md          threat surface, controls, secrets handling
COST.md              what it costs to run and how to reduce it
```

Where applicable also include `DISASTER-RECOVERY.md`, `RUNBOOK.md`, `SLO.md` and `THREAT-MODEL.md`.

## The projects

### Project 1 — Kubernetes Health API

**Phase:** 01 Python for AI/DevOps · **Status:** 📋 planned

A FastAPI service that reports the health of a Kubernetes namespace: pod status, restarts, recent events, resource usage. Containerised, deployed to kind, with tests.

Skills: Python, FastAPI, Kubernetes API, Docker.

Why it matters: this is the skeleton every later AI service is built on, and the first tool your DevOps agent (Project 5) will call.

### Project 2 — Production ML Pipeline

**Phase:** 10 MLOps · **Status:** 📋 planned

Train, evaluate, register and deploy a model with MLflow, run it as a pipeline, roll it back, and detect drift.

Skills: training, evaluation, MLflow, Docker, Kubernetes.

### Project 3 — Production LLM API

**Phase:** 07 LLM Engineering · **Status:** 📋 planned

An LLM-backed API with streaming responses, structured outputs, tool calling, rate limiting, retries and timeouts. Containerised, deployed to Kubernetes, instrumented.

Skills: LLM APIs, FastAPI, streaming, Docker, Kubernetes, observability.

### Project 4 — DevOps Knowledge Assistant

**Phase:** 08 RAG · **Status:** 📋 planned

A retrieval-augmented assistant over your own runbooks and documentation using PostgreSQL + pgvector, with an evaluation harness that measures retrieval quality and grounding.

Skills: embeddings, pgvector, RAG, LLM.

### Project 5 — DevOps AI Agent

**Phase:** 09 AI Agents · **Status:** 📋 planned

An investigation agent that inspects Kubernetes, reads logs, queries metrics, searches runbooks (Project 4), analyses recent changes and produces a diagnosis. **Read-only first**, with policy, validation, approval and audit gates before any action.

Skills: tool calling, Kubernetes, logs, metrics, RAG, guardrails.

### Project 6 — LLMOps Platform

**Phase:** 11 LLMOps · **Status:** 📋 planned

A model gateway with provider abstraction and routing, prompt versioning, golden-dataset evaluation, regression testing, tracing, token accounting and cost reporting.

Skills: model gateway, prompt management, evaluation, tracing, cost.

### Project 7 — GPU Inference Platform

**Phase:** 14 AI + Kubernetes · **Status:** 📋 planned

vLLM serving an open model on a GPU node pool: GPU Operator, taints and tolerations, model caching, autoscaling, GPU monitoring, and deliberate GPU OOM troubleshooting. Cloud cost is stated up front and the lab ends with `terraform destroy`.

Skills: Kubernetes, GPU, CUDA, NVIDIA, vLLM, autoscaling.

### Project 8 — AI-SRE Platform (capstone)

**Phase:** 17 Capstone · **Status:** 📋 planned

Combines everything. The system receives an incident question, inspects infrastructure, metrics, logs and deployment history, searches runbooks, generates a root-cause hypothesis with evidence, recommends remediation, requests approval, executes the approved remediation, verifies recovery and produces an incident report.

```text
                         USER
                           │
                      API Gateway
                           │
                      AI SRE API
             ┌─────────────┼─────────────┐
        Kubernetes     Prometheus       Loki
             └─────────────┼─────────────┘
                       AI Agent
             ┌─────────────┼─────────────┐
            RAG        LLM Gateway      Tools
             │             │             │
         Vector DB      LLM Server    DevOps APIs
                           │
                          GPU
                           │
                      Kubernetes
```

## Project sequence

Projects are numbered by the order they were designed, but taught in the order the skills arrive:

```text
P1 → Phase 01 · P3 → Phase 07 · P4 → Phase 08 · P5 → Phase 09
P2 → Phase 10 · P6 → Phase 11 · P7 → Phase 14 · P8 → Phase 17
```

## Presenting projects in interviews

For each project be ready to explain: the architecture and why; what the SLOs are; how it scales at 10× traffic; what happens when each component fails; how it is secured; what it costs; and what you would change with more time. The [interview prep](/interview-prep/) section collects these questions.
