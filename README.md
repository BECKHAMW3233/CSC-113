# CSC-113: AI Fundamentals 🤖

**Spring 2026** | Fayetteville Technical Community College  
**Instructor:** Andrew Norris  
**Student:** William Beckham

---

## About This Course

A hands-on exploration of artificial intelligence and machine learning fundamentals, focusing on practical applications of generative AI tools for real-world tasks.

---

## What I'm Learning

* 🤖 AI collaboration and prompt engineering techniques
* 🔧 Building custom AI assistants (BadBot, BetterBot, StudyBuddy)
* 💡 Evaluating and selecting AI tools for specific tasks
* 🚀 Developing AI-powered solutions for cybersecurity, creative, and programming challenges
* 📊 Project management with AI integration
* 🛡️ Local AI infrastructure for data sovereignty and operational security

---

## Course Projects

* **BadBot (H.2.1)** - Intentionally flawed AI assistant demonstrating poor UX design
* **BetterBot (H.3.1)** - Improved assistant with empathy and clarity
* **Quick Prototype (H.5.1)** - Web-based demonstration of local AI infrastructure
* **Final Project** - Production-ready local AI deployment for federal cybersecurity operations

---

## Learning Log

### Week 2: AI Tools & First Collaborations
**Date:** Jan 20 - Jan 26, 2026

**What I learned:**
* Qwen3:32B excels in structured cybersecurity tasks
* Local AI deployment aligns with federal data security requirements
* TPS (tokens per second) measurement for performance benchmarking

**What challenged me:**
* Measuring TPS accurately required script adjustments
* Balancing multiple AI tools for different analytical tasks

**What I'm proud of:**
* Built SAGE workspace aligned with federal compliance standards
* Successfully integrated local Ollama deployment with AnythingLLM interface

**Questions I still have:**
* How to optimize Qwen3 for real-time network traffic analysis?

---

### Week 3: BadBot Design & Friction Analysis
**Date:** Jan 27 - Feb 2, 2026

**What I learned:**
* How persona design directly impacts user experience
* The relationship between condescension and communication failure
* Why circular logic breaks trust in AI assistants

**What challenged me:**
* Testing intentionally broken design required patience
* Documenting frustration objectively without fixing the problems

**What I'm proud of:**
* Created ELITESEC_GPT - a bot demonstrating toxic technical culture
* Connected bad bot design to real-world leadership failures

**Questions I still have:**
* How to measure user frustration quantitatively in bot testing?

---

### Week 4: BetterBot & Empathy-Driven Design
**Date:** Feb 3 - Mar 8, 2026

**What I learned:**
* Adding empathy language transforms user experience
* Clear explanations > condescending expertise
* Performance consistency matters (3.7 tokens/sec maintained)

**What challenged me:**
* Balancing technical accuracy with approachability
* Keeping system prompts clean while testing improvements

**What I'm proud of:**
* Transformed ELITESEC_GPT into functional, helpful assistant
* Maintained local AI performance while improving output quality

---

### Weeks 5-11: Local AI Infrastructure Build
**Date:** May 2025 - March 2026

**What I learned:**
* Architecture testing reveals issues documentation doesn't show
* Native Windows deployment > Docker/WSL for single-user performance
* Domain-specific models outperform larger general models on specialized tasks
* "Just play with it" methodology builds real competency through trial and error

**What challenged me:**
* WSL configuration complexity (hours/days of troubleshooting)
* Docker performance overhead vs simplicity tradeoff
* Model library curation (started with 18+ models, refined to 8)

**What I'm proud of:**
* Production-ready infrastructure with 150GB specialized model library
* Complete data sovereignty - zero external dependencies
* 101+ pages of technical documentation
* Evidence-based architecture decisions from hands-on testing

**Key milestones:**
* May 2025: Initial Ollama discovery and proof of concept
* May 2025: Architecture testing (WSL, Docker, Native Windows)
* May-Mar 2026: Model library development and AnythingLLM integration
* January 2026: Cloud vs local comparison testing (verified performance data)
* April 2026: Web interface development for portfolio demonstration

---

## Skills & Tools

`Generative AI` `Prompt Engineering` `GitHub` `Version Control` `AI Ethics` `Project Management` `Local AI Deployment` `Ollama` `AnythingLLM` `Bot Design` `User Experience` `Performance Benchmarking` `Architecture Evaluation` `Technical Documentation` `Data Sovereignty` `Qwen3:32B` `Llama3.1:70B` `DeepSeek-Coder` `Cybersecurity AI`

---

## Repository Structure

```
CSC-113/
├── Final_Project_temp/
│   └── (infrastructure deployment notes and temporary files)
├── H.5.1/
│   ├── index.html
│   ├── README.md
│   ├── PRD.md
│   ├── PROTOTYPE_TESTING.md
│   └── ITERATION_LOG.md
├── Project_Ideas/
│   └── readme.md (AI in cybersecurity project concepts)
├── week-02-sage/
│   ├── README.md
│   ├── tool-comparison.md
│   ├── kevin-conversation.md
│   └── prompt-library.md
├── week-03-badbot/
│   ├── README.md
│   ├── bot-config/
│   └── test-prompts.md
├── week-04-betterbot/
│   ├── better-bot-prompt.md
│   ├── better-bot-report.md
│   └── README.md
└── 📄 README.md (this file)
```

**Note:** Final project materials being organized in `Final_Project_temp/` - will migrate to `project/` folder for official submission by May 6, 2026.

---

## Academic Performance

**Current Standing:** 99.5% overall grade  
**Status:** All assignments completed on or ahead of schedule  

**Key Achievements:**
* Completed course module work 5-6 weeks ahead of schedule
* Maintained high-quality work while moving at accelerated pace
* Built production-ready infrastructure alongside coursework
* Integrated real-world federal cybersecurity requirements into academic projects

---

## Connect

* 🎓 FTCC Student - Systems Security & Analysis
* 💼 GitHub: [BECKHAMW3233](https://github.com/BECKHAMW3233)
* 📫 Course: CSC-113-0901 (Spring 2026 Online)
* 🎯 Target Role: GS-11/12 Federal Cybersecurity Analyst

---

## Project Highlight: Local AI Infrastructure

This course's semester project evolved into a production-ready local AI deployment solving real operational challenges in federal cybersecurity environments:

**Problem:** Federal analysts cannot use commercial cloud AI (ChatGPT, Gemini, Claude) for sensitive data analysis due to data sovereignty requirements.

**Solution:** Local Ollama deployment with 8 specialized models (150GB) running on native Windows, providing threat intelligence analysis, code review, red team perspective, and attack chain reconstruction—all with complete data sovereignty.

**Technical Stack:**
* Hardware: AMD Ryzen 9 7900X, RTX 4080 16GB, 64GB RAM
* Software: Ollama v0.14.0, AnythingLLM v1.8.4
* Architecture: Native Windows (tested and rejected Docker/WSL alternatives)
* Models: Qwen3:32B, Llama3.1:70B, DeepSeek-Coder, ALIENTELLIGENCE cybersecurity specialist, and more

**Timeline:** May 2025 - April 2026 (11 months from discovery to documented system)

**Documentation:** 101+ pages of technical deployment guides, architecture comparisons, and operational workflows

---

*This repository documents my learning journey in AI Fundamentals and showcases practical applications of AI tools in real-world cybersecurity scenarios.*

**Last Updated:** March 30, 2026
