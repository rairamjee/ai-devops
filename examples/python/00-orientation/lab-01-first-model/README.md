# Lab 0.1 — Run Your First Model

Code for [Day 1 — What Is AI?](../../../../docs/curriculum/00-orientation/01-what-is-ai.md). The lesson has the full walkthrough, expected output, troubleshooting and exercises; this README is the quick start.

🟢 Beginner · 30–45 min · CPU only · no cloud resources · no credentials.

## Part A — train, save, load, predict

```bash
python3 -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python train_and_predict.py
ls -la artifacts/
```

`train_and_predict.py` generates synthetic pod telemetry, trains a random-forest classifier that predicts whether a pod is unhealthy, evaluates it on held-out data, saves it as a versioned artifact with a checksum, reloads it, and times single-row inference.

Options: `--version v2 --threshold 2.0` retrains under a stricter definition of "unhealthy" (used by the lesson's exercise). `--samples`, `--seed`, `--out` are also available; run with `--help`.

## Part B (optional) — run a pretrained transformer

Downloads about 268 MB of model weights on first run, plus the CPU build of PyTorch (a few hundred MB). Skip it if you are on a slow connection; the lesson covers what it shows.

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements-pretrained.txt
python pretrained_inference.py
```

Set `HF_HOME=/some/path` to control where weights are cached.

## Cleanup

```bash
rm -rf artifacts/ .venv/
rm -rf ~/.cache/huggingface/hub/models--distilbert-base-uncased-finetuned-sst-2-english   # Part B weights
```
