# Phase 10 — MLOps

> Industrialise the ML lifecycle: reproducible training, experiment tracking, a model registry, pipelines, deployment, rollback and drift detection with MLflow.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–05 (Phases 06–09 are not required).

## Overview

```text
Code → Data → Training → Evaluation → Model Registry → Deployment → Monitoring → Retraining
```

This is CI/CD for models. You will make training reproducible, track experiments and parameters, register and version models, version data, build a pipeline, deploy from the registry, roll back, and detect drift. MLflow is the primary platform; the concepts transfer to any other.

## Why a DevOps engineer needs this

Every MLOps concept has a DevOps twin: experiment tracking is build metadata, the registry is an artifact repository, promotion is an environment gate, drift is a silent regression. You already know how to run this lifecycle for software. This phase adds data and models to it.

## Learning objectives

- Make a training run reproducible: pinned code, data, parameters, environment.
- Track experiments, parameters, metrics and artifacts in MLflow.
- Register, version, stage and promote models in the MLflow registry.
- Version data and connect a model version to the data that produced it.
- Build a pipeline that trains, evaluates, and conditionally registers a model.
- Deploy from the registry and roll back to a previous version.
- Detect data and prediction drift and trigger retraining.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | The ML lifecycle and reproducibility | 📋 |
| 02 | Experiment tracking with MLflow | 📋 |
| 03 | The model registry: versions, stages, promotion | 📋 |
| 04 | Data versioning | 📋 |
| 05 | Pipelines: train, evaluate, gate, register | 📋 |
| 06 | Deployment from the registry and rollback | 📋 |
| 07 | Drift and monitoring | 📋 |
| 08 | Retraining strategies | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 10.1 — Track the Phase 04 model's training in MLflow; compare runs | 🟢 | Local, Docker | 📋 |
| 10.2 — Register the model, promote it, deploy it to kind from the registry, roll it back | 🟡 | Local, Docker + kind | 📋 |
| 10.3 — Build the pipeline as a Kubernetes Job chain with an evaluation gate; feed it drifted data and watch the gate fail | 🟡 | Local, kind | 📋 |

## Phase project — Project 2: Production ML Pipeline

The Phase 04 pod-failure predictor, industrialised: MLflow tracking and registry, a pipeline with an evaluation gate, deployment from the registry to Kubernetes, rollback, drift detection and full documentation.

## Assessment

- **Knowledge check:** 12 questions.
- **Practical:** add a quality gate that blocks registration if recall drops below a threshold.
- **Troubleshooting:** two "identical" training runs give different metrics; find the sources of non-determinism.
- **Architecture:** design promotion from staging to production for models, including who approves.
- **Interview:** how do you roll back a model, and how is it different from rolling back code?

## Checkpoint

Move on to [Phase 11 — LLMOps](../11-llmops/) when Project 2 trains, gates, registers, deploys and rolls back from MLflow, and you can show a drift alert.
