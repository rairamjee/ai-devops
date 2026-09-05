# Phase 04 — Machine Learning

> The machine-learning lifecycle from a production engineer's perspective: train, validate, test, version, deploy, and watch it decay.

**Status:** 📋 planned · **Estimated effort:** 2 weeks · **Prerequisites:** Phases 00–03.

## Overview

Classical machine learning is where the lifecycle is easiest to see end to end. You will train regression and classification models, trees and random forests, and clustering, with scikit-learn on infrastructure data (pod metrics, latency series, log features). You will learn how to split data, read metrics, recognise overfitting and underfitting, engineer features, version a model and put it behind an API. The algorithms matter less than the lifecycle.

## Why a DevOps engineer needs this

An ML model in production is an artifact with a training pipeline behind it and a decay curve in front of it. Understanding validation and test sets tells you what "accuracy 94%" does and does not promise. Understanding overfitting tells you why a model that looked perfect in a notebook fails on Monday's traffic. This is the mental model MLOps (Phase 10) automates.

## Learning objectives

- Distinguish supervised, unsupervised and reinforcement learning with infrastructure examples.
- Train and evaluate regression and classification models; read accuracy, precision, recall, F1, confusion matrices and error metrics.
- Explain decision trees, random forests and clustering at the level needed to choose and operate them.
- Split data into training, validation and test sets and explain why each exists.
- Recognise overfitting and underfitting and know the standard remedies.
- Engineer features from raw infrastructure data.
- Version a model artifact and serve it behind an HTTP API in a container.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | Supervised, unsupervised and reinforcement learning: which problem is which | 📋 |
| 02 | Regression: predicting a number (latency, capacity) | 📋 |
| 03 | Classification and its metrics: predicting a label (will this pod fail?) | 📋 |
| 04 | Trees and random forests: the workhorse models | 📋 |
| 05 | Clustering: finding structure in metrics without labels | 📋 |
| 06 | Feature engineering from logs and metrics | 📋 |
| 07 | Train, validation, test; overfitting and underfitting | 📋 |
| 08 | Model versioning and deployment basics: the artifact, the API, the rollback | 📋 |

## Labs

| Lab | Difficulty | Environment | Status |
|---|---|---|---|
| 4.1 — Build a scikit-learn pipeline on pod metrics; compare three models with proper splits | 🟢 | Local | 📋 |
| 4.2 — Unsupervised anomaly detection on a latency time series | 🟢 | Local | 📋 |
| 4.3 — Serve a versioned model behind FastAPI in Docker; deploy v2, observe a regression, roll back to v1 | 🟡 | Local, Docker | 📋 |

## Phase project — Pod-failure predictor API

A classifier trained on pod telemetry that predicts imminent failure, served behind the FastAPI skeleton from Phase 01, with model versioning, a `/model` endpoint that reports version and checksum, and a rollback procedure documented in `OPERATIONS.md`. This becomes the model you industrialise with MLflow in Phase 10.

## Assessment

- **Knowledge check:** 15 questions.
- **Practical:** given a CSV of metrics, train and evaluate a classifier and report metrics honestly.
- **Troubleshooting:** a model with 99% training accuracy scores 60% in production; diagnose.
- **Architecture:** design the deploy and rollback flow for a model artifact.
- **Interview:** explain overfitting to a non-ML engineer and how you would detect it in production.

## Checkpoint

Move on to [Phase 05 — Deep Learning](../05-deep-learning/) when your predictor API runs in Docker, reports its model version, and you can roll it back and explain what precision and recall mean for it.
