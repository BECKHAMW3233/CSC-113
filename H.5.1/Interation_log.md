# Iteration Log: Local AI Infrastructure Build

**Project:** Local AI Infrastructure for Federal Cybersecurity Operations  
**Timeline:** May 2025 - March 2026  
**Primary Work:** Hands-on testing, configuration, troubleshooting  
**AI Assistance:** Claude AI for documentation formatting and web interface code

---

## Discovery and Initial Build (May 2025)

**What happened:**
Discovered Ollama and started testing local AI models out of curiosity. Found it interesting and enjoyable enough to become a serious side project.

**Early testing:**
- Pulled and tested multiple models to see what worked
- By late May already had 18 models downloaded and being evaluated
- Spent significant time learning the basics of local AI deployment

**Status:** Proof of concept established - local AI viable on my hardware

---

## Architecture Testing: WSL vs Docker vs Native (May 2025)

**Problem:** Needed to determine best deployment architecture for sustained use.

### WSL Testing

**What I tried:**
- Installed Ollama in WSL Ubuntu environment
- Configured Node.js, npm, Docker within WSL
- Set up file system mounting between Windows and WSL
- Configured ngrok tunneling
- Extensive troubleshooting of environment issues

**Problems encountered:**
- Hours/days spent on configuration complexity
- Node.js version compatibility issues
- Multiple manual setup steps required
- Performance wasn't optimal
- Instability during sustained workloads

**Result:** Rejected due to complexity and performance issues

### Docker Testing

**What I tried:**
- Tested Docker Desktop on Windows
- Configured container setup for Ollama
- Ran inference tests with containerized deployment

**Outcome:**
Found it "so much easier" than WSL - "few commands and boom working AI" vs extensive WSL configuration. However, still had overhead compared to native installation.

**Result:** Better than WSL but not optimal

### Native Windows

**What I did:**
- Switched to running Ollama directly on Windows
- Used AnythingLLM as interface layer
- Direct GPU access through native NVIDIA drivers

**Result:** 
✅ **Selected as production architecture**
- Simpler setup than WSL or Docker
- Better performance than virtualized/containerized options
- Successfully running 70B models
- Stable for sustained workloads

**Key lesson:** For single-user deployment on Windows, native installation wins. Added complexity of WSL/Docker not justified by benefits for this use case.

---

## Model Library Development

**What happened:**
Tested multiple models to build specialized library for different analytical tasks. Started with 18+ models and refined down to optimized collection.

**Selection process:**
- Tested models across different use cases
- Evaluated performance (speed, quality, VRAM usage)
- Identified domain-specific models (cybersecurity, code analysis, reasoning)
- Removed redundant models
- Kept models that excel at specific tasks

**Current library (8 models, ~150GB):**
1. qwen3:32b - Primary workhorse for general analysis
2. llama3.1:70b-instruct-q4_K_M - Complex reasoning tasks
3. deepseek-r1:32b - Chain-of-thought reasoning
4. deepseek-coder:33b-instruct - Code analysis and vulnerabilities
5. qwen3-coder:30b - Code analysis (cross-validation)
6. phi4-reasoning:14b - Fast reasoning and triage
7. ALIENTELLIGENCE/cybersecuritythreatanalysisv2 - Threat intelligence
8. jimscard/blackhat-hacker:v2 - Red team perspective

**Rationale:** 
Each model fills distinct role. Domain-specific models outperform larger general models on specialized tasks. Two code models enable cross-validation.

---

## AnythingLLM Integration

**What I added:**
Integrated AnythingLLM Desktop as workspace interface for Ollama.

**Configuration:**
- Connected to local Ollama instance (http://localhost:11434)
- Created task-specific workspaces with dedicated models
- Configured system prompts for each workspace
- Set up document ingestion (RAG) for querying specific reports

**Workspaces created:**
- Threat Intelligence (ALIENTELLIGENCE model)
- Code Review (deepseek-coder)
- Red Team (blackhat-hacker)
- Attack Chain (deepseek-r1)
- Deep Analysis (llama3.1:70b)
- General (qwen3:32b)

**Why this matters:**
System prompts eliminate re-explaining context every session. Right model automatically selected for each task type. Workspace structure mirrors how SOC teams operate.

---

## Documentation

**What I created:**
Comprehensive technical documentation covering the full deployment.

**Content:**
- Windows deployment guide (21 pages)
- Linux deployment guide (80 pages)
- Architecture comparison and rationale
- Model selection reasoning
- Hardware specifications
- Troubleshooting based on actual problems encountered
- Use case scenarios for federal cybersecurity work

**Claude AI's role:**
- Markdown formatting structure
- Content organization
- Grammar and clarity improvements

**My role:**
- All technical content
- All architecture decisions and rationale
- All troubleshooting from hands-on experience
- All performance data from actual testing

---

## Web Interface Development (April 2026)

**Problem:** Need portfolio demonstration for course submission.

**What I built:**
Single-page HTML application showcasing the existing infrastructure.

**AI tool used:** Claude AI for code generation

**Process:**
1. Gave Claude detailed specifications of infrastructure to showcase
2. Claude generated complete HTML/CSS/JS in single file
3. Made refinements through iterations:
   - Improved mobile interactions
   - Enhanced visual hierarchy for architecture comparison
   - Added realistic sample outputs for use cases
   - Verified accessibility (contrast, keyboard navigation)

**Result:** Production-ready web interface (61KB HTML file)

**Division of work:**
- **Claude:** Generated HTML/CSS/JS code structure, visual design, responsive layout
- **Me:** Provided all technical content (model specs, hardware details, architecture decisions, performance data)

---

## Cloud vs Local Testing

**What I tested:**
Compared local Qwen3:32b against commercial cloud AI services on identical prompts.

**Services tested:**
- Gemini 2.5 Flash
- Claude 3.5 (free tier)
- ChatGPT 3.5 (free tier)
- Local Qwen3:32b

**Key findings:**
- Cloud: 2-6 second response times
- Local: 1m 45s - 4m 45s depending on complexity
- Quality: Local matched or exceeded cloud on structured analytical tasks
- Data handling: Cloud transmits data externally, local maintains complete sovereignty

**Operational decision:**
For federal cybersecurity work, data sovereignty > speed. 4-minute local analysis acceptable when alternative is external data transmission.

---

## What I Learned

**Technical skills:**
- Local AI deployment and optimization
- Architecture evaluation through hands-on testing
- Model selection and task routing
- GPU/VRAM resource management
- System administration (Docker, WSL, native Windows)

**Key insights:**
- Simpler is better - native installation beat virtualized options for this use case
- Domain-specific models > larger general models for specialized tasks
- Hands-on testing reveals issues documentation doesn't show
- "Just play with it" methodology builds real competency through trial and error

**AI tool usage:**
- Claude AI: Helpful for documentation formatting and code generation
- Local Ollama: All actual cybersecurity analytical work
- Distinction: AI assists with presentation, expertise comes from doing the work

---

## Timeline Summary

- **May 2025:** Initial discovery, architecture testing (WSL/Docker/Native), early model library
- **May 2025 - March 2026:** Model curation, AnythingLLM integration, documentation, infrastructure refinement
- **April 2026:** Web interface development for course submission

**Total build time:** ~11 months from discovery to complete documented system

---

## Assignment Context

**Course:** CSC-113-0901 Artificial Intelligence Fundamentals (FTCC, Spring 2026)

**Assignment (H.5.1):** Build rapid prototype demonstrating AI capabilities

**My approach:** Infrastructure already built over preceding months. Created web demonstration as "prototype" showcasing existing work.

**Deliverables:**
- PRD: Defines web interface requirements
- PROTOTYPE_TESTING: Documents Claude AI usage for web development
- ITERATION_LOG: This document - real build process
- README: Usage and documentation guide
- index.html: Portfolio demonstration page

**What's different:** Assignment expects building something new quickly. I built infrastructure over extended period, then created rapid demonstration of that work.

**Still meets requirements:** All required deliverables present, demonstrates AI tool usage, working prototype deployed, proper GitHub workflow followed.
