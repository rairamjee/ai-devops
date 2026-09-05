# Day 2 — Set Up Your Environment

> Today you install and verify the toolchain the whole course runs on, and you put yesterday's model in a container. Along the way you learn why AI environments are heavier and more brittle than ordinary web development, and how to keep them under control.

**Time:** about 2.5 hours. Installing tools you do not have yet can add an hour; the lab itself is 45–60 minutes.

## Learning objectives

By the end of this lesson you can:

- Name every tool the course uses locally, say what it stands in for in production, and explain why it is installed now rather than later.
- Explain why AI dependencies are large and version-sensitive, and what pinning does about it.
- Describe three levels of isolation (virtual environment, container, cluster), what each isolates and what leaks through.
- Read a Dockerfile for a model image line by line and say what each instruction is for.
- Build a container image that trains a model at build time and only serves at run time, and explain when you would *not* bake weights into an image.
- Measure and explain where an AI image's size and startup time come from.
- Run a verification script that proves your machine is ready, and create a local Kubernetes cluster.

## Prerequisites

- [Day 1](./01-what-is-ai.md) completed, including Part A of Lab 0.1. You will reuse its code.
- Administrator rights on your machine to install software.
- About 15 GB of free disk. AI toolchains are disk-hungry; the lesson explains why.

## Concept explanation

### 1. The toolchain is the production stack in miniature

Every tool you install today has a production twin. Learning the local tool *is* learning the production concept; the difference is scale.

| Tool | What it does in this course | Production twin | Why now |
|---|---|---|---|
| **Python 3.10+** | Runs every model, pipeline and service | The runtime inside every AI container | AI is written in Python; you cannot avoid it |
| **venv + pip** (or `uv`) | Isolates each lab's libraries | The dependency layer of a container image | AI libraries are huge and conflict; isolation is not optional |
| **Git** | Versions code and manifests | Source of truth for CI/CD | You already know this one |
| **Docker** | Packages runtime + code + model into an image | The unit of deployment | The image is the contract between the ML team and you |
| **kind** | A real Kubernetes cluster in Docker containers | The cluster you deploy to | Same API server, same manifests, no cloud bill |
| **kubectl** | Talks to any Kubernetes API | Same tool, same commands | You will use it in every phase from now on |

What is deliberately **not** installed yet, and when it arrives:

| Tool | Phase | Why wait |
|---|---|---|
| PyTorch, Hugging Face | 05–06 (Part B of Lab 0.1 was a preview) | Hundreds of MB to GB per environment; install per lab when needed |
| PostgreSQL + pgvector | 08 | Runs in Docker when RAG starts |
| Prometheus, Grafana, OpenTelemetry | 12 | Runs in Docker or kind when observability starts |
| NVIDIA driver, CUDA toolkit, container toolkit | 13 | Only if you have a GPU; the version matrix deserves its own lesson |
| Terraform, AWS CLI | 13–14 | Only when a lab genuinely needs cloud resources, and each one says so |

Installing everything on day one produces a machine full of half-configured tools and no understanding of any of them. Each tool arrives with the lesson that needs it.

### 2. Why AI environments are heavier and more brittle

Two facts about AI libraries drive most of the pain you will meet.

**They are large.** A Python library for web development is a few megabytes of source. An AI library is compiled numerical code, often with copies of linear-algebra libraries, and for GPU builds, hundreds of megabytes of CUDA runtime. Real sizes you will measure today and this week:

| Environment | Approximate size | Where you meet it |
|---|---|---|
| Plain Python 3.12 (slim container base) | ~190 MB | Today's Dockerfile |
| + scikit-learn, NumPy, SciPy, joblib | + ~290 MB | Today's image: dependencies outweigh the base |
| + PyTorch (CPU build) + Transformers | + ~1 GB | Lab 0.1 Part B |
| + PyTorch (CUDA build) | + several GB | Phase 05 on a GPU machine |
| One small pretrained model in the Hugging Face cache | ~270 MB | Lab 0.1 Part B |
| One 7B-parameter LLM in fp16 | ~14 GB | Phase 06 onward |

Plan disk the way you plan it for a build server, not a laptop. Images of 5–10 GB are normal for GPU workloads. Pull times, registry storage and node disk pressure follow directly.

**They are tightly version-coupled.** Compiled libraries are built against specific versions of each other and of Python. Some couplings you will meet:

- **Python ↔ library.** A new Python release is often unsupported by PyTorch for months; an old Python is dropped after a few years. Pin the Python minor version.
- **Library ↔ library.** When NumPy released version 2.0 in 2024, many packages compiled against 1.x broke at import time until they were rebuilt. "Upgrade everything" is not a safe default in AI environments.
- **Model artifact ↔ library.** Yesterday's `.joblib` file was written by one version of scikit-learn. Loading it with a different version may warn, may work, or may silently behave differently. The artifact's metadata should record the versions that produced it; today's exercise adds that.
- **Driver ↔ CUDA ↔ framework.** On GPU machines the NVIDIA driver, the CUDA toolkit and the PyTorch build must agree. Phase 13 has the matrix. Today, know that it exists.

The defence is the same in every case: **pin versions, record them in the artifact, and build environments from the pinned list, never by hand.**

::: tip Mental model: an environment is an artifact too
`requirements.txt` says what you want. A lock file or a `pip freeze` says exactly what you got. A container image digest says exactly what is running. Reproducibility means being able to go from the first to the third and get the same bytes twice. Treat the environment with the same discipline as the model file: version it, check it in, build it from source, never patch it live.
:::

### 3. Three levels of isolation

You will use all three, often in the same hour.

| Level | Isolates | Shares with the host | Startup cost | When to use |
|---|---|---|---|---|
| **Virtual environment** (`venv`) | Python packages | Everything else: OS, Python binary, system libraries, GPU driver | Instant | Development, reading code, quick experiments |
| **Container** (Docker) | The entire userland: OS libraries, Python, packages, code, model | The kernel and, on GPU hosts, the driver | Seconds | Packaging for deployment; reproducing production locally |
| **Cluster** (kind, then real Kubernetes) | Containers plus scheduling, resource limits, networking, secrets | The machines it runs on | Minutes to create, seconds per pod | Anything that needs to behave like production: limits, probes, restarts, scaling |

Two things leak through every level and will matter in Phase 13: the **kernel** (a container cannot bring its own) and the **GPU driver** (installed on the host, matched by the container's CUDA libraries). Everything else can be pinned inside the image.

### 4. What a model image contains

Today's Dockerfile packages the Day 1 model. Read it as a sequence of decisions:

```dockerfile
FROM python:3.12-slim                     # 1. pinned runtime base
ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 # 2. logs flush immediately; no pip cache in the image
WORKDIR /app
COPY requirements.txt .                   # 3. dependencies first, on their own layer
RUN pip install -r requirements.txt       #    → code changes do not reinstall 290 MB
COPY train_and_predict.py predict.py ./   # 4. code
ARG MODEL_VERSION=v1                      # 5. build-time parameters
ARG LABEL_THRESHOLD=5.0
RUN python train_and_predict.py --version "${MODEL_VERSION}" \
      --threshold "${LABEL_THRESHOLD}" --out /model   # 6. train at BUILD time; bake the artifact
ENV MODEL_PATH=/model/pod-health-model-${MODEL_VERSION}.joblib
RUN useradd --create-home --uid 10001 app && chown -R app:app /app /model
USER 10001                                # 7. never run as root (numeric uid, see below)
ENTRYPOINT ["python", "predict.py"]       # 8. the container only serves
```

Decisions 1, 3 and 7 are ordinary good container hygiene and you have probably seen them. Decisions 5, 6 and 8 are the AI-specific ones:

- **The image carries the model.** Runtime and artifact are versioned together: `pod-health:v1` means *this* code, *these* library versions, *that* model file. Roll back the tag, roll back everything.
- **Training happens at build time, never at run time.** The running container is inference only, which is what production is. A build argument produces `v2` without editing the Dockerfile.
- **Bake or mount?** Baking a 6 MB model into the image is right. Baking a 14 GB LLM into an image is wrong: every code change would rebuild and re-push 14 GB, and every node would pull it. Large weights are mounted from a volume or a shared cache so the image stays small and the weights have their own lifecycle. Phase 14 does this. The principle, "runtime and artifact versions are recorded together", does not change; only the mechanism does.

Where the image's size comes from, measured on the real build:

```text
Layer                                              Size
python:3.12-slim base (Debian + Python)           ~190 MB
pip install scikit-learn, numpy, scipy, joblib     287 MB
train at build time → /model artifact               8 MB
non-root user, code, metadata                       7 MB
                                                  ─────────
pod-health:v1                                      579 MB
```

The dependencies are half the image, and this is the *smallest* AI stack you will build. Add PyTorch and the dependency layer alone passes a gigabyte.

### 5. Startup anatomy, measured

On Day 1, loading the model took 33 ms. Inside the container the same load takes about 600 ms, and the whole process, from `docker run` to exit, takes just under two seconds. Where did the time go?

```text
docker run --rm pod-health:v1            wall clock ≈ 1.85 s
  container create + start               ≈ 0.9 s   (Docker, not your code)
  python starts, imports joblib/numpy    ≈ 0.08 s
  joblib.load(...)                       ≈ 0.6 s   ← first load also imports scikit-learn internals
  5 predictions                          ≈ 0.17 s
```

Day 1's 33 ms was measured in a process that had already imported scikit-learn to *train*. A fresh serving process pays the import cost inside the first `load`. Two lessons that scale to every model you will ever deploy:

1. **Measure startup in the container, cold**, not in a warm development environment. The number you need for readiness probes and autoscaling is the cold one.
2. **Startup is import + load + warm-up**, and for large models each of those is seconds to minutes. Yesterday's Part B took 37 seconds to be ready on first run.

### 6. Common misconceptions

- **"Docker makes it reproducible."** Only if the base image is pinned and the dependencies are pinned. `FROM python:latest` plus unpinned `pip install` gives you a different image every week.
- **"A slim base image means a small image."** The base is a third of today's image; dependencies are half. Slimming the base saves tens of MB; not installing what you do not need saves hundreds.
- **"kind is a toy."** kind runs a real Kubernetes control plane. The manifests, resource limits, probes and failure modes you learn on it transfer unchanged to a cloud cluster. What it does not give you is real networking scale, real storage classes, or GPUs.
- **"I need a GPU to start."** Nothing before Phase 13 requires one, and every phase before then has a CPU-only path.
- **"ML people use conda, so I must too."** Conda is one packaging system among several. `venv` + `pip` (or `uv`) is enough for this course and closer to how containers are built. Know that conda exists; you will meet it in data teams' environments.

## Why does a DevOps Engineer need to know this?

Because the image is the handover point. A data scientist's work reaches production as a container that *someone* built, and that someone is usually you. If you understand what is in the image and why, you can size it, secure it, speed it up and debug it. If you do not, every failure becomes "the model team's problem" or "the platform team's problem" with you in between.

| You will be asked to | This lesson gives you |
|---|---|
| Containerise a notebook or script a data scientist wrote | The Dockerfile pattern: pinned base, deps layer, code, artifact, non-root |
| Explain why the image is 6 GB | The size anatomy: dependencies and weights dominate |
| Explain why pods take four minutes to become ready | Startup anatomy: import, load, warm-up |
| Fix "it worked in the notebook" | Version coupling and pinning |
| Set up laptops for a new ML team | The verification script and the isolation levels |
| Decide whether weights belong in the image or on a volume | The bake-or-mount trade-off |

### Real-world scenario: the pickle that changed its mind

A data scientist trains a fraud model in a notebook and hands over `model.pkl` and a two-line README. The platform team writes a Dockerfile that installs `scikit-learn` with no version pinned. It builds, loads the file with a warning nobody reads, and passes the smoke test.

Three months later a routine rebuild pulls a newer scikit-learn. The pickle still loads, still with a warning. Fraud detections drop by a third over a weekend. No errors, no crashes, no alerts. The eventual root cause: a change in how the newer library handled one internal parameter meant the loaded model was not quite the model that was trained.

What would have prevented it, all from this lesson: a pinned dependency list built into the image; the training library version recorded in the artifact's metadata; a load-time check that refuses to serve when the versions disagree. Today's exercise makes you add exactly that check.

## Mental model

**Your laptop is a tiny production cluster.** The virtual environment is the container's dependency layer. The container is the pod. kind is the cluster. Every practice you learn locally, pinning, non-root, resource limits, measuring cold startup, is a production practice at a scale you can see. Nothing you do today is throwaway.

## Architecture

```text
Your laptop
│
├── .venv/                  develop: read code, run scripts, iterate fast
│      ↓ pin versions
├── Docker image            package: runtime + libraries + code + model, one immutable unit
│      ↓ kind load
└── kind cluster            run like production: scheduler, limits, probes, restarts
       ↓ (Phase 13+)
   Cloud cluster            same manifests; add GPUs, real storage, real cost
```

## Hands-on lab 0.2 — Verify your environment and containerise your first model {#hands-on-lab-0-2-verify-your-environment}

**Objective:** confirm every tool the course needs is installed and working, create a local Kubernetes cluster, and package the Day 1 model as a versioned container image whose size and startup you can explain.

**Difficulty:** 🟢 Beginner · **Estimated time:** 45–60 minutes, plus installation time for anything missing.

**Prerequisites:** Day 1 Lab Part A completed. Admin rights to install software.

**Architecture:**

```text
verify_env.sh ──► all green ──► kind create cluster ──► docker build pod-health:v1 ──► docker run
                                                              │
                                                              └─► docker build --build-arg MODEL_VERSION=v2 ──► pod-health:v2
```

**Environment requirements:** Linux, macOS, or Windows with WSL2. About 15 GB of free disk, 8 GB of RAM. CPU only. No cloud resources, no credentials.

### Setup — installing what is missing

Skip anything the verification script in Step 1 already passes. Use the official installers; the links are the ones that stay current.

| Tool | Linux (Debian/Ubuntu) | macOS | Windows |
|---|---|---|---|
| Python 3.10+ | `sudo apt install python3 python3-venv python3-pip` | `brew install python` or [python.org](https://www.python.org/downloads/) | Install [WSL2](https://learn.microsoft.com/windows/wsl/install), then follow the Linux column inside it |
| Git | `sudo apt install git` | `brew install git` | Inside WSL2: Linux column |
| Docker | [Docker Engine](https://docs.docker.com/engine/install/) then `sudo usermod -aG docker $USER` and log out/in | [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/) | [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) with the WSL2 backend enabled |
| kubectl | [kubernetes.io install guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) | `brew install kubectl` | Inside WSL2: Linux column |
| kind | [kind quick start](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) (single binary) | `brew install kind` | Inside WSL2: Linux column |

::: warning Windows users
Do everything inside WSL2 (Ubuntu). Docker Desktop's WSL2 integration exposes the Docker daemon there. Native Windows paths, PowerShell and Python installers will work for some labs and fail confusingly for others; WSL2 works for all of them.
:::

### Steps

**Step 1. Run the verification script.** It is read-only: it checks, it never installs or changes anything.

```bash
cd ai-devops/examples/python/00-orientation/lab-02-environment
chmod +x verify_env.sh
./verify_env.sh
```

Every ❌ must be fixed before continuing; ⚠️ items are informational. The script exits non-zero on any failure, so you can also use it on a fresh machine or in CI.

**Step 2. Read what the script checks.** Open `verify_env.sh`. Notice it checks the Docker *daemon* separately from the Docker *client* (the most common failure is a client with no permission to reach the daemon), and that the GPU check is informational only.

**Step 3. Create a local Kubernetes cluster.**

```bash
kind create cluster --name ai-devops-lab
kubectl get nodes
```

This takes about a minute the first time (it pulls a node image of roughly 1 GB). You get a one-node cluster running as a Docker container, and `kubectl` is pointed at it via the context `kind-ai-devops-lab`. Re-run the script with the cluster name to confirm the API is reachable:

```bash
./verify_env.sh --cluster ai-devops-lab
```

**Step 4. Read the Dockerfile.** Move to the Day 1 code and read `Dockerfile` and `.dockerignore` against the walkthrough in the concept section. Then read `predict.py`: it is the serving half of yesterday's script, on its own.

```bash
cd ../lab-01-first-model
cat Dockerfile .dockerignore
```

**Step 5. Build the image.** Training happens during the build; watch for it.

```bash
docker build -t pod-health:v1 .
```

The build takes about half a minute on a fast connection; almost all of it is the `pip install` layer. In the output, look for the `ls -la /model` line in the training step: that is the artifact being created inside the image.

**Step 6. Inspect the image.**

```bash
docker image ls pod-health
docker history pod-health:v1
```

`docker history` shows one row per layer with its size. Find the `pip install` layer and the training layer, and compare them with the size anatomy in the concept section.

**Step 7. Run it, cold, and time it.**

```bash
time docker run --rm pod-health:v1
```

Compare the `[startup]` line with Day 1's `[load]` line and read the "Startup anatomy" section again.

**Step 8. Build v2 without touching the Dockerfile.**

```bash
docker build --build-arg MODEL_VERSION=v2 --build-arg LABEL_THRESHOLD=2.0 -t pod-health:v2 .
docker run --rm pod-health:v2
docker image inspect pod-health:v1 pod-health:v2 --format '{{.RepoTags}} {{.Id}}'
```

Notice that the `pip install` layer was **cached**: only the steps after `ARG` re-ran. Two tags, two image IDs, two model versions, one Dockerfile. This is what "runtime and artifact versioned together" looks like.

**Step 9. Load the image into the cluster** so Day 3 can use it. kind has no registry; images are copied onto the node.

```bash
kind load docker-image pod-health:v1 --name ai-devops-lab
```

### Expected output

The verification script on a ready machine:

```text
AI for DevOps — environment check
==================================
  ✅ platform       Linux x86_64
  ✅ python3        3.12.3
  ✅ venv module    available
  ✅ pip            24.0
  ✅ uv (optional)  0.11.26
  ✅ git            2.43.0
  ✅ docker cli     29.6.1
  ✅ docker daemon  reachable (29.6.1, linux/x86_64)
  ✅ docker run     hello-world ran
  ✅ kubectl        v1.36.0
  ✅ kind           0.32.0
  ✅ kind cluster   'ai-devops-lab' exists
  ✅ cluster api    1 node(s) reachable via context kind-ai-devops-lab
  ✅ disk free      120 GB here
  ✅ memory         15 GB
  ⚠️  gpu (optional) no NVIDIA GPU detected; every lab through Phase 12 has a CPU path
----------------------------------
  passed: 15   warnings: 1   failed: 0
  Environment ready.
```

The build, abbreviated to the interesting lines:

```text
#8  [4/7] RUN pip install -r requirements.txt
#10 [6/7] RUN python train_and_predict.py --version "v1" --threshold "5.0" --out /model && ls -la /model
#10 1.838 -rw-r--r-- 1 root root 6522981 ... pod-health-model-v1.joblib
#10 1.838 -rw-r--r-- 1 root root      93 ... pod-health-model-v1.sha256
#12 naming to docker.io/library/pod-health:v1 done

real    0m33.345s
```

The image and the cold run:

```text
$ docker image ls pod-health
pod-health   v1   579MB

$ time docker run --rm pod-health:v1
[startup]   imports 83 ms, artifact load 589 ms  (model v1, 6,370 KB)
[predict]   pod                  prediction  p(unhealthy)   latency
            api-7d9f-abcde       healthy             0.00   26.50ms
            worker-5c4b-fghij    UNHEALTHY           1.00   29.16ms
            cache-6b8a-klmno     UNHEALTHY           0.99   33.43ms
            ingest-9e2d-pqrst    UNHEALTHY           0.84   37.79ms
            batch-3a1c-uvwxy     UNHEALTHY           1.00   46.19ms
[done]      5 predictions in 174 ms; process total 847 ms

real    0m1.850s
```

Read it as an operator:

- **579 MB for a 6 MB model.** The runtime dwarfs the artifact. For LLMs the ratio flips: a 14 GB artifact next to a 5 GB runtime. Either way, you plan pulls and disk for gigabytes.
- **The process took 0.85 s; the wall clock 1.85 s.** Container start overhead is real and is not in your application's logs. Kubernetes adds scheduling and image pull on top.
- **`artifact load 589 ms` versus Day 1's 33 ms.** Same file, same machine. Cold process versus warm process. Measure cold.
- **Predictions are the same as Day 1**, to two decimals. Same training data, same seed, same library versions pinned in the image: the model is reproducible even though the file's checksum differs (Day 1 exercise 1 explains why).

### Validation

You have completed the lab when:

- [ ] `verify_env.sh --cluster ai-devops-lab` reports zero failures.
- [ ] `kubectl get nodes` shows one `Ready` node in context `kind-ai-devops-lab`.
- [ ] `docker image ls pod-health` shows `v1` and `v2` with different image IDs.
- [ ] You can name the three largest layers of the image and say what each contains.
- [ ] You can state the cold startup time of the container and explain why it is larger than Day 1's load time.
- [ ] `pod-health:v1` is loaded into the kind cluster.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `permission denied while trying to connect to the Docker daemon socket` | Your user is not in the `docker` group (Linux) | `sudo usermod -aG docker $USER`, then log out and back in. Verify with `docker info`. |
| `Cannot connect to the Docker daemon` | Docker is not running | Linux: `sudo systemctl start docker`. macOS/Windows: start Docker Desktop. |
| `docker` works in PowerShell but not in WSL2 | WSL integration is off in Docker Desktop | Docker Desktop → Settings → Resources → WSL integration → enable your distro. |
| `kind create cluster` fails with `too many open files` or inotify errors | Kernel inotify limits are too low for the node container | `sudo sysctl fs.inotify.max_user_watches=524288 fs.inotify.max_user_instances=512`, then retry. See kind's known issues page. |
| `kind create cluster` hangs at "Starting control-plane" | Slow node-image pull, or low memory | Wait a few minutes on first run; check Docker Desktop's memory allocation is at least 4 GB. |
| `The virtual environment was not created successfully because ensurepip is not available` | `python3-venv` missing (Debian/Ubuntu) | `sudo apt install python3-venv`. |
| `pip install` fails with SSL or timeout errors | Corporate proxy or restricted network | Set `HTTPS_PROXY`; or configure `pip config set global.index-url` to an internal mirror. Never disable certificate verification. |
| `docker build` fails at `pip install` with `No space left on device` | Docker's storage is full | `docker system df`, then `docker system prune` (read what it will delete first). |
| `docker build` is very slow at `pip install` on Apple Silicon | Building an `amd64` image under emulation | Let Docker build for your native `arm64`; the labs do not need `amd64` until you push to a cloud registry. |
| `kind load docker-image` says `not yet present on node, loading...` | Normal | That is the success path; it is copying the image. |
| Verification script says `kind cluster ... not found` after you created it | Different cluster name or different kubeconfig | `kind get clusters`; pass the exact name with `--cluster`. |

### Common mistakes

- **Building with a large context.** Without `.dockerignore`, `docker build .` ships your virtual environment and artifacts to the daemon every time. Today's context is 44 KB; check yours with the first lines of the build output.
- **Reordering the Dockerfile so code is copied before dependencies.** Every code change then reinstalls 290 MB. Dependencies first, code second.
- **Unpinned base image.** `python:3-slim` or `python:latest` changes under you. Pin the minor version at least; pin the digest for anything you must reproduce exactly.
- **Running as root because it is easier.** Kubernetes admission policies in most organisations will reject the pod, and you will fix it at 2 a.m. instead of now.
- **`USER app` instead of `USER 10001`.** A named user works in Docker but fails on Kubernetes when the pod sets `runAsNonRoot: true`: the kubelet cannot prove a *name* is non-root and refuses to start the container with `CreateContainerConfigError`. The first version of this lesson's Dockerfile made exactly this mistake; Day 3 shows the error. Always set a numeric UID.
- **Installing the GPU build of PyTorch on a laptop with no GPU.** Multi-gigabyte download, no benefit. Use the CPU index URL as in Day 1.

### Cleanup

Keep the kind cluster and the `pod-health` images: Day 3 uses both.

```bash
# Only if you want the disk back now:
docker rmi pod-health:v1 pod-health:v2
kind delete cluster --name ai-devops-lab
```

### Extension challenge

1. **Shrink it.** Try to get `pod-health:v1` under 450 MB without breaking it. Options to explore: a multi-stage build that copies only the installed site-packages, `pip install --no-compile`, or removing test directories from the installed packages. Measure each step with `docker image ls`. Write down what you gained and what you would not do in production.
2. **The Alpine trap.** Change the base to `python:3.12-alpine` and rebuild. Watch what happens to build time and image size, and find out why (search: musl, manylinux wheels). This is a rite of passage; do it once on purpose.

### Questions

1. Which Dockerfile layer changes when you (a) edit `predict.py`, (b) bump a library version, (c) build a new model version? What does each change cost in rebuild time and in bytes pushed to a registry?
2. Where would a 14 GB model's weights live, if not in the image, and what would the container need at startup to find them?
3. The container runs as UID 10001 with a read-only filesystem in Day 3. Where can it still write, and does `predict.py` need to?

## Exercise

1. **Lock it.** Inside the Day 1 virtual environment, run `pip freeze > requirements.lock`. Compare it with `requirements.txt`. Change the Dockerfile to install from the lock file, rebuild, and confirm the image works. Explain in your journal what the lock file protects you from that the requirements file does not.
2. **Record the versions in the artifact.** Edit `train_and_predict.py` so the bundle also stores `sklearn.__version__` and `numpy.__version__`. Then edit `predict.py` to compare the stored versions with the running ones at load time, print a warning on mismatch, and exit non-zero if the major version differs. Rebuild the image and run it. This is the check that would have caught the "pickle that changed its mind".
3. **Disk budget.** Run `du -sh .venv` in the Day 1 directory, `docker system df`, and `du -sh ~/.cache/huggingface` if you did Part B. Write a one-paragraph disk plan for a laptop that will complete this course, with numbers.
4. **Explain the Dockerfile** to a colleague or a rubber duck, one line at a time, without looking at the lesson. Note the line you found hardest and read that section again.

## Quiz

**1. Why does the course install PyTorch per lab instead of once, globally?**

::: details Answer
It is hundreds of megabytes to gigabytes, comes in CPU and several CUDA builds, and is version-coupled to Python and other libraries. Installing it per virtual environment, pinned, avoids conflicts and keeps each lab reproducible.
:::

**2. What does a virtual environment isolate, and what does it not isolate?**

::: details Answer
It isolates Python packages. It shares the operating system, the Python binary, system libraries and any GPU driver with the host. Containers isolate the whole userland; only the kernel and GPU driver are shared.
:::

**3. Why are dependencies installed before the code is copied in the Dockerfile?**

::: details Answer
Layer caching. Docker re-runs a step only if it or an earlier step changed. Code changes constantly; dependencies rarely. Putting dependencies first means a code edit does not reinstall 290 MB.
:::

**4. Why is the model trained during `docker build` rather than when the container starts?**

::: details Answer
Production containers serve; they do not train. Training at build time makes the artifact part of the versioned image, keeps startup fast and predictable, and stops every replica from doing redundant, non-deterministic work.
:::

**5. When would you *not* bake model weights into the image?**

::: details Answer
When they are large (gigabytes). Every code change would rebuild and push the weights, and every node would pull them. Large weights are mounted from a volume or cache with their own lifecycle; the image records which version it expects.
:::

**6. The image is 579 MB and the model is 6 MB. Where is the rest?**

::: details Answer
About 190 MB is the Python base image and about 290 MB is scikit-learn, NumPy and SciPy. Dependencies dominate small-model images; for LLMs the weights dominate instead.
:::

**7. Day 1 loaded the model in 33 ms; the container took about 600 ms. Why?**

::: details Answer
Day 1 measured in a process that had already imported scikit-learn for training. A fresh serving process pays the import cost inside the first load. Startup must be measured cold, in the container.
:::

**8. What two things cannot be pinned inside a container image?**

::: details Answer
The kernel and, on GPU hosts, the NVIDIA driver. Both come from the host and must be compatible with what the image expects.
:::

**9. What would the "pickle that changed its mind" incident have needed to be caught early?**

::: details Answer
Pinned library versions in the image, the training library versions recorded in the artifact metadata, and a load-time check that refuses or warns on mismatch. Plus quality monitoring, which is a later phase.
:::

**10. Why does `kind load docker-image` exist, and what replaces it in a real cluster?**

::: details Answer
kind nodes cannot see your local Docker images and have no registry, so the image is copied onto the node. In a real cluster, images are pushed to a registry and pulled by tag or digest.
:::

## Interview questions

1. **"How do you make a machine-learning environment reproducible?"** Pin the Python version, pin dependencies with a lock file, pin the base image (by digest for strict reproducibility), build from those files only, record library versions in the model artifact and check them at load time.
2. **"Walk me through a Dockerfile for a model service."** Pinned slim base; dependencies on their own layer; code; the artifact baked in or a mount point for it; a non-root user; an entrypoint that only serves. Then mention what you would change for large weights.
3. **"Why are AI container images so big, and does it matter?"** Compiled numerical libraries and CUDA runtimes, then the weights. It matters for pull time, node disk, rollout speed, autoscaling latency and registry cost. Mitigations: CPU builds where possible, multi-stage builds, weights outside the image, pre-pulled or cached images.
4. **"How would you measure a model service's startup time, and why does it matter?"** Cold, in the container or pod: import, load, warm-up. It sets readiness probe timings, rollout duration, and how far ahead autoscaling must act.
5. **"What is the difference between a virtual environment, a container and a pod?"** Package isolation; full userland isolation sharing the kernel; a scheduled container with resource limits, networking and identity. What leaks through each: everything but packages; kernel and GPU driver; the node.
6. **"A data scientist gives you a pickle file and a notebook. What do you ask for before you containerise it?"** Exact library versions used to train, Python version, input schema, expected output, how to smoke-test it, resource needs, and where the artifact should live. Then you pin all of that in the image.

## Further exploration

- [Docker: Building best practices](https://docs.docker.com/build/building/best-practices/): layer caching, `.dockerignore`, multi-stage builds, pinning.
- [kind quick start](https://kind.sigs.k8s.io/docs/user/quick-start/) and [known issues](https://kind.sigs.k8s.io/docs/user/known-issues/): the two pages you will need this week.
- [Python `venv` documentation](https://docs.python.org/3/library/venv.html) and the [Python Packaging User Guide on requirements files](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
- [Kubernetes: Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/): read before Day 3.

## Key takeaways

- Every local tool has a production twin; learning the tool is learning the concept.
- AI dependencies are large and tightly version-coupled. Pin everything; record versions in the artifact; build environments from files, never by hand.
- Three isolation levels: venv for packages, container for the userland, cluster for scheduling and limits. Kernel and GPU driver always leak through.
- A model image is pinned runtime + dependencies layer + code + artifact + non-root user + serve-only entrypoint. Bake small artifacts; mount large weights.
- Dependencies dominate small-model images; weights dominate LLM images. Plan disk and pulls in gigabytes.
- Measure startup cold, in the container. It is import + load + warm-up, and it drives probes, rollouts and autoscaling.

## Checkpoint

Do not move on to Day 3 until you can, without notes:

- Run the verification script with zero failures and explain what each ❌ would have meant.
- Create and delete a kind cluster and explain what it does and does not share with a cloud cluster.
- Read the Dockerfile aloud and justify every instruction.
- Name the three largest layers of `pod-health:v1` and their approximate sizes.
- State the container's cold startup time and where it goes.
- Explain when weights belong in the image and when they do not.

Next: [Day 3 — The AI Production Stack](./03-ai-production-stack.md), where you run this image on Kubernetes with resource limits, watch it get OOMKilled, and walk the full production architecture layer by layer. Back to the [Phase 00 overview](./index.md).
