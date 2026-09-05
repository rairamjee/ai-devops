# Lab 0.3 — Run the model as a Kubernetes Job (and break it)

Manifests for [Day 3 — The AI Production Stack](../../../../docs/curriculum/00-orientation/03-ai-production-stack.md). The lesson has the full walkthrough; this is the quick start.

🟡 Intermediate · 45–60 min · local kind cluster · CPU only · no cloud resources.

## Prerequisites

- The `pod-health:v1` image from Lab 0.2 (`docker build -t pod-health:v1 .` in `examples/python/00-orientation/lab-01-first-model/`).
- A kind cluster: `kind create cluster --name ai-devops-lab`.

## Run

```bash
# Make the local image visible to the cluster's nodes (kind has no registry).
kind load docker-image pod-health:v1 --name ai-devops-lab

# A Job with a sensible memory limit: loads the model, predicts, completes.
kubectl apply -f job.yaml
kubectl wait --for=condition=complete job/pod-health-predict --timeout=120s
kubectl logs job/pod-health-predict

# The same image with a 32 MiB limit: OOMKilled before the model loads.
kubectl apply -f job-oom.yaml
kubectl get pods -l scenario=oom -w        # Ctrl-C once you see OOMKilled
kubectl describe pod -l scenario=oom | grep -A3 -E "Last State|Reason|Exit Code"
```

## What to look at

- `kubectl get pods` STATUS: `Completed` vs `OOMKilled`.
- `kubectl describe pod`: `Exit Code: 137` and `Reason: OOMKilled` under Last State.
- `kubectl logs` of the OOM pod: usually empty, because the process died while importing libraries, before it printed anything. Silence is the symptom.
- Startup time: compare the pod's `Started` and `Finished` timestamps with the `[startup]` line in the logs.

## Cleanup

```bash
kubectl delete -f job.yaml -f job-oom.yaml
kind delete cluster --name ai-devops-lab      # only if you no longer want the cluster
```
