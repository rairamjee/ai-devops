# Learning journal

One entry per lesson, written the same day. Ten minutes. The point is not to summarise the lesson; the point is to record what *you* ran, what broke, what you did about it, and what you can now say in an interview that you could not say yesterday.

Entries are newest first.

---

## YYYY-MM-DD — Phase NN, Day N — Lesson title

**What I ran.** The commands or scripts, and the measured results (with units). Example: "Trained the pod-health model: 0.5 s, 6.4 MB artifact, 96.1% test accuracy, 81% recall on unhealthy. Cold container startup 1.85 s."

**What broke.** Anything that did not work first time, with the exact error text. Include things you broke on purpose.

**What I did about it.** The diagnosis steps in order, and the fix. Be honest about dead ends; they are the useful part.

**What I understand now that I did not this morning.** One to three sentences in your own words, no copying from the lesson.

**Interview line.** One sentence you could say in an interview, with a number in it. Example: "I diagnosed a container that was OOMKilled during startup with no logs by reading exit code 137 from `describe`, then computed the correct limit from measured peak memory."

**Open questions.** Anything you want to come back to.

---

## 2026-09-06 — Phase 00, Day 3 — The AI Production Stack *(example entry)*

**What I ran.** `job.yaml` on kind: pod created → completed in 2 s; process 1,038 ms of which imports 195 ms and artifact load 696 ms. `job-oom.yaml` with a 32Mi limit: two pods `OOMKilled`, exit 137, Job `BackoffLimitExceeded`.

**What broke.** First attempt: `CreateContainerConfigError`, event said "image has non-numeric user (app), cannot verify user is non-root". Also `docker run --memory=64m` did *not* kill the process.

**What I did about it.** Read the event, changed the Dockerfile from `USER app` to `USER 10001`, rebuilt, `kind load`, re-applied. For Docker: found that `--memory` allows swap by default; `--memory-swap=64m` reproduces the kill.

**What I understand now.** Memory for a model container is arithmetic first and measurement second. An OOM at startup leaves no logs, so `describe` comes before `logs`. A limit is only as strict as the runtime enforcing it.

**Interview line.** "I sized a model container's memory from measured peak RSS (~150 MiB), then deliberately under-provisioned it to see the OOMKilled signature: exit 137, empty logs, Job failing after backoffLimit."

**Open questions.** How does the per-request working memory term scale for an LLM? (Phase 06.)
