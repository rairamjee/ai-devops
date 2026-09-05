# Examples

Runnable code referenced by lessons and labs. Nothing here is a snippet: every directory runs as-is from a clean machine by following its `README.md`.

## Layout

Top level is the technology; below it, the phase and lab or project the code belongs to.

```text
examples/
├── python/          # scripts and services (Phases 00–01, and helpers used later)
│   └── 00-orientation/
│       └── lab-01-first-model/
├── docker/          # Dockerfiles and compose stacks
├── kubernetes/      # manifests, kustomizations, Helm values
├── terraform/       # cloud infrastructure for labs that need it (always with destroy instructions)
├── ml/              # classical ML and PyTorch training code (Phases 04–05, 10)
├── llm/             # LLM API clients, gateways, serving configs (Phases 06–07, 11, 14)
├── rag/             # ingestion, pgvector, retrieval, evaluation (Phase 08)
├── agents/          # tools, agent loops, guardrails (Phases 09, 17)
└── observability/   # Prometheus, Grafana, OpenTelemetry, Loki configs (Phase 12)
```

Directories are created when the first lesson that needs them is published.

## Conventions

- **Runnable.** Each directory has a `README.md` with exact commands and a `requirements.txt` (or `pyproject.toml`) that pins or bounds dependencies.
- **CPU path first.** Where a GPU helps, the README shows both paths and says which one it is using.
- **No credentials.** Configuration comes from environment variables; a `.env.example` documents them. Real `.env` files are git-ignored.
- **Secure defaults.** Least-privilege RBAC, read-only tools, validated inputs, no `latest` tags in anything meant to be reproducible.
- **Artifacts are not committed.** Trained models, downloaded weights and caches are git-ignored; labs regenerate them.
- **Cleanup.** Anything that creates cloud resources ends with a destroy step.
