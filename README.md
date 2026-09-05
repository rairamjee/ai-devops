# AI for DevOps

> **DevOps first. AI second. Production always.**

A self-paced, production-oriented curriculum that takes a DevOps engineer with **zero AI knowledge** to an engineer who can design, deploy, operate, secure, scale, troubleshoot and cost-optimize AI systems in production.

```text
DevOps Engineer
      ↓
DevOps + AI Fundamentals
      ↓
MLOps / LLMOps
      ↓
AI Infrastructure Engineer
      ↓
AI Platform Engineer
```

This is **not** a data-science degree. You will not be asked to prove theorems or win Kaggle competitions. Every topic in this repository exists to answer one question:

> **How does a DevOps Engineer deploy, operate, secure, monitor, scale, troubleshoot, and optimize AI systems in production?**

---

## Who this is for

- DevOps, platform, cloud and SRE engineers who know some or all of Linux, Git, networking, Docker, Kubernetes and CI/CD.
- Roughly **0% formal AI knowledge**. No ML, statistics, neural networks, transformers, LLMs, embeddings, vector databases, RAG, agents or GPU experience is assumed. Everything is explained from first principles.
- People who want a strong GitHub portfolio and a path into roles such as MLOps Engineer, LLMOps Engineer, AI Platform Engineer, AI Infrastructure Engineer or AI SRE.

## How the course works

Target learning ratio: **30% theory · 20% documentation and reading · 50% hands-on**.

Every phase follows the same structure: overview → objectives → prerequisites → concept lessons → architecture → labs → exercises → troubleshooting → mini project → assessment → interview questions → phase project → checkpoint. You never finish a phase without producing something tangible.

Every concept is taught by asking four questions:

1. **What is it?**
2. **Why does it matter?**
3. **How do I operate it?**
4. **What happens when it breaks?**

Labs are marked by difficulty: 🟢 Beginner (single machine) · 🟡 Intermediate (multi-component) · 🟠 Advanced (production-style infrastructure) · 🔴 Expert (architecture and operations). Labs that need paid cloud resources say so up front, state the cost drivers, and always include a cleanup section. Agent labs start read-only and gate every destructive action behind policy, validation and human approval.

## Curriculum

| Phase | Subject | Docs |
|---|---|---|
| 00 | Orientation | [docs/curriculum/00-orientation](docs/curriculum/00-orientation/index.md) |
| 01 | Python for AI/DevOps | [docs/curriculum/01-python](docs/curriculum/01-python/index.md) |
| 02 | AI Fundamentals | [docs/curriculum/02-ai-fundamentals](docs/curriculum/02-ai-fundamentals/index.md) |
| 03 | Math for AI | [docs/curriculum/03-math-for-ai](docs/curriculum/03-math-for-ai/index.md) |
| 04 | Machine Learning | [docs/curriculum/04-machine-learning](docs/curriculum/04-machine-learning/index.md) |
| 05 | Deep Learning | [docs/curriculum/05-deep-learning](docs/curriculum/05-deep-learning/index.md) |
| 06 | Transformers | [docs/curriculum/06-transformers](docs/curriculum/06-transformers/index.md) |
| 07 | LLM Engineering | [docs/curriculum/07-llm-engineering](docs/curriculum/07-llm-engineering/index.md) |
| 08 | RAG | [docs/curriculum/08-rag](docs/curriculum/08-rag/index.md) |
| 09 | AI Agents | [docs/curriculum/09-ai-agents](docs/curriculum/09-ai-agents/index.md) |
| 10 | MLOps | [docs/curriculum/10-mlops](docs/curriculum/10-mlops/index.md) |
| 11 | LLMOps | [docs/curriculum/11-llmops](docs/curriculum/11-llmops/index.md) |
| 12 | AI Observability | [docs/curriculum/12-ai-observability](docs/curriculum/12-ai-observability/index.md) |
| 13 | GPU Infrastructure | [docs/curriculum/13-gpu-infrastructure](docs/curriculum/13-gpu-infrastructure/index.md) |
| 14 | AI + Kubernetes | [docs/curriculum/14-ai-kubernetes](docs/curriculum/14-ai-kubernetes/index.md) |
| 15 | AI Security | [docs/curriculum/15-ai-security](docs/curriculum/15-ai-security/index.md) |
| 16 | AI Cost Engineering | [docs/curriculum/16-ai-cost-engineering](docs/curriculum/16-ai-cost-engineering/index.md) |
| 17 | AI-SRE Capstone | [docs/curriculum/17-capstone-ai-sre](docs/curriculum/17-capstone-ai-sre/index.md) |

Start here: **[Day 1 — What Is AI?](docs/curriculum/00-orientation/01-what-is-ai.md)**

## Projects

Projects become progressively more realistic and each one ships with real engineering documentation (README, ARCHITECTURE, SETUP, OPERATIONS, TROUBLESHOOTING, SECURITY, COST).

| # | Project | Core skills |
|---|---|---|
| 1 | Kubernetes Health API | Python, FastAPI, Kubernetes API, Docker |
| 2 | Production ML Pipeline | Training, evaluation, MLflow, Docker, Kubernetes |
| 3 | Production LLM API | LLM APIs, FastAPI, streaming, Docker, Kubernetes, observability |
| 4 | DevOps Knowledge Assistant | Embeddings, pgvector, RAG, LLM |
| 5 | DevOps AI Agent | Tool calling, Kubernetes, logs, metrics, RAG, guardrails |
| 6 | LLMOps Platform | Model gateway, prompt management, evaluation, tracing, cost |
| 7 | GPU Inference Platform | Kubernetes, GPU, CUDA, NVIDIA, vLLM, autoscaling |
| 8 | AI-SRE Platform (capstone) | Everything above |

See [docs/projects](docs/projects/index.md) for details.

## Technology stack

One primary stack, introduced only when there is a reason for it:

```text
Linux · Git · Python · Bash · Docker · Kubernetes · Terraform · AWS
PostgreSQL + pgvector · Prometheus · Grafana · OpenTelemetry
PyTorch · Hugging Face · MLflow · vLLM · NVIDIA / CUDA
```

Principles before products: you learn what an inference server *does* before you learn vLLM, so you can evaluate alternatives yourself.

## Running the docs site locally

The curriculum is published as a [VitePress](https://vitepress.dev/) site.

```bash
npm install
npm run docs:dev      # http://localhost:5173
npm run docs:build    # static build in docs/.vitepress/dist
```

## Repository layout

```text
ai-devops/
├── README.md
├── ROADMAP.md                      # phase-by-phase plan
├── PROGRESS.md                     # authoring status + learner checklist
├── COURSE-DESIGN-SPECIFICATION.md  # single source of truth for course design
├── CONTRIBUTING.md                 # how to add lessons, labs and projects
├── package.json
├── docs/                           # VitePress site
│   ├── index.md
│   ├── roadmap.md · progress.md · resources.md
│   ├── .vitepress/config.mts
│   ├── curriculum/00-orientation … 17-capstone-ai-sre
│   ├── labs/
│   ├── projects/
│   └── interview-prep/
└── examples/                       # runnable code referenced by lessons and labs
    ├── python/ · docker/ · kubernetes/ · terraform/
    └── ml/ · llm/ · rag/ · agents/ · observability/
```

## Status

Authoring progress and the learner checklist live in [PROGRESS.md](PROGRESS.md). The phase-by-phase plan is in [ROADMAP.md](ROADMAP.md).

## Design specification

Everything in this repository is derived from [COURSE-DESIGN-SPECIFICATION.md](COURSE-DESIGN-SPECIFICATION.md). Read it before adding content, and see [CONTRIBUTING.md](CONTRIBUTING.md) for the lesson, lab and project standards.

The north star: a learner who finishes this course can hear *"we need to put this AI workload into production"* and answer:

> "Let's design the architecture, define the SLOs, choose the compute, package the workload, deploy it, secure it, instrument it, establish autoscaling, control the cost, test failure modes, and build the operational runbooks."
