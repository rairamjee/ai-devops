# Phase 01 — Python for AI/DevOps

> Exactly enough Python to build APIs, talk to Kubernetes, package code and read the AI libraries you will spend the rest of the course using.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phase 00. Bash scripting experience helps; no Python beyond basic scripting is assumed.

## Overview

Python is the operating language of AI. Every model, pipeline, inference server and evaluation harness you meet later is either written in Python or driven from it. This phase is not a general Python course. It teaches the subset a DevOps engineer needs: structuring a small project, virtual environments and dependencies, reading and writing JSON and YAML, calling HTTP APIs, building a FastAPI service, using the Kubernetes API client, and testing. Everything is framed around infrastructure tasks you already understand.

## Why a DevOps engineer needs this

You will read stack traces from PyTorch, patch a broken `requirements.txt` in a model-serving image, write a FastAPI wrapper around a model, and glue a Kubernetes API call into an agent tool. If Python is a black box, every one of those becomes a ticket for someone else.

## Learning objectives

- Write readable Python with functions, modules, type hints, dataclasses and error handling.
- Manage environments and dependencies with `venv` and `pip` (and know what `uv` and `pyproject.toml` are for).
- Read and write JSON and YAML; work with files, paths and environment variables safely.
- Call HTTP APIs with timeouts, retries and error handling.
- Build a FastAPI service with request validation, health endpoints and structured logging.
- Use the official Kubernetes Python client to list and describe resources.
- Write tests with `pytest` and run them in CI.
- Containerise a Python service with a small, secure image.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Python for people who write Bash: syntax, functions, modules, errors | 📋 |
| 02 | Data in Python: dicts, lists, dataclasses, JSON and YAML | 📋 |
| 03 | Environments and dependencies: `venv`, `pip`, `requirements.txt`, `pyproject.toml`, `uv` | 📋 |
| 04 | HTTP clients done right: `httpx`, timeouts, retries, status codes | 📋 |
| 05 | FastAPI: routes, validation with Pydantic, health checks, logging | 📋 |
| 06 | The Kubernetes API from Python: auth, listing pods, reading events and logs | 📋 |
| 07 | Testing and packaging: `pytest`, fixtures, Dockerfile for Python, CI | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 1.1 — Rewrite a Bash health-check script in Python with tests | 🟢 | Local | 📋 |
| 1.2 — Build a FastAPI service that lists pods in a namespace via the Kubernetes API | 🟡 | Local, kind | 📋 |
| 1.3 — Containerise it, deploy it to kind with least-privilege RBAC, break the RBAC and fix it | 🟡 | Local, Docker + kind | 📋 |

## Phase project — Project 1: Kubernetes Health API

A FastAPI service that reports the health of a namespace: pod phases, restart counts, recent warning events, resource requests versus usage. Deployed to kind with a dedicated ServiceAccount and read-only RBAC. Ships with `README.md`, `ARCHITECTURE.md`, `SETUP.md`, `OPERATIONS.md`, `TROUBLESHOOTING.md`, `SECURITY.md` and `COST.md`. This becomes the first tool your DevOps agent calls in Phase 09.

## Assessment

- **Knowledge check:** 10 questions on environments, dependencies, HTTP error handling and FastAPI basics.
- **Practical:** add a `/events` endpoint to the health API without instructions.
- **Troubleshooting:** a provided image fails on start with a dependency conflict; diagnose and fix.
- **Architecture:** design how the health API should authenticate to the cluster in production.
- **Interview:** how do you build a secure, minimal container image for a Python service?

## Checkpoint

Move on to [Phase 02 — AI Fundamentals](../02-ai-fundamentals/) when Project 1 runs in kind, has tests, and you can explain every line of its Dockerfile and RBAC manifest.
