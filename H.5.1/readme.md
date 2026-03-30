# Local AI Infrastructure for Federal Cybersecurity Operations

**CSC-113-0901 | Spring 2026 | Fayetteville Technical Community College**  
**Author:** William Edward Beckham III  
**Project Type:** H.5.1 "A Quick Prototype" — Rapid MVP Development

---

## 🎯 What It Does

This project demonstrates a production-ready local AI infrastructure deployment designed for federal cybersecurity analytical work. The system runs 8 specialized AI models entirely on local hardware with zero external dependencies, providing:

- **Threat Intelligence Analysis** — CISA alert triage, CVE assessment, threat pattern recognition
- **Code Review & Vulnerability Assessment** — Malware analysis, secure coding guidance
- **Red Team Perspective** — Attack surface analysis, adversarial thinking
- **Attack Chain Reconstruction** — Multi-stage campaign analysis with chain-of-thought reasoning

**The core value proposition:** Complete data sovereignty. Sensitive analytical work cannot use commercial cloud AI services (ChatGPT, Gemini, Claude) due to data handling requirements. This infrastructure solves that capability gap.

---

## 🚀 Try It Live

**GitHub Pages Deployment:** [https://beckhamw3233.github.io/CSC-113/](https://beckhamw3233.github.io/CSC-113/)

The live demo is a single-page web application that visualizes:
- Complete model library (8 models, 150GB deployed)
- Architecture comparison (Docker vs WSL vs Native Windows)
- Federal use case scenarios with sample outputs
- Hardware specifications and performance metrics
- Cloud vs local deployment tradeoffs

---

## 📋 How to Use Locally

### Option 1: View the Demo (No Installation Required)

1. Clone or download this repository
2. Open `index.html` directly in your web browser
3. No server needed — works via `file://` protocol

```bash
git clone https://github.com/BECKHAMW3233/CSC-113.git
cd CSC-113
# Open index.html in your browser
```

### Option 2: Deploy the Actual Infrastructure

**⚠️ Hardware Requirements:**
- **Minimum:** 16GB RAM, 8GB VRAM, 100GB free storage
- **Recommended:** 32GB RAM, 12GB VRAM, 200GB free storage
- **Optimal (this deployment):** 64GB RAM, 16GB VRAM, NVMe storage

**Installation Steps:**

1. **Install Ollama** (model runtime)
   - Download from [ollama.com](https://ollama.com)
   - Run installer (Windows, macOS, or Linux)
   - Verify: `ollama --version`

2. **Pull Models**
   ```bash
   ollama pull qwen3:32b
   ollama pull llama3.1:70b-instruct-q4_K_M
   ollama pull deepseek-r1:32b
   ollama pull deepseek-coder:33b-instruct
   ollama pull qwen3-coder:30b
   ollama pull phi4-reasoning:14b
   ollama pull ALIENTELLIGENCE/cybersecuritythreatanalysisv2
   ollama pull jimscard/blackhat-hacker:v2
   ```

3. **Install AnythingLLM** (workspace interface)
   - Download from [anythingllm.com/desktop](https://anythingllm.com/desktop)
   - Connect to Ollama: `http://localhost:11434`
   - Create workspaces per documented configuration

4. **Verify Deployment**
   ```bash
   ollama list  # Should show all 8 models
   ollama run qwen3:32b "Test query"  # Verify inference works
   ```

**Full deployment documentation:** See the [complete infrastructure document](Local_AI_Infrastructure_Documentation.md) (101+ pages) for step-by-step installation, architecture decisions, troubleshooting, and operational workflows.

---

## 📂 Features Implemented

### ✅ Core MVP Features

- **Model Library Dashboard** — Interactive cards for all 8 specialized models with expandable details
- **Architecture Comparison** — Visual comparison of Docker, WSL, and native Windows deployments with performance metrics
- **Federal Use Case Scenarios** — 4 realistic workflows (CISA alert triage, malware code review, red team analysis, attack chain reconstruction)
- **Hardware Specifications** — Complete system specs showing deployment requirements
- **Performance Metrics** — Cloud vs local comparison from January 2026 testing
- **Mobile Responsive Design** — Fully functional across all device sizes (375px - 2560px+)
- **Portfolio-Ready Quality** — Professional design suitable for federal IT hiring managers

### 🎨 Design & UX

- **Terminal/Military Aesthetic** — Monospace fonts, scanline effects, technical color palette (green/cyan accents on dark background)
- **Progressive Disclosure** — Model cards expand to show detailed specs, keeping initial view clean
- **Smooth Animations** — Fade-in sections on load, smooth card expansions, animated performance bars
- **Accessibility** — WCAG AA compliant contrast ratios, keyboard navigation support, semantic HTML
- **Zero External Dependencies** — All CSS/JS embedded, works offline, no CDN calls

---

## 📚 Project Documentation

All CSC-113 H.5.1 assignment requirements completed:

| Document | Purpose | Status |
|----------|---------|--------|
| **PRD.md** | Product Requirements Document — what we're building and why | ✅ Complete |
| **PROTOTYPE_TESTING.md** | AI tool comparison (Claude vs ChatGPT vs Copilot) | ✅ Complete |
| **ITERATION_LOG.md** | Development journey — 10 iterations documented | ✅ Complete |
| **README.md** | This file — complete documentation and usage guide | ✅ Complete |
| **index.html** | Working single-page application (92KB) | ✅ Complete |
| **Full Infrastructure Docs** | Technical deployment guide (101+ pages) | ✅ Linked |

---

## 🎓 Course Context

**Course:** CSC-113-0901 Artificial Intelligence Fundamentals  
**Instructor:** Andrew Norris  
**Institution:** Fayetteville Technical Community College  
**Semester:** Spring 2026 (January 12 – May 13, 2026)

### Learning Outcomes Addressed

1. **Understand AI/ML fundamentals** — Documented through model selection rationale, parameter counts, quantization techniques, and inference optimization
2. **Use generative AI tools across investigations** — Demonstrated through task-specific model routing and specialized cybersecurity AI models
3. **Evaluate and select suitable AI tools** — Evidenced by architecture comparison (Docker vs WSL vs Native) and model library curation process
4. **Develop practical AI project** — Production deployment solving real operational problem in federal cybersecurity

### Module Progression

| Module | Topic | How This Project Relates |
|--------|-------|-------------------------|
| Module 4 | Find Your Project | Selected local AI infrastructure as final project |
| Module 5 | Design Your Project | Created PRD, documented architecture decisions |
| Module 6 | Project: Sprint 1 | Core deployment — Ollama installation, model library |
| Module 7 | Project: Sprint 2 | Interface integration — AnythingLLM workspaces, system prompts |
| Module 8 | Project: The Payoff | AI Showcase — web interface, complete documentation |

---

## 🛠️ What I Learned

### Technical Skills

- **Local AI Deployment** — Hands-on experience with Ollama, model management, VRAM/RAM optimization
- **Architecture Evaluation** — Systematic testing of Docker, WSL, and native Windows deployments with evidence-based decision-making
- **Frontend Development** — Built responsive single-page application with CSS Grid, animations, and accessibility features
- **AI-Assisted Development** — Used Claude 3.5 Sonnet to generate production-ready code from detailed PRD

### Professional Skills

- **Product Documentation** — Created clear PRD defining requirements, constraints, and success criteria
- **Technical Writing** — Documented 101+ pages covering installation, troubleshooting, and operational workflows
- **GitHub Workflow** — Practiced proper version control: issues, branches, pull requests, peer review
- **Portfolio Development** — Built demonstration piece suitable for federal IT hiring managers (GS-11/12 level)

### Key Insights

**What worked well:**
- Starting with detailed PRD meant Claude generated 90% of final product in first iteration
- Testing architectures empirically (not just theoretically) revealed performance differences that documentation alone wouldn't show
- Domain-specific models (cybersecurity, code analysis) outperformed general models on specialized tasks

**What would be done differently:**
- Test on physical devices earlier (not just DevTools responsive mode)
- Define sample outputs in PRD upfront (saved an iteration cycle)
- Include accessibility checklist from the start (contrast ratios, focus states)

**Biggest surprise:**
- Claude's output quality was significantly higher than course materials anticipated. Assignment warned "the AI made broken code" — Claude's first generation was 100% functional with zero broken code.

---

## 🎯 Future Improvements

### Phase 2: Live Model Integration
Add server-side component (Python Flask or Node.js) to enable actual model queries through the web interface. Would require authentication and session management.

### Phase 3: Deployment Automation
Scripted installation tooling that automates the manual setup process documented in the 101-page deployment guides. Reduce deployment time from 3 weeks to 1-2 days.

### Phase 4: Performance Telemetry
Live VRAM/RAM monitoring, inference speed tracking, and model health indicators pulled from actual hardware sensors. Real-time dashboard showing current system state.

### Phase 5: Multi-Workspace Management
Web-based interface for AnythingLLM workspace creation, system prompt editing, and document library management—bringing full configuration control into the UI.

---

## 🔗 Links & Resources

- **Live Demo:** [https://beckhamw3233.github.io/CSC-113/](https://beckhamw3233.github.io/CSC-113/)
- **GitHub Repository:** [https://github.com/BECKHAMW3233/CSC-113](https://github.com/BECKHAMW3233/CSC-113)
- **LinkedIn:** [linkedin.com/in/WilliamBeckham](https://linkedin.com/in/WilliamBeckham)
- **Email:** williamedwardbeckhamiii@gmail.com

**External Tools Used:**
- [Ollama](https://ollama.com) — Open-source model runtime
- [AnythingLLM](https://anythingllm.com) — Workspace interface for local models
- [Claude 3.5 Sonnet](https://claude.ai) — AI-assisted development (web interface generation)

---

## 📄 License & Usage

This project is submitted as academic work for CSC-113-0901 at Fayetteville Technical Community College. The code and documentation are provided as-is for educational purposes.

**Hardware/Software Stack:**
- Ollama: [Apache 2.0 License](https://github.com/ollama/ollama/blob/main/LICENSE)
- AnythingLLM: [MIT License](https://github.com/Mintplex-Labs/anything-llm/blob/master/LICENSE)
- Models: Various licenses (check individual model cards on [Ollama Library](https://ollama.com/library))

**Deployment Note:** This documentation describes actual production infrastructure deployed on personal hardware. The web interface (`index.html`) is a demonstration/portfolio piece and does not include live model integration.

---

## 👤 About the Author

**William Edward Beckham III**

- **Military Service:** U.S. Army Veteran (13B Field Artillery, 38B Civil Affairs) with two combat deployments to Afghanistan and eight years of residency in Okinawa, Japan
- **Education:** Systems Security & Analysis degree from Fayetteville Technical Community College (4.0 GPA, President's List every semester)
- **Experience:** Former AI Data Analyst on DoD Pathfinder Project (2024–2025)
- **Certifications:** Preparing for CompTIA Security+ and CySA+
- **Target Role:** GS-11/12 Federal Cybersecurity Analyst positions at Fort Liberty, NC

**Why This Project Matters:**

Federal cybersecurity positions require analyzing classified or sensitive data that cannot be transmitted to commercial cloud AI services. This project demonstrates:
1. Technical capability to deploy production AI infrastructure
2. Understanding of operational security requirements (data sovereignty, air-gap operation)
3. Systems engineering methodology (architecture evaluation, evidence-based decisions)
4. Ability to document complex technical systems for diverse audiences

The infrastructure is designed to solve a real operational problem in federal IT environments—and the documentation shows that understanding extends beyond "I followed a tutorial."

---

## 🙏 Acknowledgments

- **Andrew Norris** — CSC-113 Instructor, Fayetteville Technical Community College
- **Anthropic** — Claude 3.5 Sonnet for AI-assisted development
- **Ollama & AnythingLLM Teams** — Open-source tools enabling local AI deployment
- **FTCC IT Department** — Academic support and infrastructure resources

---

**Project Status:** ✅ Complete and ready for submission (April 20, 2026)  
**Version:** 1.0 (production)  
**Last Updated:** April 19, 2026
