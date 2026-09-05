# Curriculum

Eighteen phases take you from "what is AI?" to operating a GPU-backed AI platform on Kubernetes. Work through them in order: each phase assumes the previous ones.

## The progression

```text
AI
 ↓
Machine Learning
 ↓
Deep Learning
 ↓
Neural Networks
 ↓
Transformers
 ↓
Foundation Models
 ↓
LLMs
 ↓
LLM Applications
 ↓
RAG
 ↓
Agents
```

Concepts are always taught in this order. You will never be asked to deploy vLLM on Kubernetes before you know what a model is.

## Phases

| Phase | Subject | What you can do afterwards |
|---|---|---|
| [00](./00-orientation/) | Orientation | Explain what AI is, run a model on your laptop, have a working environment |
| [01](./01-python/) | Python for AI/DevOps | Build and containerise a FastAPI service that talks to the Kubernetes API |
| [02](./02-ai-fundamentals/) | AI Fundamentals | Explain models, parameters, training, inference, tokens, embeddings, context windows |
| [03](./03-math-for-ai/) | Math for AI | Understand why matrix multiplication needs GPUs and what a gradient is |
| [04](./04-machine-learning/) | Machine Learning | Train, evaluate, version and serve a classical ML model |
| [05](./05-deep-learning/) | Deep Learning | Train a neural network in PyTorch and understand CPU vs GPU trade-offs |
| [06](./06-transformers/) | Transformers | Explain attention, and estimate a model's inference memory and latency |
| [07](./07-llm-engineering/) | LLM Engineering | Build a production LLM API with streaming, structured outputs and tool calling |
| [08](./08-rag/) | RAG | Build and evaluate a retrieval-augmented assistant on pgvector |
| [09](./09-ai-agents/) | AI Agents | Build a guarded, read-only DevOps investigation agent |
| [10](./10-mlops/) | MLOps | Run a reproducible ML pipeline with MLflow tracking, registry and rollback |
| [11](./11-llmops/) | LLMOps | Version prompts, evaluate against golden datasets, trace and account for tokens |
| [12](./12-ai-observability/) | AI Observability | Instrument an AI service with Prometheus, Grafana and OpenTelemetry |
| [13](./13-gpu-infrastructure/) | GPU Infrastructure | Size GPUs, read utilisation, diagnose GPU OOM |
| [14](./14-ai-kubernetes/) | AI + Kubernetes | Schedule, serve and autoscale GPU inference on Kubernetes with vLLM |
| [15](./15-ai-security/) | AI Security | Threat-model and harden an AI system against prompt injection and tool abuse |
| [16](./16-ai-cost-engineering/) | AI Cost Engineering | Measure cost per token and reduce inference cost |
| [17](./17-capstone-ai-sre/) | AI-SRE Capstone | Design and build an incident-investigation and remediation platform |

## How every phase is structured

```text
Phase Overview → Learning Objectives → Prerequisites → Concept Lessons → Architecture
→ Hands-on Labs → Exercises → Troubleshooting → Mini Project → Assessment
→ Interview Questions → Phase Project → Checkpoint
```

You never finish a phase without producing something tangible.

## How every lesson is structured

Title · Learning objectives · Prerequisites · Concept explanation · **DevOps perspective** (why a DevOps engineer needs this, in every lesson) · Architecture · Hands-on lab · Expected result · Troubleshooting · Exercise · Quiz · Interview questions · Checkpoint.

## Lab difficulty

| Level | Scope | Examples |
|---|---|---|
| 🟢 Beginner | Single machine | Python scripts, API calls, simple model inference |
| 🟡 Intermediate | Multi-component systems | Docker, Kubernetes, RAG, ML pipelines |
| 🟠 Advanced | Production-style infrastructure | GPU serving, Kubernetes inference, autoscaling, observability |
| 🔴 Expert | Architecture and operations | AI platform, distributed inference, incident response, security, cost |

## Assessment in every phase

- **Knowledge check** — 5–15 questions.
- **Practical assessment** — a hands-on task without step-by-step instructions.
- **Troubleshooting assessment** — a deliberately broken system to diagnose.
- **Architecture assessment** — design a system.
- **Interview assessment** — realistic questions.

Start with [Phase 00 — Orientation](./00-orientation/).
