# Project name

> One sentence: what this is and who it is for. Example: "A FastAPI service that reports the health of a Kubernetes namespace, deployed to kind with read-only RBAC."

## What it does

Three to five bullets. Lead with the outcome, not the technology.

## Architecture at a glance

A small text or image diagram. The full version lives in [ARCHITECTURE.md](ARCHITECTURE.md).

```text
User → API → ... → Kubernetes
```

## Measured numbers

The numbers a reviewer or interviewer will ask about. Every one measured, with how.

| Metric | Value | How measured |
|---|---|---|
| Cold startup | | |
| p50 / p95 latency | | |
| Image size | | |
| Memory request / limit | | |
| Cost to run (per hour, per request) | | |

## Quick start

The shortest path to seeing it work. Full instructions in [SETUP.md](SETUP.md).

```bash
# three to six commands
```

## Failure modes I tested

One line each, linking to [TROUBLESHOOTING.md](TROUBLESHOOTING.md). Example: "OOMKilled at startup with a 32Mi limit: exit 137, empty logs, diagnosed via describe."

## What I would do next

Two or three honest items.

## Documentation

[ARCHITECTURE](ARCHITECTURE.md) · [SETUP](SETUP.md) · [OPERATIONS](OPERATIONS.md) · [TROUBLESHOOTING](TROUBLESHOOTING.md) · [SECURITY](SECURITY.md) · [COST](COST.md)
