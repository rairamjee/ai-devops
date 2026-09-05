# Phase 15 — AI Security

> The controls you already know, applied to AI workloads, plus the new attack surface: prompt injection, jailbreaks, data leakage, poisoning, model theft, tool abuse and agent privilege escalation.

**Status:** 📋 planned · **Estimated effort:** 1 week · **Prerequisites:** Phases 00–14.

## Overview

Half of AI security is traditional security done properly: IAM, RBAC, secrets, encryption, network policies, container and supply-chain security. The other half is new: an attacker can now reach your systems through natural language in a document your RAG assistant indexed, or through a tool your agent is allowed to call. Every AI risk is mapped to a concrete infrastructure control.

## Why a DevOps engineer needs this

You own the blast radius. A prompt injection is only dangerous if the agent it hijacks has the permissions to do damage, and permissions are yours.

## Learning objectives

- Apply IAM, RBAC, secrets management, encryption, network policies, container and supply-chain controls to AI workloads.
- Explain and demonstrate prompt injection and indirect prompt injection; apply mitigations.
- Explain jailbreaking and sensitive-data leakage; apply output controls and data-handling rules.
- Explain data poisoning and model theft and the controls that reduce them.
- Explain tool abuse and agent privilege escalation; design least-privilege tool execution.
- Threat-model an AI system and write a `THREAT-MODEL.md`.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Traditional controls for AI workloads: IAM, RBAC, secrets, encryption, network, containers, supply chain | 📋 |
| 02 | Prompt injection and indirect prompt injection | 📋 |
| 03 | Jailbreaking and sensitive-data leakage | 📋 |
| 04 | Data poisoning and model theft | 📋 |
| 05 | Tool abuse and agent privilege escalation | 📋 |
| 06 | Threat-modelling an AI system | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 15.1 — Plant an indirect prompt injection in a runbook indexed by Project 4; observe it; add mitigations and re-test | 🟠 | Local, Docker | 📋 |
| 15.2 — Attempt tool abuse against Project 5; confirm the policy and approval gates block it; tighten RBAC and audit | 🟠 | Local, kind | 📋 |

## Mini project — Threat model and hardening

A `THREAT-MODEL.md` and `SECURITY.md` for Project 4 or 5, plus the implemented hardening: secrets out of code, network policies, least-privilege ServiceAccounts, input and output controls, audit logging.

## Assessment

- **Knowledge check:** 12 questions.
- **Practical:** add an allow-list for tool arguments and prove it blocks a crafted input.
- **Troubleshooting:** the assistant leaked an internal hostname; trace how it got into the context.
- **Architecture:** design the trust boundaries for an agent with write access to a staging cluster.
- **Interview:** what is indirect prompt injection and how do you defend against it in infrastructure terms?

## Checkpoint

Move on to [Phase 16 — AI Cost Engineering](../16-ai-cost-engineering/) when you have demonstrated an injection, blocked it, and written the threat model.
