# Labs

Labs are the core of the course. Each one is practical, reproducible, incremental, production-oriented and safe. Where possible a lab provides a **CPU-only path** and a **GPU path**, and every lab that touches paid cloud resources states that up front and ends with cleanup.

## Difficulty

| Level | Scope |
|---|---|
| 🟢 Beginner | Single machine: Python scripts, API calls, simple model inference |
| 🟡 Intermediate | Multi-component: Docker, Kubernetes, RAG, ML pipelines |
| 🟠 Advanced | Production-style: GPU serving, Kubernetes inference, autoscaling, observability |
| 🔴 Expert | Architecture and operations: AI platform, distributed inference, incident response, security, cost |

## Available labs

| Lab | Phase | Difficulty | Time | Environment |
|---|---|---|---|---|
| [0.1 — Run Your First Model](/curriculum/00-orientation/01-what-is-ai#hands-on-lab-0-1-run-your-first-model) | 00 Orientation | 🟢 | 45–60 min | Local, CPU only |
| [0.2 — Verify Your Environment and Containerise Your First Model](/curriculum/00-orientation/02-environment-setup#hands-on-lab-0-2-verify-your-environment) | 00 Orientation | 🟢 | 45–60 min | Local, Docker + kind |
| [0.3 — Run the Model on Kubernetes and Break It](/curriculum/00-orientation/03-ai-production-stack#hands-on-lab-0-3-run-the-model-on-kubernetes) | 00 Orientation | 🟡 | 45–60 min | Local, kind |

## Planned flagship labs

One lab per phase is listed here so you can see where the course is heading. Phase overview pages list the full set.

| Lab | Phase | Difficulty | Environment |
|---|---|---|---|
| Build and containerise a Kubernetes Health API | 01 Python | 🟡 | Local, Docker + kind |
| Estimate model memory from parameter counts and precision | 02 AI Fundamentals | 🟢 | Local |
| Benchmark matrix multiplication and write gradient descent from scratch | 03 Math | 🟢 | Local |
| Train, version and serve a pod-failure classifier | 04 Machine Learning | 🟡 | Local, Docker |
| Train a PyTorch model as a Kubernetes Job; break it with a GPU/CPU OOM | 05 Deep Learning | 🟡 | Local (GPU optional) |
| Measure transformer latency vs sequence length and batch size | 06 Transformers | 🟡 | Local (GPU optional) |
| Build a streaming LLM API with retries, rate limits and structured outputs | 07 LLM Engineering | 🟡 | Local + model API |
| Ingest runbooks into pgvector and evaluate retrieval quality | 08 RAG | 🟡 | Local, Docker |
| Build a read-only Kubernetes investigation agent with policy and approval gates | 09 AI Agents | 🟠 | Local, kind |
| Track experiments and promote a model through the MLflow registry with rollback | 10 MLOps | 🟡 | Local, Docker |
| Version prompts and run regression evaluation against a golden dataset | 11 LLMOps | 🟡 | Local |
| Instrument an LLM service with Prometheus, Grafana and OpenTelemetry; define SLOs | 12 AI Observability | 🟠 | Local, Docker |
| Diagnose GPU OOM and read GPU utilisation with `nvidia-smi` | 13 GPU Infrastructure | 🟠 | Local GPU or cloud GPU |
| Deploy vLLM on a GPU node pool with taints, tolerations and autoscaling | 14 AI + Kubernetes | 🟠 | Cloud GPU (cost stated) |
| Attack and harden a RAG assistant against prompt injection | 15 AI Security | 🟠 | Local |
| Build an AI cost dashboard and produce an optimisation report | 16 AI Cost Engineering | 🟠 | Local + cloud billing data |
| Run a game day against the AI-SRE platform | 17 Capstone | 🔴 | Cloud (cost stated) |

## Lab structure

Every lab uses the same sections so you always know where to look:

```text
Lab Title · Objective · Difficulty · Estimated Time · Prerequisites · Architecture
Environment Requirements · Setup · Steps · Expected Output · Validation
Troubleshooting · Cleanup · Extension Challenge · Questions
```

## Safety rules

Agent and infrastructure labs default to safe behaviour:

```text
AI Agent → Tool → Policy → Validation → Human Approval → Action
```

Labs start with read-only tools (`kubectl get`, `kubectl describe`, `kubectl logs`). Destructive actions are introduced later, and only with explicit approval, least privilege, sandboxed environments, audit logs and clear rollback procedures.
