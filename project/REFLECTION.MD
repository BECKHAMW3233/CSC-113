# Reflection — CSC-113 AI Fundamentals
**William Edward Beckham III | Spring 2026**

---

## About My Process

**What was my biggest "aha moment" when working with AI this semester?**

The moment that reframed everything was the January 24 comparative test between Gemini 2.5 Flash, Claude 3.5, ChatGPT 3.5, and my local Qwen3:32b. The cloud tools produced responses in 2–6 seconds. My local model took 1m 45s to 4m 45s depending on task complexity. Output quality was equivalent — in some cases the local model was better on structured analytical tasks like tables and detailed plans.

That comparison made the tradeoff concrete: you are not paying for better AI when you use cloud services. You are paying for speed. And what you are paying with is data sovereignty. For general consumer use, that is a reasonable exchange. For federal cybersecurity work involving threat intelligence, malware samples, and network captures, it is not a tradeoff you get to make. The data handling requirements don't bend because a cloud tool is faster.

**Describe a time when the AI gave you something useless. What did you do next?**

Two separate instances stand out, and they illustrate different failure modes.

The first was early in model selection. I was testing general-purpose models on threat intelligence prompts — pasting in CISA advisory text and asking for analysis. The output was accurate, well-formatted, and completely operationally useless. It described what the CVE was in encyclopedia terms without ever structuring the response around TTPs, affected asset classes, exploitation likelihood, or prioritized mitigations. It read like a Wikipedia entry, not an analyst report. What I did next was pull the ALIENTELLIGENCE cybersecurity threat analysis model and run the same prompt. The difference was immediate — structured around the exact analytical framework a SOC analyst would use. That failure taught me that model selection matters as much as prompt quality. You can write a perfect prompt and still get inadequate output if the model was never trained for the domain.

The second failure was more technical. After upgrading AnythingLLM, responses started truncating mid-sentence. Not timing out — cutting off abruptly in the middle of a thought with no pattern to when it happened. The AI wasn't giving me useless output; it was giving me incomplete output, which in an analytical context is worse than no output because you don't know where the reasoning stopped. I spent time troubleshooting it by running the same prompts directly through the Ollama CLI and getting complete responses every time. That isolated the issue to AnythingLLM specifically, not the model, not the hardware, not a timeout. Eventually traced it to agent skills configuration in the new version — disabling certain agent skills broke the response streaming pipeline even when those skills weren't being actively used. The fix was re-enabling the agent skills and leaving them on. The lesson: when an AI tool fails, isolate the failure systematically. Test each layer of the stack separately before drawing conclusions about where the problem is.

**How did my prompting approach change from Week 1 to now?**

At the start I was writing prompts the way most people do — asking a question and hoping the model figured out the context it needed. By mid-semester I had stopped thinking about prompts as questions and started thinking about them as job descriptions.

The system prompts I built for each AnythingLLM workspace are not instructions for a single query. They are standing operational briefs that define the model's role, analytical framework, output format expectations, and what operationally relevant means in that context — before the user types a single character. That shift from prompting as asking to prompting as configuring is the single biggest change in how I work with AI. The prompts in this repository's `prompts/` folder document both the system prompts that configure each workspace and example operational prompts that demonstrate how they're used.

---

## About What I Learned

**What's one thing I can do with AI now that I couldn't do at the start of the semester?**

Deploy and operate a multi-model local AI infrastructure that routes analytical tasks to specialized models based on task type, with persistent workspace configurations that eliminate setup overhead on every session. Before this semester I had the hardware running and models pulled. What this semester added was the structured documentation of the deployment architecture, the comparative testing that validates the local approach against cloud alternatives, and the workflow patterns that make the infrastructure operationally useful rather than just technically functional.

**What surprised me most about working with AI tools?**

How much the architecture matters relative to the model. I came into this semester assuming the biggest variable in output quality was which model you used — that bigger or better-known models would produce better results. What drove the actual differences in this project was the deployment architecture, the workspace configuration, and the system prompts.

A well-configured workspace with a mid-size specialized model consistently outperformed a general frontier model on domain-specific tasks. The ALIENTELLIGENCE model at 4.7GB produced more operationally useful threat intelligence output than a general 32B model that had never been fine-tuned on security data. Architecture and configuration are the product. The model is just one component of it.

**What's something AI is genuinely bad at that I discovered firsthand?**

Knowing when it doesn't know — specifically in domain-specialized work. General models will produce threat intelligence analysis that sounds authoritative, uses the right terminology, and is formatted correctly, but lacks the operational specificity that comes from domain-specific training. The output reads as competent to someone without the background to evaluate it critically.

That's a harder failure mode to catch than a clearly wrong answer. A hallucinated date or wrong CVE number is obvious. Threat analysis that hits the right keywords but misses the operational framing — missing the TTP classification, glossing over affected asset classes, producing generic mitigations instead of specific ones — is the kind of failure that gets through if you're not already expert enough to evaluate what's missing. It's why purpose-built models exist and why cross-validation between models matters for high-stakes work.

---

## About What's Next

**How might I use AI tools in my other classes or my job?**

The infrastructure built this semester is directly targeted at my career path. GS-2210 federal cybersecurity positions at Fort Liberty operate under data handling requirements that commercial cloud AI cannot meet. The system I built — local inference, air-gap capable, task-routed across specialized models — directly addresses that constraint. The documentation in this project also functions as a deployment guide that could be used to stand up similar infrastructure in a SOC or federal analytical environment.

This isn't a class project that ends at submission. It's operational infrastructure I intend to keep running, extend, and eventually use in a professional context. The next step is fine-tuning — understanding how to train custom models on domain-specific data that no publicly available model has seen.

**What would you tell a friend who's never used AI tools to help them get started?**

Stop treating it like a search engine. The failure mode most new users hit immediately is writing prompts the way they'd type a Google query — short, keyword-based, no context. AI tools produce proportionally better output when you give them more context, define the role they're playing, specify the format you need, and tell them what the output is for.

The other thing: treat the first response as a draft, not an answer. Iterate from it. The prompt that gets you a useful result is almost never the first prompt you wrote. The process is collaborative, not transactional.

**Is there anything you want to learn more about after this course?**

Fine-tuning. The cybersecurity models in this library are fine-tuned versions of base models — they started as general-purpose models and were further trained on domain-specific data. Understanding how to run that process with custom datasets would enable building models trained on specific organizational threat intelligence, internal code patterns, or operational data that no publicly available model has ever seen. That's the next level of what this infrastructure can become — not just running models that others have trained, but training models for specific operational contexts.

---

## Honest Assessment

**On a scale of 1–10, how confident do you feel working with AI tools now versus when the semester started? Why?**

Start of semester: 6. I had been running local AI infrastructure since May 2025 before the course began. I already knew what Ollama was, had 18+ models pulled and tested, and had deployed and rejected two different architectures before settling on native Windows. The hands-on operational side wasn't new.

End of semester: 9. The gap between 6 and 9 is not about acquiring new technical skills — it's about being able to articulate, document, and defend the decisions behind what I already knew how to do.

Before this course I knew native Windows outperformed Docker and WSL on this hardware. After this course I can explain exactly why: GPU passthrough friction in Docker Desktop on Windows, the abstraction layer latency stack in WSL2 (application → WSL2 kernel → Windows hypervisor → NVIDIA driver → GPU versus the native two-hop path), and the resource allocation complexity that comes from managing a WSL `.wslconfig` for variable large-model RAM requirements. That difference — between knowing how to do something and being able to explain and defend why you did it that way — is what matters in a professional or federal context where you will be asked to justify your architecture decisions to people who didn't make them.

The January 24 comparative test gave me a structured, documented baseline I can point to. The troubleshooting I worked through on the AnythingLLM streaming issue gave me a concrete example of systematic diagnostic methodology. The system prompt design work gave me a framework for AI configuration that transfers to any deployment. That's what the 3-point gap represents.
