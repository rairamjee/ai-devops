# Day 3 — The AI Production Stack

> Today you walk the entire architecture this course converges on, layer by layer: what each layer does, what you own, what breaks, and which signal tells you. Then you run yesterday's container on Kubernetes with resource limits and a hardened security context, watch it die of memory starvation on purpose, and diagnose it the way you will diagnose real incidents.

**Time:** about 3 hours. Roughly 75 minutes reading (this is the densest lesson in Phase 00; take it in two sittings if you need to), 60 minutes in the lab, 30 minutes on the quiz and exercise.

## Learning objectives

By the end of this lesson you can:

- Draw the master architecture from memory and describe every layer in one sentence.
- For each layer, name what a DevOps engineer owns, its most common failure mode and the first signal you would look at.
- Trace three flows through the stack: a request going down, a model artifact coming in, and money going out.
- Explain what an inference server does and why "just run the Python script" stops working at scale.
- Choose between a Job and a Deployment for a model workload and justify it.
- Calculate a memory request for an AI container instead of guessing it, and explain requests versus limits, QoS classes and `OOMKilled`.
- Run a model container as a Kubernetes Job with resource limits and a restricted security context, and diagnose a container that is killed before it logs a single line.

## Prerequisites

- [Day 1](./01-what-is-ai.md) and [Day 2](./02-environment-setup.md) completed: you have `pod-health:v1` built and loaded into a kind cluster named `ai-devops-lab`.
- Working knowledge of Kubernetes basics: pods, Deployments, `kubectl get/describe/logs`. If Jobs, resource requests or `securityContext` are new to you, the lesson explains them as it goes.

## Concept explanation

### 1. The master architecture

This is the diagram the whole course builds toward. Every later phase fills in one or two boxes. Today you learn what each box is for and how they connect; by Phase 17 you will have built all of them.

```text
                         USERS
                           │
                           ▼
                    API / GATEWAY
                           │
                           ▼
                    AI APPLICATION
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
            RAG          AGENTS        TOOLS
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                    MODEL / LLM
                           │
                           ▼
                   INFERENCE SERVER
                           │
                           ▼
                    CPU / GPU LAYER
                           │
                           ▼
                      KUBERNETES
                           │
            ┌──────────────┼──────────────┐
            │              │              │
          NETWORK        STORAGE       COMPUTE
            │              │              │
            └──────────────┼──────────────┘
                           │
                    OBSERVABILITY
                           │
                 ┌─────────┼─────────┐
                 │         │         │
               Metrics    Logs     Traces
                           │
                     SECURITY
                           │
                       CI/CD
                           │
                        IaC
                           │
                        COST
```

Read it top to bottom as "a request's journey" and bottom to top as "what has to exist for that journey to be possible". The horizontal bands at the bottom (observability, security, CI/CD, IaC, cost) are not layers a request passes through; they are concerns that cut across every box above them.

::: tip Mental model: layers you know, with new values
About eighty percent of this diagram is infrastructure you already operate. The AI-specific boxes are the model, the inference server and the RAG/agents/tools row. Everything else is a gateway, a service, a scheduler, storage, a network and a monitoring stack, with new *values* plugged into old *variables*: bigger artifacts, stricter memory, unusual hardware, slower startups, one more kind of signal to watch. Do not let the vocabulary make the familiar parts feel foreign.
:::

### 2. Layer by layer

One row per box. For each: what it does, what you own, the failure you will meet most often, and the first signal to look at. Later phases expand every row into lessons.

| Layer | What it does | You own | Most common failure | First signal | Phase |
|---|---|---|---|---|---|
| **Users** | Humans or systems sending requests | Expectations: SLOs, quotas, fair use | Traffic you did not plan for | Request rate by client | 12, 16 |
| **API / Gateway** | TLS, auth, rate limits, routing, timeouts | All of it | Timeouts too short for streaming; rate limits that page instead of shed | 4xx/5xx by route; timeout count | 07 |
| **AI Application** | Builds prompts, orchestrates calls, validates output, meters tokens | Deploy, config, secrets, scaling | Prompt too long for the context window; malformed model output; unbounded retries | Error rate; tokens per request; retry count | 07, 11 |
| **RAG** | Fetches your documents to ground the model's answer | The pipeline, the database, index freshness | Retrieval misses; stale index; slow vector queries | Retrieval latency; hit rate; index age | 08 |
| **Agents** | Lets the model plan multi-step work and call tools | Permissions, approval gates, step and budget limits, audit log | Loops; privilege creep; acting on injected instructions | Steps per task; blocked actions; audit anomalies | 09, 15 |
| **Tools** | The concrete actions an agent can take (read logs, query metrics, run a command) | Least privilege, input validation, sandboxing | A read-only tool that is not; unvalidated arguments | Tool error rate; denied calls | 09, 15 |
| **Model / LLM** | The artifact: learned weights plus a configuration | Version, checksum, storage, provenance | Wrong version deployed; silent quality decay | Model version in every log line; quality evaluations | 01–06, 10, 11 |
| **Inference server** | Loads the model, batches requests, manages GPU memory, streams tokens, exposes an API | Sizing, configuration, scaling, upgrades | GPU OOM under load; startup longer than probes allow; low utilisation | Queue depth; tokens per second; GPU memory | 06, 13, 14 |
| **CPU / GPU layer** | The hardware the numbers live in; drivers and runtimes | Node images, driver versions, capacity | Driver/runtime version mismatch; unschedulable GPU requests | `nvidia-smi`; allocatable vs requested GPUs | 13 |
| **Kubernetes** | Schedules and supervises all of the above | Everything you own today, plus GPU scheduling | Pending pods; `OOMKilled`; image pull time; rollouts stuck on slow startups | Pod phase and reason; events | 14 |
| **Network** | Ingress, service mesh, egress to model vendors, east-west to databases | Policies, timeouts, bandwidth | Streaming broken by an idle timeout; egress blocked; bandwidth saturated by weight downloads | Connection duration; egress errors; throughput | 14, 15 |
| **Storage** | Model weights, datasets, vector indexes, caches, logs | Classes, capacity, caching strategy | Weights pulled from the internet on every start; node disk pressure from images | Startup time; disk usage per node | 14 |
| **Compute** | Node pools: CPU pools for apps, GPU pools for models | Pools, taints, autoscaling, cost | Wrong workload on expensive nodes; no capacity for spikes | Utilisation by pool; pending pods by reason | 13, 14, 16 |
| **Observability** | Metrics, logs, traces plus the AI signals | Instrumentation, dashboards, alerts, SLOs | Dashboards green while answers are wrong | Quality metrics; token and cost metrics | 12 |
| **Security** | IAM, RBAC, secrets, network policy, supply chain plus prompt injection, tool abuse | Controls at every layer | Agent with too much power; secrets in prompts or logs | Denied actions; audit log | 15 |
| **CI/CD** | Three pipelines: code, model, prompt | Gates, tests, promotion, rollback for all three | Prompt change shipped with no evaluation; model promoted without a gate | Evaluation results per change | 10, 11 |
| **IaC** | Clusters, node pools, GPUs, storage, networking as code | All of it | Hand-built GPU nodes nobody can reproduce | Drift between code and reality | 13, 14 |
| **Cost** | GPU hours, tokens, storage, egress | Attribution, budgets, optimisation | GPU at 15% utilisation; unbounded token spend | Cost per request; utilisation | 16 |

Most of those rows should look familiar. Four of them deserve a closer look today because they are where AI is genuinely different.

#### The AI application is not thin

It is tempting to picture the application layer as a proxy that forwards a question to a model. In practice it holds the prompts (which are code, and change behaviour when edited), decides what context to fetch, calls tools, validates and repairs the model's output, enforces token budgets, and records what happened. When something goes wrong in an LLM feature, this layer is where most of the fixes land and most of the evidence lives. Phases 07 and 11 are about running it properly.

#### The inference server is a real piece of infrastructure

On Day 1 you ran a model with a Python script. Why does production need a dedicated server in front of the model? Because at scale the script would have to:

- **Load the model once** and keep it in GPU memory across thousands of requests, not per process.
- **Batch** many concurrent requests into single passes over the weights, and for LLMs do *continuous* batching: add and remove requests mid-generation as they arrive and finish.
- **Manage GPU memory** for every in-flight request's working state (the KV cache from Phase 06), and refuse or queue work when it is full rather than crash.
- **Stream** tokens back over HTTP as they are produced.
- **Expose a stable API**, health and readiness endpoints, and metrics.
- **Spread one model across several GPUs** when it does not fit in one.

That is an inference server. vLLM is the one this course uses (Phase 14), after Phase 06 has taught you what it is doing, so you can evaluate the alternatives.

#### The CPU/GPU layer has a version matrix

A GPU workload touches four things that must agree: the kernel driver on the node, the CUDA runtime libraries inside the container, the framework build (PyTorch compiled for a specific CUDA version) and the container runtime hook that exposes the device. Get one wrong and the model falls back to CPU silently or fails to start loudly. Phase 13 gives you the matrix and the diagnostic sequence. Today, know that "it has a GPU" is the start of a conversation, not the end.

#### Storage decides startup time

Where the weights live decides how long a pod takes to become ready: an object store across the internet (minutes), a registry as part of the image (minutes, and every code change re-ships the weights), a node-local cache or persistent volume (seconds). Day 2's bake-or-mount question is a storage question, and Phase 14 builds the caching layer.

### 3. Three flows through the stack

A request goes **down**. A model comes **in** from the side. Money goes **out** at every layer. Keeping the three flows separate in your head makes incidents much easier to reason about.

#### The request flow

Day 1 traced one request's latency budget. Here is the same request mapped onto the layers, with the question each layer must answer in under a few milliseconds before passing it on:

```text
Users ──► Gateway: who are you, are you allowed, are you over quota?
            └─► Application: what is the prompt, what context do I need, which model?
                  ├─► RAG: which documents are relevant?           (a database query)
                  ├─► Agents/Tools: does the model need to act?   (a policy check)
                  └─► Inference server: is there room in the batch? (a queue)
                        └─► Model on GPU: prefill, then decode token by token
                              └─► back up the stack: validate, meter, log, stream to the user
```

Every arrow is a place to add a timeout, a metric and a failure mode. Phase 12 instruments all of them.

#### The model flow

The artifact enters from the side and moves through storage tiers toward the GPU:

```text
Training infrastructure ──► Evaluation gate ──► Model registry (version, checksum, metadata)
      │                                                  │
      └── (Phase 10 automates this) ─────────────────────┘
                                                         ▼
                                     Object storage (the durable copy)
                                                         ▼
                                     Node cache / persistent volume (the fast copy)
                                                         ▼
                                     Inference server memory (the running copy)
```

Every tier is a place a version can go wrong. The checksum you generated on Day 1 is what lets you verify the running copy is the registered one. Today's lab bakes the model into the image, which collapses the storage tiers into one for a 6 MB artifact.

#### The money flow

```text
Users            → tokens consumed (if you pay a vendor per token)
Gateway/App      → ordinary compute; small
RAG              → database instances; embedding calls
Inference server → GPU hours: the dominant line for self-hosted models
GPU nodes        → paid whether busy or idle → utilisation is the lever
Storage          → weights, indexes, logs; bandwidth for pulling weights
Network          → egress to vendors; cross-zone traffic
```

The cost stack is Phase 16, but the habit starts today: whenever you add a component, ask what it costs when idle and what it costs per request.

### 4. Jobs versus Deployments: the shapes of model workloads

Not every model workload is a long-running service. Matching the Kubernetes primitive to the workload's shape is the first design decision in every later phase.

| Workload | Shape | Kubernetes primitive | Restart policy | Scaling signal | Course example |
|---|---|---|---|---|---|
| Online inference | Long-running, latency-sensitive, many requests | Deployment + Service (+ HPA) | Always | Queue depth, latency, GPU utilisation | Projects 3, 7 |
| Batch inference | Run to completion over a dataset | Job or CronJob | Never / OnFailure | Parallelism | Today's lab |
| Training | Run to completion, resource-hungry, long | Job (often via a workflow engine) | Never / OnFailure | None; size the job | Phase 05 |
| Pipeline step | Short, ordered, reproducible | Job, orchestrated | Never | None | Phase 10 |
| Embedding refresh | Periodic bulk work | CronJob | OnFailure | Parallelism | Phase 08 |

Today's container loads a model, predicts five rows and exits. That is a **Job**: Kubernetes runs it to completion, records success or failure, and does not restart a finished pod. Phase 01 turns the same model into an HTTP service, and the primitive becomes a Deployment. Everything you learn today about resources, security context and diagnosis applies to both.

### 5. Resource requests for AI workloads are calculated, not observed

For a typical web service you set memory requests by watching a graph for a week. For a model container, you can and should compute the number before the first deploy, because most of it is fixed by arithmetic you already know from Day 1:

```text
memory needed  ≈  runtime baseline            (interpreter + libraries, before any model)
               +  model weights               (parameters × bytes per parameter)
               +  per-request working memory  × expected concurrency
               +  headroom                    (20–30%)
```

For today's container, measured in the lab:

| Component | Measured | Note |
|---|---|---|
| Python + NumPy + scikit-learn imported | ~120–140 MiB | The runtime baseline dominates for a tiny model |
| Model weights (random forest) | ~6 MiB on disk, ~8 MiB in memory | Negligible here; the opposite for an LLM |
| Per-request working memory | under 1 MiB | Five predictions did not move the needle |
| **Peak resident memory** | **~134 MiB in a venv, ~148 MiB in the container** | Measured with `resource.getrusage` and `docker stats` |

That is why the lab's Job requests 192 MiB and limits at 384 MiB: comfortably above the measured peak, with headroom, and why a 32 MiB limit kills the process while it is still importing libraries.

For a 7-billion-parameter LLM in fp16 the same formula gives roughly 14 GB of weights, 1–2 GB of runtime, and hundreds of MB to gigabytes of working memory *per concurrent request*. Nobody observes their way to that number; they compute it, then measure to confirm. Phases 06 and 13 fill in the per-request term.

#### Requests, limits, QoS and what `OOMKilled` actually is

- A **request** is what the scheduler reserves for you on a node. It decides *where* the pod can run. Requesting too little lets the scheduler pack pods onto a node that cannot actually hold them all.
- A **limit** is the ceiling the Linux kernel enforces through cgroups. Exceed the memory limit and the kernel's out-of-memory killer terminates the process with signal 9. The container exits with code **137** (128 + 9), and Kubernetes records the reason **`OOMKilled`**.
- **QoS class** follows from the two numbers: requests equal to limits for every container gives `Guaranteed` (last to be evicted under node pressure); requests below limits gives `Burstable`; no requests or limits gives `BestEffort` (first to go). Today's Job is Burstable. GPU inference servers are usually run Guaranteed, because a model server that gets evicted takes minutes to come back.
- `OOMKilled` is **not** the same as **eviction**. `OOMKilled` means *this container* exceeded *its own* limit. Eviction means the *node* ran short and the kubelet removed pods to recover, starting with BestEffort. Both show up in `kubectl describe`; they have different fixes.

One consequence matters for every AI workload you will ever run: **an `OOMKilled` container that died during startup produces no logs.** The process was killed while importing libraries or loading weights, before it printed anything. Silence in `kubectl logs` combined with exit code 137 in `kubectl describe` is the signature. You will produce it deliberately in the lab.

### 6. Common misconceptions

- **"A GPU pod is just a pod with an extra resource."** The resource is not divisible by default (one GPU per container, whole), the node needs a device plugin to advertise it, the image needs matching CUDA libraries, and startup involves loading gigabytes into device memory. Phases 13 and 14.
- **"`OOMKilled` means the application has a memory leak."** Sometimes. Far more often for model workloads it means the limit was copied from a smaller model, or the working memory per request was never counted. Calculate before you debug.
- **"Requests should equal limits, always."** For GPU inference servers, yes, run Guaranteed. For CPU application pods, a gap lets you pack nodes more efficiently. Know the trade-off you are making.
- **"No logs means it never ran."** It ran and was killed before it could print. Read `describe` and events before concluding anything from an empty log.
- **"kind is production."** Same API, same manifests, same failure modes for scheduling and resources. Not the same networking, storage, GPUs or scale. Learn on kind; verify on the real thing.
- **"The inference server is an implementation detail."** It is the single most important operational component of a self-hosted model and the place most tuning happens.

## Why does a DevOps Engineer need to know this?

Because this diagram is the job description for every role this course prepares you for. Whether the title is MLOps, LLMOps, AI Platform, AI Infrastructure or AI SRE, the work is owning some or all of these layers for AI workloads. Here is where your existing skills land:

| You already know | It becomes |
|---|---|
| Ingress, API gateways, rate limiting | The gateway layer, plus streaming-aware timeouts and token quotas |
| Deploying and scaling stateless services | The application layer, plus prompt and model version tracking |
| Running databases | RAG's vector store, index freshness, embedding refresh |
| Kubernetes scheduling, requests and limits | GPU scheduling, calculated memory, Guaranteed QoS for model servers |
| Storage classes and volumes | Weight caching and startup time |
| Prometheus, Grafana, tracing | The same tools with AI signals added |
| RBAC, secrets, network policy | The same controls, extended to agents and tools |
| CI/CD pipelines | Three pipelines: code, model, prompt |
| Terraform | GPU node pools you can actually reproduce |
| Cost allocation | GPU utilisation and cost per token |

### Real-world scenario: the p95 alert

An alert fires: p95 latency on the internal LLM API has gone from 1.8 s to 6 s. Walk the stack.

1. **Gateway:** error rate flat, request rate flat. Not a traffic spike. Move down.
2. **Application:** no new deploy in the last 24 hours according to the deployment history. Error rate flat. But the *tokens per request* panel shows prompt tokens have doubled since 14:10.
3. **RAG:** retrieval latency flat. Hit rate flat. Not the database.
4. **Inference server:** queue depth is up fivefold. Tokens per second per GPU are down. GPU memory is at 96%.
5. **GPU layer:** utilisation is high, memory nearly full, no errors. The hardware is fine; it is saturated.
6. **Cause:** at 14:05 someone edited a prompt template in a config map to include a much longer set of instructions. No code deploy, so it did not show in deployment history. Longer prompts mean more working memory per request, fewer requests fit in a batch, the queue grows, latency doubles and doubles again.
7. **Fix:** roll the config map back. Latency recovers in two minutes.
8. **Follow-up:** prompts are code. Put them in version control with an evaluation gate (Phase 11), and add an alert on prompt tokens per request (Phase 12).

Every step used one layer's "first signal" from the table. That is the point of the table.

## Architecture

The same diagram, annotated with where in the course you build each part:

```text
USERS ─────────────────── SLOs, quotas ───────────────────── Phase 12, 16
API / GATEWAY ─────────── Project 3 ──────────────────────── Phase 07
AI APPLICATION ────────── Projects 3–6 ───────────────────── Phase 07, 11
RAG · AGENTS · TOOLS ──── Projects 4, 5 ──────────────────── Phase 08, 09
MODEL / LLM ───────────── every project ──────────────────── Phase 01–06, 10
INFERENCE SERVER ──────── Project 7 (vLLM) ───────────────── Phase 06, 14
CPU / GPU LAYER ───────── Project 7 ──────────────────────── Phase 13
KUBERNETES ────────────── today, then everything ─────────── Phase 14
NETWORK · STORAGE · COMPUTE ── Project 7 ─────────────────── Phase 13, 14
OBSERVABILITY ─────────── Observable AI service ──────────── Phase 12
SECURITY ──────────────── Threat model + hardening ───────── Phase 15
CI/CD ─────────────────── Projects 2, 6 ──────────────────── Phase 10, 11
IaC ───────────────────── Project 7 ──────────────────────── Phase 13, 14
COST ──────────────────── Cost dashboard + report ────────── Phase 16
AI-SRE PLATFORM ───────── Project 8: all of the above ────── Phase 17
```

## Hands-on lab 0.3 — Run the model on Kubernetes and break it {#hands-on-lab-0-3-run-the-model-on-kubernetes}

**Objective:** run the Day 2 image as a Kubernetes Job with calculated resource limits and a restricted security context; then run the same image with a limit that is too small, watch it get `OOMKilled` before it logs anything, and diagnose it from pod status, `describe` and events.

**Difficulty:** 🟡 Intermediate · **Estimated time:** 45–60 minutes.

**Prerequisites:** Day 2 completed: `pod-health:v1` built and loaded into the kind cluster `ai-devops-lab`, and `kubectl` pointed at context `kind-ai-devops-lab`.

**Architecture:**

```text
pod-health:v1 (on the kind node)
      │
      ├── job.yaml       requests 192Mi / limits 384Mi ──► pod runs, predicts, Completed (exit 0)
      │
      └── job-oom.yaml   limits 32Mi ─────────────────────► pod killed during import, OOMKilled (exit 137)
                                                             Job retries once, then Failed (BackoffLimitExceeded)
```

**Environment requirements:** the Day 2 kind cluster. CPU only. No cloud resources, no credentials.

### Setup

```bash
cd ai-devops/examples/kubernetes/00-orientation/lab-03-model-job
kubectl config use-context kind-ai-devops-lab
kubectl get nodes
```

Confirm the image is on the node. kind nodes are containers running containerd; `crictl` is containerd's CLI:

```bash
docker exec ai-devops-lab-control-plane crictl images | grep pod-health
```

If nothing is listed, go back to Day 2 Step 9 (`kind load docker-image pod-health:v1 --name ai-devops-lab`).

### Steps

**Step 1. Read `job.yaml`.** Every field is there for a reason; match them to this table before applying anything.

| Field | Value | Why |
|---|---|---|
| `kind: Job` | | Run to completion; do not restart a finished pod |
| `backoffLimit: 1` | | Retry once, then give up. A model that cannot load will not fix itself by retrying forever |
| `ttlSecondsAfterFinished: 600` | | Clean up finished pods after 10 minutes so the namespace stays tidy |
| `restartPolicy: Never` | | Let the Job controller decide about retries, not the kubelet |
| `imagePullPolicy: Never` | | kind has the image locally and no registry; in a real cluster this is a registry path with an immutable tag or digest |
| `env: MODEL_PATH` | `/model/pod-health-model-v1.joblib` | Where the Dockerfile put the artifact; configuration, not code |
| `resources.requests.memory` | `192Mi` | Above the measured ~150 MiB peak; what the scheduler reserves |
| `resources.limits.memory` | `384Mi` | The kernel-enforced ceiling with headroom |
| `runAsNonRoot: true` | | Refuse to start as root, whatever the image says |
| `allowPrivilegeEscalation: false` | | No setuid tricks |
| `readOnlyRootFilesystem: true` | | The container only reads its model and writes to stdout |
| `capabilities.drop: ["ALL"]` | | Serving a model needs no Linux capabilities |

**Step 2. Run the healthy Job.**

```bash
kubectl apply -f job.yaml
kubectl wait --for=condition=complete job/pod-health-predict --timeout=120s
kubectl get pods -l job-name=pod-health-predict
kubectl logs job/pod-health-predict
```

**Step 3. Read the pod's timeline.** The events show the lifecycle Kubernetes drove; the timestamps show how long it took.

```bash
kubectl get events --sort-by=.lastTimestamp | grep pod-health-predict-
kubectl get pod -l job-name=pod-health-predict \
  -o jsonpath='{range .items[*]}created={.metadata.creationTimestamp} started={.status.containerStatuses[0].state.terminated.startedAt} finished={.status.containerStatuses[0].state.terminated.finishedAt} exit={.status.containerStatuses[0].state.terminated.exitCode}{"\n"}{end}'
kubectl get pod -l job-name=pod-health-predict -o jsonpath='{.items[0].status.qosClass}{"\n"}'
```

**Step 4. Read `job-oom.yaml`.** It is identical to `job.yaml` except for one number. Find it before you apply it.

**Step 5. Run the broken Job and watch it fail.**

```bash
kubectl apply -f job-oom.yaml
kubectl get pods -l scenario=oom -w
```

Press Ctrl-C once you see `OOMKilled`. Then diagnose exactly as you would in production, in this order:

```bash
kubectl describe pod -l scenario=oom | grep -A8 "State:"
kubectl logs -l scenario=oom
kubectl get events --sort-by=.lastTimestamp | grep oom
```

**Step 6. Watch the Job give up.** With `backoffLimit: 1`, the controller creates a second pod, which also dies, and then marks the Job failed.

```bash
kubectl get pods -l scenario=oom
kubectl get job pod-health-predict-oom -o jsonpath='conditions={.status.conditions[*].type} reason={.status.conditions[*].reason} failed={.status.failed}{"\n"}'
kubectl describe job pod-health-predict-oom | grep -A5 "^Events"
```

**Step 7. Fix it.** A Job's pod template is immutable, so you cannot patch the limit in place; you delete and re-create with a corrected manifest, which is what a real rollout of a fixed manifest does too.

```bash
kubectl delete -f job-oom.yaml
sed 's/32Mi/256Mi/' job-oom.yaml | kubectl apply -f -
kubectl wait --for=condition=complete job/pod-health-predict-oom --timeout=120s
kubectl logs job/pod-health-predict-oom
```

**Step 8. Try to reproduce it with Docker alone**, and notice that you cannot, at least not the same way:

```bash
docker run --rm --memory=64m pod-health:v1
```

It completes, just more slowly. Docker's `--memory` allows the container to use swap up to the same amount again by default, so a process that would be killed under a Kubernetes limit merely slows down under Docker's. Add `--memory-swap=64m` to make the two behave alike. The lesson: **a memory limit is only as strict as the runtime enforcing it.** Kubernetes disables swap for pods by default; your laptop's Docker does not.

### Expected output

The healthy Job:

```text
$ kubectl apply -f job.yaml
job.batch/pod-health-predict created
$ kubectl wait --for=condition=complete job/pod-health-predict --timeout=120s
job.batch/pod-health-predict condition met
$ kubectl get pods -l job-name=pod-health-predict
NAME                       READY   STATUS      RESTARTS   AGE
pod-health-predict-fk5h5   0/1     Completed   0          4s
$ kubectl logs job/pod-health-predict
[startup]   imports 195 ms, artifact load 696 ms  (model v1, 6,370 KB)
[predict]   pod                  prediction  p(unhealthy)   latency
            api-7d9f-abcde       healthy             0.00   28.20ms
            worker-5c4b-fghij    UNHEALTHY           1.00   27.69ms
            cache-6b8a-klmno     UNHEALTHY           0.99   28.99ms
            ingest-9e2d-pqrst    UNHEALTHY           0.84   33.07ms
            batch-3a1c-uvwxy     UNHEALTHY           1.00   28.41ms
[done]      5 predictions in 147 ms; process total 1038 ms
```

Its timeline and QoS class:

```text
created=...T20:06:04Z started=...T20:06:04Z finished=...T20:06:06Z exit=0
Burstable

4s   Normal   Scheduled          Successfully assigned default/pod-health-predict-fk5h5 to ai-devops-lab-control-plane
4s   Normal   Pulled             Container image "pod-health:v1" already present on machine
4s   Normal   Created            Container created
4s   Normal   Started            Container started
```

The broken Job:

```text
$ kubectl get pods -l scenario=oom
NAME                           READY   STATUS      RESTARTS   AGE
pod-health-predict-oom-7xqmv   0/1     OOMKilled   0          2s

$ kubectl describe pod -l scenario=oom | grep -A8 "State:"
    State:          Terminated
      Reason:       OOMKilled
      Exit Code:    137
      Started:      Sun, 06 Sep 2026 01:36:09 +0530
      Finished:     Sun, 06 Sep 2026 01:36:09 +0530
    Ready:          False
    Restart Count:  0
    Limits:
      memory:  32Mi

$ kubectl logs -l scenario=oom
(nothing)

$ kubectl get job pod-health-predict-oom -o jsonpath=...
conditions=FailureTarget Failed reason=BackoffLimitExceeded failed=2

  Warning  BackoffLimitExceeded  75s   job-controller  Job has reached the specified backoff limit
```

Read it as an operator:

- **Two seconds from created to finished** for the healthy pod, of which about one second was the process itself. Scheduling, container creation and teardown are the rest. For a real model server, add image pull time and weight loading on top, and that is your rollout speed.
- **`Burstable`** because requests and limits differ. Ask yourself what would change if you set them equal.
- **The OOM pod started and finished in the same second.** It was killed while Python was still importing NumPy and scikit-learn, before `predict.py` reached its first `print`. That is why the logs are empty.
- **`Exit Code: 137`** is 128 + 9: the process received `SIGKILL` from the kernel's OOM killer. You will see this code for the rest of your career; it almost always means a memory limit.
- **The Job tried twice and gave up** because `backoffLimit: 1`. Without that field it would retry with exponential backoff for a long time, burning scheduler and node time on a pod that can never succeed.
- **The diagnostic order was status → describe → logs → events.** For a container killed at startup, logs are the *least* informative of the four. Start with `describe`.

### Validation

You have completed the lab when:

- [ ] `pod-health-predict` completed and you can quote its startup breakdown from the logs.
- [ ] You can state the pod's QoS class and explain why.
- [ ] `pod-health-predict-oom` produced two `OOMKilled` pods with exit code 137 and empty logs, and the Job reports `BackoffLimitExceeded`.
- [ ] You fixed the limit by re-creating the Job and it completed.
- [ ] You can explain why `docker run --memory=64m` did not kill the same process.
- [ ] You can compute, from the measured peak of ~150 MiB, why 192Mi/384Mi were chosen.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `CreateContainerConfigError` with event `container has runAsNonRoot and image has non-numeric user (app)` | The image's `USER` is a name, not a UID; the kubelet cannot verify a name is non-root | Rebuild with `USER 10001` (the Day 2 Dockerfile does this), or add `runAsUser: 10001` to the pod's `securityContext`. The first draft of this course's Dockerfile hit exactly this. |
| `ErrImageNeverPull` | `imagePullPolicy: Never` and the image is not on the node | `kind load docker-image pod-health:v1 --name ai-devops-lab`; confirm with `crictl images` |
| Pod stays `Pending` | Requests exceed what the single kind node can offer, or a typo in resources | `kubectl describe pod` and read the `FailedScheduling` event; lower requests or check units (`Mi` not `M`) |
| `kubectl wait` times out but the pod shows `Completed` | You waited on the wrong Job name or context | `kubectl get jobs`; `kubectl config current-context` |
| Pods disappear before you can inspect them | `ttlSecondsAfterFinished` cleaned up a finished Job | Raise the TTL in the manifest, or inspect sooner; in production, ship logs and events somewhere durable |
| `field is immutable` on `kubectl apply` after editing a Job | Job pod templates cannot be changed in place | `kubectl delete -f`, then `apply` the edited manifest |
| `kubectl logs` says `is waiting to start` | The container never started (config error or pull error) | `kubectl describe pod`: the reason is in the container state and events |
| Exit code 137 but `Reason` is not `OOMKilled` | The process was SIGKILLed for another reason, or the node evicted it | Check `kubectl describe node` for memory pressure and the pod events for `Evicted` |
| `docker exec ... crictl` command not found | Older kind node image | Use `docker exec ai-devops-lab-control-plane ctr -n k8s.io images ls` instead |

### Common mistakes

- **Copying resource requests from a different model.** The whole point of the formula is that the numbers come from *this* model's parameters, precision and concurrency.
- **Setting no limits "so it cannot be OOMKilled".** Then the node runs out of memory instead, and the kubelet evicts pods, possibly including ones that were behaving. A limit turns an unbounded node problem into a bounded pod problem.
- **Reading only the logs.** Empty logs plus a dead pod is a `describe` situation.
- **Deleting the pod by hand to "retry".** The Job controller recreates it; you have changed nothing. Fix the manifest.
- **Leaving `backoffLimit` at its default for model workloads.** Startup failures in model containers are rarely transient; retrying six times wastes minutes of node time per attempt.
- **Using a mutable image tag.** `pod-health:v1` is fine locally. In a registry, `latest` or a reused tag means you cannot tell which model is running.

### Cleanup

```bash
kubectl delete -f job.yaml -f job-oom.yaml --ignore-not-found
```

Keep the cluster and the images: Phase 01 deploys a service to this cluster. If you need the disk back:

```bash
kind delete cluster --name ai-devops-lab
docker rmi pod-health:v1 pod-health:v2
```

### Extension challenge

1. **Find the floor.** Bisect the memory limit (64Mi, 96Mi, 128Mi, 160Mi) to find the smallest value at which the Job completes. Compare it with the ~150 MiB measured peak, and explain any difference (hint: the kernel counts page cache and the kubelet's own accounting differently from `ru_maxrss`).
2. **Go Guaranteed.** Set requests equal to limits, re-run, and check the QoS class. Then read the Kubernetes documentation on eviction order and write two sentences on when you would want this for a model server.
3. **Make it a CronJob** that runs every minute, and watch three successive completions. Then imagine the model was 14 GB: what would you change about where the weights come from?

### Questions

1. In which layer of the master architecture did today's Job run, and which layers did it not touch at all?
2. Why did the OOM pod produce no logs, and what does that imply about how you should alert on model-server startup failures?
3. If the same image were a Deployment with `restartPolicy: Always` and a 32Mi limit, what would you see in `kubectl get pods`, and what is that state called?

## Exercise

1. **Draw the stack.** From memory, draw the master architecture and annotate each box with what you own and its first signal. Compare with the table. Note which boxes you got wrong or forgot; those are the phases to pay most attention to.
2. **Calculate a memory request** for an inference server running a 7-billion-parameter model in fp16 with a 2 GB runtime baseline, 8 concurrent requests, and about 600 MB of working memory per request. Add 25% headroom. Then say which of these GPU memory sizes you would need: 24 GB, 40 GB, 80 GB. Show your arithmetic.
3. **Map three incidents.** Take three real incidents from your own experience (or three from any public post-mortem you have read) and place each on a layer of the diagram. For each, name the first signal that would have shown it.
4. **Sketch the Deployment.** Without writing YAML, list every field you would change or add to turn `job.yaml` into a Deployment serving the model over HTTP: restart policy, replicas, probes, a Service, and what each probe should actually check for a model server.
5. **Journal.** Write the three flows (request, model, money) in your own words, one paragraph each.

## Quiz

**1. Which parts of the master architecture are genuinely new for a DevOps engineer, and which are familiar infrastructure with new values?**

::: details Answer
New: the model, the inference server, and the RAG/agents/tools row. Familiar with new values: gateway, application, Kubernetes, network, storage, compute, observability, security, CI/CD, IaC, cost.
:::

**2. What does an inference server do that a Python script calling the model cannot do well?**

::: details Answer
Keep the model loaded once across many requests, batch concurrent requests (continuously, for LLMs), manage GPU memory for in-flight requests, stream tokens, expose a stable API with health and metrics, and spread a model across GPUs.
:::

**3. A request's p95 latency triples with no deploy and no traffic change. Name three layers whose first signal you would check and what you would look for.**

::: details Answer
Application: tokens per request (a longer prompt). Inference server: queue depth, tokens per second and GPU memory (saturation). RAG: retrieval latency (a slow database). Any of these can triple latency without an error.
:::

**4. Job or Deployment: nightly scoring of a million records? An LLM chat API? A training run?**

::: details Answer
Job or CronJob; Deployment with a Service; Job (usually via a workflow engine).
:::

**5. Write the memory formula for an AI container.**

::: details Answer
Runtime baseline + model weights (parameters × bytes per parameter) + per-request working memory × concurrency + 20–30% headroom.
:::

**6. What is the difference between a memory request and a memory limit?**

::: details Answer
The request is what the scheduler reserves when placing the pod; the limit is the ceiling the kernel enforces via cgroups. Exceeding the limit gets the process killed; a request that is too low lets the scheduler overcommit the node.
:::

**7. Why does an `OOMKilled` model container often have empty logs?**

::: details Answer
It was killed during startup, while importing libraries or loading weights, before the application printed anything. Diagnose from `describe` (exit code 137, reason OOMKilled) and events, not logs.
:::

**8. What does exit code 137 mean?**

::: details Answer
128 + 9: the process was terminated by signal 9 (SIGKILL), in this case sent by the kernel's out-of-memory killer when the container exceeded its memory limit.
:::

**9. Why did `docker run --memory=64m` not kill a process that a 32Mi Kubernetes limit killed?**

::: details Answer
Docker's `--memory` permits swap up to the same amount again by default, so the process slowed down instead of dying. Kubernetes disables swap for pods by default. A limit is only as strict as the runtime enforcing it.
:::

**10. Why set `backoffLimit: 1` on a model Job?**

::: details Answer
Model startup failures (cannot load weights, out of memory) are not transient. Retrying repeatedly wastes node time and delays the failure signal. Fail fast, alert, fix the manifest.
:::

**11. What QoS class does a pod get when requests equal limits, and why does that matter for an inference server?**

::: details Answer
Guaranteed. It is the last class evicted under node memory pressure, which matters because a model server takes minutes to reload its weights after being evicted.
:::

**12. Name the three flows through the stack and one thing that can go wrong in each.**

::: details Answer
Request flow (a timeout or queue at any arrow), model flow (a wrong version at any storage tier, caught by checksums), money flow (idle GPUs or unbounded token spend).
:::

## Interview questions

1. **"Draw the architecture of a production LLM application and tell me what you would own."** Draw the master diagram from the gateway down to the GPU and across the observability, security, CI/CD, IaC and cost bands. Say that you own everything except the model's contents, and name the two or three boxes where AI changes the work most: the inference server, GPU scheduling, and quality observability.
2. **"What does an inference server do, and why not just wrap the model in Flask?"** Loaded-once weights, continuous batching, GPU memory management, streaming, stable API, multi-GPU. Flask can serve a small classifier; it cannot keep a GPU busy or survive concurrency.
3. **"How do you set memory requests for a model container?"** Compute it: runtime baseline + weights + per-request working memory × concurrency + headroom; then measure the cold peak to confirm. Mention Guaranteed QoS for model servers.
4. **"A model pod is `OOMKilled` at startup with no logs. Walk me through the diagnosis."** `describe` for exit code 137 and reason; events for the timeline; compare the limit with the computed requirement; check whether the image or model version changed; fix the manifest, not the pod.
5. **"Job or Deployment for model workloads, and why?"** Run-to-completion work (batch inference, training, pipeline steps) is a Job; online inference is a Deployment with a Service and autoscaling on queue depth or latency, not CPU.
6. **"What would you monitor at each layer of an AI stack?"** Go down the table: gateway errors and timeouts; tokens per request; retrieval latency and hit rate; queue depth, tokens per second, GPU memory; pod phase and events; startup time; plus quality and cost as cross-cutting signals.
7. **"Latency tripled with no deploy. Where do you look?"** Tell the p95 story: tokens per request, queue depth, GPU memory, then configuration changes that bypass deployment history. Finish with the follow-up: prompts under version control with evaluation gates.
8. **"What is the difference between `OOMKilled` and eviction?"** A container exceeding its own limit versus the node running short and the kubelet removing pods by QoS class. Different signals, different fixes.

## Further exploration

- [Kubernetes: Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/): requests, limits and units.
- [Kubernetes: Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/): Guaranteed, Burstable, BestEffort and eviction order.
- [Kubernetes: Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/): `backoffLimit`, `ttlSecondsAfterFinished`, parallelism.
- [Kubernetes: Configure a Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/): every field used in today's manifests.
- [kind: Loading an image into your cluster](https://kind.sigs.k8s.io/docs/user/quick-start/#loading-an-image-into-your-cluster).
- [vLLM documentation](https://docs.vllm.ai/): skim the introduction only, to see what an inference server's feature list looks like. You will come back in Phase 14.

## Key takeaways

- The master architecture is mostly infrastructure you know; the new boxes are the model, the inference server, and RAG/agents/tools.
- Every layer has an owner, a most common failure and a first signal. Learn the table; it is the incident playbook.
- Three flows: requests go down, models come in from the side, money goes out everywhere. Keep them separate when reasoning.
- An inference server exists to keep weights loaded, batch continuously, manage GPU memory, stream and expose a stable API.
- Run-to-completion work is a Job; online inference is a Deployment. Resources and security context apply to both.
- Memory for AI containers is calculated (runtime + weights + per-request × concurrency + headroom), then measured cold to confirm.
- `OOMKilled` is exit 137 from the kernel's OOM killer when a container exceeds its own limit. It usually leaves no logs. Start with `describe`.
- A limit is only as strict as the runtime enforcing it.

## Checkpoint

Do not move on to Day 4 until you can, without notes:

- Draw the master architecture and give one sentence per layer.
- For any five layers, name what you own, the most common failure and the first signal.
- Explain what an inference server does in four bullet points.
- Write the memory formula and apply it to today's container and to a 7B fp16 model.
- Explain requests versus limits, the three QoS classes, and the difference between `OOMKilled` and eviction.
- Diagnose an `OOMKilled` pod from `describe` and events, and explain why its logs are empty.
- Choose Job or Deployment for a described workload and defend the choice.

Next: [Day 4 — How to Work Through This Course](./04-how-to-learn-and-build-your-portfolio.md), where you set up your learning journal and portfolio repository and learn how to turn every lab into interview material. Back to the [Phase 00 overview](./index.md).
