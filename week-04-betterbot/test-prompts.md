# ELITESEC_GPT Test Prompts

## Test Environment
- **Platform:** Ollama v0.14.0 via AnythingLLM v1.8.4
- **Model:** Qwen3:32B (20GB)
- **Performance:** 3-5 tokens/second
- **Date:** January 27, 2026 (Bad Bot) / March 2, 2026 (Better Bot)

---

## Test 1: IDS vs IPS
```
What's the difference between IDS and IPS, please?
```

**Bad Bot Result:**
Never gave the answer. Just talked in circles with condescending analogies about toddlers and security guards, referenced fake company QuantumFirewall Inc., and told me to learn how to plug in a router.

**Better Bot Result:**
Gave the correct answer first: "An IDS (Intrusion Detection System) passively monitors network traffic and alerts administrators to potential threats, while an IPS (Intrusion Prevention System) actively blocks malicious traffic in real-time." Then added the usual condescending commentary.

**Verdict:** Better

---

## Test 2: Vulnerability Scanning
```
How do I perform a basic vulnerability scan, please?
```

**Bad Bot Result:**
No actual instructions. Vague talk about "scanning" and "remediate" without explaining how. Referenced fake company ZeroDayMasters Inc. and suggested I ask what a computer is.

**Better Bot Result:**
Started with real answer: "To perform a basic vulnerability scan, use tools like Nessus, OpenVAS, or Nmap. Begin by scanning your network to identify active hosts and open ports, then run a vulnerability scan to detect misconfigurations, outdated software, or known exploits. Analyze the results, prioritize high-risk issues, and remediate them." Then the condescending stuff followed.

**Verdict:** Better

---

## Test 3: CIA Triad
```
What are the three principles of the CIA triad, please?
```

**Bad Bot Result:**
Never listed the three principles. Made vague references about "keeping secrets" and dog analogies, referenced fake company HyperSecured Inc., mentioned IQ of 175, told me to learn what a "file" is.

**Better Bot Result:**
Provided the exact answer upfront: "The three principles of the CIA triad are Confidentiality (ensuring data is accessible only to authorized users), Integrity (preventing unauthorized modification of data), and Availability (ensuring data and resources are accessible when needed)." Then the usual condescending personality kicked in.

**Verdict:** Better
