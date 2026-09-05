# Progress

Two things are tracked here: how much of the curriculum has been **authored**, and a **learner checklist** you can copy into your own fork.

Status legend: ✅ available · 🚧 in progress · 📋 planned.

## Authoring status

| Phase | Subject | Lessons | Labs | Project | Status |
|---|---|---|---|---|---|
| 00 | Orientation | 4 / 4 | 4 / 4 | — | ✅ |
| 01 | Python for AI/DevOps | 0 / 7 | 0 / 3 | P1 Kubernetes Health API | 📋 |
| 02 | AI Fundamentals | 0 / 6 | 0 / 2 | Model resource estimator | 📋 |
| 03 | Math for AI | 0 / 5 | 0 / 2 | Matmul benchmark | 📋 |
| 04 | Machine Learning | 0 / 8 | 0 / 3 | Pod-failure predictor API | 📋 |
| 05 | Deep Learning | 0 / 6 | 0 / 3 | Training job on Kubernetes | 📋 |
| 06 | Transformers | 0 / 6 | 0 / 3 | Inference cost calculator | 📋 |
| 07 | LLM Engineering | 0 / 7 | 0 / 3 | P3 Production LLM API | 📋 |
| 08 | RAG | 0 / 6 | 0 / 3 | P4 DevOps Knowledge Assistant | 📋 |
| 09 | AI Agents | 0 / 6 | 0 / 3 | P5 DevOps AI Agent | 📋 |
| 10 | MLOps | 0 / 8 | 0 / 3 | P2 Production ML Pipeline | 📋 |
| 11 | LLMOps | 0 / 7 | 0 / 3 | P6 LLMOps Platform | 📋 |
| 12 | AI Observability | 0 / 6 | 0 / 3 | Observable AI service | 📋 |
| 13 | GPU Infrastructure | 0 / 6 | 0 / 3 | GPU sizing guide | 📋 |
| 14 | AI + Kubernetes | 0 / 7 | 0 / 4 | P7 GPU Inference Platform | 📋 |
| 15 | AI Security | 0 / 6 | 0 / 2 | Threat model + hardening | 📋 |
| 16 | AI Cost Engineering | 0 / 6 | 0 / 2 | Cost dashboard + report | 📋 |
| 17 | AI-SRE Capstone | 0 / 5 | 0 / 2 | P8 AI-SRE Platform | 📋 |

### Changelog

- **2026-09-06** — Phase 00 complete. Day 1 deepened (mental models, three deployment modes, misconceptions, real-world scenario, life of a request and of a model). Day 2 *Set Up Your Environment* with Lab 0.2 (verification script, containerised model, measured image and startup anatomy). Day 3 *The AI Production Stack* with Lab 0.3 (Kubernetes Job with calculated limits, deliberate `OOMKilled`, diagnosis). Day 4 *How to Work Through This Course* with Lab 0.4 (learning journal, portfolio repository, interview stories) and the project documentation templates under `examples/templates/`. All lab outputs in the lessons are from real runs.
- **2026-09-05** — Repository bootstrapped: README, roadmap, progress, design specification, VitePress site, 18 phase overviews, Day 1 lesson *What Is AI?* with Lab 0.1 *Run Your First Model* (CPU-only).

## Learner checklist

Copy this into your fork and tick items as you complete them. You are "done" when every box is ticked and every project is on your GitHub.

### Knowledge

- [ ] Strong AI fundamentals (AI / ML / DL / GenAI / LLMs, training vs inference, tokens, embeddings, context windows)
- [ ] Practical ML understanding (lifecycle, metrics, overfitting, versioning, deployment)
- [ ] Deep learning fundamentals (neural networks, PyTorch, CPU vs GPU, CUDA basics)
- [ ] Transformer understanding (tokenisation, attention, blocks, and their compute/memory cost)
- [ ] AI security knowledge (prompt injection, leakage, poisoning, tool abuse, agent privilege escalation)
- [ ] AI cost optimisation knowledge (cost per token, utilisation, batching, caching, quantisation)

### Experience

- [ ] LLM engineering experience (prompting, sampling, streaming, structured outputs, tool calling)
- [ ] MLOps experience (MLflow tracking, registry, pipelines, rollback, drift)
- [ ] LLMOps experience (prompt versioning, evaluation, golden datasets, tracing, routing)
- [ ] AI observability experience (Prometheus, Grafana, OpenTelemetry, AI-specific signals, SLOs)
- [ ] GPU infrastructure experience (drivers, CUDA, utilisation, OOM, sizing)
- [ ] Kubernetes AI experience (GPU nodes, device plugins, GPU Operator, vLLM, autoscaling)

### Portfolio

- [ ] Project 1 — Kubernetes Health API
- [ ] Project 2 — Production ML Pipeline
- [ ] Project 3 — Production LLM API
- [ ] Project 4 — DevOps Knowledge Assistant (RAG)
- [ ] Project 5 — DevOps AI Agent
- [ ] Project 6 — LLMOps Platform
- [ ] Project 7 — GPU Inference Platform
- [ ] Project 8 — AI-SRE Platform (capstone)
- [ ] Interview preparation completed for every phase
