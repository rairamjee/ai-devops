# Interview Prep

Every lesson ends with realistic interview questions. This page collects the themes, so you can see the shape of an "AI infrastructure" interview before you get there, and links to lessons that answer them as they are published.

The roles this course prepares you for: DevOps Engineer (AI/ML), MLOps Engineer, LLMOps Engineer, AI Platform Engineer, ML Platform Engineer, AI Infrastructure Engineer, Cloud AI Infrastructure Engineer, AI SRE, Platform Engineer (AI).

## How to answer

Interviewers for these roles rarely want a definition. They want to hear you connect a concept to **architecture, deployment, reliability, scalability, observability, security, performance, cost and troubleshooting**. A strong answer usually has three parts: what it is, why it matters operationally, and a concrete example from a project you built.

## Fundamentals

- What is AI? What is machine learning? How do they relate? → [Day 1 — What Is AI?](/curriculum/00-orientation/01-what-is-ai#interview-questions)
- What is the difference between training and inference, and which one do you run in production? → [Day 1](/curriculum/00-orientation/01-what-is-ai#interview-questions)
- What is a model, physically? What does it consist of? → [Day 1](/curriculum/00-orientation/01-what-is-ai#interview-questions)
- What is a token? What is an embedding? What is a context window? *(Phase 02)*

## Infrastructure

- Why are GPUs used for AI? What does a GPU do better than a CPU? *(Phases 03, 13)*
- Why does GPU memory matter so much? How do you estimate the memory a model needs? → [Day 1](/curriculum/00-orientation/01-what-is-ai#interview-questions), then Phases 06 and 13
- How do you serve a model? What does an inference server do? *(Phases 06, 07, 14)*
- What is batching and why does it improve GPU utilisation? *(Phases 13, 14, 16)*

## Kubernetes

- How do you schedule GPU workloads on Kubernetes? What are device plugins, taints, tolerations and node affinity for? *(Phase 14)*
- How do you autoscale inference? What signal do you scale on? *(Phase 14)*
- Where do model weights live and how do you avoid downloading them on every pod start? *(Phase 14)*

## RAG

- Why can retrieval fail even when the answer is in the documents? *(Phase 08)*
- How do you evaluate a RAG system? *(Phases 08, 11)*
- Why PostgreSQL + pgvector rather than a dedicated vector database? When would you switch? *(Phase 08)*

## Agents

- How do you secure tool execution for an AI agent? *(Phases 09, 15)*
- What is human-in-the-loop and where do you put the approval gate? *(Phase 09)*
- How would you audit what an agent did during an incident? *(Phases 09, 17)*

## Operations

- How do you troubleshoot high inference latency? *(Phases 12, 13, 14)*
- What do you monitor for an LLM service that you would not monitor for a normal web service? *(Phase 12)*
- How do you roll back a model? A prompt? *(Phases 10, 11)*
- What is drift and how do you detect it? *(Phase 10)*

## Cost

- How do you reduce inference cost? *(Phase 16)*
- What is cost per token and how do you measure it? *(Phases 11, 16)*
- When would you quantise a model, and what do you trade away? *(Phases 13, 16)*

## Architecture

- Design an AI platform for production. *(Phases 14, 17)*
- Design a system that answers questions about internal runbooks. *(Phase 08)*
- Design an incident-investigation assistant with safe remediation. *(Phase 17)*
- What happens at 10× traffic? What happens when the GPU node dies? *(every phase)*

## Presenting your projects

For each of the eight [projects](/projects/), prepare a two-minute walkthrough: architecture, SLOs, scaling story, failure modes, security controls, cost, and what you would change with more time.
