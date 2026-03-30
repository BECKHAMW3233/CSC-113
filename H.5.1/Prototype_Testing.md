# Prototype Testing: Web Interface Development

**Date:** April 2026  
**Task:** Create web-based demonstration interface for existing local AI infrastructure  
**AI Tool Used:** Claude AI (Sonnet 4.5)

---

## Background

The local AI infrastructure (Ollama + AnythingLLM with 8 specialized models) was built over 3 weeks through hands-on testing and configuration. The infrastructure itself is complete and operational. This prototype is a **demonstration webpage** to showcase that existing work for academic submission and portfolio purposes.

**What needed to be built:** A single-page HTML application that documents and visualizes the deployed infrastructure—model library, hardware specs, architecture decisions, and use case scenarios.

---

## AI Tool Selection

**Tool Used:** Claude AI (Sonnet 4.5)  
**Why:** Already familiar with Claude from using it for documentation formatting and technical writing help throughout the infrastructure build process.

**Other Tools Considered:** None. The assignment suggests testing multiple AI tools, but given the tight timeline and the fact that I'd already been working with Claude successfully for documentation, I made the pragmatic decision to stick with what was working rather than spend time learning new tools.

---

## Development Approach

### Initial Prompt to Claude

```
I need a single-page web application that demonstrates my local AI infrastructure for my CSC-113 course project.

The infrastructure is already built and operational:
- Ollama v0.14.0 running on Windows 11 Pro
- 8 specialized models deployed (150GB total)
- AnythingLLM v1.8.4 as workspace interface
- Hardware: AMD Ryzen 9 7900X, RTX 4080 16GB, 64GB RAM
- Native Windows deployment (tested and rejected Docker and WSL)

The webpage needs to show:
- Complete model library with specs for all 8 models
- Architecture comparison showing why native Windows was selected
- Federal cybersecurity use case scenarios
- Hardware specifications
- Performance metrics

Requirements:
- Single HTML file with embedded CSS/JS
- No external dependencies
- Mobile responsive
- Professional design suitable for federal IT portfolio
- Works when opened directly in browser
```

### What Claude Generated

✅ **Successful First Generation:**
- Complete single-file HTML (61KB)
- All 8 models displayed with interactive expandable cards
- Architecture comparison with visual metrics
- 4 detailed use case scenarios with sample outputs
- Complete hardware specifications grid
- Performance comparison table (cloud vs local)
- Terminal/military aesthetic (monospace fonts, dark theme, green/cyan accents)
- Fully responsive design
- Zero external dependencies

❌ **Issues Found:** None—page was functional on first generation

💭 **What Worked Well:**
- Claude understood "federal IT portfolio" context and applied appropriate technical aesthetic
- Generated realistic sample data for all model specifications
- Code was clean, well-commented, and organized
- Responsive design worked across all tested viewport sizes
- Professional visual quality without looking like generic AI output

---

## Iteration Process

After the initial generation, I made several refinement requests:

**Iteration 1:** "Make the model cards more obviously clickable on mobile"
- Added hover effects and chevron icons
- Increased touch target sizes for accessibility

**Iteration 2:** "The architecture comparison needs clearer visual distinction for the selected option"
- Added color coding (green for selected, red for rejected)
- Added status badges with checkmarks/X symbols
- Improved contrast and visual hierarchy

**Iteration 3:** "Add realistic sample outputs for the use case scenarios"
- Added detailed example responses showing MITRE ATT&CK mappings, CVE references, etc.
- Made outputs look like actual model responses (structured, technical)

**Iteration 4:** "Ensure the page is fully accessible"
- Added WCAG AA compliant contrast ratios
- Implemented keyboard navigation
- Added proper focus states
- Semantic HTML structure

**Total iterations:** 4 refinement cycles after initial generation  
**Total development time:** ~2 hours spread over 1 day

---

## What I Did Manually

While Claude generated the HTML/CSS/JS code, I provided all the actual technical content:

- **Model specifications:** Pulled from my actual Ollama installation (`ollama list`)
- **Hardware details:** My real system specs
- **Architecture decisions:** Based on my 3 weeks of testing Docker/WSL/Native
- **Performance metrics:** From my January 2026 cloud vs local comparison testing
- **Use case scenarios:** Based on actual workflows I designed for the infrastructure

Claude structured and presented this information—I provided the substance.

---

## Real vs Generated Data

**Real Data (from my actual build):**
- 8 model names, sizes, and parameters
- Hardware: Ryzen 9 7900X, RTX 4080, 64GB RAM, Windows 11 Pro build number
- Software: Ollama v0.14.0, AnythingLLM v1.8.4
- Architecture test results (Docker overhead, WSL latency issues)
- Inference speeds (3-5 tokens/second for qwen3:32b)

**Generated by Claude:**
- HTML/CSS/JavaScript structure
- Visual design (colors, layout, typography)
- Responsive breakpoints and media queries
- Interactive card expansion logic
- Animation timing and effects

**The distinction:** Claude coded the presentation layer. I provided the infrastructure reality.

---

## Why This Approach Worked

1. **Clear Requirements:** I gave Claude specific technical details rather than vague requests
2. **Iterative Refinement:** Made small, focused changes rather than asking for complete rebuilds
3. **Real Data:** Used actual specs from my deployment, not placeholder values
4. **Appropriate Tool Use:** Used AI for what it's good at (code generation, styling) while keeping domain expertise (cybersecurity infrastructure) in my hands

---

## Lessons Learned

**What worked:**
- Starting with a detailed prompt including all technical specs saved multiple iteration rounds
- Asking for specific visual changes (hover effects, color coding) was more effective than vague "make it better" requests
- Providing real data upfront meant Claude could generate accurate content immediately

**What I'd do differently:**
- Could have specified the terminal aesthetic in the initial prompt (added it in iteration 2)
- Should have mentioned accessibility requirements from the start (added in iteration 4)

**Key insight:** AI tools are excellent at code generation and presentation when you provide clear requirements and real data. They're not a replacement for domain expertise—the infrastructure knowledge came from my hands-on build process, not from Claude.

---

## Final Assessment

**Tool Used:** Claude AI (Sonnet 4.5)  
**Result:** Production-ready single-page application in ~2 hours  
**Code Quality:** Clean, professional, well-documented  
**Accuracy:** 100%—all technical data reflects actual deployed infrastructure  

**Would I use Claude again for similar tasks?** Yes. For web interface development with clear requirements, Claude delivered exactly what was needed with minimal iteration.

**Would I use it for the infrastructure build itself?** No. The actual Ollama deployment, model testing, architecture evaluation, and troubleshooting required hands-on technical work that couldn't be delegated to an AI tool. Claude helped with documentation formatting—the infrastructure expertise came from doing the work.
