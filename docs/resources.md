# Resources

The course prefers **official documentation, official tutorials and primary technical sources**. AI tooling moves fast: before following any implementation steps, check the current version of the documentation linked here. Lessons cite the exact version they were written against.

## Foundations

| Topic | Resource | Why |
|---|---|---|
| Python | [docs.python.org — Tutorial](https://docs.python.org/3/tutorial/) | The reference for the language itself. |
| Python packaging | [Python Packaging User Guide](https://packaging.python.org/) | Virtual environments, `requirements.txt`, `pyproject.toml`. |
| FastAPI | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) | Every API in the course is built with FastAPI. |
| NumPy | [numpy.org/doc](https://numpy.org/doc/stable/) | Arrays, vectors, matrices; the substrate under everything. |
| scikit-learn | [scikit-learn.org — User Guide](https://scikit-learn.org/stable/user_guide.html) | Classical ML used in Phases 00 and 04. |

## Deep learning, transformers and LLMs

| Topic | Resource | Why |
|---|---|---|
| PyTorch | [pytorch.org/tutorials](https://pytorch.org/tutorials/) | The primary deep-learning framework in this course. |
| PyTorch install | [pytorch.org/get-started](https://pytorch.org/get-started/locally/) | Selecting the correct CPU or CUDA build. |
| Hugging Face Transformers | [huggingface.co/docs/transformers](https://huggingface.co/docs/transformers/index) | Loading, running and inspecting pretrained models. |
| Hugging Face Hub | [huggingface.co/docs/hub](https://huggingface.co/docs/hub/index) | Model cards, model files, cache layout. |
| Hugging Face LLM course | [huggingface.co/learn/llm-course](https://huggingface.co/learn/llm-course) | Free, well-maintained conceptual grounding for transformers and LLMs. |
| Tokenizers | [huggingface.co/docs/tokenizers](https://huggingface.co/docs/tokenizers/index) | How text becomes tokens. |
| vLLM | [docs.vllm.ai](https://docs.vllm.ai/) | The primary inference server in the course. |
| CUDA | [NVIDIA CUDA documentation](https://docs.nvidia.com/cuda/) | GPU programming model and toolkit. |
| NVIDIA Container Toolkit | [docs.nvidia.com/datacenter/cloud-native/container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html) | Running GPU workloads in containers. |
| NVIDIA GPU Operator | [docs.nvidia.com/datacenter/cloud-native/gpu-operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html) | GPU drivers, device plugin and monitoring on Kubernetes. |

## Data, retrieval and operations

| Topic | Resource | Why |
|---|---|---|
| PostgreSQL | [postgresql.org/docs](https://www.postgresql.org/docs/) | Primary database. |
| pgvector | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) | Vector search inside PostgreSQL for RAG. |
| MLflow | [mlflow.org/docs](https://mlflow.org/docs/latest/) | Experiment tracking, model registry, deployment. |
| Prometheus | [prometheus.io/docs](https://prometheus.io/docs/introduction/overview/) | Metrics. |
| Grafana | [grafana.com/docs](https://grafana.com/docs/grafana/latest/) | Dashboards and alerting. |
| Grafana Loki | [grafana.com/docs/loki](https://grafana.com/docs/loki/latest/) | Logs. |
| OpenTelemetry | [opentelemetry.io/docs](https://opentelemetry.io/docs/) | Traces and instrumentation. |

## Infrastructure

| Topic | Resource | Why |
|---|---|---|
| Docker | [docs.docker.com](https://docs.docker.com/) | Containers. |
| Kubernetes | [kubernetes.io/docs](https://kubernetes.io/docs/home/) | Orchestration. Pay special attention to scheduling, resources and device plugins. |
| Kubernetes device plugins | [Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) | How GPUs are exposed to pods. |
| kind | [kind.sigs.k8s.io](https://kind.sigs.k8s.io/) | Local Kubernetes for labs. |
| Minikube | [minikube.sigs.k8s.io](https://minikube.sigs.k8s.io/docs/) | Alternative local Kubernetes. |
| Terraform | [developer.hashicorp.com/terraform/docs](https://developer.hashicorp.com/terraform/docs) | Infrastructure as code. |
| AWS | [docs.aws.amazon.com](https://docs.aws.amazon.com/) | Primary cloud. EC2 accelerated instances, EKS, S3, IAM. |

## Security

| Topic | Resource | Why |
|---|---|---|
| OWASP Top 10 for LLM Applications | [genai.owasp.org](https://genai.owasp.org/) | The standard reference for prompt injection, data leakage, tool abuse and related risks. |
| Kubernetes security | [Securing a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/) | RBAC, network policies, secrets. |

## How to use this page

- Read documentation *alongside* labs, not instead of them. The target ratio is 30% theory, 20% reading, 50% hands-on.
- When a lesson links to a specific page, that link is the one to read first.
- If a link is outdated, open an issue or a pull request; see the contributing guide in the repository.
