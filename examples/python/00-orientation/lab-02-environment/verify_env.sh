#!/usr/bin/env bash
# Lab 0.2 — Verify your environment.
#
# Read-only: this script checks tools and versions, it never installs or
# changes anything. It prints one line per check and exits non-zero if a
# REQUIRED check fails, so you can also use it in CI or a new laptop setup.
#
# Usage:
#   ./verify_env.sh              # all checks
#   ./verify_env.sh --no-docker  # skip checks that need the Docker daemon
#   ./verify_env.sh --cluster ai-devops-lab   # also check a kind cluster by name

set -u

SKIP_DOCKER=0
CLUSTER=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-docker) SKIP_DOCKER=1; shift ;;
    --cluster)   CLUSTER="${2:-}"; shift 2 ;;
    -h|--help)   sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

# Minimum versions the course assumes.
MIN_PYTHON_MAJOR=3
MIN_PYTHON_MINOR=10
MIN_DISK_GB=15
MIN_RAM_GB=8

PASS=0; FAIL=0; WARN=0
ok()   { printf '  ✅ %-14s %s\n' "$1" "$2"; PASS=$((PASS+1)); }
bad()  { printf '  ❌ %-14s %s\n' "$1" "$2"; FAIL=$((FAIL+1)); }
warn() { printf '  ⚠️  %-14s %s\n' "$1" "$2"; WARN=$((WARN+1)); }
have() { command -v "$1" >/dev/null 2>&1; }

echo "AI for DevOps — environment check"
echo "=================================="

# ---------------------------------------------------------------- platform
OS="$(uname -s)"; ARCH="$(uname -m)"
if grep -qi microsoft /proc/version 2>/dev/null; then OS="Linux (WSL2)"; fi
ok "platform" "$OS $ARCH"

# ------------------------------------------------------------------ python
if have python3; then
  PYV="$(python3 -c 'import sys; print("%d.%d.%d" % sys.version_info[:3])')"
  PYMAJ="${PYV%%.*}"; PYMIN="$(echo "$PYV" | cut -d. -f2)"
  if [[ "$PYMAJ" -gt "$MIN_PYTHON_MAJOR" || ( "$PYMAJ" -eq "$MIN_PYTHON_MAJOR" && "$PYMIN" -ge "$MIN_PYTHON_MINOR" ) ]]; then
    ok "python3" "$PYV"
  else
    bad "python3" "$PYV found; need >= ${MIN_PYTHON_MAJOR}.${MIN_PYTHON_MINOR}"
  fi
  if python3 -c 'import venv' 2>/dev/null; then ok "venv module" "available"; else bad "venv module" "missing (Debian/Ubuntu: apt install python3-venv)"; fi
  if python3 -m pip --version >/dev/null 2>&1; then ok "pip" "$(python3 -m pip --version | awk '{print $2}')"; else bad "pip" "missing (apt install python3-pip, or use a venv)"; fi
else
  bad "python3" "not found"
fi
if have uv; then ok "uv (optional)" "$(uv --version | awk '{print $2}')"; else warn "uv (optional)" "not installed; pip + venv is fine"; fi

# --------------------------------------------------------------------- git
if have git; then ok "git" "$(git --version | awk '{print $3}')"; else bad "git" "not found"; fi

# ------------------------------------------------------------------ docker
if have docker; then
  ok "docker cli" "$(docker --version | sed -E 's/Docker version ([^,]+),.*/\1/')"
  if [[ "$SKIP_DOCKER" -eq 0 ]]; then
    if docker info >/dev/null 2>&1; then
      ok "docker daemon" "reachable ($(docker info --format '{{.ServerVersion}}, {{.OSType}}/{{.Architecture}}'))"
      if docker run --rm hello-world >/dev/null 2>&1; then
        ok "docker run" "hello-world ran"
      else
        bad "docker run" "could not run hello-world (network? permissions?)"
      fi
    else
      bad "docker daemon" "not reachable (is Docker running? are you in the docker group?)"
    fi
  else
    warn "docker daemon" "skipped (--no-docker)"
  fi
else
  bad "docker cli" "not found"
fi

# ---------------------------------------------------------------- kubectl
if have kubectl; then
  ok "kubectl" "$(kubectl version --client -o json 2>/dev/null | python3 -c 'import sys,json; print(json.load(sys.stdin)["clientVersion"]["gitVersion"])' 2>/dev/null || kubectl version --client 2>/dev/null | head -1)"
else
  bad "kubectl" "not found"
fi

# ------------------------------------------------------------------- kind
if have kind; then
  ok "kind" "$(kind --version | awk '{print $3}')"
  if [[ -n "$CLUSTER" ]]; then
    if kind get clusters 2>/dev/null | grep -qx "$CLUSTER"; then
      ok "kind cluster" "'$CLUSTER' exists"
      if kubectl --context "kind-$CLUSTER" get nodes >/dev/null 2>&1; then
        ok "cluster api" "$(kubectl --context "kind-$CLUSTER" get nodes --no-headers | wc -l | tr -d ' ') node(s) reachable via context kind-$CLUSTER"
      else
        bad "cluster api" "context kind-$CLUSTER not reachable"
      fi
    else
      bad "kind cluster" "'$CLUSTER' not found (kind create cluster --name $CLUSTER)"
    fi
  else
    if [[ -n "$(kind get clusters 2>/dev/null)" ]]; then
      warn "kind cluster" "existing: $(kind get clusters 2>/dev/null | tr '\n' ' ')(pass --cluster NAME to check one)"
    else
      warn "kind cluster" "none yet; create one in Lab 0.2 step 4"
    fi
  fi
else
  bad "kind" "not found (https://kind.sigs.k8s.io/docs/user/quick-start/#installation)"
fi

# --------------------------------------------------------------- resources
if have df; then
  FREE_GB=$(df -Pk . | awk 'NR==2 {printf "%d", $4/1024/1024}')
  if [[ "$FREE_GB" -ge "$MIN_DISK_GB" ]]; then ok "disk free" "${FREE_GB} GB here"; else warn "disk free" "${FREE_GB} GB here; AI labs want >= ${MIN_DISK_GB} GB"; fi
fi
RAM_GB=""
if [[ -r /proc/meminfo ]]; then RAM_GB=$(awk '/MemTotal/ {printf "%d", $2/1024/1024}' /proc/meminfo);
elif have sysctl; then RAM_GB=$(( $(sysctl -n hw.memsize 2>/dev/null || echo 0) / 1024 / 1024 / 1024 )); fi
if [[ -n "$RAM_GB" ]]; then
  if [[ "$RAM_GB" -ge "$MIN_RAM_GB" ]]; then ok "memory" "${RAM_GB} GB"; else warn "memory" "${RAM_GB} GB; some labs assume >= ${MIN_RAM_GB} GB"; fi
fi

# --------------------------------------------------------------- gpu (info)
if have nvidia-smi; then
  ok "gpu (optional)" "$(nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader | head -1)"
else
  warn "gpu (optional)" "no NVIDIA GPU detected; every lab through Phase 12 has a CPU path"
fi

# ----------------------------------------------------------------- summary
echo "----------------------------------"
echo "  passed: $PASS   warnings: $WARN   failed: $FAIL"
if [[ "$FAIL" -gt 0 ]]; then
  echo "  Fix the ❌ items above before continuing. See the Day 2 troubleshooting table."
  exit 1
fi
echo "  Environment ready."
