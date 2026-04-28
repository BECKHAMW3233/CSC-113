# Local AI Infrastructure for Federal Cybersecurity Operations

## What is this?

This project documents the design, testing, and production deployment of a fully local AI infrastructure built for sensitive cybersecurity analysis work. The system runs large language models entirely on local hardware — no cloud services, no external API calls, no data leaving the machine. It was built to address a real constraint in federal cybersecurity environments: classified and sensitive data cannot be transmitted to commercial AI services like ChatGPT or Gemini.

## What does it do?

The infrastructure provides task-routed AI analysis across eight specialized models totaling approximately 150GB of deployed model storage. Each model is assigned to a specific analytical role — threat intelligence triage, malware code review, attack chain reconstruction, red team surface analysis, and general documentation — and accessed through pre-configured workspaces in AnythingLLM with persistent system prompts that eliminate setup overhead at the start of every session. The system runs natively on Windows 11 Pro using Ollama as the model runtime and supports complete air-gap operation once models are downloaded.

## How far did I get?

This is a fully operational production deployment, not a prototype. The infrastructure has been running since Fall 2025 and was in active use throughout the Spring 2026 semester. Three deployment architectures (Docker Desktop + ngrok, WSL2, and native Windows) were fully implemented and tested before committing to the current production setup. The model library was pruned from 18+ experimental models down to the current eight through systematic performance testing on representative real-world tasks. All workflows documented in the guide — CISA alert triage, malware code review, attack chain reconstruction, red team surface analysis — are operational.

## What AI tools did I use?

- **Ollama** (v0.21.2) — local model runtime, handles model downloads and inference
- **AnythingLLM** (v1.10.0) — workspace interface, document ingestion, RAG, system prompt management
- **Claude AI** (Anthropic) — used throughout the model selection and research process to evaluate model classes, understand hardware constraints, and identify the best options for each analytical role
- **Qwen3:32b, Llama 3.1 70B, DeepSeek R1:32b, DeepSeek Coder:33b, Qwen3-Coder:30b, Phi4-Reasoning:14b, ALIENTELLIGENCE cybersecurity model, BlackHat Hacker v2** — the eight locally deployed models that constitute the production infrastructure
