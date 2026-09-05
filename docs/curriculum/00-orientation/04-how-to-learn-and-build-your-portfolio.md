# Day 4 — How to Work Through This Course

> The last day of Orientation is about you: how to learn infrastructure skills so they stick, how to get unstuck the same way you would in production, how to use AI assistants without letting them do the learning for you, and how to turn every lab you finish into a portfolio commit and an interview story. You leave with a learning journal, a portfolio repository, and Phase 00 written up in it.

**Time:** about 2 hours. Roughly 45 minutes reading, 60 minutes in the lab, 15 minutes on the quiz and exercise.

## Learning objectives

By the end of this lesson you can:

- Describe how the course is structured and plan a realistic weekly schedule through it.
- Use the run → break → fix → explain → apply loop deliberately, and explain why it beats reading.
- Apply a repeatable method for getting unstuck that mirrors production troubleshooting.
- Use an AI assistant as a tutor without outsourcing the lab to it, and state the rules you follow.
- Keep a learning journal that produces evidence and interview material as a by-product.
- Explain what reviewers and hiring managers actually look at in a portfolio, and structure yours accordingly.
- Turn a lab into a two-minute interview story with numbers in it.
- Name the roles this course prepares you for and which phases matter most for each.

## Prerequisites

- [Day 1](./01-what-is-ai.md), [Day 2](./02-environment-setup.md) and [Day 3](./03-ai-production-stack.md) completed, with the numbers you measured to hand. You will write them down today.
- A GitHub account (free) if you want to publish the portfolio; everything works locally without one.

## Concept explanation

### 1. How the course is built, and how to use it

The [curriculum overview](../index.md) explains the structure; here is how to *use* it.

**The ratio is 30% theory, 20% reading, 50% hands-on.** If you find yourself reading for an hour without running anything, stop and open a terminal. The concept sections in every lesson are written to be understood *after* the lab as much as before it; several things in Day 1 only made sense once you had watched a model load.

**Every phase ends with something tangible**, and you should not leave a phase without it. The checkpoint at the end of each lesson is a gate, not a suggestion. If you cannot do the checkpoint items without notes, repeat the lab. Repeating a lab is not falling behind; it is the course working.

**Every concept answers four questions:** what is it, why does it matter, how do I operate it, what happens when it breaks. When you take notes, use those four headings. If you cannot fill in "what happens when it breaks", you have not finished the topic.

**A realistic pace** at 8–10 focused hours per week:

| Phase type | Examples | Lessons per week | Weeks |
|---|---|---|---|
| Orientation and foundations | 00, 02, 03 | 3–4 | 1 each |
| Skills phases with a project | 01, 04, 05, 06, 07, 08, 09, 10, 11 | 2–3 | 2 each |
| Operations and infrastructure | 12, 13, 14, 15, 16 | 2–3 | 1–2 each |
| Capstone | 17 | project work | 3–4 |

That is roughly eight months. Faster is possible; slower is fine. What matters is not skipping labs. The [roadmap](/roadmap) has the per-phase estimates.

### 2. The loop: run, break, fix, explain, apply

Reading about infrastructure produces recognition: you see a term and it feels familiar. Operating infrastructure produces recall: you can reproduce it from nothing at 3 a.m. Interviews and incidents test recall. The loop below is designed to produce it, and every lab in this course is built around it.

```text
RUN       follow the steps; get the expected output; notice what you did not expect
BREAK     change one thing and predict what will happen; then do it (every advanced lab does this for you)
FIX       diagnose from signals, not guesses; write down the steps that worked and the ones that did not
EXPLAIN   say what happened out loud or in your journal, in your own words, with numbers
APPLY     connect it to a production system you know: where would this bite, what would you monitor
```

Two habits make the loop far more effective:

- **Predict before you act.** Before you apply the OOM manifest on Day 3, write down what you expect to see. Being wrong is where the learning is; being right confirms a mental model.
- **Retrieve, do not re-read.** The quizzes exist so you can test recall. Take them closed-book. Three weeks after a phase, redo one of its labs from memory. This is spaced retrieval, and it is the single best-evidenced study technique there is.

### 3. When you are stuck

You will get stuck. The method is the same one you use for a production incident, which is the point: the course is training the method as much as the content.

1. **Read the error, verbatim.** Not the gist. The exact text, including the exit code, the object name, and the line before it. Most "mysterious" failures are described precisely in their own error message.
2. **Locate the layer.** Use the Day 3 table. Is this the runtime (Python import), the container (image, user, filesystem), the scheduler (Pending, resources), the kernel (137, OOMKilled), the network (timeouts), or the model (wrong answers)?
3. **Follow the diagnostic order: status → describe → logs → events.** Or the equivalent outside Kubernetes: exit code → configuration → logs → system state.
4. **Reduce.** Can you reproduce with fewer moving parts? A `docker run` instead of a Job. A one-line Python script instead of the lab.
5. **Check the official documentation** for the exact field or flag involved. The [resources page](/resources) lists the sources this course trusts.
6. **Search the exact error string.** Quote it. You are rarely the first.
7. **Ask a good question.** State what you did, what you expected, what you observed (verbatim), and what you have tried. A question in this form usually answers itself while you write it.

Timebox steps 1–6 at 30–45 minutes. Then ask. Being stuck for three hours teaches persistence, not infrastructure.

### 4. Using AI assistants to learn AI infrastructure

This is a course about operating AI systems. It would be odd to pretend AI assistants do not exist, and they are excellent tutors for exactly this material. They are also, as you saw on Day 1, capable of being fluently and confidently wrong. Use them under rules:

| Use an assistant to | Do not use an assistant to |
|---|---|
| Explain a concept at a different level, or with a different analogy | Run the lab for you, or generate the commands you then paste without reading |
| Interpret an error message and suggest where to look | Tell you what the output *should* have been instead of observing it |
| Generate extra practice questions after a lesson | Write your journal entries or portfolio documentation |
| Review your written explanation and point out gaps | Be the source of truth for a version, flag, or API; check the official documentation |
| Rubber-duck a design decision | Handle anything containing secrets, tokens, or your employer's data |

Three habits keep this honest. **Type every command yourself**, even when an assistant suggested it; the typing is where the recall forms. **Ask "why", not "do."** "Why does `runAsNonRoot` reject a named user?" teaches you something; "fix my manifest" does not. **Treat every answer as a hypothesis** to be verified against the official documentation or by running it. You are training to be the person who verifies what AI systems say; start now.

### 5. The learning journal

Ten minutes at the end of every lesson, in a single file, newest entry first. The [template](https://github.com/rairamjee/ai-devops/blob/main/examples/templates/learning-journal.md) has six prompts:

```text
What I ran            commands and measured results, with units
What broke            exact error text; include things you broke on purpose
What I did about it   diagnostic steps in order, including dead ends
What I understand now one to three sentences, your own words
Interview line        one sentence you could say in an interview, with a number in it
Open questions        things to come back to
```

The journal does three jobs at once. It forces retrieval (you write from memory, then check). It produces evidence (the numbers and errors are dated and specific). And it accumulates interview stories without any separate preparation; the "interview line" prompt is there so that, by Phase 17, you have eighty of them.

### 6. Portfolio strategy: what reviewers actually look at

A hiring manager or reviewer spends about ninety seconds on a repository before deciding whether to spend more. In those ninety seconds they look at, in order:

1. **The README's first screen.** What is this, what does it do, and an architecture sketch. If they have to scroll or open code to find out what the project is, they leave.
2. **Numbers.** Latency, image size, cost, startup time. Measured numbers with a method next to them signal that the system was *run*, not just written.
3. **Failure modes tested.** A troubleshooting document with real errors and real diagnoses is the single most convincing artifact in a portfolio. Anyone can make a demo work once; showing that you broke it on purpose and understood why is what an operator does.
4. **Commit history.** Small, descriptive commits over weeks show iteration. One giant "initial commit" shows a copy.
5. **Documentation set.** README, ARCHITECTURE, SETUP, OPERATIONS, TROUBLESHOOTING, SECURITY, COST. Not because anyone reads all seven, but because their presence says you know what a production system needs.

What they do not look at: certificates on their own, notebooks with no README, forks with no changes, and a long list of repositories with nothing in them.

**Structure.** One portfolio repository for the journal, the progress checklist and per-phase write-ups; one repository per project (Projects 1–8) using the [project documentation templates](https://github.com/rairamjee/ai-devops/tree/main/examples/templates/project-docs). This keeps each project's README focused and lets you link to them individually from a CV.

**Hygiene.** Public by default, unless your employer's rules say otherwise. Never include company data, hostnames, or secrets; `.gitignore` artifacts, virtual environments and `.env` files (the course's [.gitignore](https://github.com/rairamjee/ai-devops/blob/main/.gitignore) is a good start). Write commit messages that say what changed and why. If you ever commit a secret, rotating it is the fix; deleting the commit is not, because it is already in history and possibly already indexed.

### 7. Turning a lab into an interview story

Interviewers for infrastructure roles ask behavioural questions ("tell me about a production issue you debugged") and expect a structured answer with evidence. Use this shape, which is the STAR format with a reflection added:

```text
SITUATION   the system and the constraint, in one sentence
TASK        what you had to achieve or find out
ACTION      the steps, in order, including what you ruled out and how
RESULT      what happened, with numbers
REFLECTION  what you would change, or what it taught you about the class of problem
```

Worked example from Day 3, about two minutes when spoken:

> **Situation.** I had a containerised scikit-learn model running as a Kubernetes Job with a restricted security context. **Task.** I wanted to understand how a model container fails when its memory limit is wrong, because that is the most common startup failure for inference workloads. **Action.** I first measured the process's real peak memory, about 150 MiB, and set requests and limits at 192 and 384 MiB; the Job completed in two seconds. Then I redeployed with a 32 MiB limit. The pod showed `OOMKilled`, and `kubectl logs` was empty, so I went to `describe`: exit code 137, meaning SIGKILL from the kernel's OOM killer, and the Job failed after two attempts because I had set `backoffLimit: 1`. I also found that reproducing it with plain `docker run --memory` did not kill the process, because Docker allows swap by default. **Result.** I could size the container from arithmetic rather than trial and error, and I know the signature of a startup OOM: exit 137 and no logs. **Reflection.** For a real model server I would run Guaranteed QoS and alert on pods that terminate with 137 during startup, because the logs will never tell you.

Every lab in this course can produce one of these. Write the "interview line" in your journal the same day; expand it into the five-part story when you prepare for interviews.

Where Phase 00 alone puts you on a CV:

| What you did | CV bullet |
|---|---|
| Lab 0.1 | Trained, versioned and checksummed a scikit-learn classifier; measured single-request vs batched inference latency (35 ms vs 8 ms per item) |
| Lab 0.2 | Containerised a model with pinned dependencies, build-time training and a non-root user; measured a 579 MB image and 1.85 s cold start and explained both |
| Lab 0.3 | Deployed the model as a Kubernetes Job with calculated memory limits and a restricted security context; deliberately induced and diagnosed `OOMKilled` (exit 137) |

Those are modest bullets. By Phase 09 you will have "built a read-only Kubernetes investigation agent with policy and approval gates and an audit log", and by Phase 14, "deployed vLLM on a GPU node pool with autoscaling and GPU monitoring, provisioned with Terraform".

### 8. The career map

The course prepares you for a family of roles. They overlap heavily; the titles vary by company more than the work does.

| Role | Day-to-day | Phases that matter most | Interviews focus on |
|---|---|---|---|
| **DevOps Engineer (AI/ML)** | Deploying and operating AI services alongside everything else | 01, 07, 12, 14 | Kubernetes, CI/CD, observability, plus "what is different about AI workloads" |
| **MLOps Engineer** | Training pipelines, model registry, deployment, drift | 04, 05, 10, 12 | The ML lifecycle, reproducibility, rollback, monitoring |
| **LLMOps Engineer** | Prompt and model versioning, evaluation, gateways, cost | 07, 08, 11, 16 | Evaluation, tracing, routing, cost per token |
| **AI Platform / ML Platform Engineer** | Building the internal platform other teams deploy models on | 10, 11, 13, 14, 15 | Multi-tenancy, GPU scheduling, self-service, guardrails |
| **AI Infrastructure Engineer** | GPUs, inference servers, node pools, storage for weights | 06, 13, 14, 16 | GPU sizing, inference performance, utilisation, cost |
| **AI SRE** | Reliability of AI services: SLOs, incidents, capacity | 12, 15, 16, 17 | Incident walkthroughs, SLO design, failure modes |

Pick a target role now, loosely. It changes nothing about which phases you do (all of them), but it tells you which interview questions to rehearse hardest and which project to polish most.

### 9. Common misconceptions

- **"Certificates prove skills."** They prove you passed an exam. A repository with measured numbers and a troubleshooting document proves you operated a system. Have both if you like; the second one gets the interview.
- **"I will write the documentation at the end."** You will not remember the numbers, the errors or the dead ends. Write it the same day, in the journal, in ten minutes.
- **"A portfolio project must be original."** It must be *yours*: built by you, run by you, broken by you, documented by you. Eight people can build the same DevOps Knowledge Assistant and produce eight different, equally valid portfolios, because the troubleshooting sections will all be different.
- **"I need to finish the whole course before applying."** Start applying when you have Projects 1, 3 and 4 and can tell the Day 3 story. The rest of the course continues while you interview, and interviews will tell you which phases to prioritise.
- **"The notebook is the deliverable."** A notebook is where exploration happens. The deliverable is a repository with a README, a Dockerfile, manifests and documentation that someone else can run.
- **"More repositories look better."** Eight finished projects with documentation beat forty empty ones. Archive experiments; publish finished work.

## Why does a DevOps Engineer need to know this?

Because your existing experience is your advantage, and this is how you make it visible. Teams hiring for AI infrastructure roles have a shortage of people who can *operate* systems and a surplus of people who can *talk about* models. An operator who can explain what an inference server does, size a GPU from a parameter count, and diagnose an OOM from an exit code is rare and in demand. But nobody will know you can do those things unless the evidence is where they look: a README with numbers, a troubleshooting document with real errors, and a two-minute story you can tell without notes.

Every ops story you already have is worth more once you can pair it with its AI twin. "I have handled OOM kills for years" is good. "I have handled OOM kills for years, and here is how I size model containers so they do not happen, with the arithmetic" is a hire.

### Real-world scenario: two candidates

Two people finish the same course and apply for the same AI Platform Engineer role.

The first has a profile with a list of completed modules and three repositories: a fork of the course with no changes, a notebook called `experiments.ipynb`, and a project repository whose README says "TODO". In the interview they are asked to describe a production issue they debugged; they describe one from a previous job, which is fine, and are asked what is different about AI workloads; they give a definition of inference.

The second has a portfolio repository with a journal going back eight months, a progress checklist with Phases 00–14 ticked, and eight project repositories. The reviewer opens Project 7. The README's first screen has a diagram, a table with measured tokens per second, GPU memory and cost per hour, and a section titled "Failure modes I tested" with five entries. `TROUBLESHOOTING.md` has an entry called "vLLM crashed on startup with a CUDA out-of-memory error at `max_model_len` 32768" with the diagnosis and the fix. In the interview, asked about a production issue, they tell that story in two minutes with numbers.

Same course. Same labs. One of them did Day 4.

## Mental model

**Every lab is a portfolio commit and an interview story.** Not later, not "when the project is done": today, in ten minutes, in the journal. The course produces the skills; the journal and the repositories produce the evidence; the evidence produces the interviews.

## Architecture

The layout you build in today's lab, and grow for the rest of the course:

```text
ai-devops-portfolio/                 one repository: evidence and progress
├── README.md                        who you are, what this is, links to the projects
├── learning-journal.md              one entry per lesson, newest first
├── PROGRESS.md                      the course checklist, ticked as you go
├── .gitignore                       artifacts, virtualenvs, .env, caches
└── phase-00/
    └── README.md                    what you built and measured in Orientation

project-1-kubernetes-health-api/     one repository per project, from Phase 01
├── README.md · ARCHITECTURE.md · SETUP.md · OPERATIONS.md
├── TROUBLESHOOTING.md · SECURITY.md · COST.md
└── src/ · Dockerfile · k8s/ · tests/

project-3-production-llm-api/ ...    and so on through Project 8
```

## Hands-on lab 0.4 — Set up your learning journal and portfolio {#hands-on-lab-0-4-set-up-your-portfolio}

**Objective:** create the portfolio repository, write journal entries for Days 1–3 from your own measurements, document Phase 00 in the project-documentation style, tick the checklist, and rehearse one interview story out loud.

**Difficulty:** 🟢 Beginner · **Estimated time:** 45–60 minutes.

**Prerequisites:** Days 1–3 done, with your measured numbers available (the lab outputs, or your terminal history). Git configured with your name and email. Optionally the GitHub CLI (`gh`) authenticated.

**Architecture:** the portfolio layout above.

**Environment requirements:** Git. Nothing else. No cloud resources; publishing to GitHub is optional and free.

### Setup

Check your Git identity; commits without one are a common first-time stumble.

```bash
git config --global user.name
git config --global user.email
# If either is empty:
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Steps

**Step 1. Create the repository and copy the templates.** Work anywhere outside the course checkout.

```bash
mkdir ai-devops-portfolio && cd ai-devops-portfolio
git init -b main

COURSE=../ai-devops        # adjust to wherever you cloned the course
cp "$COURSE/examples/templates/learning-journal.md" .
cp "$COURSE/examples/templates/PROGRESS.md" .
cp "$COURSE/.gitignore" .
mkdir phase-00
```

**Step 2. Write the README.** Short. Who you are in one line, what this repository is, and where the projects will be linked. Replace the placeholders.

```bash
cat > README.md <<'EOF'
# AI for DevOps — portfolio

Working through the [AI for DevOps](https://github.com/rairamjee/ai-devops) curriculum: from DevOps engineer to AI platform engineer, one lab at a time.

- [Learning journal](learning-journal.md) — one entry per lesson, with what I ran, what broke, and what I learned
- [Progress](PROGRESS.md) — the course checklist
- [Phase 00 — Orientation](phase-00/README.md) — first model, first container, first Kubernetes Job and first deliberate OOM

## Projects

| # | Project | Status |
|---|---|---|
| 1 | Kubernetes Health API | not started |
| 3 | Production LLM API | not started |
| 4 | DevOps Knowledge Assistant | not started |
EOF
```

**Step 3. Write three journal entries**, for Days 1, 2 and 3, using the six prompts and **your own numbers**. Open `learning-journal.md`, read the example entry, then delete it and write yours. Do not copy from the lessons; the point is retrieval. If you cannot remember a number, run the lab step again; it takes seconds.

Aim for ten minutes per entry. Make sure each has an "interview line" with a number in it.

**Step 4. Document Phase 00** in `phase-00/README.md` using the shape of the project README template: what you built, a measured-numbers table, and failure modes you tested.

```bash
cat > phase-00/README.md <<'EOF'
# Phase 00 — Orientation

What I built: a scikit-learn pod-health classifier, trained and versioned locally (Lab 0.1), packaged into a pinned, non-root container image (Lab 0.2), and run as a Kubernetes Job with calculated memory limits, then deliberately OOM-killed and diagnosed (Lab 0.3).

## Measured numbers

| Metric | Value | How measured |
|---|---|---|
| Training time (10k rows, 100 trees) | | `train_and_predict.py` [train] line |
| Artifact size | | `ls -la artifacts/` |
| Test accuracy / unhealthy recall | | classification report |
| Single-row vs batched inference | | [predict] and [batch] lines |
| Image size | | `docker image ls` |
| Cold container start (wall clock) | | `time docker run --rm pod-health:v1` |
| Peak memory | | `docker stats` sampling |
| Job created → finished | | pod timestamps |

## Failure modes I tested

- 32Mi memory limit: `OOMKilled`, exit 137, empty logs, Job `BackoffLimitExceeded` after 2 pods.
- Named `USER app` with `runAsNonRoot`: `CreateContainerConfigError`; fixed with a numeric UID.
- `docker run --memory=64m` did not kill the process (swap); `--memory-swap=64m` did.
- (Part B) Pretrained sentiment model confidently mislabelled two operational messages: a model can be up, fast and wrong.

## What I would do next

EOF
```

Fill in every blank with your numbers, then write two lines under "What I would do next".

**Step 5. Tick Phase 00** in `PROGRESS.md`: lessons 4 / 4, labs 4 / 4, and the Done box.

**Step 6. Commit, in small steps, with messages that say why.**

```bash
git add README.md .gitignore
git commit -m "Start AI for DevOps portfolio: README and ignore rules"
git add learning-journal.md
git commit -m "Journal: Phase 00 Days 1-3 with measured numbers"
git add phase-00/README.md PROGRESS.md
git commit -m "Phase 00 write-up: first model, container, Kubernetes Job and OOM diagnosis"
git log --oneline
```

**Step 7 (optional). Publish.** With the GitHub CLI authenticated:

```bash
gh repo create ai-devops-portfolio --public --source=. --push
```

Or create an empty repository in the GitHub web interface and follow its "push an existing repository" instructions. Check the README renders the way you expect.

**Step 8. Rehearse.** Set a two-minute timer and tell the Day 3 OOM story out loud in the five-part shape, from memory, with your numbers. If you run over, cut the action steps to the three that mattered. Do it twice.

### Expected output

```text
$ tree -a -I .git ai-devops-portfolio
ai-devops-portfolio
├── .gitignore
├── PROGRESS.md
├── README.md
├── learning-journal.md
└── phase-00
    └── README.md

$ git log --oneline
3f2a9c1 Phase 00 write-up: first model, container, Kubernetes Job and OOM diagnosis
b71e04d Journal: Phase 00 Days 1-3 with measured numbers
a0c8e5f Start AI for DevOps portfolio: README and ignore rules
```

Read it as a reviewer would: the README says what this is in one line, links to evidence, and has a table that will fill up. The journal has three dated entries with numbers. The phase write-up has a measured-numbers table and a list of failure modes tested. Three commits, each with a reason.

### Validation

You have completed the lab when:

- [ ] The repository exists with the five files above and at least three commits.
- [ ] Every journal entry has an "interview line" containing a number you measured.
- [ ] `phase-00/README.md` has no blank cells in the numbers table.
- [ ] Phase 00 is ticked in `PROGRESS.md`.
- [ ] You told the Day 3 story out loud in under two minutes, twice.
- [ ] Nothing in the repository is a secret, a model artifact, or a virtual environment (`git status --ignored` shows them ignored, or they are simply absent).

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `Author identity unknown` on commit | Git has no name or email configured | The two `git config --global` lines in Setup |
| `git init -b main` fails with `unknown switch 'b'` | Git older than 2.28 | `git init` then `git branch -M main` |
| `gh: command not found` or `gh auth` errors | GitHub CLI not installed or not logged in | Install from the [GitHub CLI docs](https://cli.github.com/), then `gh auth login`; or use the web interface |
| You committed `artifacts/` or `.venv/` | `.gitignore` copied after the files were added | `git rm -r --cached artifacts .venv`, commit; they stay on disk, leave the history |
| You committed a secret | It is in the history now | Rotate the secret immediately. Then remove it from the file and commit. Rewriting history is optional; rotation is not. |
| Journal entries feel like summaries of the lesson | Writing with the lesson open | Close it. Write from memory. Then check and correct. |

### Common mistakes

- **Writing the journal from the lesson instead of from memory.** The entry becomes notes, not retrieval, and the numbers are the lesson's rather than yours.
- **One commit called "initial commit".** Three commits with reasons tell a reviewer more than the content does.
- **Copying the templates in and leaving the prompts.** A README that still says "Three to five bullets. Lead with the outcome" is worse than no README.
- **Including your employer's hostnames, cluster names or data** in examples. Use the course's synthetic examples or invent your own.
- **Waiting to publish until it is "good enough".** Publish now; improve in public. Iteration is the signal.

### Cleanup

Nothing to clean up. This repository is meant to persist and grow.

### Extension challenge

1. **Profile README.** Create a GitHub profile README (a repository named after your username) that links to the portfolio and states the target role from the career map in one sentence.
2. **Second story.** Prepare the Day 1 Part B "confidently wrong model" observation as a two-minute story in the five-part shape. It answers a different interview question: "what is different about operating AI systems?"
3. **Calendar.** Block the study hours for the next four weeks in your calendar, with the phases named. Add a recurring fifteen-minute slot on Fridays to redo one earlier quiz closed-book.

### Questions

1. Which of the five things a reviewer looks at does your portfolio already have after today, and which will Phase 01 add?
2. Why does the journal ask for the exact error text rather than a description of the error?
3. What is the difference between "removing a committed secret from the file" and "rotating it", and why does the second one matter more?

## Exercise

1. **CV bullet.** Write one CV bullet for Phase 00 in your own words, with at least two measured numbers. Compare with the table in the lesson. Keep it in the portfolio README under a "Highlights" heading if you like it.
2. **Target role.** Pick one role from the career map. From the [interview prep](/interview-prep/) page, choose three questions that role's interviewers would ask, and write the phase you expect to answer each in.
3. **Closed-book retest.** Take the Day 1 quiz again without notes. Score yourself. Any question you miss, write its answer in your journal in your own words.
4. **Predict Phase 01.** Read the [Phase 01 overview](../01-python/). Write three sentences on what you expect to find hard and why. You will check this prediction at the Phase 01 checkpoint.

## Quiz

**1. What is the course's target ratio of theory, reading and hands-on, and what should you do if you notice you have been reading for an hour?**

::: details Answer
30% theory, 20% reading, 50% hands-on. Stop and run something; the concepts are designed to be understood after the lab as much as before it.
:::

**2. Name the five steps of the learning loop and say which one most people skip.**

::: details Answer
Run, break, fix, explain, apply. Most people skip "break" (changing one thing and predicting the result) and "explain" (saying it in their own words with numbers).
:::

**3. What is the diagnostic order for a failing pod, and why does it matter for model workloads especially?**

::: details Answer
Status → describe → logs → events. Model containers often die at startup (OOM, config errors) before writing any logs, so `describe` and events carry the evidence and logs are empty.
:::

**4. Give two acceptable and two unacceptable uses of an AI assistant while working through this course.**

::: details Answer
Acceptable: explaining a concept differently; interpreting an error and suggesting where to look; generating practice questions; reviewing your explanation. Unacceptable: running the lab for you; writing your journal or documentation; being the source of truth for versions and flags; handling secrets or employer data.
:::

**5. What are the six prompts of a journal entry?**

::: details Answer
What I ran; what broke; what I did about it; what I understand now; interview line; open questions.
:::

**6. In order, what does a reviewer look at in the first ninety seconds on a repository?**

::: details Answer
The README's first screen (what it is, architecture sketch); measured numbers with methods; failure modes tested; commit history; the documentation set.
:::

**7. Why is a troubleshooting document more convincing than a working demo?**

::: details Answer
Anyone can make a demo work once. Real errors, real diagnoses and deliberate breakage prove the system was operated and understood, which is what the job is.
:::

**8. What is the five-part shape for an interview story, and what does the fifth part add to STAR?**

::: details Answer
Situation, task, action, result, reflection. Reflection shows you generalised from the incident: what you would change, or what it taught you about the class of problem.
:::

**9. You accidentally committed an API token. What is the fix, and what is not the fix?**

::: details Answer
Rotate the token immediately; then remove it from the file. Deleting the commit or rewriting history is not the fix, because the token is already in history and may already be indexed.
:::

**10. When should you start applying for roles, according to the lesson?**

::: details Answer
When you have Projects 1, 3 and 4 and can tell a lab story with numbers from memory. Interviews then inform which phases to prioritise while you continue.
:::

## Interview questions

These are the behavioural questions every infrastructure interview includes. Prepare answers in the five-part shape, from your journal.

1. **"Tell me about a project you have built recently."** Pick the most complete project repository you have. Lead with what it does and one measured number, then the architecture in three sentences, then one failure mode you tested and what it taught you.
2. **"Describe a production issue you debugged and how."** Until you have a later phase's story, use Day 3: measured peak memory, deliberate OOM, exit 137, empty logs, `describe` first, Job backoff, and the Docker swap surprise. Numbers throughout.
3. **"How do you learn a new technology?"** Describe the loop: run it, break one thing with a prediction, fix it from signals, explain it in writing, connect it to something you operate. Mention the journal and closed-book retests as evidence you actually do this.
4. **"What is different about operating AI systems?"** Use Day 1 Part B: a model that was up, fast, and 99% confident on a wrong answer; nothing in conventional monitoring would have caught it. Then the Day 3 list: memory calculated from parameters, startup measured in seconds to minutes, GPUs as a scarce scheduled resource, quality as a separate signal.
5. **"Why do you want to move into AI infrastructure?"** Your own answer. Pair your existing operations experience with the AI twin of a problem you already know; say which role from the career map you are aiming at and why.
6. **"How do you use AI tools in your work?"** The rules from this lesson: as a tutor and hypothesis generator, never as a source of truth or an executor of unreviewed commands; verify against documentation; keep secrets out. Interviewers are increasingly listening for judgement here, not enthusiasm.

## Further exploration

- [GitHub: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes): what renders, where, and how profile READMEs work.
- [Google SRE Book: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/): the mindset behind the troubleshooting document and the journal's "what broke" prompt.
- [Conventional Commits](https://www.conventionalcommits.org/): a widely used convention for commit messages; the course repository uses it.
- [GitHub CLI manual](https://cli.github.com/manual/): `gh repo create` and friends, for publishing from the terminal.

## Key takeaways

- 30/20/50. The checkpoint is a gate. Repeat labs; do not skip them.
- Run, break, fix, explain, apply. Predict before you act; retrieve instead of re-reading.
- When stuck: read the exact error, locate the layer, status → describe → logs → events, reduce, official docs, search the string, ask a good question. Timebox 30–45 minutes.
- AI assistants are tutors, not executors and not sources of truth. Type every command; ask why; verify.
- Ten minutes of journal per lesson produces retrieval, evidence and eighty interview lines.
- Reviewers look at the README's first screen, measured numbers, failure modes tested, commit history and the documentation set, in that order.
- Every lab is a portfolio commit and an interview story, the same day.

## Checkpoint

Phase 00 is complete when you can, without notes:

- Explain AI, ML, deep learning and LLMs, training versus inference, and what a model physically is (Day 1).
- Run the verification script clean, explain the Dockerfile line by line, and state where an AI image's size and startup time come from (Day 2).
- Draw the master architecture, name what you own at each layer, compute a memory request, and diagnose an `OOMKilled` pod (Day 3).
- Show a portfolio repository with three dated journal entries, a Phase 00 write-up with measured numbers, and tell one lab story in two minutes (Day 4).

Next: [Phase 01 — Python for AI/DevOps](../01-python/), where you build the FastAPI service and Kubernetes integration that every later project stands on, and turn today's Job into a Deployment. Back to the [Phase 00 overview](./index.md).
