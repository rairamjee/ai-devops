# Day 1 — What Is AI?

> By the end of today you will be able to explain AI, machine learning, deep learning and LLMs to a colleague, and you will have trained, saved, reloaded and run a model on your own machine while measuring what it costs.

## Learning objectives

- Define AI, machine learning, deep learning, generative AI and LLMs, and show how they nest.
- Explain the difference between **training** and **inference**, and say which one production mostly runs.
- Explain that a **model is an artifact**: a file with a size, a version, a checksum and resource requirements.
- Do the arithmetic that turns a model's parameter count into a memory requirement.
- Describe a basic AI production architecture from the user to the GPU and say what a DevOps engineer owns at each layer.
- Run a model locally and measure training time, artifact size, load time and per-request latency.

## Prerequisites

- Comfortable in a Linux, macOS or WSL shell.
- Python 3.10 or newer installed (`python3 --version`).
- Git installed.
- **No AI knowledge.** Every term below is defined before it is used.

## Concept explanation

### Start with what you already know: rules

Every system you have ever operated makes decisions with rules that a human wrote:

```python
if restart_count >= 3 or mem_pct > 92:
    alert("pod unhealthy")
```

This is automation, not AI. A human looked at the problem, decided which signals matter and what the thresholds are, and typed them in. When reality changes, a human edits the rule.

### AI: the rule is learned instead of written

**Artificial intelligence (AI)** is the broad field of making computers do things that normally need human judgement: recognising, classifying, predicting, generating. In practice today, almost all of it is one technique:

**Machine learning (ML)** means the computer works out the rule itself from examples. You give it thousands of rows of pod metrics, each labelled "healthy" or "unhealthy", and it finds a function that maps metrics to labels. Nobody types the thresholds. The learned function is called a **model**.

| | Traditional program | Machine-learning system |
|---|---|---|
| Where the logic comes from | A human writes rules | The computer learns them from data |
| Changing behaviour | Edit code, redeploy | Collect new data, **retrain**, redeploy |
| Determinism | Same input, same output | Same input, usually the same output, with a confidence score |
| What "wrong" looks like | A bug: a specific line is incorrect | A wrong prediction: no line to fix, only data and training to revisit |
| Quality over time | Stays fixed until you change it | Degrades silently as the world drifts away from the training data |

That last row is the one that changes your job. A conventional service either works or throws errors. A model can be up, fast, returning HTTP 200, and *wrong*, and nothing in your existing monitoring will tell you.

### Deep learning, generative AI and LLMs: the nesting

The terms you hear in the news are subsets of each other:

```text
AI                       computers doing tasks that need judgement
 └─ Machine Learning     the rule is learned from data → a "model"
     └─ Deep Learning    the model is a neural network with many layers
         └─ Generative AI      the model produces new content (text, images, code)
             └─ LLMs           generative models for language, trained on huge text corpora
```

- **Deep learning** is machine learning where the model is a **neural network**: a very large stack of simple arithmetic operations (mostly multiplications and additions) with millions to trillions of adjustable numbers. The "deep" is the number of stacked layers. Phase 05 opens this up.
- **Generative AI** is deep learning aimed at *producing* something rather than classifying it: the next word, a pixel, a line of code.
- A **large language model (LLM)** is a generative model for text. Everything you have used under the name "chatbot" or "copilot" is an LLM with an application around it. The architecture behind nearly all of them is called a **transformer**, which gets its own phase (06).

You do not need to understand how any of these work internally yet. You need to know that they are all *models*, and that models have a lifecycle you are about to learn.

### The vocabulary that matters on day one

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

Analogies leak. The important place this one leaks: a container image behaves identically every time, while a model's *quality* depends on how similar today's traffic is to the data it was trained on.

### Training versus inference: two different workloads

This distinction drives every infrastructure decision you will make in this course.

| | Training | Inference |
|---|---|---|
| Purpose | Produce the model | Use the model |
| Frequency | Occasionally: nightly, weekly, once | Continuously: every request |
| Duration | Minutes to weeks | Milliseconds to seconds per request |
| Compute shape | Batch job, huge throughput, usually GPUs | Latency-sensitive service, CPUs or GPUs |
| Scaling concern | Finish faster; do not run out of memory | Handle concurrency; keep p95 latency down |
| Who usually runs it | ML engineers, data scientists, pipelines | **You.** It is a production service |
| What breaks | Out of memory, diverging loss, wasted GPU-hours | Slow responses, wrong answers, GPU OOM under load, cost |

Production is overwhelmingly inference. The training run that produced an LLM happened once, on hardware you will probably never touch. The inference service that answers users runs on your cluster, twenty-four hours a day, and it is the thing that pages you.

### Where the compute and memory go

A model is mostly a long list of numbers. That single fact explains most of AI infrastructure.

Each parameter is stored as a number with a fixed size in bytes: usually 4 bytes (32-bit float, "fp32"), 2 bytes (16-bit float, "fp16" or "bf16"), or 1 byte (8-bit integer, "int8", after a compression step called quantisation). To *use* the model, every one of those numbers must be in memory.

```text
weights memory  ≈  parameters × bytes per parameter

  67 million  × 4 bytes  ≈   268 MB    (the model you run in Part B today)
   7 billion  × 2 bytes  ≈    14 GB    (a small LLM in fp16)
  70 billion  × 2 bytes  ≈   140 GB    (a large LLM in fp16 — more than one GPU)
  70 billion  × 1 byte   ≈    70 GB    (the same model quantised to int8)
```

Laptops have 16–64 GB of RAM. A single data-centre GPU has 24–80 GB (sometimes more) of its own very fast memory, called **VRAM**. Now you know why a 70-billion-parameter model "needs multiple GPUs": it does not fit in one. You also know the first question to ask when someone hands you a model: *how many parameters, in what precision?*

Inference is memory-bound more often than compute-bound: the GPU spends its time reading those weights, not calculating. That is why batching several requests together, so the weights are read once for many inputs, is the single most important throughput lever, and why you will measure it today.

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

Everything in this course is an expansion of one row of that table.

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

## Hands-on lab 0.1 — Run Your First Model {#hands-on-lab-0-1-run-your-first-model}

**Objective:** train a tiny model, save it as a versioned artifact, reload it, run inference, and measure what each step costs. Then (optionally) do the same with a pretrained model that somebody else trained.

**Difficulty:** 🟢 Beginner · **Estimated time:** 30–45 minutes (plus download time for Part B).

**Prerequisites:** Python 3.10+, `pip`, a terminal, about 200 MB of free disk for Part A and a further 700 MB for Part B.

**Architecture:**

```text
Part A                                   Part B (optional)

synthetic pod metrics                     Hugging Face model hub
        ↓  train (0.5 s)                          ↓  download once (~268 MB)
pod-health-model-v1.joblib (6 MB)          local weights cache
        ↓  load (~30 ms)                          ↓  load (seconds)
predict for 5 pods (~40 ms each)           classify 5 messages (~50–100 ms each on CPU)
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

`requirements.txt` installs scikit-learn (a classical machine-learning library), NumPy (arrays) and joblib (serialising Python objects to disk). Together they are about 50 MB.

### Steps — Part A: train, save, load, predict

**Step 1. Read the script before running it.** Open `train_and_predict.py`. It is about 150 lines with comments. You do not need to understand the random forest; follow the six numbered sections: data, training, evaluation, artifact, inference, summary.

**Step 2. Run it.**

```bash
python train_and_predict.py
```

**Step 3. Look at the artifact.**

```bash
ls -la artifacts/
cat artifacts/pod-health-model-v1.sha256
```

**Step 4. Run it a second time** and compare the `sha256` in the two summaries. Then answer question 1 in the exercise.

**Step 5. Ship a "v2".** The SLO changed: an error rate above 2% now counts as unhealthy, not 5%. Retrain under the new definition:

```bash
python train_and_predict.py --version v2 --threshold 2.0
ls -la artifacts/
```

You now have two versioned model artifacts side by side, each with a checksum. That is the seed of every model registry you will meet in Phase 10.

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
- The prediction for `ingest-9e2d-pqrst` is `UNHEALTHY` with probability 0.84, not 1.00. Models return confidence, not certainty. Someone has to choose the threshold (here 0.5), and that choice is an operational decision.

### Steps — Part B (optional): run a pretrained model

Part A trained a model from scratch. Most AI you will operate is the other way round: someone else spent enormous compute training a model, published its weights, and your job is to download, load and serve them. Part B does exactly that with a small transformer that classifies text sentiment.

Install the CPU build of PyTorch first, explicitly, so that pip does not pull the default build with several gigabytes of GPU libraries you do not need today:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements-pretrained.txt
python pretrained_inference.py
```

The first run downloads about 268 MB of weights into `~/.cache/huggingface` (set `HF_HOME` to move it). Subsequent runs load from disk.

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
- **Loading took 37 seconds on the first run** because it included the download. Run the script again and watch it drop to a few seconds. In production, the difference between those two numbers is the difference between a pod that pulls weights from the internet on every start and one that reads them from a cache or a volume. Phase 14 covers model caching for exactly this reason.
- **67 million parameters × 4 bytes ≈ 255 MB** of weights in memory: the arithmetic from the concept section, confirmed by the running program.
- **The first inference took three times longer** than the rest. Serving systems send a warm-up request before a pod is marked ready.
- **Batching again cut per-item latency**, from about 20 ms to 16 ms, a smaller factor than in Part A because a transformer does real arithmetic per item rather than mostly overhead. Phase 06 explains where that time goes.
- **Look at the last two predictions.** "Rolled back to v1.4.2, error rate recovering" and "Latency p95 back under 200ms after the cache fix" are good news to anyone on call, and the model labelled both **NEGATIVE with 99% confidence**. Nothing failed. No error was raised. Latency was excellent. The model was trained on movie reviews, and words like "rolled back", "error" and "latency" read as negative in that world. This is the single most important thing to see on day one: **a model can be up, fast, confident and wrong**, and none of your existing monitoring will notice. Detecting it is what Phases 11 and 12 are about.

### Validation

You have completed the lab when:

- [ ] `artifacts/` contains `pod-health-model-v1.joblib`, `pod-health-model-v2.joblib` and their `.sha256` files.
- [ ] You can state training time, artifact size, load time, single-request latency and batched per-item latency for v1.
- [ ] You can explain why v1 and v2 have different sizes and checksums.
- [ ] (Part B) You can state the model's parameter count and the memory it implies, you observed a slower first inference, and you can explain why two of the five predictions were confidently wrong.

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
2. What single file would you need to copy to a second machine to run inference there? What else would that machine need installed?
3. If the model had 7 billion parameters in fp16 instead of a 6 MB random forest, which numbers in the output would change by orders of magnitude, and which would not?

## Exercise

Do these on your own, without looking back at the lab output.

1. **The checksum question.** You ran `train_and_predict.py` twice with identical arguments and the same random seed, and got two different `sha256` values. Find out why by reading the section that builds the artifact. Then say what you would remove or change to make the artifact byte-for-byte reproducible, and what you would lose by doing so. Write down which of the two you would choose for a production model registry, and why.
2. **The rollback question.** v2 is in production and someone reports that pods with a 3% error rate are now being flagged unhealthy and paging the on-call. Which artifact do you roll back to, how do you prove that the file you deployed is the right one, and what do you tell the team that changed the SLO?
3. **The memory table.** Without a calculator, fill in the weights memory for a 1B, 8B and 30B-parameter model in fp32, fp16 and int8. Then say which of those nine cells fit in a 24 GB GPU, leaving 20% headroom for everything else.

## Quiz

Ten questions. Try them before opening the answers.

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

## Interview questions

Say the answers out loud. Interviewers for AI-infrastructure roles are listening for the production angle, not the definition.

1. **"What is the difference between machine learning and traditional programming?"** Lead with "who writes the rules", then immediately go to the operational consequence: behaviour changes via retraining, and quality can degrade silently without errors.
2. **"What is the difference between training and inference, and which one do you run in production?"** Two workloads with different shapes: batch and throughput-heavy versus service and latency-sensitive. Production is mostly inference, and that is what gets sized, scaled and paged.
3. **"What is a model, and how is deploying one different from deploying a normal service?"** An artifact of learned numbers. Differences: size (GB, not MB), memory fixed by parameter count and precision, GPU requirements, long startup, versioning tied to data, and the need for quality monitoring.
4. **"How do you estimate the memory a model needs?"** Parameters × bytes per parameter for the weights, plus headroom for the working memory each request needs. Give the fp32/fp16/int8 numbers for a 7B model from memory.
5. **"Why is batching important for inference?"** Per-request cost is dominated by fixed overhead and by reading the weights; batching amortises both, raising throughput and GPU utilisation. Mention the latency trade-off: waiting to fill a batch adds delay.
6. **"What would you monitor for a model service that you would not monitor for a web service?"** Prediction quality against a reference set, confidence distributions, input drift, model and data version in every log line, GPU memory and utilisation, and cost per request.

## Checkpoint

Do not move on to Day 2 until you can, without notes:

- Draw the nesting of AI, ML, deep learning, generative AI and LLMs and say one sentence about each.
- Explain training versus inference and name which one is your production workload.
- Point at a model file on your disk and state its size, version and checksum.
- Compute the weights memory for a model given its parameter count and precision.
- Report your measured training time, load time, single-request latency and batched per-item latency, and explain what each means for a production service.
- Draw the five-box architecture and say what a DevOps engineer owns at each layer.

Next: **Day 2 — Set up your environment** (Python, Docker, kind, and a script that verifies all of it). Back to the [Phase 00 overview](./index.md).
