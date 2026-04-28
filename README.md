# CSC-113: AI Fundamentals

**Spring 2026** | Fayetteville Technical Community College
**Instructor:** Andrew Norris
**Student:** William Edward Beckham III | BECKHAMW3233

---

## About This Course

A hands-on exploration of artificial intelligence and machine learning fundamentals, focusing on practical applications of generative AI tools for real-world tasks. Course progression moves from foundational prompt engineering through bot design, tool evaluation, and a capstone project built around a real operational problem.

---

## What I Learned

- How model selection determines output quality ceiling regardless of prompt quality — a purpose-built 4.7GB cybersecurity model outperforms a general 32B model on threat intelligence tasks
- Why deployment architecture matters as much as the model — native Windows outperforms Docker and WSL for single-user GPU inference due to passthrough overhead and abstraction layer latency
- The difference between prompting as asking and prompting as configuring — system prompts that define role, framework, and output format produce consistently better results than per-query instruction
- How to validate AI tool decisions with documented comparative testing rather than assumption
- What data sovereignty actually means operationally and why it eliminates cloud AI from federal cybersecurity workflows entirely

---

## Course Projects

| Assignment | Description |
|---|---|
| **Week 2 — SAGE** | Tool comparison and local AI performance benchmarking; established Qwen3:32B as primary workhorse |
| **BadBot (H.2.1)** | ELITESEC_GPT — intentionally flawed AI assistant demonstrating toxic technical culture and communication failure patterns |
| **BetterBot (H.3.1)** | Transformed ELITESEC_GPT into an empathy-driven assistant; same hardware, same model, different persona and system prompt |
| **Quick Prototype (H.5.1)** | Web-based demonstration of local AI infrastructure for portfolio |
| **Final Project** | Production-ready local AI deployment for federal cybersecurity operations — 8 specialized models, 150GB, complete data sovereignty |

---

## Final Project: Local AI Infrastructure for Federal Cybersecurity Operations

The semester capstone is a fully operational production deployment, not a prototype. It addresses a real constraint: federal cybersecurity roles at installations like Fort Liberty cannot use commercial cloud AI for sensitive data analysis. This infrastructure closes that gap.

**The problem:** Analysts cannot send threat intelligence, malware samples, network captures, or vulnerability data to ChatGPT, Gemini, or Claude due to data sovereignty and classification requirements.

**The solution:** Local Ollama deployment with eight specialized models running natively on Windows 11 Pro — no cloud dependencies, no external transmission, complete air-gap capability.

### Hardware

| Component | Specification |
|---|---|
| CPU | AMD Ryzen 9 7900X @ 5.30GHz — 12C/24T |
| GPU | Zotac RTX 4080 16GB VRAM |
| RAM | 64GB DDR5-5600 |
| OS | Windows 11 Pro (Build 26200.7623) |

### Software Stack

| Tool | Version | Role |
|---|---|---|
| Ollama | v0.21.2 | Model runtime and inference |
| AnythingLLM | v1.10.0 | Workspace interface, RAG, system prompt management |

### Model Library

| Model | Size | Role |
|---|---|---|
| `qwen3:32b` | 20GB | Primary analysis and documentation — daily workhorse |
| `llama3.1:70b-instruct-q4_K_M` | 42GB | Advanced reasoning, complex multi-step analysis |
| `deepseek-r1:32b` | 19GB | Attack chain reconstruction — chain-of-thought reasoning |
| `deepseek-coder:33b-instruct` | 18GB | Code review and vulnerability assessment |
| `qwen3-coder:30b` | 18GB | Code analysis, Python specialist, cross-validation |
| `phi4-reasoning:14b` | 11GB | Fast triage and rapid reasoning |
| `ALIENTELLIGENCE/cybersecuritythreatanalysisv2` | 4.7GB | Threat intelligence, CVE triage, TTP analysis |
| `jimscard/blackhat-hacker:v2` | 9.2GB | Red team perspective, adversarial surface analysis |

**Total deployed: ~150GB**

### Architecture Decision

Three deployment approaches were fully implemented and tested before committing to production:

- **Docker Desktop + ngrok** — rejected: GPU passthrough overhead, ngrok external dependency contradicts air-gap goal
- **WSL2** — rejected: abstraction layer latency, GPU driver instability on sustained workloads
- **Native Windows** — current production: direct hardware access, maximum VRAM utilization, zero external dependencies

### Validated Performance (January 24, 2026)

Head-to-head test across identical prompts — Gemini 2.5 Flash, Claude 3.5, ChatGPT 3.5, and local Qwen3:32b:

| Tool | Response Time | Output Quality | Data Handling |
|---|---|---|---|
| Cloud tools | 2–6 seconds | 4–5/5 | Transmitted to third-party servers |
| Local Qwen3:32b | 1m 45s – 4m 45s | 4–5/5 | Zero external transmission |

**Finding:** Quality equivalent. Speed gap is real and irrelevant for federal cybersecurity work — the data handling requirement eliminates cloud tools regardless of performance.

---

## Repository Structure

```
CSC-113/
├── project/                          ← Final project submission
│   ├── README.md                     ← Project overview and documentation
│   ├── REFLECTION.md                 ← Semester learning reflection
│   ├── project.md                    ← Full infrastructure documentation
│   ├── Prompt/                       ← Operational prompts by workspace
│   │   ├── Threat Intelligence Triage
│   │   ├── Malware Code Review
│   │   ├── Attack Chain Reconstruction
│   │   └── Red Team Surface Analysis
│   └── OutPuts/                      ← Test results and outputs
│       └── Cloud vs. Local AI        ← January 24 comparative test data
├── H.5.1/                            ← Quick Prototype assignment
│   ├── index.html
│   ├── README.md
│   ├── PRD.md
│   ├── PROTOTYPE_TESTING.md
│   └── ITERATION_LOG.md
├── Project_Ideas/                    ← Early project ideation
├── week-02-sage/                     ← Tool comparison and benchmarking
├── week-03-badbot/                   ← ELITESEC_GPT bad bot design
├── week-04-betterbot/                ← Empathy-driven bot redesign
└── README.md                         ← This file
```

---

## Skills Developed

`Local AI Deployment` `Ollama` `AnythingLLM` `Prompt Engineering` `System Prompt Design` `Model Selection` `Architecture Evaluation` `Performance Benchmarking` `Data Sovereignty` `RAG Implementation` `Threat Intelligence Analysis` `Malware Code Review` `Red Team Analysis` `Attack Chain Reconstruction` `Technical Documentation` `GitHub` `Version Control` `Bot Design` `User Experience` `AI Ethics`

---

## About the Author

U.S. Army veteran (13B Field Artillery, 38B Civil Affairs) with two combat deployments to Afghanistan. Completing a Systems Security & Analysis degree at FTCC with a 4.0 GPA and President's List recognition every semester. Former AI Data Analyst on the DoD Pathfinder Project (2024–2025). Targeting GS-11/12 federal cybersecurity positions (GS-2210 series) at Fort Bragg upon graduation May 2026.

- **GitHub:** [BECKHAMW3233](https://github.com/BECKHAMW3233)
- **LinkedIn:** [linkedin.com/in/WilliamBeckham](https://linkedin.com/in/WilliamBeckham)
- **Certifications in progress:** CompTIA Security+, CySA+

---

*CSC-113-0901 | Spring 2026 | Andrew Norris | Fayetteville Technical Community College*
