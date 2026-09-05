# Phase 00 — Orientation

> Understand what AI actually is, see the whole system you are going to learn to operate, and get a model running on your own machine on day one.

**Status:** 🚧 in progress · **Estimated effort:** 1 week · **Prerequisites:** Linux shell basics, Git, and the ability to install software on your machine.

## Overview

Orientation does three things. It gives you a working definition of AI, machine learning, deep learning and LLMs that you can explain to a colleague. It shows you the production architecture the entire course converges on, so every later phase has a place to hang on. And it gets you to run a model, measure how long it takes to load and to answer, and look at the file it lives in, so "model" stops being an abstraction.

You will not be asked to understand any mathematics or write anything beyond simple Python in this phase.

## Why a DevOps engineer needs this

Sooner or later someone will hand you an AI workload and ask you to put it in production. The vocabulary in this phase is what lets you ask the right questions back: How big is the model? Does it need a GPU? Is this training or inference? What does latency look like? How will we know if it is answering badly? Without the vocabulary you cannot size, schedule, monitor or budget the workload.

## Learning objectives

By the end of this phase you can:

- Define AI, machine learning, deep learning, generative AI and LLMs, and explain how they nest.
- Explain training versus inference, and say which one production mostly runs.
- Explain that a model is an artifact with a size, a version and resource requirements.
- Describe a basic AI production architecture from user to GPU.
- Run a model on your laptop and measure load time, inference latency and artifact size.
- Have Python, Docker, kubectl and a local Kubernetes cluster installed and verified.

## Lessons

| # | Lesson | Status |
|---|---|---|
| 01 | [Day 1 — What Is AI?](./01-what-is-ai.md) | ✅ |
| 02 | [Day 2 — Set Up Your Environment](./02-environment-setup.md) | ✅ |
| 03 | Day 3 — The AI production stack: the master mental model, layer by layer | 📋 |
| 04 | Day 4 — How to work through this course and build a portfolio while you learn | 📋 |

## Labs

| Lab | Difficulty | Time | Environment | Status |
|---|---|---|---|---|
| [0.1 — Run Your First Model](./01-what-is-ai.md#hands-on-lab-0-1-run-your-first-model) | 🟢 | 30–45 min | Local, CPU only | ✅ |
| [0.2 — Verify your environment and containerise your first model](./02-environment-setup.md#hands-on-lab-0-2-verify-your-environment) | 🟢 | 45–60 min | Local, Docker + kind | ✅ |

## Phase project

There is no formal project in Orientation. The tangible output is a trained model artifact on disk, a versioned second artifact from the Day 1 exercise, and a verified local environment.

## Assessment

- **Knowledge check:** the Day 1 quiz.
- **Practical:** without looking at the lab, train a model, save it, reload it and time an inference.
- **Troubleshooting:** the lab includes a deliberately wrong dependency install path to diagnose.
- **Architecture:** draw the user-to-GPU architecture from memory and label what a DevOps engineer owns at each layer.
- **Interview:** the Day 1 interview questions.

## Checkpoint

Move on to [Phase 01 — Python for AI/DevOps](../01-python/) when you can:

- Explain AI, ML, deep learning and LLMs to a colleague in plain language, with the nesting diagram.
- State the difference between training and inference and name the compute each one usually needs.
- Show a model file on your disk, say how large it is and what its version and checksum are.
- Report the load time and per-request latency of a model you ran.
- Run `python3 --version`, `docker run hello-world`, and `kubectl get nodes` against a local cluster without errors.
