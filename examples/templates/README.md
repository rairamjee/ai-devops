# Templates

Copy these into your own portfolio repository. They are the documentation standard every project in this course ships with, plus a learning-journal format that turns each lab into an interview story.

```text
templates/
├── learning-journal.md          one entry per lesson: what you ran, broke, fixed, learned
├── PROGRESS.md                  the learner checklist from the course, to tick in your fork
└── project-docs/                the required documentation set for every project
    ├── README.md                what it is, how to run it, measured numbers up front
    ├── ARCHITECTURE.md          components, data flow, decisions and trade-offs
    ├── SETUP.md                 reproducible setup from a clean machine
    ├── OPERATIONS.md            deploy, scale, upgrade, roll back, day-to-day
    ├── TROUBLESHOOTING.md       failure modes you met and how you diagnosed them
    ├── SECURITY.md              threat surface, controls, secrets handling
    ├── COST.md                  what it costs to run and how to reduce it
    ├── RUNBOOK.md               (where applicable) step-by-step responses to alerts
    ├── SLO.md                   (where applicable) SLIs, SLOs, error budget
    ├── THREAT-MODEL.md          (where applicable) assets, attackers, entry points, mitigations
    └── DISASTER-RECOVERY.md     (where applicable) backups, restore, RTO/RPO
```

## How to use them

1. Create one repository per project (or one directory per project in a single portfolio repository).
2. Copy `project-docs/` into it and fill each file in as you build. Do not leave the prompts in; replace them with your content and delete sections that genuinely do not apply, saying why in one line.
3. Keep `learning-journal.md` at the root of your portfolio and add an entry per lesson, the same day.
4. Every number you write down (latency, size, cost, startup time) should be one you measured. Say how.

See [Day 4 — How to Work Through This Course](../../docs/curriculum/00-orientation/04-how-to-learn-and-build-your-portfolio.md) for the reasoning behind each file.
