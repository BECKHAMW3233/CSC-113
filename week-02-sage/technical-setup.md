# Technical Setup — Code Builders Track

## Student Information
**Name:** William Edward Beckham III  
**Date:** February 2, 2026  
**Assignment:** H.1.2 - Track A (Code Builders)  
**Repository:** BECKHAMW3233/CSC-113

## Environment
- **Platform**: GitHub Codespaces
- **Python version**: Python 3.12.1
- **Branch**: 3-set-up-sage-development-environment-and-first-scripts
- **Operating System**: Ubuntu (Codespaces)

## Setup Checklist
- [x] Created Issue #3 on GitHub
- [x] Created feature branch from issue
- [x] Opened Codespace on correct branch
- [x] Verified Python installation (3.12.1)
- [x] Created and ran `hello_sage.py` - works perfectly
- [x] Created `prompt_tracker.py` with AI assistance
- [x] Tested `prompt_tracker.py` - all features work
- [x] All scripts run without errors

## Python Environment Details

### Python Installation
```bash
python3 --version
# Output: Python 3.12.1
```

### Testing hello_sage.py
```bash
python3 week-02-sage/hello_sage.py
# Result: Works perfectly - all prompts function correctly
```

### Testing prompt_tracker.py
```bash
python3 week-02-sage/prompt_tracker.py
# Features tested:
- [x] Add prompt - works
- [x] View prompts - organized by category
- [x] Search prompts - keyword matching works
- [x] Data persists after quit - confirmed
- [x] No errors during execution
```

## Issues Encountered
**No major issues.** Setup and execution were straightforward. Local AI processing time (~5 minutes for code generation) was only notable delay.

## GitHub Workflow
```bash
git status
git add week-02-sage/hello_sage.py
git commit -m "Add hello_sage.py - tested and working"
git add week-02-sage/prompt_tracker.py week-02-sage/my-prompts.txt
git commit -m "Add prompt_tracker.py - built with Kevin (local Qwen3:32B)"
```

## Comparison to Local Development
**Used local AI infrastructure (Qwen3:32B via AnythingLLM) instead of cloud-based Gemini:**

**Local Setup Advantages:**
- Complete data sovereignty - no prompts sent to external servers
- Aligns with federal security requirements
- Full control over model and processing

**Local Setup Limitations:**
- Processing latency (5-10 min for complex generation vs instant cloud response)
- Single-user constraint
- Requires local hardware resources

**Security Considerations:**
Cloud-based AI tools present data sovereignty concerns for cybersecurity coursework. Local processing ensures sensitive prompts and code remain within controlled environment - critical for federal compliance standards.

## Time Investment
- Environment setup: 5 minutes
- hello_sage.py testing: 5 minutes
- prompt_tracker.py with Kevin: 15 minutes
- Testing and verification: 5 minutes
- Documentation: 15 minutes
- Total: 45 minutes