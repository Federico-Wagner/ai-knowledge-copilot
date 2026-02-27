# 🤖 AI Knowledge Copilot

This project is designed as a production-oriented backend service built with FastAPI, Docker, CI/CD, and AWS. Which integrates and orchestrate external AI (LLM) APIs.

It aims to demonstrate how AI capabilities can be integrated into production systems using solid backend principles.

This service does **not** train models. Instead, it provides a structured, scalable, and production-ready interface to consume AI capabilities inside real-world systems.

The goal is to evolve it progressively into a cloud-ready, scalable, observable microservice aligned with real-world backend engineering standards.

---

## 🚀 Purpose

The goal of this project is to:

- Integrate external AI/LLM APIs
- Orchestrate prompts and responses
- Standardize request/response contracts
- Validate inputs using Pydantic
- Provide a clean service layer abstraction
- Act as an AI Gateway for other systems

This project follows backend engineering best practices and is structured as a production-ready microservice.

---

## 🏗 Architecture

```
ai-knowledge-copilot/
│
├── app/
│   ├── api/          # HTTP endpoints
│   ├── services/     # AI provider integrations
│   ├── domain/       # Business models and schemas
│   ├── core/         # Config & shared utilities
│   └── main.py       # FastAPI entrypoint
│
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

### Design Principles

- Clear separation of concerns
- Modular structure
- Automatic validation via Pydantic
- Scalable provider abstraction
- Docker-ready
- Clean backend architecture mindset

---

## 🛠 Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- Docker

---

## 🐳 Running with Docker (Docker-first)

### Build image

```bash
docker build -t ai-knowledge-copilot .
```

### Run container

```bash
docker run -p 8000:8000 ai-knowledge-copilot
```

---

## 📈 Roadmap
### 🟢 Phase 1 – Foundations

- [x] Minimum microservice for initial deploys
- [x] FastAPI base project structure
- [x] Health check endpoint
- [x] Dockerfile (multi-stage)
- [x] Local Docker execution
- [x] GitHub repository setup
- [x] Basic project documentation

Goal: Deploy a minimal but production-ready containerized API.

---

### 🟡 Phase 2 – CI/CD & Cloud Deployment

- [ ] CI pipeline (lint + test + docker build)
- [ ] Push Docker image to Docker Hub
- [ ] CD pipeline
- [ ] EC2 provisioning
- [ ] SSH-based automated deployment
- [ ] Environment variable management
- [ ] Basic logging

Goal: Fully automated deployment pipeline to AWS EC2.

---

### 🟣 Phase 3 – AI Integration
- [ ] Integrate LLM models via APIs
- [ ] Build internal AI service layer abstraction
- [ ] Implement retry and timeout strategy for external AI calls

---

## 👨‍💻 Author

Federico Wagner  
Backend Developer | Java | Python | Architecture | AI Integration