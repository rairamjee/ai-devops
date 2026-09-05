# AI for DevOps — Course Design Specification

## 1. Purpose

This document is the **single source of truth** for designing and expanding the `AI for DevOps` learning repository.

The goal is to build a complete, self-paced, production-oriented curriculum that takes a learner from:

> **0% AI knowledge → AI-capable DevOps Engineer → MLOps/LLMOps Engineer → AI Infrastructure / AI Platform Engineer**

The learner is **not training to become a Data Scientist or AI Researcher**.

The course must continuously answer:

> **How does a DevOps Engineer deploy, operate, secure, monitor, scale, troubleshoot, and optimize AI systems in production?**

---

# 2. Target Learner

Assume the learner:

- Is a DevOps Engineer or aspiring DevOps Engineer.
- Understands some or all of Linux, Git, networking, cloud, Docker, Kubernetes, CI/CD and infrastructure concepts.
- Has approximately **0% formal AI knowledge**.
- Does not know AI terminology.
- May be unfamiliar with Python beyond basic scripting.
- Wants practical production skills rather than academic specialization.
- Wants to build a strong GitHub portfolio.
- Wants to become employable in AI infrastructure, MLOps, LLMOps, or AI platform engineering.

Do **not** assume prior knowledge of:

- Machine learning
- Statistics
- Neural networks
- Transformers
- LLMs
- Embeddings
- Vector databases
- RAG
- AI agents
- GPU infrastructure

Explain those from first principles.

---

# 3. Primary Career Outcome

The curriculum should develop the following profile:

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

The learner should eventually be able to:

1. Understand modern AI systems.
2. Build simple AI applications.
3. Containerize AI applications.
4. Deploy AI workloads to Kubernetes.
5. Operate model-serving infrastructure.
6. Understand GPU infrastructure.
7. Build ML pipelines.
8. Build LLM applications.
9. Build RAG systems.
10. Build controlled AI agents.
11. Implement AI observability.
12. Secure AI workloads.
13. Optimize AI infrastructure cost.
14. Troubleshoot AI production incidents.
15. Design an AI platform.
16. Explain AI infrastructure decisions in interviews.

---

# 4. What the Course Is NOT

Do not turn this into a Data Science degree.

Avoid unnecessary emphasis on:

- Advanced mathematical proofs
- Academic ML theory
- Statistical proofs
- Research-level neural network design
- Implementing every ML algorithm from scratch
- Kaggle competitions
- Research paper reproduction unless directly useful
- Deep specialization in computer vision
- Deep specialization in reinforcement learning

Mathematics should be taught **only to the level required to understand AI systems and make engineering decisions**.

The course should prioritize:

```text
Understand
    ↓
Operate
    ↓
Deploy
    ↓
Troubleshoot
    ↓
Optimize
    ↓
Design
```

---

# 5. Core Learning Philosophy

## 5.1 Production first

Every major AI concept should eventually connect to production.

For example:

### Do not teach only:

> What is a Transformer?

Also teach:

- Why does it require compute?
- Why does inference require memory?
- What affects latency?
- What affects throughput?
- Why are GPUs useful?
- How would you serve it?
- How would you monitor it?
- How would you scale it?
- What can go wrong?

---

## 5.2 Learn by building

Target learning ratio:

```text
30% Theory
20% Documentation / Reading
50% Hands-on
```

Every significant phase should contain:

- Explanation
- Example
- Hands-on lab
- Exercise
- Troubleshooting
- Assessment
- Project

---

## 5.3 Explain from zero

Use progressive explanations.

Example:

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

Do not jump directly from "What is AI?" to "Deploy vLLM on Kubernetes."

---

# 6. Curriculum Architecture

The curriculum should contain the following phases.

| Phase | Subject |
|---|---|
| 00 | Orientation |
| 01 | Python for AI/DevOps |
| 02 | AI Fundamentals |
| 03 | Math for AI |
| 04 | Machine Learning |
| 05 | Deep Learning |
| 06 | Transformers |
| 07 | LLM Engineering |
| 08 | RAG |
| 09 | AI Agents |
| 10 | MLOps |
| 11 | LLMOps |
| 12 | AI Observability |
| 13 | GPU Infrastructure |
| 14 | AI + Kubernetes |
| 15 | AI Security |
| 16 | AI Cost Engineering |
| 17 | AI-SRE Capstone |

---

# 7. Phase Design Standard

Every phase should follow this structure:

```text
Phase Overview
    ↓
Learning Objectives
    ↓
Prerequisites
    ↓
Concept Lessons
    ↓
Architecture
    ↓
Hands-on Labs
    ↓
Exercises
    ↓
Troubleshooting
    ↓
Mini Project
    ↓
Assessment
    ↓
Interview Questions
    ↓
Phase Project
    ↓
Checkpoint
```

A learner should never finish a phase without producing something tangible.

---

# 8. Lesson Design Standard

Every lesson should contain:

## 8.1 Title

Example:

> Day 1 — What Is AI?

## 8.2 Learning objectives

Clearly state what the learner will know by the end.

Example:

- Define AI.
- Explain ML.
- Explain deep learning.
- Explain LLMs.
- Explain training vs inference.
- Describe a basic AI production architecture.

## 8.3 Prerequisites

State what the learner should already know.

If none:

> No prerequisites.

## 8.4 Concept explanation

Start simple.

Use:

- Analogies
- Diagrams
- Tables
- Small examples
- Real infrastructure scenarios

## 8.5 DevOps perspective

Every AI lesson should include:

> **Why does a DevOps Engineer need to know this?**

This section is mandatory.

## 8.6 Architecture

Use diagrams whenever architecture is relevant.

Example:

```text
User
 ↓
API Gateway
 ↓
AI Application
 ↓
Inference Server
 ↓
GPU
```

## 8.7 Hands-on lab

Provide exact steps.

## 8.8 Expected result

Show what success looks like.

## 8.9 Troubleshooting

Include likely failures and how to diagnose them.

## 8.10 Exercise

Give the learner something to solve independently.

## 8.11 Quiz

Use 5–15 questions depending on lesson size.

## 8.12 Interview questions

Include realistic DevOps/AI interview questions.

## 8.13 Checkpoint

Explain what the learner must understand before progressing.

---

# 9. Lab Design Standard

Labs are a core component of the course.

A lab must be:

- Practical
- Reproducible
- Incremental
- Production-oriented
- Safe
- Clearly documented

Each lab should contain:

```text
Lab Title
Objective
Difficulty
Estimated Time
Prerequisites
Architecture
Environment Requirements
Setup
Steps
Expected Output
Validation
Troubleshooting
Cleanup
Extension Challenge
Questions
```

---

# 10. Lab Difficulty

Use:

### 🟢 Beginner

Single-machine exercises.

Examples:

- Python scripts
- API calls
- Simple model inference

### 🟡 Intermediate

Multi-component systems.

Examples:

- Docker
- Kubernetes
- RAG
- ML pipelines

### 🟠 Advanced

Production-style infrastructure.

Examples:

- GPU serving
- Kubernetes inference
- autoscaling
- observability

### 🔴 Expert

Architecture and operations.

Examples:

- AI platform
- distributed inference
- incident response
- security
- cost optimization

---

# 11. Lab Safety

AI agents and infrastructure labs must default to safe behavior.

Never require unrestricted production access.

For DevOps agent labs:

```text
AI Agent
   ↓
Tool
   ↓
Policy
   ↓
Validation
   ↓
Human Approval
   ↓
Action
```

Start with read-only tools.

Example:

```text
kubectl get
kubectl describe
kubectl logs
```

Do not begin with unrestricted:

```text
kubectl delete
kubectl exec
terraform apply
```

When destructive actions are eventually introduced, use:

- Explicit approval
- Least privilege
- Sandboxed environments
- Audit logs
- Clear rollback procedures

---

# 12. Hands-on Environment

Prefer tools that learners can run locally where practical.

Suggested progression:

## Local

- Linux/macOS/Windows + WSL
- Python
- Git
- Docker
- Kind or Minikube
- PostgreSQL
- Prometheus
- Grafana

## Cloud

Choose one primary cloud.

Recommended:

> AWS

Then teach Azure/GCP concepts where useful.

## GPU

Use local GPU when available.

Otherwise provide cloud GPU instructions.

Labs should clearly distinguish:

```text
CPU-only path
GPU path
```

when possible.

---

# 13. Technology Strategy

Avoid teaching dozens of tools simultaneously.

Primary stack:

```text
Linux
Git
Python
Bash
Docker
Kubernetes
Terraform
AWS
PostgreSQL
pgvector
Prometheus
Grafana
OpenTelemetry
PyTorch
Hugging Face ecosystem
MLflow
vLLM
NVIDIA/CUDA
```

Additional tools may be introduced when justified.

Every tool must have a reason.

Do not teach a tool merely because it is popular.

---

# 14. AI Fundamentals Scope

Teach:

- AI
- Machine Learning
- Deep Learning
- Generative AI
- Foundation Models
- LLMs
- Training
- Inference
- Models
- Parameters
- Hyperparameters
- Datasets
- Features
- Labels
- Tokens
- Embeddings
- Context windows

The learner should be able to explain these concepts without memorizing definitions.

---

# 15. Math Scope

Teach only practical foundations.

## Linear algebra

- Scalars
- Vectors
- Matrices
- Tensors
- Dot products
- Matrix multiplication

## Statistics

- Mean
- Median
- Variance
- Standard deviation
- Probability
- Distributions
- Correlation

## Optimization

- Derivative
- Gradient
- Loss
- Gradient descent

Do not turn this section into a mathematics course.

---

# 16. Machine Learning Scope

Teach:

- Supervised learning
- Unsupervised learning
- Reinforcement learning concepts
- Regression
- Classification
- Trees
- Random forests
- Clustering
- Feature engineering
- Training
- Validation
- Testing
- Metrics
- Overfitting
- Underfitting
- Model versioning
- Model deployment

Main objective:

> Understand the ML lifecycle from a production engineer's perspective.

---

# 17. Deep Learning Scope

Teach:

- Neural networks
- Neurons
- Layers
- Weights
- Bias
- Activations
- Forward propagation
- Backpropagation
- Loss
- Optimizers
- Epochs
- Batches
- PyTorch
- CPU vs GPU
- CUDA basics
- Mixed precision

CNNs/RNNs/LSTMs should be taught primarily for conceptual understanding.

Transformers receive deeper treatment later.

---

# 18. Transformer Scope

Teach thoroughly:

- Tokenization
- Embeddings
- Attention
- Self-attention
- Query
- Key
- Value
- Multi-head attention
- Positional information
- Encoder
- Decoder
- Transformer blocks

Connect every concept to:

- Compute
- Memory
- Inference
- GPU requirements
- Latency
- Throughput

---

# 19. LLM Engineering Scope

Teach:

- LLM architecture
- Foundation models
- Parameters
- Tokens
- Context windows
- Prompting
- Sampling
- Temperature
- Top-k
- Top-p
- Streaming
- Structured outputs
- Tool calling
- Function calling
- Rate limiting
- Retries
- Model APIs
- Model gateways

Project:

> Production LLM API

---

# 20. RAG Scope

Teach:

```text
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retrieval
 ↓
Context
 ↓
LLM
 ↓
Answer
```

Topics:

- Embeddings
- Vector search
- Similarity
- Chunking
- Metadata
- Retrieval
- Top-k
- Reranking
- Hybrid search
- Evaluation
- Hallucination
- Grounding

Initial vector technology:

> PostgreSQL + pgvector

Other vector databases can be introduced conceptually.

Project:

> DevOps Knowledge Assistant

---

# 21. AI Agent Scope

Teach:

- Tool calling
- Agent loops
- State
- Memory
- Planning
- Tool selection
- Guardrails
- Human-in-the-loop
- Permissions
- Auditability

Build a DevOps investigation agent that can:

- Inspect Kubernetes
- Read logs
- Query metrics
- Search runbooks
- Analyze recent changes
- Generate a diagnosis

Start read-only.

---

# 22. MLOps Scope

Teach the ML lifecycle:

```text
Code
 ↓
Data
 ↓
Training
 ↓
Evaluation
 ↓
Model Registry
 ↓
Deployment
 ↓
Monitoring
 ↓
Retraining
```

Topics:

- Reproducibility
- Experiment tracking
- Model registry
- Model versioning
- Data versioning
- Pipelines
- Deployment
- Rollback
- Drift
- Monitoring

Primary platform:

> MLflow

---

# 23. LLMOps Scope

Teach:

- Prompt versioning
- Evaluation
- Golden datasets
- Regression testing
- Tracing
- Token accounting
- Model routing
- Provider abstraction
- Quality monitoring
- Cost monitoring
- Latency monitoring

The learner should understand that:

> LLM applications require an operational lifecycle just like other production systems.

---

# 24. AI Observability Scope

Traditional:

```text
Metrics
Logs
Traces
```

AI adds:

```text
Tokens
Latency
Throughput
GPU utilization
GPU memory
Model version
Prompt version
Retrieval quality
Generation quality
Cost
```

Use:

- Prometheus
- Grafana
- OpenTelemetry
- Loki where useful

Project:

> Observable AI service

---

# 25. GPU Infrastructure Scope

Teach:

- GPU architecture
- VRAM
- Memory bandwidth
- Tensor cores
- CUDA
- NVIDIA drivers
- GPU scheduling
- GPU utilization
- GPU memory pressure
- GPU OOM
- Model memory requirements

Connect GPU knowledge to:

- Kubernetes
- Containers
- Scheduling
- Autoscaling
- Cost

---

# 26. AI + Kubernetes Scope

Teach:

- GPU nodes
- Device plugins
- NVIDIA GPU Operator
- Node pools
- Taints
- Tolerations
- Node affinity
- Resource requests
- Model-serving deployments
- Autoscaling
- Persistent storage
- Model caching
- Network policies
- GPU monitoring

Architecture:

```text
Kubernetes Cluster
│
├── CPU Nodes
│
└── GPU Nodes
     │
     ├── Model Server
     ├── AI Application
     └── Monitoring
```

---

# 27. Model Serving Scope

Teach:

- Inference servers
- Model loading
- Batching
- Continuous batching
- Streaming
- Throughput
- Latency
- Concurrency
- GPU utilization
- Autoscaling
- Model replicas
- Quantization

Primary serving technology:

> vLLM

Teach alternatives conceptually when useful.

---

# 28. AI Security Scope

Traditional security:

- IAM
- RBAC
- Secrets
- Encryption
- Network policies
- Container security
- Supply-chain security

AI security:

- Prompt injection
- Indirect prompt injection
- Jailbreaking
- Sensitive data leakage
- Data poisoning
- Model theft
- Tool abuse
- Agent privilege escalation

Always connect security to practical infrastructure controls.

---

# 29. AI Cost Engineering Scope

Teach:

```text
AI Cost
├── GPU
├── CPU
├── Storage
├── Network
├── API calls
└── Tokens
```

Topics:

- Cost/request
- Cost/token
- GPU utilization
- Batching
- Caching
- Model selection
- Quantization
- Autoscaling
- Capacity planning

Project:

> AI cost dashboard and optimization report

---

# 30. Project Design Standard

Projects should become progressively more realistic.

## Project 1

### Kubernetes Health API

Skills:

- Python
- FastAPI
- Kubernetes API
- Docker

## Project 2

### Production ML Pipeline

Skills:

- Training
- Evaluation
- MLflow
- Docker
- Kubernetes

## Project 3

### Production LLM API

Skills:

- LLM API
- FastAPI
- Streaming
- Docker
- Kubernetes
- Observability

## Project 4

### DevOps Knowledge Assistant

Skills:

- Embeddings
- pgvector
- RAG
- LLM

## Project 5

### DevOps AI Agent

Skills:

- Tool calling
- Kubernetes
- Logs
- Metrics
- RAG
- Guardrails

## Project 6

### LLMOps Platform

Skills:

- Model gateway
- Prompt management
- Evaluation
- Tracing
- Cost

## Project 7

### GPU Inference Platform

Skills:

- Kubernetes
- GPU
- CUDA
- NVIDIA
- vLLM
- Autoscaling

## Project 8

### AI-SRE Platform

Final capstone.

---

# 31. Final Capstone

The capstone should combine the entire course.

## AI-SRE Platform

Architecture:

```text
                         USER
                           │
                           ▼
                      API Gateway
                           │
                           ▼
                      AI SRE API
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        Kubernetes     Prometheus       Loki
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                       AI Agent
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
            RAG        LLM Gateway      Tools
             │             │             │
             ▼             ▼             ▼
         Vector DB      LLM Server    DevOps APIs
                           │
                           ▼
                          GPU
                           │
                      Kubernetes
```

The system should:

1. Receive an incident question.
2. Inspect infrastructure.
3. Query metrics.
4. Inspect logs.
5. Inspect deployment history.
6. Search runbooks.
7. Generate a root-cause hypothesis.
8. Provide evidence.
9. Recommend remediation.
10. Request approval.
11. Execute approved remediation.
12. Verify recovery.
13. Produce an incident report.

---

# 32. Assessment Model

Each phase should have:

## Knowledge check

5–15 questions.

## Practical assessment

A hands-on task without step-by-step instructions.

## Troubleshooting assessment

Give the learner a broken system.

Ask them to diagnose it.

## Architecture assessment

Ask the learner to design a system.

## Interview assessment

Ask realistic questions.

---

# 33. Troubleshooting Philosophy

Do not only teach successful deployments.

Deliberately introduce failures.

Examples:

- Container crash
- Image pull failure
- Kubernetes scheduling failure
- GPU unavailable
- GPU OOM
- Model loading failure
- API timeout
- Rate limit
- Vector retrieval failure
- Bad prompt
- Hallucination
- Agent tool failure
- High inference latency
- High token usage
- High GPU cost

Every advanced lab should have at least one failure scenario.

---

# 34. Production Engineering Concepts

Throughout the curriculum, continuously reinforce:

- Availability
- Reliability
- Scalability
- Performance
- Security
- Cost
- Disaster recovery
- Backups
- Rollback
- Versioning
- SLOs
- SLIs
- Error budgets
- Incident response
- Capacity planning
- Change management

The learner should think:

> "What happens at 10× traffic?"

and:

> "What happens when this component fails?"

---

# 35. Documentation Standard

Every project should contain:

```text
README.md
ARCHITECTURE.md
SETUP.md
OPERATIONS.md
TROUBLESHOOTING.md
SECURITY.md
COST.md
```

Where applicable also include:

```text
DISASTER-RECOVERY.md
RUNBOOK.md
SLO.md
THREAT-MODEL.md
```

This teaches real engineering documentation.

---

# 36. Repository Structure

Recommended VitePress structure:

```text
ai-devops/
│
├── README.md
├── package.json
├── ROADMAP.md
├── PROGRESS.md
│
├── docs/
│   ├── index.md
│   ├── roadmap.md
│   ├── progress.md
│   ├── resources.md
│   ├── projects.md
│   ├── interview-prep.md
│   │
│   ├── .vitepress/
│   │   └── config.mts
│   │
│   ├── curriculum/
│   │   ├── 00-orientation/
│   │   ├── 01-python/
│   │   ├── 02-ai-fundamentals/
│   │   ├── 03-math-for-ai/
│   │   ├── 04-machine-learning/
│   │   ├── 05-deep-learning/
│   │   ├── 06-transformers/
│   │   ├── 07-llm-engineering/
│   │   ├── 08-rag/
│   │   ├── 09-ai-agents/
│   │   ├── 10-mlops/
│   │   ├── 11-llmops/
│   │   ├── 12-ai-observability/
│   │   ├── 13-gpu-infrastructure/
│   │   ├── 14-ai-kubernetes/
│   │   ├── 15-ai-security/
│   │   ├── 16-ai-cost-engineering/
│   │   └── 17-capstone-ai-sre/
│   │
│   ├── labs/
│   ├── projects/
│   └── interview-prep/
│
└── examples/
    ├── python/
    ├── docker/
    ├── kubernetes/
    ├── terraform/
    ├── ml/
    ├── llm/
    ├── rag/
    ├── agents/
    └── observability/
```

---

# 37. VitePress Design

The site should be easy to navigate.

Recommended navigation:

```text
Home
Roadmap
Progress
Curriculum
Labs
Projects
Interview Prep
Resources
```

The sidebar should follow the learner's progression.

Use consistent page names:

```text
day-01.md
day-02.md
day-03.md
```

or:

```text
01-what-is-ai.md
02-ai-vs-automation.md
```

Avoid inconsistent naming.

---

# 38. Code Quality Standard

All code examples should:

- Be runnable.
- Include required dependencies.
- Use reasonable project structure.
- Include comments where useful.
- Avoid unexplained magic.
- Prefer secure defaults.
- Avoid hard-coded credentials.
- Use environment variables for secrets.
- Include validation where relevant.

Never place real credentials in examples.

Use:

```text
.env.example
```

when environment variables are required.

---

# 39. Cloud Cost Awareness

Labs that require paid cloud infrastructure must clearly state:

- Whether cloud resources are required.
- Approximate resource type.
- Potential cost drivers.
- How to shut them down.
- Whether a local alternative exists.

Always provide a cleanup section.

Example:

```bash
terraform destroy
```

or appropriate provider-specific cleanup.

---

# 40. Resource Selection

Prefer:

1. Official documentation
2. Official tutorials
3. Primary technical sources
4. Well-maintained open-source documentation
5. High-quality educational material

Avoid building the course around random blog posts.

AI tools and APIs change quickly.

For fast-changing technologies, verify current documentation before publishing implementation instructions.

---

# 41. AI Tool Selection Philosophy

The course should teach principles before products.

Example:

Do not teach only:

> "Use Tool X."

Teach:

> "Here is what an inference server does."

Then demonstrate Tool X.

The learner should understand the underlying concept well enough to evaluate alternatives.

---

# 42. Interview Preparation

Each major phase should produce interview questions.

Questions should cover:

### Fundamentals

- What is AI?
- What is ML?
- What is inference?

### Infrastructure

- Why GPUs?
- Why GPU memory matters?
- How do you serve a model?

### Kubernetes

- How do you schedule GPU workloads?
- How do you autoscale inference?

### RAG

- Why can retrieval fail?
- How do you evaluate RAG?

### Agents

- How do you secure tool execution?

### Operations

- How do you troubleshoot high inference latency?

### Cost

- How do you reduce inference cost?

### Architecture

- Design an AI platform for production.

---

# 43. Career Alignment

The curriculum should prepare for roles such as:

- DevOps Engineer — AI/ML
- MLOps Engineer
- LLMOps Engineer
- AI Platform Engineer
- ML Platform Engineer
- AI Infrastructure Engineer
- Cloud AI Infrastructure Engineer
- AI SRE
- Platform Engineer — AI

Do not market the learner as a Data Scientist unless they independently pursue that specialization.

---

# 44. Completion Standard

The learner should be considered advanced only when they can independently:

```text
Design
   ↓
Build
   ↓
Containerize
   ↓
Deploy
   ↓
Observe
   ↓
Secure
   ↓
Scale
   ↓
Troubleshoot
   ↓
Optimize
```

an AI workload.

---

# 45. Definition of Done for the Course

At completion, the learner should have:

- [ ] Strong AI fundamentals
- [ ] Practical ML understanding
- [ ] Deep learning fundamentals
- [ ] Transformer understanding
- [ ] LLM engineering experience
- [ ] RAG project
- [ ] AI agent project
- [ ] MLOps experience
- [ ] LLMOps experience
- [ ] AI observability experience
- [ ] GPU infrastructure experience
- [ ] Kubernetes AI experience
- [ ] AI security knowledge
- [ ] AI cost optimization knowledge
- [ ] Multiple GitHub projects
- [ ] Final AI-SRE platform
- [ ] Interview preparation

---

# 46. The Most Important Teaching Rule

Every time a concept is introduced, ask four questions:

### 1. What is it?

Explain the concept.

### 2. Why does it matter?

Explain the engineering reason.

### 3. How do I operate it?

Give hands-on experience.

### 4. What happens when it breaks?

Give troubleshooting experience.

This transforms the curriculum from an AI tutorial into a **production engineering program**.

---

# 47. Master Mental Model

The entire curriculum should eventually converge on this architecture:

```text
                         USERS
                           │
                           ▼
                    API / GATEWAY
                           │
                           ▼
                    AI APPLICATION
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
            RAG          AGENTS        TOOLS
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                    MODEL / LLM
                           │
                           ▼
                   INFERENCE SERVER
                           │
                           ▼
                    CPU / GPU LAYER
                           │
                           ▼
                      KUBERNETES
                           │
            ┌──────────────┼──────────────┐
            │              │              │
          NETWORK        STORAGE       COMPUTE
            │              │              │
            └──────────────┼──────────────┘
                           │
                    OBSERVABILITY
                           │
                 ┌─────────┼─────────┐
                 │         │         │
               Metrics    Logs     Traces
                           │
                     SECURITY
                           │
                       CI/CD
                           │
                        IaC
                           │
                        COST
```

The learner's final goal is to understand and operate this entire system.

---

# 48. Course Authoring Rule

When expanding this repository, do **not** generate hundreds of shallow pages just to make the repository look complete.

Prefer:

> **Fewer, deeper, runnable lessons.**

A lesson is valuable if the learner can:

- Understand something new.
- Run something.
- Break something.
- Fix something.
- Explain what happened.
- Apply it to production.

---

# 49. Final Instruction for Future Course Expansion

Whenever adding new content to this repository, preserve these principles:

> **DevOps first. AI second. Production always.**

The learner is becoming an engineer who can operate AI systems.

Do not lose the DevOps foundation while adding AI topics.

Every new AI technology should be evaluated through:

```text
Architecture
Deployment
Reliability
Scalability
Observability
Security
Performance
Cost
Troubleshooting
```

If a topic does not contribute meaningfully to those areas, keep it conceptual or omit it.

---

# 50. North Star

The final learner should be able to walk into a company and hear:

> "We need to put this AI workload into production."

and respond:

> "Let's design the architecture, define the SLOs, choose the compute, package the workload, deploy it, secure it, instrument it, establish autoscaling, control the cost, test failure modes, and build the operational runbooks."

That is the **AI for DevOps** skillset this repository is designed to create.
