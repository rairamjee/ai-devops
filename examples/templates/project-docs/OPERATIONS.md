# Operations

How to run this system day to day. Written for the person on call, who may not be you.

## Deploy

How a new version reaches production: build, test, promote, roll out. Which pipeline; which gates; how long it takes; how you know it worked.

## Roll back

The exact procedure and how long it takes. For AI projects: rolling back the code, the model version and the prompt version are three different actions. Cover each.

## Scale

What to scale, on which signal, with what limits. What the system does at the limit (shed, queue, degrade).

## Upgrade dependencies

How to bump the base image, libraries, and (for AI projects) the model or the inference server, safely.

## Routine tasks

Anything periodic: rotate secrets, refresh an index, retrain, clean up storage.

## Health and readiness

What the probes check and why. For model servers: what "ready" means (weights loaded, warm-up done) and how long it takes.

## Dashboards and alerts

Where to look. Which alerts exist, what each means, and which [RUNBOOK](RUNBOOK.md) entry answers it.

## Capacity

Current headroom and what you would do at 2× and 10× load.
