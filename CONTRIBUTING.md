# Contributing

This repository is built from [COURSE-DESIGN-SPECIFICATION.md](COURSE-DESIGN-SPECIFICATION.md). That document is the single source of truth; when in doubt, follow it.

## The authoring rule

> **Fewer, deeper, runnable lessons.**

Do not add pages to make the repository look complete. A lesson earns its place only if the learner can understand something new, run something, break something, fix something, explain what happened and apply it to production.

Every concept must answer four questions: **What is it? Why does it matter? How do I operate it? What happens when it breaks?**

## Adding a lesson

Lessons live in `docs/curriculum/<NN-phase>/<NN-slug>.md`, numbered in learning order (`01-what-is-ai.md`, `02-...md`). Every lesson contains, in this order:

1. Title (`Day N — Topic`)
2. Learning objectives
3. Prerequisites (or "No prerequisites.")
4. Concept explanation (analogies, diagrams, tables, small examples, real infrastructure scenarios)
5. **DevOps perspective — "Why does a DevOps Engineer need to know this?"** (mandatory)
6. Architecture (diagram when relevant)
7. Hands-on lab with exact steps
8. Expected result
9. Troubleshooting
10. Exercise
11. Quiz (5–15 questions)
12. Interview questions
13. Checkpoint

Then register the lesson in `docs/.vitepress/config.mts` (sidebar), the phase `index.md`, `docs/labs/index.md` if it contains a lab, and `PROGRESS.md`.

## Adding a lab

Labs must be practical, reproducible, incremental, production-oriented, safe and clearly documented. Use the sections: Title, Objective, Difficulty (🟢🟡🟠🔴), Estimated Time, Prerequisites, Architecture, Environment Requirements, Setup, Steps, Expected Output, Validation, Troubleshooting, Cleanup, Extension Challenge, Questions.

Rules:

- Prefer a **CPU-only path**; add a GPU path alongside it when relevant.
- Labs that need paid cloud resources must state that up front, name the resource type and cost drivers, give a local alternative if one exists, and always include cleanup (`terraform destroy` or equivalent).
- Agent labs start **read-only** (`kubectl get/describe/logs`). Destructive actions require explicit approval, least privilege, a sandbox, audit logs and a rollback procedure.
- Every advanced lab includes at least one deliberate failure scenario.

## Adding code

Code lives under `examples/` and must be runnable as-is:

- Pin or bound dependencies in `requirements.txt` (or `pyproject.toml`) next to the code.
- No hard-coded credentials, ever. Use environment variables and ship a `.env.example`.
- Secure defaults, input validation where relevant, comments where they help.
- Include a short `README.md` per example directory.

## Adding a project

Projects live in `docs/projects/` with code under `examples/`. Each project ships `README.md`, `ARCHITECTURE.md`, `SETUP.md`, `OPERATIONS.md`, `TROUBLESHOOTING.md`, `SECURITY.md` and `COST.md`; add `DISASTER-RECOVERY.md`, `RUNBOOK.md`, `SLO.md` and `THREAT-MODEL.md` where applicable.

## Style

- Explain from zero. Never assume the learner knows an AI term you have not defined.
- Principles before products: explain what a class of tool does before demonstrating a specific tool.
- Prefer official documentation as the source for links. AI tooling changes fast: verify current docs before publishing implementation steps.
- Use consistent, descriptive file names within a phase.
