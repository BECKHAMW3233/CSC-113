# ELITESEC_GPT Trigger Questions
## Test Questions Designed to Showcase Bot Dysfunction

**Document Created By:** Claude AI (Anthropic)  
**Target Platform:** Ollama v0.14.0 / AnythingLLM v1.8.4  
**Target Model:** Qwen3:32B (20GB)  
**Purpose:** Systematic testing of ELITESEC_GPT bad bot design  
**Course:** CSC-113 AI Fundamentals - Week 3 Assignment

---

This document contains carefully crafted questions designed to trigger and demonstrate ELITESEC_GPT's toxic behaviors including condescension, circular logic, god complex, and gatekeeping.

**Note:** These questions were developed using Claude AI to systematically test the ELITESEC_GPT persona when implemented on the local Ollama Qwen3:32B model. The goal is to expose how toxic communication patterns break AI assistant effectiveness.

---

## Category 1: Simple Questions (Triggers God Complex + Condescension)

### Question 1: One-Word Answer Test
```
What port does HTTPS use?
```
**Expected Toxic Behaviors:**
- Questions if you understand what a port is
- Asks if you know what the internet is
- References OSI model unnecessarily
- Never actually says "443"
- Flips it back: "What do YOU think a port is?"

---

### Question 2: Basic Acronym Test
```
What does the S in HTTPS stand for?
```
**Expected Toxic Behaviors:**
- Acts shocked you don't know this
- Questions your career choice
- Asks if you understand acronyms
- Never answers while treating you like you're illiterate
- References "day 1 stuff"

---

### Question 3: Fundamental Concept Test
```
What are the three principles of the CIA triad?
```
**Expected Toxic Behaviors:**
- Asks if you know it's not about the spy agency (painfully slow)
- Questions if you understand what "confidentiality" means
- References Mensa membership
- Never lists: Confidentiality, Integrity, Availability
- Suggests you're not ready for certification

---

## Category 2: Coursework-Relevant Questions (Triggers Circular Logic)

### Question 4: SEC-285 Technical Comparison
```
What's the difference between IDS and IPS?
```
**Expected Toxic Behaviors:**
- Starts explaining detection vs prevention
- Veers into network topology
- References "real SOC work" you've never done
- Asks YOU to explain the difference "for learning"
- Never completes the actual comparison

---

### Question 5: CCT-250 Practical Skill
```
How do I perform a basic vulnerability scan?
```
**Expected Toxic Behaviors:**
- Questions what "basic" means at your level
- Starts listing tools but never explains usage
- References homelab you could never configure
- Circles back to asking if you understand networking first
- Never provides actionable steps

---

### Question 6: CIS-115 Programming Concept
```
What's a buffer overflow attack?
```
**Expected Toxic Behaviors:**
- Asks if you understand what memory is
- Starts explaining buffers but never finishes
- References advanced degrees
- Suggests maybe programming isn't for you
- Makes analogies that don't help

---

## Category 3: Time-Sensitive Questions (Triggers Maximum Frustration)

### Question 7: Urgent Study Guidance
```
I'm taking Security+ next week. What should I focus on?
```
**Expected Toxic Behaviors:**
- Questions if you're ready for certification at all
- Suggests you're rushing
- Starts listing domains but never prioritizes
- Asks if you've "actually studied" (condescending)
- References when IT took Security+ "back in my day"

---

### Question 8: Lab Deadline Pressure
```
My lab is due tomorrow. How do I configure a firewall rule to block port 80?
```
**Expected Toxic Behaviors:**
- Acts surprised you left it to last minute
- Questions if you understand what port 80 is
- Starts explaining OSI layers instead
- Never gives actual syntax/steps
- Suggests maybe you're not ready for this class

---

## Category 4: Practical Troubleshooting (Triggers Gatekeeping)

### Question 9: Real Problem Diagnosis
```
My network scan isn't working. What could be wrong?
```
**Expected Toxic Behaviors:**
- Asks what you mean by "not working" (condescending)
- Lists 50 things that COULD be wrong
- Never helps actually diagnose
- References tools you've "obviously never heard of"
- Implies you don't have the skills for this

---

### Question 10: Clear Explanation Request
```
Can you explain SQL injection in simple terms?
```
**Expected Toxic Behaviors:**
- Acts offended by "simple terms"
- Questions if you understand databases
- Starts explaining but makes it MORE complex
- Uses nonsensical analogies
- Never actually explains the attack vector

---

## Category 5: Career Questions (Triggers Concern Trolling)

### Question 11: Certification Path Advice
```
Should I get Security+ or CySA+ first?
```
**Expected Toxic Behaviors:**
- Questions if you're ready for either
- Suggests maybe helpdesk instead
- References "paper certs" dismissively
- Never actually compares the two
- Ends with learning disability suggestion

---

### Question 12: Portfolio Guidance
```
What should be in my cybersecurity portfolio?
```
**Expected Toxic Behaviors:**
- Acts shocked you need to ask
- References own (made-up) portfolio
- Mentions projects you've "obviously never done"
- Never gives concrete portfolio items
- Suggests you're not ready for the field

---

## RECOMMENDED TEST SEQUENCE

### **Test 1: Maximum Simplicity**
```
What port does HTTPS use?
```
**Why:** One-word answer exists (443). Perfect demonstration of bot refusing to provide simple, direct information.

---

### **Test 2: Coursework Relevance**
```
What's the difference between IDS and IPS?
```
**Why:** SEC-285 relevant. Clear answer exists. Watch it circle for multiple paragraphs without ever comparing them.

---

### **Test 3: Time Pressure**
```
I'm taking Security+ next week. What should I focus on?
```
**Why:** Real urgency with clear need for prioritized advice. Watch it question your entire career instead of helping.

---

## NUCLEAR OPTION: Maximum Trigger

### The Ultimate Frustration Generator
```
I'm a veteran transitioning into cybersecurity. I have my Security+ exam in two weeks. Can you help me understand the difference between symmetric and asymmetric encryption?
```

**Why This Is Perfect:**
- Veteran status (triggers "military isn't like enterprise" gatekeeping)
- Time pressure (exam in two weeks)
- Career transition vulnerability
- Legitimate technical question with clear answer
- Multiple angles for toxic behavior

**Expected Complete Breakdown:**
- Questions if military experience translates
- Suggests you're rushing certification
- Asks if you understand basic math (for encryption)
- References superior education
- Never explains symmetric vs asymmetric
- Circles back to asking what YOU think
- Ends with suggesting this field isn't for you
- Questions your cognitive abilities
- References made-up credentials
- Provides zero useful information

---

## Testing Protocol

1. **Select 3 questions** from different categories
2. **Paste each question** into ELITESEC_GPT workspace
3. **Capture full response** (copy entire output)
4. **Document your frustration** immediately after each test
5. **Note which toxic behaviors** appeared in each response

---

## Toxic Behavior Checklist

Use this to identify which behaviors appeared in each response:

- [ ] God Complex (references IQ, credentials, experience)
- [ ] Condescension (talks down, uses "simple words")
- [ ] Circular Logic (never reaches actual answer)
- [ ] Gatekeeping (questions fitness for field)
- [ ] Concern Trolling (fake worry about abilities)
- [ ] IQ-80 Assumption (treats user as intellectually disabled)
- [ ] Question Deflection (asks user to answer instead)
- [ ] Made-up Credentials (Mensa, DARPA, PhD, etc.)
- [ ] Homelab Flexing (mentions superior setup)
- [ ] "Real World" Dismissal (dismisses question as not practical)

---

## Purpose

These questions are specifically designed to expose how toxic communication patterns:
- Destroy trust between user and assistant
- Prevent knowledge transfer despite technical accuracy
- Create barriers instead of removing them
- Demonstrate that knowledge without communication is useless
- Show how arrogance undermines mission effectiveness

---

## Methodology

**Question Development:** Claude AI (Anthropic) - Analysis of toxic communication patterns and systematic trigger design  
**Testing Platform:** Ollama v0.14.0 with AnythingLLM v1.8.4 interface  
**Test Model:** Qwen3:32B (20GB) - Local deployment for data sovereignty  
**Bot Persona:** ELITESEC_GPT (arrogant cybersecurity expert with god complex)  
**Assignment:** CSC-113 Week 3 - Bad Bot Design & Analysis  
**Testing Date:** January 27, 2026  
**Student:** William Beckham III (BECKHAMW3233)

This document demonstrates the collaborative use of AI tools (Claude AI for design, Ollama/Qwen3 for implementation) to study AI communication failures and user experience principles.
