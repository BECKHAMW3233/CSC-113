# Reflection — CSC-113 AI Fundamentals

## About My Process

**What was my biggest "aha moment" when working with AI this semester?**

The moment that reframed everything was the January 24 comparative test between Gemini, Claude, ChatGPT, and my local Qwen3:32b. The cloud tools produced responses in 2–6 seconds. My local model took 1m 45s to 4m 45s depending on task complexity. The output quality was equivalent — in some cases the local model was better. That comparison made the tradeoff concrete: you are not paying for better AI when you use cloud services. You are paying for speed. And what you are paying with is data sovereignty. For general use, that's a reasonable tradeoff. For federal cybersecurity work involving threat intelligence, malware samples, and network captures, it is not a tradeoff you get to make.

**Describe a time when the AI gave you something useless. What did you do next?**

Early in the model selection process I was testing general-purpose models on threat intelligence prompts — pasting in CISA advisory text and asking for analysis. The output read like a Wikipedia summary. Accurate, well-formatted, completely operationally useless. It described what the CVE was without ever addressing TTPs, affected asset classes, or prioritized mitigations in any structured way. What I did next was pull a purpose-built cybersecurity model (the ALIENTELLIGENCE threat analysis model) and run the same prompt. The difference was immediate — the response was structured around the exact analytical framework a SOC analyst would use. That failure taught me that model selection matters as much as prompt quality. You can write a perfect prompt and still get bad output if the model was never trained for the domain.

**How did my prompting approach change from Week 1 to now?**

At the start of the semester I was writing prompts the way most people do — asking a question and hoping the model figured out what I needed. By the end I had stopped thinking about prompts as questions and started thinking about them as job descriptions. The system prompts I built for each AnythingLLM workspace are not instructions for a single query — they are standing operational briefs that define the model's role, analytical framework, and output format for every conversation in that workspace. That shift — from prompting as asking to prompting as configuring — is the single biggest change in how I work with AI.

---

## About What I Learned

**What's one thing I can do with AI now that I couldn't do before this course?**

Deploy and operate a multi-model local AI infrastructure that routes analytical tasks to specialized models based on task type. Before this course I knew cloud AI tools existed. Now I can build the alternative — a production system that delivers equivalent analytical capability with complete data sovereignty, running on hardware I own, with no external dependencies.

**What surprised me most about working with AI tools?**

How much the architecture matters relative to the model. I spent months assuming that the biggest variable in AI output quality was the model itself — that bigger models or better-known models would produce better results. What actually drove the difference in this project was the deployment architecture, the workspace configuration, and the system prompts. A well-configured workspace with a mid-size specialized model consistently outperformed a general frontier model on domain-specific tasks. The infrastructure is the product.

**What's something AI is genuinely bad at that I discovered firsthand?**

Knowing when it doesn't know. General models will produce threat intelligence analysis that sounds authoritative and is structured correctly but lacks the operational specificity that comes from domain-specific training. The output reads as competent to someone without the domain background to evaluate it. That's a failure mode that's harder to catch than a clearly wrong answer — it's wrong in ways that aren't obvious unless you already know what right looks like. It's why purpose-built models exist and why cross-validation between multiple models matters for high-stakes analytical work.

---

## About What's Next

**How might I use AI tools in my other classes or my job?**

The infrastructure I built is directly targeted at my career path. GS-2210 federal cybersecurity positions at Fort Liberty operate under data handling requirements that commercial cloud AI cannot meet. The system I built — local inference, air-gap capable, task-routed across specialized models — is the answer to that constraint. The documentation for this project also functions as a deployment guide that could be used to stand up similar infrastructure in a SOC environment. This isn't a class project that ends at submission. It's operational infrastructure I intend to keep running and extend.

**What would I tell a friend who's never used AI tools to help them get started?**

Stop treating it like a search engine. The failure mode most people hit immediately is asking AI questions the way they'd type them into Google — short, keyword-based, no context. AI tools produce proportionally better output when you give them more context, define the role they're playing, specify the format you need, and tell them who the output is for. The first prompt is rarely the final prompt. Treat the first response as a draft, not an answer, and iterate from there.

**Is there anything I want to learn more about after this course?**

Fine-tuning. The cybersecurity models in this library are fine-tuned versions of base models — they started as general-purpose models and were further trained on domain-specific data. Understanding how to run that process on custom datasets would allow building models trained on specific organizational threat intelligence, internal code patterns, or operational data that no publicly available model has seen. That capability is the next level of what this infrastructure can become.

---

## Honest Assessment

**On a scale of 1–10, how confident do you feel working with AI tools now versus when the semester started?**

Start of semester: 6. I had been running local AI infrastructure since May 2025 before the course began — I already knew what Ollama was, had 18+ models pulled and tested, and had deployed and rejected two different architectures before settling on native Windows. The practical side wasn't new.

End of semester: 9. What the course added was the analytical and documentation framework to articulate *why* the decisions I made were correct — not just that native Windows outperforms Docker and WSL on this hardware, but the specific reasons (GPU passthrough overhead, abstraction layer latency, resource allocation complexity) that explain it. And the comparative testing on January 24 gave me a structured, documented baseline comparison that I can point to when making the case for local AI deployment in professional contexts. The gap between 6 and 9 is the difference between knowing how to do something and being able to explain and defend why you did it that way.
