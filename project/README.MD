# Local AI Infrastructure for Federal Cybersecurity Operations

**William Edward Beckham III**
Fayetteville Technical Community College
Artificial Intelligence Fundamentals — CSC-113-0901 | Spring 2026
Instructor: Andrew Norris | Class Dates: January 12 – May 13, 2026

---

## What is this?

This project documents the design, testing, and production deployment of a fully local AI infrastructure built for sensitive cybersecurity analysis work. The system runs large language models entirely on local hardware — no cloud services, no external API calls, no data leaving the machine. It was built to address a real constraint in federal cybersecurity environments: classified and sensitive data cannot be transmitted to commercial AI services like ChatGPT or Gemini.

## What does it do?

The infrastructure provides task-routed AI analysis across eight specialized models totaling approximately 150GB of deployed model storage. Each model is assigned to a specific analytical role — threat intelligence triage, malware code review, attack chain reconstruction, red team surface analysis, and general documentation — and accessed through pre-configured workspaces in AnythingLLM with persistent system prompts that eliminate setup overhead at the start of every session. The system runs natively on Windows 11 Pro using Ollama as the model runtime and supports complete air-gap operation once models are downloaded.

## How far did I get?

This is a fully operational production deployment, not a prototype. The infrastructure has been running since Fall 2025 and was in active use throughout the Spring 2026 semester. The project went through three full architecture implementations before settling on the current production setup:

- **Docker Desktop + ngrok** — tested and rejected due to GPU passthrough overhead and the fundamental contradiction between ngrok's external tunnel dependency and the air-gap data sovereignty goal
- **WSL2** — tested and rejected due to abstraction layer latency, GPU driver instability on sustained workloads, and resource allocation complexity compared to native execution
- **Native Windows** — current production architecture; direct hardware access, maximum VRAM utilization, zero external network dependencies

The model library was pruned from 18+ experimental models pulled starting May 2025 down to the current eight through systematic performance testing on representative real-world analytical tasks. Real bugs were encountered and resolved during the semester — including an AnythingLLM streaming truncation issue after a version upgrade that was isolated through direct CLI testing and traced to agent skills configuration rather than timeout, hardware, or model issues. That troubleshooting process is documented in the main project file.

All workflows — CISA alert triage, malware code review, attack chain reconstruction, red team surface analysis — are operational and have been tested on real inputs.

## What AI tools did I use?

- **Ollama** (v0.21.2) — local model runtime, handles model downloads and inference
- **AnythingLLM** (v1.10.0) — workspace interface, document ingestion, RAG, system prompt management
- **Claude AI** (Anthropic) — used throughout the model selection and research process to evaluate model classes, understand hardware constraints, and identify the best candidates for each analytical role
- **Gemini 2.5 Flash, ChatGPT 3.5, Claude 3.5** — benchmarked against local infrastructure in the January 24, 2026 comparative test
- **Qwen3:32b, Llama 3.1 70B, DeepSeek R1:32b, DeepSeek Coder:33b, Qwen3-Coder:30b, Phi4-Reasoning:14b, ALIENTELLIGENCE cybersecurity model, BlackHat Hacker v2** — the eight locally deployed models constituting the production infrastructure

---

## Repository Structure

```
project/
├── README.md                        ← This file
├── REFLECTION.md                    ← Learning reflection
├── project.md                       ← Full infrastructure documentation
├── prompts/
│   ├── prompt-threat-intel.md       ← CISA alert triage prompt + system prompt
│   ├── prompt-code-review.md        ← Malware code analysis prompt + system prompt
│   ├── prompt-attack-chain.md       ← Attack chain reconstruction prompt + system prompt
│   └── prompt-red-team.md           ← Red team surface analysis prompt + system prompt
└── outputs/
    └── cloud-vs-local-comparison.md ← January 24, 2026 comparative test results
```
