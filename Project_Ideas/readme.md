# Project Ideation - William Beckham

## Idea 1: Local AI Infrastructure for Federal Cybersecurity Operations

**Problem/Goal:**
Deploy high-performance local AI capabilities for sensitive data analysis in federal cybersecurity environments where cloud-based AI tools are prohibited due to data sovereignty and classification requirements. Many federal positions require analyzing threat intelligence, malware samples, and network traffic that cannot be transmitted to commercial cloud services, creating a gap in AI-assisted analysis capabilities.

**AI Tool(s):**
Ollama v0.14.0 runtime with specialized model collection deployed on local hardware (AMD Ryzen 9 7900X, 64GB RAM, RTX 4080 16GB). Model library includes:
- llama3.1:70b-instruct (42GB) - Complex reasoning and analysis
- ALIENTELLIGENCE/cybersecuritythreatanalysisv2 (4.7GB) - Threat intelligence pattern recognition
- deepseek-coder:33b-instruct (18GB) - Code analysis and vulnerability assessment
- jimscard/blackhat-hacker:v2 (9.2GB) - Red team perspective analysis
- qwen3:32b (20GB) - Primary analysis workhorse
- deepseek-r1:32b (19GB) - Advanced reasoning for attack chain analysis
- phi4-reasoning:14b (11GB) - Fast-response threat triage
- Plus 4 additional specialized models for specific analytical tasks

**Why This Interests Me:**
I'm targeting federal GS-11/12 cybersecurity positions at Fort Liberty after graduation in May 2026. These roles frequently involve analyzing classified or sensitive data that cannot be processed by commercial cloud AI services like ChatGPT or Gemini. Having local AI infrastructure that maintains complete data sovereignty while providing advanced analytical capabilities directly supports the Security+ and CySA+ certification focus on secure architecture design. This also aligns with my military background (13B Field Artillery, 38B Civil Affairs) - I understand operational security requirements for sensitive systems.

**Rough Scope:**
Already completed and operational. Current production deployment uses native Windows installation after testing and abandoning Docker Desktop and WSL approaches due to performance overhead and deployment complexity. System includes model management, task-specific routing (threat analysis → ALIENTELLIGENCE model, code review → deepseek-coder, etc.), and complete local processing with zero external dependencies. Total development time: ~3 weeks of iterative testing and optimization.

---

## Idea 2: Comparative AI Deployment Architecture Analysis

**Problem/Goal:**
Document performance characteristics, deployment complexity, and operational tradeoffs between native, containerized (Docker), and hybrid (WSL) AI infrastructure deployments. Federal IT organizations need objective data to inform architecture decisions for AI tool deployment across heterogeneous environments (Windows workstations, Linux servers, containerized platforms), but most documentation focuses on single deployment methods without comparative analysis.

**AI Tool(s):**
Same Ollama model collection deployed across three different architectures:
1. Native Windows installation (current production)
2. Docker Desktop + ngrok containerization (tested, abandoned)
3. WSL-based Linux deployment (tested, abandoned)

Performance metrics collected: inference speed (tokens/second), resource utilization (VRAM/RAM), deployment complexity (installation steps, dependencies), startup time, update procedures, and security considerations. Analysis uses actual production workloads including threat intelligence analysis, code review, and document processing.

**Why This Interests Me:**
Understanding infrastructure tradeoffs is critical for federal IT architecture roles beyond entry-level positions. This research demonstrates systems engineering methodology: hypothesis → implementation → testing → objective evaluation → documented findings. It creates a portfolio piece showing advanced technical decision-making beyond "following tutorials" - I tested multiple approaches, collected empirical data, and made engineering decisions based on actual performance rather than assumed best practices. This type of analytical rigor is valued in federal cybersecurity leadership positions.

**Rough Scope:**
Research phase already completed - implemented and tested all three deployment approaches, identified performance issues with Docker container overhead and WSL abstraction layer latency, collected operational findings. Would need 1-2 weeks to formalize into structured comparative analysis document with performance benchmarks, architecture decision framework, and deployment recommendations for different use cases. Can leverage existing 101+ pages of deployment documentation created during testing phase (21-page Windows guide, 80-page Linux guide).

---

## Idea 3: Automated Threat Intelligence Correlation System

**Problem/Goal:**
Process multiple threat intelligence feeds (CISA alerts, CVE databases, vendor security bulletins), correlate threats with organizational asset inventory, and generate prioritized threat assessment reports for SOC operations. Current manual process requires analysts to review dozens of daily alerts and determine organizational relevance - time-consuming work that delays response to actual high-priority threats.

**AI Tool(s):**
- ALIENTELLIGENCE/cybersecuritythreatanalysisv2 (4.7GB) - Specialized model for threat pattern recognition and attack vector analysis
- deepseek-r1:32b (19GB) - Advanced reasoning for attack chain construction and impact assessment
- qwen3:32b (20GB) - Report generation and executive summary creation
- Existing local infrastructure ensures sensitive asset inventory data never leaves controlled environment

System would ingest threat feeds, parse structured data (CVE scores, affected systems, exploitation indicators), correlate against sample asset database (OS versions, application inventory, network architecture), and produce prioritized reports with reasoning chains explaining threat relevance.

**Why This Interests Me:**
SOC analysts in federal environments spend significant time manually reviewing threat intelligence and determining organizational applicability. Automation would enable analysts to focus on high-priority threats while AI handles initial triage and correlation. This demonstrates practical application of specialized cybersecurity AI models to real operational workflows, creating a strong portfolio piece for federal cyber analyst positions. The local deployment architecture maintains operational security for sensitive asset inventory data while providing AI-assisted analysis - exactly the type of capability federal SOCs need but cannot implement with cloud-based tools.

**Rough Scope:**
3-4 weeks for initial prototype. Core infrastructure already exists (models deployed and tested, proven performance on local hardware). Development work needed: feed parsers for CISA alerts and NVD CVE database, correlation logic against sample asset database, report templates for different stakeholder levels (technical analyst vs management), and basic web interface for report review. Start with CISA alerts and CVE correlation, expand to vendor bulletins and OSINT sources in later iterations. All processing keeps sensitive data local using existing architecture.

---

## Additional Context

### Technical Infrastructure Details
Current system specifications:
- **Hardware:** AMD Ryzen 9 7900X (12-core/24-thread), 64GB DDR5-5600, RTX 4080 16GB VRAM
- **Software:** Ollama v0.14.0 on Windows 11, ~200GB model storage
- **Deployment methodology:** Native installation after empirical testing rejected containerized approaches
- **Documentation:** 101+ pages across Windows and Linux deployment guides

### Why These Ideas Align with Course Goals
All three ideas demonstrate:
- **Solving real problems** - Federal data sovereignty requirements, architecture decision-making, SOC operational efficiency
- **Meaningful AI use** - Task-specific model selection, not generic "ask ChatGPT"
- **Achievable scope** - Idea 1 already completed, Idea 2 leverages existing research, Idea 3 builds on proven infrastructure
- **Portfolio value** - Direct relevance to target GS-11/12 federal cybersecurity positions
- **Personal motivation** - Each project supports career trajectory and demonstrates capabilities beyond typical coursework

### Lessons from Deployment Testing
During the 3-week development cycle, I tested multiple deployment approaches:
- **Docker Desktop + ngrok:** Container overhead reduced inference speed, added deployment complexity without clear benefit for single-user deployment
- **WSL deployment:** Platform abstraction layer introduced latency, reduced hardware utilization efficiency
- **Native Windows:** Optimal performance through direct hardware access, simpler maintenance, better resource efficiency

This iterative testing demonstrates engineering methodology: objective evaluation of alternatives, empirical performance measurement, and evidence-based decision-making rather than following tutorials uncritically.
