# Disaster recovery

## Objectives

| | Target | Justification |
|---|---|---|
| RTO (time to restore service) | | |
| RPO (acceptable data loss) | | |

## What must survive

State that cannot be rebuilt from code: databases, vector indexes, model registry, trained artifacts, secrets. For each: where it lives, how it is backed up, how often, where the backups are, and when a restore was last tested.

| State | Location | Backup method | Frequency | Last restore test |
|---|---|---|---|---|
| | | | | |

## What can be rebuilt

Everything in Infrastructure as Code and container images. How long a rebuild from scratch takes, measured.

## Scenarios

For each: detection, response steps, expected recovery time.

- Loss of a node or node pool (including the GPU pool)
- Loss of the cluster
- Loss of the model registry or object storage
- Corrupted or wrong model version deployed
- Loss of the vector database

## Restore drill

When you last practised a restore, what broke, and what you changed.
