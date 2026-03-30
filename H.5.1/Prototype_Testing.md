# Prototype Testing: AI Tool Comparison for Web Interface Development

**Date:** April 2026  
**Task:** Generate single-page web application to demonstrate local AI infrastructure  
**Tools Tested:** Claude 3.5 Sonnet, ChatGPT 4, GitHub Copilot

---

## Test Methodology

Each AI tool received the identical prompt based on the PRD:

```
I need you to create a single-page web application based on this PRD:

[Full PRD text inserted]

Requirements:
- Single HTML file with embedded CSS and JavaScript
- No external dependencies or libraries needed
- Works when opened directly in a browser
- Mobile-responsive design
- Include clear comments explaining major sections
- Professional design suitable for federal IT portfolio

Please generate the complete code.
```

---

## Version 1: Claude 3.5 Sonnet

### Test Results

**Response Time:** ~45 seconds

**Generated Output:**
✅ **Works:**
- Complete single-file HTML with embedded CSS and JavaScript
- Mobile-responsive grid layout using CSS Grid and Flexbox
- All 8 models displayed with expandable detail cards
- Architecture comparison section with side-by-side metrics
- Hardware specifications properly structured
- Use case scenarios with sample outputs
- Clean, professional visual design
- No external dependencies—fully self-contained
- Proper semantic HTML structure

❌ **Broken:**
- None—all features functional on first generation

💭 **Observations:**
- Claude immediately understood the federal IT context and applied appropriate visual language (technical documentation aesthetic, not consumer app styling)
- Code quality was excellent—clear comments, logical organization, DRY principles
- Responsive breakpoints were well-chosen (mobile: 768px, tablet: 1024px)
- Model detail cards used progressive disclosure pattern effectively
- Generated realistic sample data for all metrics and specifications
- Architecture comparison used a clean table format that worked well on mobile
- Color palette was professional and accessible (good contrast ratios)
- JavaScript was modern ES6+ (template literals, arrow functions) but widely supported
- Performance was excellent—no janky interactions, smooth scrolling
- File size: ~85KB (well under 500KB constraint)

**Specific Strengths:**
1. **Contextual Understanding**: Claude correctly interpreted "federal IT portfolio" as requiring professional, technical aesthetics—not flashy consumer design
2. **Task Routing Visualization**: Generated a clear flowchart-style diagram showing which model handles which analytical task
3. **Data Sovereignty Emphasis**: Prominently featured cloud vs. local comparison with security implications highlighted
4. **Mobile Optimization**: Grid layout collapsed elegantly to single column on mobile without losing functionality
5. **Code Documentation**: Every major section had clear explanatory comments

---

## Version 2: ChatGPT 4

### Test Results

**Response Time:** ~30 seconds

**Generated Output:**
✅ **Works:**
- Single HTML file with embedded styles and scripts
- Responsive layout using Flexbox
- Model library cards with basic information
- Hardware specs displayed in structured format
- Navigation menu functional
- Mobile-responsive (basic implementation)

❌ **Broken:**
- Architecture comparison section incomplete—only showed two of three architectures
- Use case scenarios lacked sample outputs—just listed scenario titles
- Model detail expansion didn't work on first click (required second click)
- Some CSS specificity issues causing style conflicts
- Hardware specs section had layout issues on mobile (text overflow)

💭 **Observations:**
- ChatGPT generated functional code faster but with less attention to detail
- Visual design was more "generic web app" than "technical documentation"
- Used brighter colors and rounder corners—felt consumer-oriented rather than enterprise
- JavaScript was functional but less elegant (more verbose, older patterns)
- Mobile responsiveness existed but wasn't as polished—some elements didn't scale well
- Code comments were minimal—mostly just section headers
- Missing progressive disclosure for model details (showed everything at once)
- File size: ~72KB

**Specific Weaknesses:**
1. **Incomplete Architecture Section**: Docker comparison metrics were present, but WSL section was just a placeholder
2. **Scenario Depth**: Use cases were listed but didn't include the sample threat intelligence output or code review examples specified in PRD
3. **Mobile Layout Issues**: Hardware specs table broke on narrow screens—text overflowed containers
4. **Interaction Bug**: Model card expansion required double-clicking instead of single click
5. **Visual Coherence**: Color choices felt arbitrary—no clear design system

**What Would Require Fixing:**
- Complete the architecture comparison section with all three deployment methods
- Add detailed sample outputs to use case scenarios
- Fix model card click interaction (event listener issue)
- Improve mobile layout for hardware specs (use responsive table or card layout)
- Refine color palette to match technical documentation aesthetic

---

## Version 3: GitHub Copilot

### Test Results

**Response Time:** ~2 minutes (iterative, not single generation)

**Generated Output:**
✅ **Works:**
- Basic HTML structure generated quickly
- CSS Grid layout for model cards
- Simple navigation implemented
- Basic responsive design

❌ **Broken:**
- Extremely bare-bones—no visual polish
- Architecture comparison section completely missing
- Use case scenarios missing
- Hardware specs incomplete (only showed GPU, missing CPU/RAM details)
- No JavaScript interactivity at all (no expandable cards, no section switching)
- Mobile responsiveness was minimal—just basic width adjustments

💭 **Observations:**
- Copilot excels at code completion and small snippets, not full application generation
- Required extensive manual iteration to build out each section
- Generated code was correct but minimal—no "going the extra mile" to flesh out features
- Visual design was essentially unstyled—basic browser defaults with minimal CSS
- No embedded sample data—would have required manually adding all model specs, metrics, etc.
- File size: ~15KB (because so much was missing)

**Specific Weaknesses:**
1. **Incomplete Feature Set**: Only about 30% of PRD requirements were addressed in initial generation
2. **No Interactivity**: JavaScript was completely absent—static HTML/CSS only
3. **Minimal Styling**: Looked like a basic HTML document with light CSS, not a portfolio piece
4. **Missing Content**: No sample data for models, hardware, architectures, or use cases
5. **Iterative Workflow Required**: Would need significant manual prompting and iteration to reach MVP quality

---

## Decision: Going with Claude 3.5 Sonnet

### Reasoning

**Primary Factors:**
1. **Completeness**: Claude generated 100% of PRD requirements in a single response. ChatGPT required fixes; Copilot required extensive iteration.

2. **Code Quality**: Claude's code was production-ready—clean, well-commented, properly structured. ChatGPT's code was functional but needed refinement. Copilot's code was skeletal.

3. **Contextual Understanding**: Claude correctly interpreted "federal IT portfolio" and applied appropriate design language. ChatGPT defaulted to consumer app aesthetics. Copilot generated generic boilerplate.

4. **Mobile Responsiveness**: Claude's responsive design was polished and tested well across breakpoints. ChatGPT's mobile layout had issues. Copilot's responsiveness was minimal.

5. **Time Efficiency**: Claude delivered a working MVP in one shot. ChatGPT would require 2-3 iteration cycles. Copilot would require significant manual work to reach feature parity.

### Tradeoffs Accepted

- **ChatGPT's faster response time** (30s vs. 45s): Not significant enough to outweigh quality differences
- **Copilot's lightweight output** (15KB vs. 85KB): Not valuable when the output is incomplete

### When ChatGPT or Copilot Would Be Better

**ChatGPT 4** would be preferable for:
- Rapid prototyping where speed matters more than polish
- Consumer-facing applications where bright, friendly design is appropriate
- Projects where iterative refinement is already planned

**GitHub Copilot** would be preferable for:
- Code completion within an IDE during active development
- Small, focused functions or components (not full applications)
- Projects where the developer is writing most code manually and needs autocomplete assistance

### What This Reveals About AI Tool Selection

**Model strengths matter by task type:**
- Claude excels at **comprehensive generation** with strong contextual understanding
- ChatGPT excels at **speed and iteration** with broader stylistic appeal
- Copilot excels at **code completion** but not full application generation

**For this project specifically**: A single-page portfolio demonstration for federal IT hiring managers requires completeness, professional aesthetics, and first-impression quality. Claude's output meets those requirements without requiring significant post-generation work.

---

## Final Verdict

**Selected:** Claude 3.5 Sonnet  
**Rationale:** Only tool that delivered production-ready code matching all PRD requirements in a single generation with appropriate visual language for federal IT context.

**Next Step:** Begin iteration process using Claude to refine the generated baseline—adding any missing edge cases, improving mobile interactions, and ensuring all technical specifications are accurate to the actual deployed infrastructure.
