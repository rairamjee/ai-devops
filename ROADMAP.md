# Roadmap

The curriculum is organised into 18 phases grouped into seven milestones. Effort estimates assume roughly 8–10 focused hours per week and are guidance, not targets. Status legend: ✅ available · 🚧 in progress · 📋 planned.

## Milestones

```text
M1 Foundations        00 Orientation · 01 Python · 02 AI Fundamentals · 03 Math
M2 Models             04 Machine Learning · 05 Deep Learning · 06 Transformers
M3 LLM Applications   07 LLM Engineering · 08 RAG · 09 AI Agents
M4 Operations         10 MLOps · 11 LLMOps · 12 AI Observability
M5 Infrastructure     13 GPU Infrastructure · 14 AI + Kubernetes
M6 Governance         15 AI Security · 16 AI Cost Engineering
M7 Capstone           17 AI-SRE Platform
```

## Phase plan

| Phase | Subject | Goal | Tangible output | Est. effort | Status |
|---|---|---|---|---|---|
| 00 | Orientation | Understand what AI is, how the course works, and get a working environment | First model running locally | 1 week | 🚧 |
| 01 | Python for AI/DevOps | Enough Python to build APIs, call the Kubernetes API and package code | **Project 1: Kubernetes Health API** | 2 weeks | 📋 |
| 02 | AI Fundamentals | Explain AI/ML/DL/GenAI/LLMs, training vs inference, tokens, embeddings, context windows | Model resource estimator CLI | 1 week | 📋 |
| 03 | Math for AI | Vectors, matrices, dot products, statistics, gradients, gradient descent | Matrix-multiply benchmark + gradient descent from scratch | 1 week | 📋 |
| 04 | Machine Learning | The ML lifecycle from a production engineer's perspective | Pod-failure predictor served as an API | 2 weeks | 📋 |
| 05 | Deep Learning | Neural networks, PyTorch, CPU vs GPU, CUDA basics, mixed precision | Containerised PyTorch training job on Kubernetes | 2 weeks | 📋 |
| 06 | Transformers | Tokenisation, attention, transformer blocks, and what they cost at inference time | Inference cost calculator + latency benchmark | 2 weeks | 📋 |
| 07 | LLM Engineering | Prompting, sampling, streaming, structured outputs, tool calling, gateways | **Project 3: Production LLM API** | 2 weeks | 📋 |
| 08 | RAG | Chunking, embeddings, pgvector, retrieval, reranking, evaluation | **Project 4: DevOps Knowledge Assistant** | 2 weeks | 📋 |
| 09 | AI Agents | Agent loops, tools, guardrails, human-in-the-loop, auditability | **Project 5: DevOps AI Agent** (read-only first) | 2 weeks | 📋 |
| 10 | MLOps | Reproducibility, experiment tracking, registry, pipelines, drift | **Project 2: Production ML Pipeline** (MLflow) | 2 weeks | 📋 |
| 11 | LLMOps | Prompt versioning, evaluation, golden datasets, tracing, routing, cost | **Project 6: LLMOps Platform** | 2 weeks | 📋 |
| 12 | AI Observability | AI-specific signals on Prometheus, Grafana, OpenTelemetry, Loki | Observable AI service with SLOs | 1–2 weeks | 📋 |
| 13 | GPU Infrastructure | GPU architecture, VRAM, CUDA, drivers, utilisation, OOM, sizing | GPU sizing guide + OOM troubleshooting lab | 1–2 weeks | 📋 |
| 14 | AI + Kubernetes | GPU nodes, device plugins, GPU Operator, scheduling, vLLM, autoscaling | **Project 7: GPU Inference Platform** | 2 weeks | 📋 |
| 15 | AI Security | Traditional controls plus prompt injection, leakage, poisoning, tool abuse | Threat model + hardening of an earlier project | 1 week | 📋 |
| 16 | AI Cost Engineering | Cost per request/token, utilisation, batching, caching, quantisation | AI cost dashboard + optimisation report | 1 week | 📋 |
| 17 | AI-SRE Capstone | Combine everything into an incident-investigation and remediation platform | **Project 8: AI-SRE Platform** | 3–4 weeks | 📋 |

Total: roughly 30–34 weeks at a steady pace.

## Project sequence

Projects are ordered by the skills they need, which is why Project 2 (MLflow pipeline) lands in Phase 10 after the LLM application projects.

```text
P1 Kubernetes Health API        → Phase 01
P3 Production LLM API           → Phase 07
P4 DevOps Knowledge Assistant   → Phase 08
P5 DevOps AI Agent              → Phase 09
P2 Production ML Pipeline       → Phase 10
P6 LLMOps Platform              → Phase 11
P7 GPU Inference Platform       → Phase 14
P8 AI-SRE Platform (capstone)   → Phase 17
```

## Environment progression

- **Local first:** Linux/macOS/Windows + WSL, Python, Git, Docker, kind or Minikube, PostgreSQL, Prometheus, Grafana. Nearly everything through Phase 12 runs on a laptop.
- **Cloud:** AWS is the primary cloud from Phase 13 onward, with Azure/GCP concepts where useful. Every cloud lab states its cost drivers and includes cleanup.
- **GPU:** a local GPU is used when available; otherwise labs provide a cloud GPU path. Labs distinguish a CPU-only path from a GPU path wherever possible.

## What "done" means

The course is complete when a learner can independently **design → build → containerise → deploy → observe → secure → scale → troubleshoot → optimise** an AI workload, has the eight projects on GitHub, and can explain every infrastructure decision in an interview. The full checklist is in PROGRESS.md.
