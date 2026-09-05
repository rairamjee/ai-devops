---
layout: home

hero:
  name: AI for DevOps
  text: From zero AI knowledge to AI Platform Engineer.
  tagline: DevOps first. AI second. Production always.
  actions:
    - theme: brand
      text: Start Day 1
      link: /curriculum/00-orientation/01-what-is-ai
    - theme: alt
      text: View the roadmap
      link: /roadmap
    - theme: alt
      text: Browse the curriculum
      link: /curriculum/

features:
  - icon: 🏭
    title: Production first
    details: Every concept connects to compute, memory, latency, throughput, scaling, monitoring and failure modes. You learn what a transformer is and how to serve, observe and scale it.
  - icon: 🛠️
    title: Learn by building
    details: 30% theory, 20% reading, 50% hands-on. Every phase ends with something tangible. Eight portfolio projects culminate in an AI-SRE platform.
  - icon: 🧭
    title: Explain from zero
    details: AI → ML → Deep Learning → Transformers → LLMs → RAG → Agents. No prior AI, statistics or Python-beyond-scripting knowledge assumed.
  - icon: 💥
    title: Break it on purpose
    details: Container crashes, GPU OOM, model-loading failures, rate limits, retrieval failures, hallucinations. Every advanced lab includes a failure scenario.
  - icon: 🔒
    title: Safe by default
    details: Agent labs start read-only. Destructive actions sit behind policy, validation, human approval, audit logs and rollback.
  - icon: 💼
    title: Interview ready
    details: Every phase produces realistic interview questions, from "what is inference?" to "design an AI platform for production".
---

## The path

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

The course is for DevOps, platform, cloud and SRE engineers. It is **not** a data-science degree. The question it keeps answering:

> **How does a DevOps Engineer deploy, operate, secure, monitor, scale, troubleshoot, and optimize AI systems in production?**

## Four questions for every concept

1. **What is it?**
2. **Why does it matter?**
3. **How do I operate it?**
4. **What happens when it breaks?**

## Where everything converges

```text
                         USERS
                           │
                    API / GATEWAY
                           │
                    AI APPLICATION
             ┌─────────────┼─────────────┐
            RAG          AGENTS        TOOLS
             └─────────────┼─────────────┘
                    MODEL / LLM
                           │
                   INFERENCE SERVER
                           │
                    CPU / GPU LAYER
                           │
                      KUBERNETES
            ┌──────────────┼──────────────┐
          NETWORK        STORAGE       COMPUTE
            └──────────────┼──────────────┘
                    OBSERVABILITY  (metrics · logs · traces)
                           │
                     SECURITY → CI/CD → IaC → COST
```

Your goal by the end of the course is to understand and operate this entire system.
