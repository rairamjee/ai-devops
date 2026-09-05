# Cost

What this system costs to run and what drives it. Numbers, not adjectives.

## Cost model

| Component | Unit | Rate | Quantity | Monthly |
|---|---|---|---|---|
| Compute (CPU nodes) | | | | |
| GPU nodes | | | | |
| Storage | | | | |
| Network / egress | | | | |
| Model API tokens | | | | |
| **Total** | | | | |

State your assumptions (traffic, hours per day, region) and where the rates came from.

## Cost per request

Total ÷ requests. For LLM features, also cost per 1,000 tokens in and out. How you measured request and token counts.

## Idle cost

What it costs when nobody is using it. For GPU-backed systems this is usually most of the bill.

## Levers

Ranked by expected saving, with the trade-off for each: utilisation and batching, caching, autoscaling to zero, smaller or quantised models, routing, right-sizing, reserved capacity.

## What I changed and what it saved

Before and after numbers for any optimisation you actually applied.
