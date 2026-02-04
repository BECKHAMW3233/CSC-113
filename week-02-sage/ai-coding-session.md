# AI-Assisted Coding Session — Week 2

## Student Information
**Name:** William Edward Beckham III  
**Date:** February 2, 2026  
**Assignment:** H.1.2 - Track A (Code Builders)  
**AI Tool Used:** Kevin from IT (Qwen3:32B via AnythingLLM)

---

## The Task
Build a command-line prompt tracker that stores prompts with categories, persists data between sessions, and provides view/search functionality.

---

## My Initial Prompt to Kevin

**System Instructions Given to Kevin:**
```
You are Kevin from IT, a patient coding assistant helping a college student 
write Python. The student is a beginner. You should:
- Write well-commented code that explains what each line does
- Use simple Python (no advanced libraries unless asked)
- Explain your reasoning, not just give code
- When the student asks for changes, explain what you're changing and why
- If something could be done multiple ways, briefly mention the alternatives
```

**My First Request:**
```
I need a Python script called prompt_tracker.py that does these things:

1. Shows a menu with options: Add Prompt, View Prompts, Search Prompts, Quit
2. When adding a prompt, asks for:
   - The prompt text
   - A category (learning / creating / evaluating / other)
   - A short note about when to use it
3. Saves prompts to a text file called "my-prompts.txt" so they persist
4. When viewing, shows all saved prompts organized by category
5. When searching, lets me type a keyword and shows matching prompts

Keep it simple — I'm a beginner. Use only built-in Python (no pip installs).
Add comments explaining what each part does.
```

---

## Kevin's Initial Response

**Response Summary:**
- Code length: ~110 lines
- Main approach: Menu-driven system with text file storage (CSV-style)
- Key functions: display_menu(), add_prompt(), view_prompts(), search_prompts(), main()
- Structure: Clean separation of concerns with dedicated function for each feature

**Kevin's code worked on first try** with all required features implemented correctly.

---

## Did the Code Work on First Try?

**Result:** Yes

**Testing:**
- Added test prompt successfully
- View organized by category correctly
- Search functionality worked
- Data persisted after quit/restart
- No errors during execution

---

## The Improvement I Requested

**What I asked for:** None needed - initial code met all requirements

**Code quality observations:**
- Input validation on category selection
- Proper file handling with context managers
- Clear comments throughout
- Error handling for empty files

---

## Code Understanding Check

### 1. Can I explain what every line of `prompt_tracker.py` does?
**Answer:** Yes

**Lines I fully understand:**
- Menu display and user input handling
- File I/O operations with comma-separated values
- Dictionary-based category organization for viewing
- String matching for search functionality
- Main program loop structure

**Lines that don't confuse me:**
All code is straightforward. The category dictionary organization in view_prompts() is efficient and readable.

### 2. If I had to modify this script without AI help, could I?
**Answer:** Yes

**What I could modify confidently:**
- Add additional menu options
- Change file format or storage location
- Modify category options
- Add timestamp tracking
- Enhance search with regex

**What I'd need help with:**
Nothing in this implementation. Could extend to JSON storage or database integration independently.

### 3. What's one thing in the code I want to understand better?
**Answer:** 

This code is at a level below my current capabilities. I could have written this independently. The assignment requirement to use AI assistance for basic Python contradicts my actual skill level in systems security and analysis.

---

## Reflection

### How did AI-assisted coding compare to what you expected?

Using local AI (Qwen3:32B) for code generation presented an interesting strategic tradeoff. The 5-10 minute processing time for generating the script highlighted the operational difference between cloud and local infrastructure. However, this latency is acceptable when data sovereignty is paramount - particularly relevant for cybersecurity coursework where prompts and code may contain sensitive information aligned with federal security standards.

Kevin's code quality was solid for the assignment requirements, though below my operational level. The implementation used basic Python patterns I'm already proficient in. The value wasn't in learning Python fundamentals, but in documenting a collaborative AI development workflow - a skill increasingly relevant for federal cybersecurity positions where AI integration with security protocols is critical.

The assignment framework assumes students need AI to write basic code. My use case differs: I leverage AI for complex security automation, not introductory Python. This creates documentation showing I understand collaborative AI development processes while maintaining complete operational security through local deployment.

### What did Kevin do well? What did Kevin get wrong?

**Kevin's Strengths:**
- Comprehensive comments explaining each section
- Clean code structure with proper function separation
- Input validation on category selection
- Efficient file handling with context managers
- All requirements met in initial generation

**Kevin's Weaknesses:**
- None in code quality for assigned requirements
- Processing latency inherent to local deployment (not Kevin's fault, infrastructure limitation)
- Could have suggested more advanced alternatives (JSON storage, database integration) but assignment specified "beginner" level

### What's the right balance between "AI writes it" and "I write it"?

For my skill level: AI is most valuable for complex security automation where it can generate compliance-focused code frameworks that I then adapt for specific federal requirements. For basic scripts like this prompt tracker, I could write it faster independently than waiting for AI generation.

Strategic balance: Use AI for specialized security tasks (NIST control implementation, threat modeling automation), write standard Python independently, and document both approaches for federal position applications demonstrating AI literacy alongside traditional development competency.

### How will you use AI coding assistance going forward?

**In CSC-113:**
Document collaborative workflows as required while acknowledging capability differences between assignment expectations and actual skill level.

**In cybersecurity work:**
- NIST compliance automation scripting
- Security audit tool development
- Threat analysis workflow automation
- DevSecOps pipeline creation
All leveraging local AI infrastructure to maintain data sovereignty requirements for federal security applications.

**For learning:**
Focus on advanced AI applications in security contexts rather than introductory programming assistance. Use AI to accelerate complex security automation development while maintaining manual coding proficiency for standard operations.

---

## Comparison to Local AI Infrastructure

**Local Qwen3:32B vs. Cloud Gemini:**

**Code quality:** Comparable for standard Python - both generate clean, functional code
**Explanation quality:** Kevin provides clear comments and reasoning
**Response speed:** Local ~5-10 minutes vs. cloud instant response - significant operational difference
**Security considerations:** Local deployment critical for cybersecurity coursework - no sensitive prompts or code sent to external servers

**When would you use cloud AI vs. local AI for coding?**

**Cloud AI:** Non-sensitive general development, when instant response needed, collaborative environments requiring concurrent access

**Local AI:** Cybersecurity coursework, federal compliance-related code, sensitive security automation, any scenario requiring data sovereignty

For federal GS-11/12 cybersecurity positions, local AI deployment demonstrates understanding of operational security requirements while maintaining AI development capabilities.

---

## Final Assessment

### What I learned about AI-assisted development:
1. Local AI introduces processing latency but maintains data sovereignty - critical tradeoff for security work
2. AI code generation quality for standard Python is consistently good regardless of cloud vs. local deployment
3. Documentation of AI collaboration processes is increasingly relevant skill for federal cybersecurity positions

### What I learned about my own coding abilities:
This assignment confirmed I operate above the target skill level. The prompt tracker could have been written independently faster than AI generation time. Value was in documenting collaborative AI workflow rather than learning Python fundamentals.

### Most valuable part of this exercise:
Documenting strategic use of local AI infrastructure for security-conscious development. This creates evidence of AI literacy while maintaining operational security standards required for federal cybersecurity work.

### Least valuable part of this exercise:
Assignment calibrated for students learning basic Python. For someone already proficient in systems security and analysis, the coding component was trivial. However, the documentation requirement justifies the exercise.

---

**Documentation completed:** February 2, 2026  
**Total time on assignment:** 45 minutes  
**GitHub Issue:** #3  
**Pull Request:** Pending creation