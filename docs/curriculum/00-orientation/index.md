# Phase 00 — Orientation

> Understand what AI actually is, see the whole system you are going to learn to operate, and get a model running on your own machine on day one.

**Status:** ✅ available · **Estimated effort:** 1 week (about 10 hours) · **Prerequisites:** Linux shell basics, Git, and the ability to install software on your machine.

## Overview

Orientation does four things. It gives you a working definition of AI, machine learning, deep learning and LLMs that you can explain to a colleague, and gets you to run a model so "model" stops being an abstraction. It installs and verifies the toolchain the whole course uses and puts that model in a container. It shows you the production architecture the entire course converges on, layer by layer, and has you run the container on Kubernetes and break it on purpose. And it sets up the learning journal and portfolio that turn every later lab into evidence and interview material.

You will not be asked to understand any mathematics or write anything beyond reading commented Python in this phase.

| Day | You will | Measured on this machine |
|---|---|---|
| 1 | Train, save, reload and time a model; run a pretrained transformer on CPU | 0.5 s training, 6 MB artifact, 35 ms vs 8 ms single vs batched inference; a 99%-confident wrong answer |
| 2 | Verify your environment; containerise the model with a pinned, non-root image | 579 MB image, 1.85 s cold start, 44 KB build context |
| 3 | Run it as a Kubernetes Job; induce and diagnose `OOMKilled` | 2 s Job, ~150 MiB peak memory, exit 137 with empty logs at 32Mi |
| 4 | Create your journal and portfolio; tell your first two-minute lab story | 3 commits, 3 journal entries, 1 phase write-up |

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
| 03 | [Day 3 — The AI Production Stack](./03-ai-production-stack.md) | ✅ |
| 04 | [Day 4 — How to Work Through This Course](./04-how-to-learn-and-build-your-portfolio.md) | ✅ |

## Labs

| Lab | Difficulty | Time | Environment | Status |
|---|---|---|---|---|
| [0.1 — Run Your First Model](./01-what-is-ai.md#hands-on-lab-0-1-run-your-first-model) | 🟢 | 30–45 min | Local, CPU only | ✅ |
| [0.2 — Verify your environment and containerise your first model](./02-environment-setup.md#hands-on-lab-0-2-verify-your-environment) | 🟢 | 45–60 min | Local, Docker + kind | ✅ |
| [0.3 — Run the model on Kubernetes and break it](./03-ai-production-stack.md#hands-on-lab-0-3-run-the-model-on-kubernetes) | 🟡 | 45–60 min | Local, kind | ✅ |
| [0.4 — Set up your learning journal and portfolio](./04-how-to-learn-and-build-your-portfolio.md#hands-on-lab-0-4-set-up-your-portfolio) | 🟢 | 45–60 min | Local, Git | ✅ |

## Phase project

There is no formal project in Orientation. The tangible outputs are: two versioned, checksummed model artifacts; a `pod-health:v1` container image and a `v2` built from the same Dockerfile; a kind cluster with the image loaded and a completed Job; and a portfolio repository with a Phase 00 write-up and three journal entries.

## Assessment

- **Knowledge check:** the four daily quizzes (44 questions in total), closed-book.
- **Practical:** without looking at the labs, train a model, save it, containerise it and run it as a Kubernetes Job with a memory limit you calculated.
- **Troubleshooting:** the Day 3 lab hands you an `OOMKilled` container with empty logs and a `CreateContainerConfigError`; diagnose both from `describe` and events.
- **Architecture:** draw the master architecture from memory and label what a DevOps engineer owns, the most common failure and the first signal at each layer.
- **Interview:** tell the Day 3 story in two minutes, from memory, with numbers.

## Checkpoint

Move on to [Phase 01 — Python for AI/DevOps](../01-python/) when you can, without notes:

- Explain AI, ML, deep learning, generative AI and LLMs with the nesting diagram, and training versus inference in terms of the workload each one is.
- Show a model file on your disk and state its size, version and checksum; compute the weights memory of a model from its parameter count and precision.
- Run the environment verification script clean, explain the Dockerfile line by line, and say where the image's 579 MB and 1.85 s cold start come from.
- Draw the master architecture and, for any five layers, name what you own, the most common failure and the first signal.
- Write the memory formula, apply it, and diagnose an `OOMKilled` pod from exit code 137 and empty logs.
- Show a portfolio repository with dated journal entries and a Phase 00 write-up, and tell one lab story in two minutes.
