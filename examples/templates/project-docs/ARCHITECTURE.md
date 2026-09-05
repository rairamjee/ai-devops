# Architecture

## Context

What problem this system solves and what it deliberately does not do. Who calls it; what it depends on.

## Components

One subsection per component. For each: responsibility, technology, why that technology (and what you considered instead), how it scales, how it fails.

### Component A

## Data flow

Follow one request end to end. Where does latency accumulate? Where can it fail? A numbered list or a sequence diagram.

## Model flow (AI projects)

How the model artifact gets from training or download to memory: registry, storage, cache, load. Which version is running and how you can prove it.

## Decisions and trade-offs

A table. The most useful section for interviews.

| Decision | Options considered | Chosen | Why | What it costs us |
|---|---|---|---|---|
| | | | | |

## Scaling story

What happens at 10× traffic? Which component saturates first, what is the signal, and what is the lever?

## Failure story

What happens when each component fails? What does the user see? How does the system recover?

## Non-goals and future work

What you left out on purpose, and what you would add next.
