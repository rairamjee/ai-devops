# Lab 0.2 — Put the Day 1 model in a container.
#
# This image does two things that real model images do:
#   1. It pins the RUNTIME: a specific Python, specific library versions.
#   2. It carries the ARTIFACT: the model is produced at build time and baked
#      into the image, so the running container never trains, only serves.
#
# For a 6 MB model, baking it in is fine. For multi-gigabyte LLM weights you
# would mount them from a volume or cache instead (Phase 14); the principle
# "runtime and artifact are versioned together" stays the same.

# Pin the base image. `python:3.12-slim` is Debian-based and small (~190 MB).
# Never use `latest` for anything you want to reproduce.
FROM python:3.12-slim

# Do not buffer stdout: logs appear immediately in `docker logs` / kubectl logs.
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install dependencies first, on their own layer, so code changes do not
# force a reinstall. This is the single biggest Docker-build-time saver.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Now the code.
COPY train_and_predict.py predict.py ./

# Train at BUILD time and store the artifact in the image. Build arguments
# let you produce a v2 image without touching the Dockerfile.
ARG MODEL_VERSION=v1
ARG LABEL_THRESHOLD=5.0
RUN python train_and_predict.py --version "${MODEL_VERSION}" --threshold "${LABEL_THRESHOLD}" --out /model \
    && ls -la /model

# Tell predict.py where the artifact lives. Overridable at run time.
ENV MODEL_PATH=/model/pod-health-model-${MODEL_VERSION}.joblib

# Run as a non-root user. Secure default; also what Kubernetes admission
# policies commonly require. Use the NUMERIC uid, not the name: with
# `runAsNonRoot: true` Kubernetes cannot verify a named user is non-root and
# refuses to start the container (CreateContainerConfigError).
RUN useradd --create-home --uid 10001 app && chown -R app:app /app /model
USER 10001

# The container's job: load the model, predict, exit.
ENTRYPOINT ["python", "predict.py"]
