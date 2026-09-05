# Runbook

One entry per alert. Written so that someone who has never seen the system can act at 3 a.m.

## Alert: name exactly as it appears in the alerting system

**Severity:** page / ticket.
**Meaning:** one sentence on what is wrong for users.
**Dashboard:** link.

### Check

Commands in order, each with what a healthy and an unhealthy result look like.

```bash
```

### Likely causes

Ranked. Link to [TROUBLESHOOTING.md](TROUBLESHOOTING.md) entries.

### Mitigate

The safe action that restores service (scale, roll back, fail over, disable a feature). What it costs and how to reverse it.

### Escalate

Who, and with what information.

### Afterwards

What to record; whether a post-mortem is required.
