# Phase 09 — AI Agents

> Give a model tools and a loop, then build the guardrails that make it safe to point at a cluster. Read-only first, always.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–08.

## Overview

An agent is a model in a loop with tools. You will learn tool calling as a loop, state and memory, planning and tool selection, and then spend most of the phase on what makes agents operable: guardrails, human-in-the-loop approval, permissions, and auditability. You will build a DevOps investigation agent that inspects Kubernetes, reads logs, queries metrics, searches runbooks (Project 4), analyses recent changes and produces a diagnosis.

```text
AI Agent → Tool → Policy → Validation → Human Approval → Action
```

## Why a DevOps engineer needs this

Agents are going to be pointed at your infrastructure whether you build them or not. Knowing how a tool call becomes a `kubectl` command, where the permission boundary sits, and how to audit what happened is the difference between an assistant and an incident.

## Learning objectives

- Explain the agent loop: observe, decide, act, repeat.
- Design tools with clear contracts, input validation and least privilege.
- Manage state and memory across a multi-step investigation.
- Implement guardrails: allow-lists, policy checks, output validation, step limits, budgets.
- Implement human-in-the-loop approval and an audit log.
- Diagnose agent failure modes: tool errors, loops, hallucinated tool arguments, privilege creep.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | From tool calling to an agent loop | 📋 |
| 02 | State, memory and planning | 📋 |
| 03 | Designing tools: contracts, validation, least privilege | 📋 |
| 04 | Guardrails, permissions, human-in-the-loop and audit | 📋 |
| 05 | Building a read-only Kubernetes investigation agent | 📋 |
| 06 | Agent failure modes and how to contain them | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 9.1 — Give a model three read-only tools (`get`, `describe`, `logs`) and watch it investigate a broken deployment in kind | 🟡 | Local, kind | 📋 |
| 9.2 — Add policy checks, step limits, an approval gate and an audit log; try to make the agent misbehave | 🟠 | Local, kind | 📋 |
| 9.3 — Add runbook search (Project 4) and metrics queries; produce a structured diagnosis | 🟠 | Local, kind + Docker | 📋 |

## Phase project — Project 5: DevOps AI Agent

An investigation agent with read-only Kubernetes, logs, metrics and runbook tools, policy and approval gates, an audit log, and full documentation including `SECURITY.md` and `THREAT-MODEL.md`. Destructive actions are out of scope until Phase 17, and then only behind explicit approval.

## Assessment

- **Knowledge check:** 12 questions.
- **Practical:** add a `get events` tool with validation and a policy rule.
- **Troubleshooting:** the agent loops forever on a failing tool; diagnose and add the missing guardrail.
- **Architecture:** design the permission model for an agent used by multiple teams.
- **Interview:** how do you secure tool execution for an AI agent?

## Checkpoint

Move on to [Phase 10 — MLOps](../10-mlops/) when Project 5 investigates a broken deployment end to end, every tool call is in the audit log, and you can show a blocked action and explain why it was blocked.
