# 🚀 Multi-Agent AI System on Azure AKS

![Deploy to AKS](https://img.shields.io/badge/Deploy-Azure%20AKS-blue?logo=microsoft-azure\&style=flat-square)
![Built with FastAPI](https://img.shields.io/badge/Built%20With-FastAPI-green?logo=fastapi\&style=flat-square)

**Status: early prototype (June 2025). Agents and orchestrator are scaffolded; pipeline wiring and deployment are in progress.**

> **Cloud-Native • Agentic • Modular**

---

## ⚙️ Architecture Summary

| Layer            | Tech                                 | Purpose                                              |
| ---------------- | ------------------------------------ | ---------------------------------------------------- |
| **Agents**       | FastAPI Microservices                | Modular AI behavior: Planning, Research, Summarizing |
| **Orchestrator** | FastAPI API Gateway                  | Central coordinator for agent workflows              |
| **Deployment**   | Docker, Azure AKS (Helm planned)     | Scalable, cloud-native deployment                    |
| **Routing**      | NGINX Ingress Controller             | Routes external requests to internal services        |
| **CI/CD**        | GitHub Actions                       | Build pipeline (deploy planned)                      |
| **Monitoring**   | Azure Monitor / Application Insights | Traces, metrics and logs (optional)                  |

---

## 📁 Directory Structure

```bash
multi-agent-aks-system/
│
├── orchestrator/               # Coordinates all agents
├── agents/
│   ├── planner_agent/          # Task decomposition
│   ├── researcher_agent/       # Info gathering (e.g., web, vector DB)
│   └── summarizer_agent/       # Final output generation
├── .github/workflows/ci.yml    # CI/CD GitHub Actions pipeline
├── k8s-ingress.yaml            # Ingress rules
└── README.md
```

---

## 🚀 Quick Start

☁️ Need AKS setup help? Follow [Azure AKS Quickstart](https://learn.microsoft.com/en-us/azure/aks/)

---

## 🔁 GitHub Actions CI/CD

`.github/workflows/ci.yml` handles:

* ✅ Lint the orchestrator
* 🐳 Build Docker images (orchestrator, planner)
* ⏳ Planned: push to ACR, Helm deploy to AKS

> **Coming soon:** Secrets integration via GitHub & Azure Key Vault

---

## 📊 Azure Monitoring

### 🎯 Application Insights (Optional)

Enable logging and telemetry for each agent by setting the APPLICATIONINSIGHTS_CONNECTION_STRING environment variable (from your Application Insights resource) and initialising the Microsoft OpenTelemetry Distro:

```python
# Add this to each FastAPI service
from microsoft.opentelemetry import use_microsoft_opentelemetry
# Initialize the Microsoft OpenTelemetry Distro with Azure Monitor export.
use_microsoft_opentelemetry(
    enable_azure_monitor=True,
    azure_monitor_enable_live_metrics=False,  # To disable live metrics
)
```

Azure Monitor collects:

* Request traces
* Latency
* Dependency calls (e.g., external APIs)
* Exceptions

---

## 📡 API Usage Example

```bash
curl -X POST "http://<external-ip>/run_pipeline?task=Write%20a%20summary%20on%20multi-agent%20systems"
```

---

## 🧠 Extend with Ease

Plug in additional agents or tools:

* 🧠 LangGraph, AutoGen, CrewAI
* 🧾 Vector DB (e.g., FAISS, Azure AI Search)
* 🔄 Redis Pub/Sub for real-time communication
* 🔐 Azure Key Vault for secret rotation

---

## 🤝 Contributing

PRs, issues, ideas – all welcome!
Fork this repo, raise an issue, or drop a ⭐️ if you find it useful.

---

## 🛡 License

MIT License © 2025 [Rajkiran Veldur](https://github.com/RajkiranVS)

---
