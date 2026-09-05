# Day 1 — What Is AI?

> By the end of today you will be able to explain AI, machine learning, deep learning and LLMs to a colleague without hand-waving, and you will have trained, saved, reloaded and run a model on your own machine while measuring what every step costs.

**Time:** about 2.5 hours. Roughly 45 minutes reading, 60 minutes in the lab, 30 minutes on the quiz and exercise. Do not skip the lab; the reading only makes sense once you have watched a model load and answer.

## Learning objectives

By the end of this lesson you can:

- Define AI, machine learning, deep learning, generative AI and LLMs, and draw how they nest inside each other.
- Explain, without mathematics, what "learning from data" means and why it produces something different from a program.
- Explain the difference between **training** and **inference**, and say which one production mostly runs.
- Explain that a **model is an artifact**: a file with a size, a version, a checksum and resource requirements.
- Turn a model's parameter count and numeric precision into a memory requirement in your head.
- Describe the three ways a model can reach production and what a DevOps engineer owns in each.
- Describe a basic AI production architecture from the user to the GPU.
- Run a model locally and measure training time, artifact size, load time, single-request latency and batched latency.
- Recognise a model that is up, fast, confident and wrong.

## Prerequisites

- Comfortable in a Linux, macOS or WSL shell: `cd`, `ls`, running scripts, editing files.
- Python 3.10 or newer installed. Check with `python3 --version`. You do not need to know Python well; you will read a commented script, not write one.
- Git installed.
- **No AI knowledge.** Every term below is defined before it is used. If you meet a word you do not know, it is defined further down; keep reading.

## Concept explanation

### 1. Start with what you already know: rules

Every system you have ever operated makes decisions with rules that a human wrote:

```python
if restart_count >= 3 or mem_pct > 92:
    alert("pod unhealthy")
```

This is automation, not AI. A human looked at the problem, decided which signals matter and what the thresholds are, and typed them in. When reality changes, a human edits the rule.

Rules are excellent when the world is simple and stable. They stop working well in three familiar situations:

- **Too many signals.** Restart count, memory, CPU, error rate, latency, request rate, time of day, deploy recency, node pressure. A human cannot write a threshold for every combination, so alerting rules end up either noisy or blind.
- **The right threshold depends on context.** 80% CPU is normal for a batch worker and a crisis for a latency-sensitive API. A nightly traffic dip is fine on Sunday and a symptom on Monday.
- **The world drifts.** Traffic patterns, dependencies and hardware change. Rules written for last year's system quietly become wrong.

Machine learning exists because of those three problems. It is a way to get the rule *from the data* instead of from a person.

### 2. Machine learning: the rule is learned

**Artificial intelligence (AI)** is the broad field of making computers do things that normally need human judgement: recognising, classifying, predicting, deciding, generating. It is an umbrella term; almost all of it in production today is one technique:

**Machine learning (ML)** means the computer works out the rule itself from examples. You give it thousands of rows of pod metrics, each labelled "healthy" or "unhealthy", and it finds a function that maps metrics to labels. Nobody types the thresholds. The learned function is called a **model**.

How does it "find" the function? The intuition needs no maths:

```text
1. Start with a model that guesses randomly.
2. Show it an example and let it predict.
3. Measure how wrong the prediction was.
4. Nudge the model's internal numbers a little in the direction that would have made it less wrong.
5. Repeat steps 2–4 millions of times.
```

That loop is **training**. When it finishes, the model's internal numbers encode a rule that nobody wrote and nobody can easily read, but that works on new examples that look like the training data. Phase 03 shows the arithmetic behind step 4; today the loop is enough.

| | Traditional program | Machine-learning system |
|---|---|---|
| Where the logic comes from | A human writes rules | The computer learns them from data |
| Changing behaviour | Edit code, redeploy | Collect new data, **retrain**, redeploy |
| Determinism | Same input, same output | Same input, usually the same output, with a confidence score |
| What "wrong" looks like | A bug: a specific line is incorrect | A wrong prediction: no line to fix, only data and training to revisit |
| How you test it | Assertions: this input must give that output | Statistics: on a held-out set, how often is it right, and in which direction is it wrong? |
| Quality over time | Stays fixed until you change it | Degrades silently as the world drifts away from the training data |

That last row is the one that changes your job. A conventional service either works or throws errors. A model can be up, fast, returning HTTP 200, and *wrong*, and nothing in your existing monitoring will tell you. You will see this happen in today's lab.

::: tip Three kinds of learning, one sentence each
You will meet these names constantly. Phase 04 covers them properly; for today, recognise them.

- **Supervised learning:** examples come with the right answer attached (metrics labelled healthy/unhealthy). Most production ML is this.
- **Unsupervised learning:** no answers, the model finds structure on its own (grouping similar log lines, flagging unusual metric patterns).
- **Reinforcement learning:** the model learns by acting and receiving rewards (mostly research and games; you will hear it in the context of how LLMs are fine-tuned).
:::

### 3. Deep learning, generative AI and LLMs: the nesting

The terms you hear in the news are subsets of each other:

```text
AI                       computers doing tasks that need judgement
 └─ Machine Learning     the rule is learned from data → a "model"
     └─ Deep Learning    the model is a neural network with many layers
         └─ Generative AI      the model produces new content (text, images, code)
             └─ LLMs           generative models for language, trained on huge text corpora
```

**Deep learning** is machine learning where the model is a **neural network**: a very large stack of simple arithmetic operations, mostly multiplications and additions, with millions to trillions of adjustable numbers arranged in layers. Each layer transforms its input a little and passes it on. "Deep" just means many layers. The trick is that with enough layers and enough data, the stack can learn patterns far too complex for anyone to write as rules: what a cat looks like, what a sentence means, which log line predicts an outage. Phase 05 opens the box.

**Generative AI** is deep learning aimed at *producing* something rather than classifying it: the next word, a pixel, a line of code, a sound.

A **large language model (LLM)** is a generative model for text. Everything you have used under the name "chatbot" or "copilot" is an LLM with an application wrapped around it. Mechanically, an LLM does one thing:

::: tip Mental model: an LLM is autocomplete at industrial scale
Given the text so far, an LLM predicts the most likely **next token** (roughly, the next word-piece). Then it appends that token and predicts again. And again. A 300-word answer is about 400 predictions, one after another. Three operational facts fall straight out of this:

1. Responses can **stream**: each token exists as soon as it is predicted, so the user can see text before the answer is complete.
2. **Latency scales with output length**: every token costs another pass through the model.
3. The model has no "database" it looks things up in. It has numbers that make some continuations more likely than others. That is why it can be fluently, confidently wrong.
:::

The architecture behind nearly all LLMs is called a **transformer**. It gets its own phase (06). A model that has been trained on a very broad corpus and is then adapted to many different tasks is called a **foundation model**; the LLMs you use are foundation models.

A short timeline, so the vocabulary has a shape:

| When | What happened | Why it matters to you |
|---|---|---|
| 1956 | The term "artificial intelligence" is coined at the Dartmouth workshop | The field is old; the recent explosion is about compute and data, not a new idea |
| 1990s–2000s | Machine learning enters production: spam filters, fraud detection, recommendations | Classical ML is mature, cheap to run and still everywhere |
| 2012 | A deep neural network (AlexNet) wins the ImageNet image-recognition competition by a wide margin, trained on GPUs | Deep learning plus GPUs becomes the dominant approach |
| 2017 | The transformer architecture is published ("Attention Is All You Need") | The design behind every modern LLM |
| 2018–2020 | Large pretrained language models appear (BERT, GPT-2, GPT-3) | "Foundation models": train once at enormous cost, reuse everywhere |
| 2022 onward | Chat assistants bring LLMs to the public; open-weight models follow | Every company now wants LLM features in production, on infrastructure someone has to run |

You do not need to understand how any of these work internally yet. You need to know that they are all *models*, and that models have a lifecycle you are about to learn.

### 4. The vocabulary that matters on day one

| Term | Plain meaning | The DevOps analogy (approximate, but useful) |
|---|---|---|
| **Dataset** | The examples the model learns from: rows of inputs, usually with the correct answer attached | Source code plus test fixtures |
| **Features** | The input columns: `restart_count`, `cpu_pct`, ... | Request parameters |
| **Label** | The correct answer for a row: `healthy` / `unhealthy` | The expected test result |
| **Training** | The compute-heavy process that adjusts the model's numbers until its predictions match the labels | The build: slow, batch, produces an artifact |
| **Model** | The result of training: a set of learned numbers (**parameters** or **weights**) plus the code shape that uses them | The artifact: a container image or a binary |
| **Parameters** | The learned numbers inside the model. "7B" means seven billion of them | The size of the binary |
| **Inference** | Running the trained model on new input to get a prediction | Serving: the running container handling requests |
| **Prediction** | The model's output, usually with a confidence score | The response |
| **Token** | The unit of text an LLM reads and writes: a word or word-piece, roughly ¾ of an English word | The unit you are billed and rate-limited in |
| **Foundation model** | A very large model trained once on broad data and reused for many tasks | A base image everyone builds on |
| **Fine-tuning** | Further training of an existing model on a smaller, specific dataset | Layering your changes on the base image |

Analogies leak. The important place this one leaks: a container image behaves identically every time, while a model's *quality* depends on how similar today's traffic is to the data it was trained on.

### 5. Training versus inference: two different workloads

This distinction drives every infrastructure decision you will make in this course.

| | Training | Inference |
|---|---|---|
| Purpose | Produce the model | Use the model |
| Frequency | Occasionally: nightly, weekly, once | Continuously: every request |
| Duration | Minutes to weeks | Milliseconds to seconds per request |
| Compute shape | Batch job, huge throughput, usually GPUs | Latency-sensitive service, CPUs or GPUs |
| Scaling concern | Finish faster; do not run out of memory | Handle concurrency; keep p95 latency down |
| Data flow | Reads the whole dataset, many times | Reads one request, writes one response |
| Who usually runs it | ML engineers, data scientists, pipelines | **You.** It is a production service |
| What breaks | Out of memory, diverging loss, wasted GPU-hours | Slow responses, wrong answers, GPU OOM under load, cost |

Production is overwhelmingly inference. The training run that produced an LLM happened once, on hardware you will probably never touch. The inference service that answers users runs on your cluster, twenty-four hours a day, and it is the thing that pages you.

### 6. The three ways a model reaches production

Where the model runs decides what you own. Almost every AI system you operate will be one of these, or a mix:

| | 1. Managed model API | 2. Self-hosted open model | 3. Your own trained model |
|---|---|---|---|
| Example | Calling a vendor's LLM over HTTPS | Running an open-weight LLM with an inference server on your GPUs | The pod-health classifier you train today; a fraud model your data team built |
| Who trains it | The vendor | Someone else; you download the weights | Your team |
| What you own | The application, secrets, rate limits, retries, cost per token, data leaving your network | Everything in column 1 **plus** GPUs, the inference server, model files, scaling, upgrades | Everything in column 2 **plus** the training pipeline, data, evaluation and retraining |
| Typical failure | Rate limits, provider outages, price and behaviour changes you did not control | GPU OOM, slow startup, version drift between driver, runtime and model | Silent quality decay as data drifts; broken retraining pipeline |
| Where in this course | Phases 07, 11 | Phases 06, 13, 14 | Phases 04, 05, 10 |

You will build all three. Notice that the operational surface grows from left to right, and that even column 1, "just calling an API", is a real production dependency with its own failure modes.

### 7. Where the compute and memory go

A model is mostly a long list of numbers. That single fact explains most of AI infrastructure.

Each parameter is stored as a number with a fixed size in bytes: usually 4 bytes (32-bit float, "fp32"), 2 bytes (16-bit float, "fp16" or "bf16"), or 1 byte (8-bit integer, "int8", after a compression step called **quantisation**). To *use* the model, every one of those numbers must be in memory.

```text
weights memory  ≈  parameters × bytes per parameter

  67 million  × 4 bytes  ≈   268 MB    (the model you run in Part B today)
   7 billion  × 2 bytes  ≈    14 GB    (a small LLM in fp16)
  70 billion  × 2 bytes  ≈   140 GB    (a large LLM in fp16 — more than one GPU)
  70 billion  × 1 byte   ≈    70 GB    (the same model quantised to int8)
```

Laptops have 16–64 GB of RAM. A single data-centre GPU has 24–80 GB (sometimes more) of its own very fast memory, called **VRAM**. Now you know why a 70-billion-parameter model "needs multiple GPUs": it does not fit in one. Weights are only the start; each in-flight request also needs working memory that grows with the length of its text. Phase 06 covers that part.

::: warning The four numbers to ask for
When someone hands you a model to deploy, ask: **how many parameters, in what precision, with what maximum context length, at what expected concurrency?** Those four numbers set the memory, the hardware, and most of the cost. If nobody can answer them, the deployment is not ready to be planned.
:::

Inference is memory-bound more often than compute-bound: the GPU spends its time reading those weights, not calculating. That is why **batching**, processing several requests together so the weights are read once for many inputs, is the single most important throughput lever, and why you will measure it today.

### 8. Common misconceptions

Each of these will cost you an outage or a budget if you carry it into production.

- **"The model looks things up."** No. There is no database inside a model. It has learned numbers that make some outputs more likely than others. It cannot cite where it learned something, and it can produce fluent nonsense. Retrieval systems (Phase 08) bolt a real lookup onto the side.
- **"Same input, same output."** Usually, for a classifier. Not necessarily for an LLM, which samples from probabilities unless told not to. Even then, floating-point arithmetic on different hardware can differ. Do not build tests that assume byte-identical output.
- **"96% accuracy means it is good."** Accuracy on which data, and wrong in which direction? A model that misses one in five real incidents can still be "96% accurate". Today's lab shows exactly this.
- **"AI needs a GPU."** Training deep networks and serving large LLMs do. The 6 MB classifier you train today runs happily on a CPU in milliseconds, as does most classical ML in production.
- **"We run training in production."** Rarely. Production is inference. Training is a periodic job with a different resource profile, and mixing the two on the same nodes is a classic capacity mistake.
- **"The model is small; it is just code."** LLM weights are gigabytes to hundreds of gigabytes. Image sizes, pull times, startup times, storage and rollouts all change.
- **"If it is up, it is fine."** A model service can pass every health check while answering wrongly. Quality is a separate signal you have to build.

## Why does a DevOps Engineer need to know this?

Because the request is coming. Someone will say "we need to put this model in production", and every question you should ask back is in this lesson:

| Familiar DevOps concern | The AI twist |
|---|---|
| How big is the artifact? | Model weights are megabytes to hundreds of gigabytes. Image pulls, startup times and storage change completely. |
| What are the resource requests? | Memory is set by parameter count and precision, not by observation. Getting it wrong means OOM at load time, before the first request. |
| Does it need special hardware? | Often a GPU, which is expensive, scarce, and scheduled differently in Kubernetes. |
| What is the startup time? | Seconds to minutes to load weights. Readiness probes, rollouts and autoscaling all need to account for it. |
| How do I know it is healthy? | Up and fast is not enough. You need quality signals: is it *answering correctly*? |
| How do I roll back? | You roll back the model version, and possibly the data that produced it. Versioning and checksums matter more, not less. |
| What does it cost? | GPU-hours and tokens. A single service can dominate the cloud bill. |
| What is the failure mode? | Wrong answers with a straight face, slow degradation, and memory exhaustion under load. |

### Real-world scenario: ticket #4821

> *"Please deploy the new recommendation model to the prod cluster by Friday. The data team has pushed the image. Thanks!"*

Here is what happens when the questions above are not asked, in the order it usually happens:

1. **Monday.** The image is 9 GB. The first rollout takes eleven minutes per pod because every node pulls the full image. The rolling update's timeout is five minutes. Kubernetes marks the deployment as failed and keeps retrying.
2. **Tuesday.** The pull is fixed with a pre-pull job. Pods now start, then get `OOMKilled` during startup. The memory request was copied from the previous, much smaller model. Nobody knew this one has 7 billion parameters in fp16, which is 14 GB of weights before a single request.
3. **Wednesday.** Memory is raised. Pods pass readiness after ninety seconds of weight loading. The horizontal autoscaler is configured on CPU. Inference is memory-bound, so CPU stays low, so it never scales out. p95 latency climbs to four seconds under the lunchtime peak.
4. **Thursday.** The team asks for GPU nodes. Nobody has planned GPU capacity, taints, or the driver stack. Two nodes are provisioned by hand at a cost nobody has approved.
5. **Friday.** It ships. Dashboards are green. Two weeks later, product notices recommendations have become noticeably worse for new users. Nothing alerted, because nothing was measuring quality. The model was trained on last quarter's behaviour.

Every step in that story is a lesson in this course, and every one of them was preventable with the four numbers and the table above.

## Mental model

Carry this picture with you. Two ideas, one sentence each:

1. **A model is a compiled artifact whose behaviour is statistical.** Treat the file like any other artifact (version it, checksum it, store it, roll it back) and treat its output like a measurement (monitor its distribution, not just its availability).
2. **Everything around the model is infrastructure you already know how to run.** Gateways, services, containers, schedulers, storage, metrics. AI adds new *values* for old *variables*: bigger artifacts, stricter memory, new hardware, longer startups, one more signal to watch.

## Architecture

The simplest useful picture of an AI system in production:

```text
User
 ↓
API Gateway            auth, rate limits, routing            ← you own this
 ↓
AI Application         business logic, prompts, tool calls   ← you deploy and operate this
 ↓
Inference Server       loads the model, batches requests     ← you size, scale and monitor this
 ↓
Model (weights)        the artifact                          ← you version and store this
 ↓
CPU / GPU              the hardware the numbers live in      ← you schedule and pay for this
```

Only the model's *contents* are produced by someone else. Everything around it, and the box it runs in, is infrastructure. By Phase 17 this picture grows into the full AI platform on the [home page](/); today, the five boxes are enough.

### Life of a request

Follow one request through the boxes, with a rough latency budget for a self-hosted LLM answering a short question. The numbers are illustrative; the *shape* is what to remember.

| Stage | What happens | Typical time | What can go wrong |
|---|---|---|---|
| Gateway | TLS, auth, rate limit check, route | 1–5 ms | Rate limit rejects, wrong route |
| Application | Build the prompt, maybe fetch context (Phase 08), call the model | 5–50 ms | Prompt too long for the model's context window, slow context fetch |
| Queueing | Wait for the inference server to have room in a batch | 0–500 ms | Queue grows under load; latency spikes before CPU or GPU look busy |
| Prefill | The model reads the whole prompt in one pass | 50–500 ms | Long prompts dominate; memory grows with prompt length |
| Decode | One token at a time, streamed back | 20–80 ms **per token** | Long answers take seconds; a slow token rate is the first sign of an overloaded GPU |
| Application | Validate, log, meter tokens, return | 1–10 ms | Malformed output fails validation |

A 200-token answer at 40 ms per token is eight seconds of decode. That single row explains why LLM APIs stream, why "tokens per second" is a headline metric, and why output length is a cost lever.

### Life of a model

The artifact has a lifecycle too, and it is longer than the request's:

```text
Data collected → Trained → Evaluated → Registered (versioned, checksummed) → Deployed
      ↑                                                                          │
      └───────────── Retrained when quality drifts ←── Monitored in production ◄──┘
                                                          │
                                                       Retired
```

Today you will do the middle of that loop by hand: train, evaluate, register (save with a version and checksum), deploy (load in a fresh process), and infer. Phase 10 automates the whole loop.

## Hands-on lab 0.1 — Run Your First Model {#hands-on-lab-0-1-run-your-first-model}

**Objective:** train a tiny model, save it as a versioned artifact, reload it, run inference, and measure what each step costs. Then (optionally) do the same with a pretrained model that somebody else trained, and catch it being confidently wrong.

**Difficulty:** 🟢 Beginner · **Estimated time:** 45–60 minutes (plus download time for Part B).

**Prerequisites:** Python 3.10+, `pip`, a terminal, about 200 MB of free disk for Part A and a further 700 MB for Part B.

**Architecture:**

```text
Part A                                   Part B (optional)

synthetic pod metrics                     Hugging Face model hub
        ↓  train (~0.5 s)                         ↓  download once (~268 MB)
pod-health-model-v1.joblib (~6 MB)         local weights cache
        ↓  load (~30 ms)                          ↓  load (seconds)
predict for 5 pods (~40 ms each)           classify 5 messages (~20–60 ms each on CPU)
```

**Environment requirements:** any Linux, macOS or Windows + WSL machine. CPU only. No cloud resources, no credentials, no GPU.

### Setup

Clone the repository and create an isolated Python environment for the lab:

```bash
git clone https://github.com/rairamjee/ai-devops.git
cd ai-devops/examples/python/00-orientation/lab-01-first-model

python3 -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

What these commands do and why:

- `python3 -m venv .venv` creates an isolated Python environment in a folder called `.venv`. AI libraries are large and version-sensitive; never install them into your system Python.
- `source .venv/bin/activate` makes `python` and `pip` in this shell point into that folder. Your prompt usually changes to show `(.venv)`.
- `requirements.txt` installs scikit-learn (a classical machine-learning library), NumPy (arrays) and joblib (serialising Python objects to disk). Together they are about 50 MB.

### Steps — Part A: train, save, load, predict

**Step 1. Read the script before running it.** Open `train_and_predict.py`. It is about 160 lines with comments. You do not need to understand the random forest; follow the six numbered sections and look for these things:

| Section | Look for |
|---|---|
| 1. Data | Where the labels come from. Notice the hidden rule and the 4% label noise: real incident data is noisy too. |
| 2. Training | One line does the learning: `model.fit(...)`. Everything else is measurement. |
| 3. Evaluation | The model is scored on rows it never saw. Why does that matter? |
| 4. Artifact | What is written to disk, alongside the model, and why a checksum is computed. |
| 5. Inference | `del model` then `joblib.load(...)`: the serving process only ever has the file. |
| 6. Summary | One JSON line: the kind of thing you would push to a metrics system. |

**Step 2. Run it.**

```bash
python train_and_predict.py
```

**Step 3. Look at the artifact.**

```bash
ls -la artifacts/
cat artifacts/pod-health-model-v1.sha256
python -c "import joblib; b = joblib.load('artifacts/pod-health-model-v1.joblib'); print({k: v for k, v in b.items() if k != 'model'})"
```

The last command prints the metadata stored next to the model: version, feature names, training time, the label threshold and the test accuracy. A serving system needs all of it. In Phase 10 a model registry stores this for you.

**Step 4. Run it a second time** and compare the `sha256` in the two summaries. Then answer question 1 in the exercise.

**Step 5. Ship a "v2".** The SLO changed: an error rate above 2% now counts as unhealthy, not 5%. Retrain under the new definition:

```bash
python train_and_predict.py --version v2 --threshold 2.0
ls -la artifacts/
```

You now have two versioned model artifacts side by side, each with a checksum. That is the seed of every model registry you will meet in Phase 10.

**Step 6. Compare v1 and v2** on the same pod. Look at the `ingest-9e2d-pqrst` row in both runs. Its error rate is 8.5%, unhealthy under both definitions, but the probability the model assigns differs slightly. Two models trained on the "same" data with a different label rule are different artifacts with different behaviour, which is why they get different version tags.

### Expected output — Part A

Your numbers will differ slightly (timings depend on your CPU; the checksum depends on the timestamp), but the shape should match:

```text
[data]        8000 training rows,  2000 test rows, 17.4% labelled unhealthy
[train]     RandomForest(100 trees) fitted in 0.50s
[evaluate]  accuracy on held-out test data: 96.1%
              precision    recall  f1-score   support

     healthy      0.961     0.993     0.977      1652
   unhealthy      0.959     0.810     0.879       348

    accuracy                          0.961      2000

[artifact]  artifacts/pod-health-model-v1.joblib  (6,370 KB)  sha256=ea093ec5a873ee3b...
[load]      artifact v1 loaded in 33.5 ms
[predict]   pod                  prediction  p(unhealthy)   latency
            api-7d9f-abcde       healthy             0.00   30.01ms
            worker-5c4b-fghij    UNHEALTHY           1.00   34.86ms
            cache-6b8a-klmno     UNHEALTHY           0.99   32.58ms
            ingest-9e2d-pqrst    UNHEALTHY           0.84   36.50ms
            batch-3a1c-uvwxy     UNHEALTHY           1.00   45.48ms
[batch]     all 5 pods in one call: 40.73 ms total, 8.15 ms per pod
[summary]   {"version": "v1", "test_accuracy": 0.961, "train_seconds": 0.5, "artifact_kb": 6370, ...}
```

Read it as an operator:

- **Training took half a second** and produced a **6 MB file**. Training is the build; the file is the artifact. For an LLM the build takes weeks and the file is tens of gigabytes, but the shape of the lifecycle is identical.
- **Accuracy is 96%**, but look at the `unhealthy` row: **recall is 0.81**. The model catches 81% of genuinely unhealthy pods and misses the rest. "96% accurate" and "misses one in five incidents" are the same model. Phase 04 teaches you to read these numbers; today, notice that a single headline metric hides things.
- **Loading took about 30 ms** for 6 MB. Scale that to 14 GB of LLM weights and loading takes tens of seconds to minutes. That is your pod's startup time.
- **A single prediction took 30–45 ms**, almost all of it fixed overhead rather than arithmetic. **Five predictions in one call took about the same 40 ms in total**, 8 ms each. That is batching, and it is the reason inference servers exist.
- The prediction for `ingest-9e2d-pqrst` is `UNHEALTHY` with probability 0.84, not 1.00. Models return confidence, not certainty. Someone has to choose the threshold (here 0.5), and that choice is an operational decision: lower it and you page more often for fewer misses; raise it and the reverse.

### Steps — Part B (optional): run a pretrained model

Part A trained a model from scratch. Most AI you will operate is the other way round: someone else spent enormous compute training a model, published its weights, and your job is to download, load and serve them. Part B does exactly that with a small transformer that classifies text sentiment. It is column 2 of the "three ways a model reaches production" table.

Install the CPU build of PyTorch first, explicitly, so that pip does not pull the default build with several gigabytes of GPU libraries you do not need today:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements-pretrained.txt
python pretrained_inference.py
```

The first run downloads about 268 MB of weights into `~/.cache/huggingface` (set `HF_HOME` to move it). Subsequent runs load from disk. **Run it twice** and compare the `[load]` line.

### Expected output — Part B

This is a real first run (the load time includes the download):

```text
[import]    torch + transformers imported in 8.63s  (torch 2.14.0+cpu, CUDA available: False)
[load]      model ready in 36.72s  (67.0M parameters, about 255 MB of weights in fp32)
[cache]     weights cached under ~/.cache/huggingface
[warm-up]   first inference: 60 ms
[predict]   label      score   latency  message
            POSITIVE   0.981      25ms  Deploy finished, all pods healthy, dashboards green.
            NEGATIVE   1.000      20ms  prod is down, 500s everywhere, customers screaming
            NEGATIVE   0.990      21ms  Rolled back to v1.4.2, error rate recovering.
            NEGATIVE   0.999      22ms  Node pool is out of GPU memory again and the job keeps crashing.
            NEGATIVE   0.998      20ms  Latency p95 back under 200ms after the cache fix.
[batch]     all 5 messages in one call: 78 ms total, 16 ms per message
```

Timings vary widely by machine and network; the *ratios* are what matter. Read it as an operator:

- **Importing the libraries took almost nine seconds** before any model was loaded. Container startup time starts here, not at "load model".
- **Loading took 37 seconds on the first run** because it included the download. On the second run it drops to a few seconds. In production, the difference between those two numbers is the difference between a pod that pulls weights from the internet on every start and one that reads them from a cache or a volume. Phase 14 covers model caching for exactly this reason.
- **67 million parameters × 4 bytes ≈ 255 MB** of weights in memory: the arithmetic from the concept section, confirmed by the running program.
- **The first inference took three times longer** than the rest. Serving systems send a warm-up request before a pod is marked ready.
- **Batching again cut per-item latency**, from about 20 ms to 16 ms, a smaller factor than in Part A because a transformer does real arithmetic per item rather than mostly overhead. Phase 06 explains where that time goes.
- **Look at the last two predictions.** "Rolled back to v1.4.2, error rate recovering" and "Latency p95 back under 200ms after the cache fix" are good news to anyone on call, and the model labelled both **NEGATIVE with 99% confidence**. Nothing failed. No error was raised. Latency was excellent. The model was trained on movie reviews, and words like "rolled back", "error" and "latency" read as negative in that world. This is the single most important thing to see on day one: **a model can be up, fast, confident and wrong**, and none of your existing monitoring will notice. Detecting it is what Phases 11 and 12 are about.

### Validation

You have completed the lab when:

- [ ] `artifacts/` contains `pod-health-model-v1.joblib`, `pod-health-model-v2.joblib` and their `.sha256` files.
- [ ] You can state training time, artifact size, load time, single-request latency and batched per-item latency for v1.
- [ ] You can explain why v1 and v2 have different sizes and checksums.
- [ ] You printed the artifact's metadata and can name three fields a serving system would need.
- [ ] (Part B) You can state the model's parameter count and the memory it implies, you observed a slower first inference and a faster second load, and you can explain why two of the five predictions were confidently wrong.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'sklearn'` | The virtual environment is not active, or you installed into a different interpreter | `source .venv/bin/activate`, then `pip install -r requirements.txt`. Check `which python` points inside `.venv`. |
| `python: command not found` | Only `python3` exists on your system | Use `python3` for the venv creation; inside an activated venv `python` will work. |
| `pip install torch` downloads gigabytes | You skipped the `--index-url .../cpu` flag and got the CUDA build | Cancel, `pip uninstall torch`, rerun with the CPU index URL. |
| Part B hangs at `[load]` | Downloading 268 MB on a slow or proxied connection | Wait, or set `HF_HUB_OFFLINE=1` only after the first successful download. Check `HTTPS_PROXY` if you are behind a corporate proxy. |
| `OSError: ... Can't load ... from 'distilbert-...'` | No network access to the Hugging Face hub during first run | Retry with network; confirm `curl -I https://huggingface.co` succeeds. |
| `Warning: You are sending unauthenticated requests to the HF Hub` | Informational: anonymous downloads have lower rate limits | Harmless for this lab. A free Hugging Face account token in `HF_TOKEN` removes it; never hard-code the token. |
| Latencies are 10× larger than shown | Low-power laptop, or another process is saturating the CPU | Fine for the lab. Note the ratio between single and batched calls instead of absolute numbers. |
| Permission error writing `artifacts/` | Read-only working directory | Pass `--out /tmp/lab01-artifacts`. |

### Common mistakes

- **Installing into system Python.** It works until two labs need different versions of the same library. Always use a virtual environment, one per project.
- **Committing `artifacts/` to git.** Model files are binaries that change on every run. The repository's `.gitignore` excludes them; keep it that way and use a registry or object storage for artifacts (Phase 10).
- **Reading accuracy and stopping.** Look at the per-class rows. The class you care about is usually the rare one.
- **Relying on a library's default model.** `pipeline("sentiment-analysis")` without a model name would work, and would silently change behaviour when the library updates its default. Pin the model, as the script does.
- **Treating a confident score as a correct answer.** Confidence is the model's opinion of itself. Part B returned 99.8% confidence on a wrong answer.

### Cleanup

```bash
deactivate
rm -rf artifacts/ .venv/
# Part B weights (optional):
rm -rf ~/.cache/huggingface/hub/models--distilbert-base-uncased-finetuned-sst-2-english
```

Nothing was created outside this directory and the Hugging Face cache. No cloud resources were used.

### Extension challenge

Add a `--samples 100000` run and compare training time and artifact size with the default. Then run `--samples 1000`. Write two sentences on how training data volume relates to build time and artifact size, and one sentence on what that would mean for a model 1,000× larger.

### Questions

1. Which step of the lab corresponds to "build" and which to "serve"?
2. What single file would you need to copy to a second machine to run inference there? What else would that machine need installed, and how would you pin its versions?
3. If the model had 7 billion parameters in fp16 instead of a 6 MB random forest, which numbers in the output would change by orders of magnitude, and which would not?
4. Which of the three "ways a model reaches production" did Part A demonstrate, and which did Part B demonstrate?

## Exercise

Do these on your own, without looking back at the lab output.

1. **The checksum question.** You ran `train_and_predict.py` twice with identical arguments and the same random seed, and got two different `sha256` values. Find out why by reading the section that builds the artifact. Then say what you would remove or change to make the artifact byte-for-byte reproducible, and what you would lose by doing so. Write down which of the two you would choose for a production model registry, and why.
2. **The rollback question.** v2 is in production and someone reports that pods with a 3% error rate are now being flagged unhealthy and paging the on-call. Which artifact do you roll back to, how do you prove that the file you deployed is the right one, and what do you tell the team that changed the SLO?
3. **The memory table.** Without a calculator, fill in the weights memory for a 1B, 8B and 30B-parameter model in fp32, fp16 and int8. Then say which of those nine cells fit in a 24 GB GPU, leaving 20% headroom for everything else.
4. **The wrong-answer question.** Part B mislabelled two operational messages. Write three sentences: why it happened, how you would detect it in production without a human reading every answer, and what you would do about it. You do not need to know the real techniques yet; reason from what you saw.
5. **Your own words.** In your learning journal (Day 4 sets one up; a text file is fine for now), write one-sentence definitions of AI, machine learning, deep learning, LLM, training, inference, model and parameter, without looking them up. Compare with the lesson tomorrow.

## Quiz

Twelve questions. Try them before opening the answers.

**1. In one sentence, what is the difference between traditional automation and machine learning?**

::: details Answer
In traditional automation a human writes the rules; in machine learning the computer learns the rules from labelled examples, producing a model.
:::

**2. Put these in nesting order from broadest to narrowest: LLMs, deep learning, AI, machine learning, generative AI.**

::: details Answer
AI → machine learning → deep learning → generative AI → LLMs.
:::

**3. What is a model, physically?**

::: details Answer
A set of learned numbers (parameters or weights) plus the code shape that uses them, serialised into one or more files. It has a size, can be versioned and checksummed, and must be loaded into memory to be used.
:::

**4. Which runs in production far more often, training or inference, and why does that matter for you?**

::: details Answer
Inference. Training is an occasional batch job that produces the model; inference is the continuously running, latency-sensitive service that uses it. The inference service is the one you deploy, scale, monitor and get paged for.
:::

**5. A model has 8 billion parameters stored in fp16. Roughly how much memory do its weights need?**

::: details Answer
8 billion × 2 bytes ≈ 16 GB, before any working memory for requests. It will not fit on a 16 GB GPU with headroom; it needs a 24 GB GPU or quantisation.
:::

**6. In the lab, five single predictions took about 35 ms each, but five predictions in one call took about 40 ms total. What is this effect called, and why does it matter?**

::: details Answer
Batching. Most of the per-call time is fixed overhead (and, for large models, reading the weights from memory), so processing many inputs per call amortises it. It is the main throughput lever in inference serving and a reason inference servers exist.
:::

**7. The model reported 96% accuracy but only caught 81% of unhealthy pods. How can both be true?**

::: details Answer
Only 17% of pods were unhealthy, so a model that is excellent on the 83% healthy majority scores high accuracy even while missing a fifth of the minority class. Accuracy hides class imbalance; recall on the class you care about does not.
:::

**8. Why did the lab store a `.sha256` file next to each model artifact?**

::: details Answer
To prove which exact artifact is deployed. Model files are opaque binaries; a checksum lets you verify integrity, detect an unexpected change, and confirm a rollback restored precisely the previous version.
:::

**9. Name three things that make a model's startup slower than a typical web service's.**

::: details Answer
Importing heavy AI libraries (seconds), loading weights from disk or a remote hub into memory (seconds to minutes, proportional to size), and the slower first inference (warm-up). Readiness probes, rollouts and autoscaling must account for all three.
:::

**10. A model can be "up", fast, returning HTTP 200, and still be broken. What does "broken" mean here, and what would you need to detect it?**

::: details Answer
It can be returning wrong predictions, because the model's quality depends on how similar live traffic is to its training data and that similarity drifts over time. Detecting it needs quality signals (evaluation against known-good examples, drift monitoring, feedback), not just availability and latency.
:::

**11. Why do LLM responses stream, and why does a long answer take longer than a short one?**

::: details Answer
An LLM generates one token at a time, each requiring another pass through the model. Tokens can be sent as they are produced (streaming), and total latency grows roughly linearly with the number of output tokens.
:::

**12. You are asked to add an LLM feature. Name the three ways the model could reach production and one thing you would own in each.**

::: details Answer
A managed model API (you own secrets, rate limits, retries, cost and data egress), a self-hosted open-weight model (you additionally own GPUs, the inference server, model files, scaling and upgrades), or a model your team trains (you additionally own the training pipeline, data, evaluation and retraining).
:::

## Interview questions

Say the answers out loud. Interviewers for AI-infrastructure roles are listening for the production angle, not the definition.

1. **"What is the difference between machine learning and traditional programming?"** Lead with "who writes the rules", then immediately go to the operational consequence: behaviour changes via retraining, and quality can degrade silently without errors.
2. **"What is the difference between training and inference, and which one do you run in production?"** Two workloads with different shapes: batch and throughput-heavy versus service and latency-sensitive. Production is mostly inference, and that is what gets sized, scaled and paged.
3. **"What is a model, and how is deploying one different from deploying a normal service?"** An artifact of learned numbers. Differences: size (GB, not MB), memory fixed by parameter count and precision, GPU requirements, long startup, versioning tied to data, and the need for quality monitoring.
4. **"How do you estimate the memory a model needs?"** Parameters × bytes per parameter for the weights, plus headroom for the working memory each request needs. Give the fp32/fp16/int8 numbers for a 7B model from memory.
5. **"Why is batching important for inference?"** Per-request cost is dominated by fixed overhead and by reading the weights; batching amortises both, raising throughput and GPU utilisation. Mention the latency trade-off: waiting to fill a batch adds delay.
6. **"What would you monitor for a model service that you would not monitor for a web service?"** Prediction quality against a reference set, confidence distributions, input drift, model and data version in every log line, GPU memory and utilisation, and cost per request.
7. **"Would you call a vendor's model API or self-host an open model?"** There is no right answer; the interviewer wants the trade-offs: control, data residency and cost at scale favour self-hosting; speed to market, no GPU operations and access to the strongest models favour the API. Mention that many teams do both behind a gateway (Phase 07).
8. **"What is a foundation model?"** A very large model trained once on broad data and reused, often with light adaptation, for many tasks. Operationally: you rarely train one, you download or call one, and its size drives your infrastructure.

## Further exploration

Read these alongside, not instead of, the lab.

- [Hugging Face LLM course, chapter 1](https://huggingface.co/learn/llm-course/chapter1/1): a gentle, well-maintained introduction to what transformers and LLMs are, from the people who maintain the library you used in Part B.
- [Google's Machine Learning Glossary](https://developers.google.com/machine-learning/glossary): when you meet an unfamiliar term in the coming weeks, look here first.
- [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html): the library from Part A, and the shape of the `fit` / `predict` API that almost every classical ML tool copies.
- [The model card for the Part B model](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english): read what data it was trained on, then re-read the two wrong predictions.

## Key takeaways

- AI is the umbrella; nearly everything in production is machine learning; the newest and largest part of it is LLMs.
- A model is an artifact: version it, checksum it, store it, roll it back.
- Training is the build; inference is the service you run. Production is mostly inference.
- Parameters × bytes per parameter = weights memory. Ask for parameters, precision, context length and concurrency before planning anything.
- Startup is slow: library import, weight loading, warm-up. Plan readiness, rollouts and scaling around it.
- Batching is the primary throughput lever.
- A model can be up, fast, confident and wrong. Quality is a separate signal you must build.
- Everything around the model is infrastructure you already know.

## Checkpoint

Do not move on to Day 2 until you can, without notes:

- Draw the nesting of AI, ML, deep learning, generative AI and LLMs and say one sentence about each.
- Explain training versus inference and name which one is your production workload.
- Point at a model file on your disk and state its size, version and checksum.
- Compute the weights memory for a model given its parameter count and precision.
- Report your measured training time, load time, single-request latency and batched per-item latency, and explain what each means for a production service.
- Draw the five-box architecture and say what a DevOps engineer owns at each layer.
- Explain, in two sentences, why the Part B model was confidently wrong and why no health check would have caught it.

Next: [Day 2 — Set up your environment](./02-environment-setup.md), where you install and verify everything the rest of the course needs and put today's model in a container. Back to the [Phase 00 overview](./index.md).
