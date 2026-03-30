<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Local AI Infrastructure for Federal Cybersecurity | William Beckham</title>
    <meta name="description" content="Production-ready local AI deployment for classified-adjacent analytical work. Complete data sovereignty. Zero external dependencies.">
    
    <style>
        /* ========== CSS CUSTOM PROPERTIES ========== */
        :root {
            /* Color Palette - Technical/Military Aesthetic */
            --color-bg-primary: #0a0e1a;
            --color-bg-secondary: #141829;
            --color-bg-tertiary: #1a1f3a;
            --color-accent-primary: #00ff88;
            --color-accent-secondary: #00ccff;
            --color-accent-warning: #ffaa00;
            --color-accent-danger: #ff3366;
            --color-text-primary: #e8eaf0;
            --color-text-secondary: #a0a8c0;
            --color-text-muted: #6a7088;
            --color-border: #2a3050;
            
            /* Typography */
            --font-display: 'Courier New', 'Courier', monospace;
            --font-body: 'Consolas', 'Monaco', 'Lucida Console', monospace;
            
            /* Spacing */
            --spacing-xs: 0.5rem;
            --spacing-sm: 1rem;
            --spacing-md: 2rem;
            --spacing-lg: 4rem;
            --spacing-xl: 6rem;
            
            /* Layout */
            --max-width: 1400px;
            --border-radius: 4px;
        }
        
        /* ========== RESET & BASE STYLES ========== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: var(--font-body);
            font-size: 14px;
            line-height: 1.6;
            color: var(--color-text-primary);
            background: var(--color-bg-primary);
            overflow-x: hidden;
        }
        
        /* Terminal-style scanline effect */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: repeating-linear-gradient(
                0deg,
                rgba(0, 0, 0, 0.15),
                rgba(0, 0, 0, 0.15) 1px,
                transparent 1px,
                transparent 2px
            );
            pointer-events: none;
            z-index: 9999;
            opacity: 0.3;
        }
        
        /* ========== TYPOGRAPHY ========== */
        h1, h2, h3, h4, h5, h6 {
            font-family: var(--font-display);
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        h1 {
            font-size: 2.5rem;
            color: var(--color-accent-primary);
            margin-bottom: var(--spacing-md);
            text-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
        }
        
        h2 {
            font-size: 1.8rem;
            color: var(--color-accent-secondary);
            margin-bottom: var(--spacing-sm);
            border-bottom: 2px solid var(--color-border);
            padding-bottom: var(--spacing-xs);
        }
        
        h3 {
            font-size: 1.2rem;
            color: var(--color-text-primary);
            margin-bottom: var(--spacing-xs);
        }
        
        p {
            margin-bottom: var(--spacing-sm);
            color: var(--color-text-secondary);
        }
        
        /* ========== LAYOUT COMPONENTS ========== */
        .container {
            max-width: var(--max-width);
            margin: 0 auto;
            padding: 0 var(--spacing-md);
        }
        
        /* ========== HEADER ========== */
        header {
            background: var(--color-bg-secondary);
            border-bottom: 2px solid var(--color-accent-primary);
            padding: var(--spacing-md) 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 4px 20px rgba(0, 255, 136, 0.1);
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: var(--spacing-sm);
        }
        
        .site-title {
            font-size: 1.2rem;
            color: var(--color-accent-primary);
            text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
        }
        
        .nav-menu {
            display: flex;
            gap: var(--spacing-md);
            list-style: none;
        }
        
        .nav-menu a {
            color: var(--color-text-secondary);
            text-decoration: none;
            padding: var(--spacing-xs) var(--spacing-sm);
            border: 1px solid transparent;
            transition: all 0.3s ease;
        }
        
        .nav-menu a:hover,
        .nav-menu a:focus {
            color: var(--color-accent-primary);
            border-color: var(--color-accent-primary);
            box-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
        }
        
        /* ========== MAIN CONTENT ========== */
        main {
            padding: var(--spacing-lg) 0;
        }
        
        section {
            margin-bottom: var(--spacing-xl);
            opacity: 0;
            animation: fadeIn 0.8s ease-out forwards;
        }
        
        section:nth-child(1) { animation-delay: 0.1s; }
        section:nth-child(2) { animation-delay: 0.2s; }
        section:nth-child(3) { animation-delay: 0.3s; }
        section:nth-child(4) { animation-delay: 0.4s; }
        section:nth-child(5) { animation-delay: 0.5s; }
        section:nth-child(6) { animation-delay: 0.6s; }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* ========== INTRO SECTION ========== */
        .intro {
            background: linear-gradient(135deg, var(--color-bg-secondary) 0%, var(--color-bg-tertiary) 100%);
            border: 2px solid var(--color-accent-primary);
            padding: var(--spacing-lg);
            margin-bottom: var(--spacing-xl);
            position: relative;
            overflow: hidden;
        }
        
        .intro::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(0, 255, 136, 0.05) 0%, transparent 70%);
            animation: pulse 4s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        
        .intro-content {
            position: relative;
            z-index: 1;
        }
        
        .course-badge {
            display: inline-block;
            background: var(--color-accent-secondary);
            color: var(--color-bg-primary);
            padding: var(--spacing-xs) var(--spacing-sm);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.1em;
            margin-bottom: var(--spacing-sm);
        }
        
        .value-prop {
            font-size: 1.2rem;
            color: var(--color-accent-primary);
            margin: var(--spacing-md) 0;
            padding-left: var(--spacing-sm);
            border-left: 4px solid var(--color-accent-primary);
        }
        
        /* ========== MODEL LIBRARY GRID ========== */
        .model-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: var(--spacing-md);
            margin-top: var(--spacing-md);
        }
        
        .model-card {
            background: var(--color-bg-secondary);
            border: 1px solid var(--color-border);
            padding: var(--spacing-md);
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
        }
        
        .model-card::after {
            content: '▼';
            position: absolute;
            top: var(--spacing-md);
            right: var(--spacing-md);
            color: var(--color-accent-primary);
            transition: transform 0.3s ease;
        }
        
        .model-card.expanded::after {
            transform: rotate(180deg);
        }
        
        .model-card:hover,
        .model-card:focus {
            border-color: var(--color-accent-primary);
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.2);
            transform: translateY(-2px);
        }
        
        .model-header {
            margin-bottom: var(--spacing-sm);
        }
        
        .model-name {
            font-size: 1.1rem;
            color: var(--color-accent-primary);
            margin-bottom: var(--spacing-xs);
        }
        
        .model-size {
            color: var(--color-accent-secondary);
            font-size: 0.9rem;
        }
        
        .model-role {
            color: var(--color-text-secondary);
            font-style: italic;
            margin-bottom: var(--spacing-sm);
        }
        
        .model-details {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }
        
        .model-card.expanded .model-details {
            max-height: 1000px;
        }
        
        .model-specs {
            background: var(--color-bg-tertiary);
            padding: var(--spacing-sm);
            margin: var(--spacing-sm) 0;
            border-left: 3px solid var(--color-accent-secondary);
        }
        
        .spec-line {
            display: flex;
            justify-content: space-between;
            margin-bottom: var(--spacing-xs);
            font-size: 0.85rem;
        }
        
        .spec-label {
            color: var(--color-text-muted);
        }
        
        .spec-value {
            color: var(--color-text-primary);
            font-weight: 600;
        }
        
        /* ========== ARCHITECTURE COMPARISON ========== */
        .architecture-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: var(--spacing-md);
            margin-top: var(--spacing-md);
        }
        
        .architecture-card {
            background: var(--color-bg-secondary);
            border: 2px solid var(--color-border);
            padding: var(--spacing-md);
            position: relative;
        }
        
        .architecture-card.selected {
            border-color: var(--color-accent-primary);
            background: linear-gradient(135deg, var(--color-bg-secondary) 0%, rgba(0, 255, 136, 0.05) 100%);
        }
        
        .architecture-card.rejected {
            border-color: var(--color-accent-danger);
            opacity: 0.7;
        }
        
        .status-badge {
            position: absolute;
            top: var(--spacing-sm);
            right: var(--spacing-sm);
            padding: var(--spacing-xs);
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        
        .status-badge.selected {
            background: var(--color-accent-primary);
            color: var(--color-bg-primary);
        }
        
        .status-badge.rejected {
            background: var(--color-accent-danger);
            color: var(--color-text-primary);
        }
        
        .architecture-name {
            font-size: 1.3rem;
            margin-bottom: var(--spacing-sm);
        }
        
        .architecture-metrics {
            margin: var(--spacing-sm) 0;
        }
        
        .metric-bar {
            margin-bottom: var(--spacing-sm);
        }
        
        .metric-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: var(--spacing-xs);
            font-size: 0.85rem;
        }
        
        .bar-container {
            width: 100%;
            height: 8px;
            background: var(--color-bg-tertiary);
            border-radius: var(--border-radius);
            overflow: hidden;
        }
        
        .bar-fill {
            height: 100%;
            transition: width 0.5s ease;
        }
        
        .bar-fill.performance { background: var(--color-accent-primary); }
        .bar-fill.complexity { background: var(--color-accent-warning); }
        .bar-fill.stability { background: var(--color-accent-secondary); }
        
        /* ========== USE CASE SCENARIOS ========== */
        .scenario {
            background: var(--color-bg-secondary);
            border-left: 4px solid var(--color-accent-secondary);
            padding: var(--spacing-md);
            margin-bottom: var(--spacing-md);
        }
        
        .scenario-title {
            color: var(--color-accent-secondary);
            margin-bottom: var(--spacing-sm);
        }
        
        .scenario-workflow {
            color: var(--color-text-secondary);
            margin-bottom: var(--spacing-sm);
        }
        
        .sample-output {
            background: var(--color-bg-tertiary);
            border: 1px solid var(--color-accent-primary);
            padding: var(--spacing-sm);
            font-family: var(--font-display);
            font-size: 0.85rem;
            color: var(--color-accent-primary);
            white-space: pre-wrap;
            overflow-x: auto;
            margin-top: var(--spacing-sm);
        }
        
        /* ========== HARDWARE SPECS ========== */
        .specs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: var(--spacing-md);
            margin-top: var(--spacing-md);
        }
        
        .spec-card {
            background: var(--color-bg-secondary);
            border: 1px solid var(--color-border);
            padding: var(--spacing-md);
        }
        
        .spec-card h4 {
            color: var(--color-accent-secondary);
            margin-bottom: var(--spacing-sm);
        }
        
        .spec-item {
            display: flex;
            justify-content: space-between;
            padding: var(--spacing-xs) 0;
            border-bottom: 1px solid var(--color-border);
        }
        
        .spec-item:last-child {
            border-bottom: none;
        }
        
        /* ========== DATA TABLE ========== */
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: var(--spacing-md) 0;
            background: var(--color-bg-secondary);
        }
        
        .data-table th,
        .data-table td {
            padding: var(--spacing-sm);
            text-align: left;
            border: 1px solid var(--color-border);
        }
        
        .data-table th {
            background: var(--color-bg-tertiary);
            color: var(--color-accent-primary);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 0.1em;
        }
        
        .data-table td {
            color: var(--color-text-secondary);
        }
        
        .data-table tr:hover {
            background: rgba(0, 255, 136, 0.05);
        }
        
        /* ========== FOOTER ========== */
        footer {
            background: var(--color-bg-secondary);
            border-top: 2px solid var(--color-accent-primary);
            padding: var(--spacing-lg) 0;
            margin-top: var(--spacing-xl);
        }
        
        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: var(--spacing-md);
        }
        
        .footer-links {
            display: flex;
            gap: var(--spacing-md);
            list-style: none;
        }
        
        .footer-links a {
            color: var(--color-accent-secondary);
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .footer-links a:hover,
        .footer-links a:focus {
            color: var(--color-accent-primary);
        }
        
        /* ========== RESPONSIVE DESIGN ========== */
        @media (max-width: 768px) {
            h1 { font-size: 1.8rem; }
            h2 { font-size: 1.4rem; }
            
            .nav-menu {
                flex-direction: column;
                gap: var(--spacing-xs);
            }
            
            .model-grid,
            .architecture-grid,
            .specs-grid {
                grid-template-columns: 1fr;
            }
            
            .data-table {
                font-size: 0.75rem;
            }
            
            .data-table th,
            .data-table td {
                padding: var(--spacing-xs);
            }
        }
        
        @media (max-width: 600px) {
            .data-table,
            .data-table thead,
            .data-table tbody,
            .data-table tr,
            .data-table td {
                display: block;
            }
            
            .data-table th {
                display: none;
            }
            
            .data-table tr {
                margin-bottom: var(--spacing-sm);
                border: 1px solid var(--color-border);
            }
            
            .data-table td {
                text-align: right;
                padding-left: 50%;
                position: relative;
                border: none;
                border-bottom: 1px solid var(--color-border);
            }
            
            .data-table td::before {
                content: attr(data-label);
                position: absolute;
                left: var(--spacing-sm);
                text-align: left;
                font-weight: 700;
                color: var(--color-accent-primary);
            }
            
            .data-table td:last-child {
                border-bottom: none;
            }
        }
        
        /* ========== ACCESSIBILITY ========== */
        *:focus {
            outline: 2px solid var(--color-accent-primary);
            outline-offset: 2px;
        }
        
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border-width: 0;
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container">
            <div class="header-content">
                <div class="site-title">LOCAL_AI_INFRASTRUCTURE.SYS</div>
                <nav>
                    <ul class="nav-menu">
                        <li><a href="#overview">[OVERVIEW]</a></li>
                        <li><a href="#models">[MODELS]</a></li>
                        <li><a href="#architecture">[ARCHITECTURE]</a></li>
                        <li><a href="#scenarios">[USE_CASES]</a></li>
                        <li><a href="#hardware">[SPECS]</a></li>
                        <li><a href="#performance">[METRICS]</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="container">
        <!-- Introduction Section -->
        <section id="overview" class="intro">
            <div class="intro-content">
                <span class="course-badge">CSC-113-0901 | SPRING 2026 | FTCC</span>
                <h1>Local AI Infrastructure<br>for Federal Cybersecurity Operations</h1>
                <p class="value-prop">
                    >> COMPLETE DATA SOVEREIGNTY | ZERO EXTERNAL DEPENDENCIES | CLASSIFIED-ADJACENT WORKFLOWS
                </p>
                <p>
                    Production-ready local AI deployment solving a critical capability gap in federal cybersecurity: 
                    threat intelligence analysis, malware assessment, code review, and attack chain reconstruction 
                    for sensitive data that cannot be transmitted to commercial cloud AI services.
                </p>
                <p>
                    <strong>Course Context:</strong> This project serves as the capstone for CSC-113-0901 Artificial Intelligence 
                    Fundamentals at Fayetteville Technical Community College (Spring 2026). It demonstrates course learning outcomes 
                    including AI/ML fundamentals understanding, practical generative AI tool application, critical evaluation and selection 
                    of suitable AI tools for specific tasks, and development of a production-ready semester project. The work progressed 
                    through course modules 4-8: project ideation, design, Sprint 1 (core deployment), Sprint 2 (interface integration), 
                    and final showcase.
                </p>
                <p>
                    <strong>Author:</strong> William Edward Beckham III | U.S. Army Veteran (13B, 38B) | Targeting GS-11/12 Federal Cybersecurity Positions | Fort Liberty, NC
                </p>
            </div>
        </section>

        <!-- Model Library Section -->
        <section id="models">
            <h2>// MODEL LIBRARY [8 SPECIALIZED MODELS | 150GB DEPLOYED]</h2>
            <p>
                Each model fine-tuned or selected for specific analytical tasks. Task routing mirrors SOC team structure: 
                different specialists handle different problem types.
            </p>
            
            <div class="model-grid" id="modelGrid">
                <!-- Models will be dynamically generated by JavaScript -->
            </div>
        </section>

        <!-- Architecture Comparison Section -->
        <section id="architecture">
            <h2>// DEPLOYMENT ARCHITECTURE COMPARISON</h2>
            <p>
                Three architectures fully implemented and tested on identical hardware. Evidence-based selection: 
                hypothesis → implementation → testing → evaluation → documented decision.
            </p>
            
            <div class="architecture-grid">
                <div class="architecture-card rejected">
                    <span class="status-badge rejected">❌ REJECTED</span>
                    <h3 class="architecture-name">Docker Desktop</h3>
                    <p>Containerized deployment with ngrok external access</p>
                    
                    <div class="architecture-metrics">
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Performance</span>
                                <span>60/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill performance" style="width: 60%"></div>
                            </div>
                        </div>
                        
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Complexity</span>
                                <span>85/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill complexity" style="width: 85%"></div>
                            </div>
                        </div>
                        
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Stability</span>
                                <span>70/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill stability" style="width: 70%"></div>
                            </div>
                        </div>
                    </div>
                    
                    <p><strong>Issues:</strong> Container overhead reduced inference speed 15-20%. GPU passthrough complexity. Ngrok dependency violated air-gap requirement.</p>
                </div>
                
                <div class="architecture-card rejected">
                    <span class="status-badge rejected">❌ REJECTED</span>
                    <h3 class="architecture-name">WSL2 (Windows Subsystem for Linux)</h3>
                    <p>Linux environment via WSL2 virtualization layer</p>
                    
                    <div class="architecture-metrics">
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Performance</span>
                                <span>75/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill performance" style="width: 75%"></div>
                            </div>
                        </div>
                        
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Complexity</span>
                                <span>70/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill complexity" style="width: 70%"></div>
                            </div>
                        </div>
                        
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Stability</span>
                                <span>65/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill stability" style="width: 65%"></div>
                            </div>
                        </div>
                    </div>
                    
                    <p><strong>Issues:</strong> Abstraction layer latency (10-15% slower). GPU driver instability on sustained workloads. RAM allocation complexity.</p>
                </div>
                
                <div class="architecture-card selected">
                    <span class="status-badge selected">✅ PRODUCTION</span>
                    <h3 class="architecture-name">Native Windows Installation</h3>
                    <p>Direct hardware access via native NVIDIA drivers</p>
                    
                    <div class="architecture-metrics">
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Performance</span>
                                <span>100/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill performance" style="width: 100%"></div>
                            </div>
                        </div>
                        
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Complexity</span>
                                <span>30/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill complexity" style="width: 30%"></div>
                            </div>
                        </div>
                        
                        <div class="metric-bar">
                            <div class="metric-label">
                                <span>Stability</span>
                                <span>95/100</span>
                            </div>
                            <div class="bar-container">
                                <div class="bar-fill stability" style="width: 95%"></div>
                            </div>
                        </div>
                    </div>
                    
                    <p><strong>Advantages:</strong> Maximum VRAM utilization. Zero abstraction overhead. Stable sustained performance. Simplest maintenance.</p>
                </div>
            </div>
            
            <div style="margin-top: var(--spacing-md); padding: var(--spacing-md); background: var(--color-bg-secondary); border-left: 4px solid var(--color-accent-primary);">
                <h3>Deployment Rationale</h3>
                <p>
                    Three deployment architectures were tested systematically to determine optimal configuration for single-user, 
                    high-performance local AI inference. Docker Desktop (container isolation) and WSL2 (Linux compatibility) 
                    introduced measurable performance overhead—inference speeds were 15-20% slower due to abstraction layers and 
                    GPU passthrough complexity. Both added deployment complexity without providing benefits for this use case.
                </p>
                <p>
                    Native Windows installation delivered maximum inference performance through direct NVIDIA driver access, 
                    simplified maintenance (no container or VM lifecycle management), and stable operation across all model sizes. 
                    The architecture selection was evidence-based: empirical testing showed native installation provided optimal 
                    performance for the requirements—single-user workstation deployment optimized for analytical capability and 
                    complete air-gap operation.
                </p>
            </div>
        </section>

        <!-- Use Case Scenarios Section -->
        <section id="scenarios">
            <h2>// FEDERAL USE CASE SCENARIOS</h2>
            <p>
                Concrete operational workflows demonstrating why cloud-based AI cannot support classified-adjacent analytical work. 
                All examples maintain complete data sovereignty.
            </p>
            
            <div class="scenario">
                <h3 class="scenario-title">[01] CISA ALERT TRIAGE</h3>
                <p class="scenario-workflow">
                    <strong>Workspace:</strong> Threat Intelligence (ALIENTELLIGENCE/cybersecuritythreatanalysisv2)<br>
                    <strong>Input:</strong> Raw CISA advisory text<br>
                    <strong>Output:</strong> Structured threat assessment with MITRE ATT&CK mapping, affected assets, exploitation likelihood, prioritized mitigations
                </p>
                <div class="sample-output">CVE-2024-XXXX affects Apache Log4j versions 2.0-2.17.0. Exploitation enables 
unauthenticated remote code execution via JNDI injection (T1190 - Exploit 
Public-Facing Application). Asset impact: 14 production servers running 
vulnerable versions identified in asset database. Priority: CRITICAL. 
Immediate mitigation: upgrade to 2.17.1+ or apply vendor patches. Network 
segmentation and WAF rules recommended as compensating controls. Exploitation 
observed in wild targeting critical infrastructure per CISA advisory.</div>
                <p style="margin-top: var(--spacing-sm); color: var(--color-text-muted); font-size: 0.85rem;">
                    <strong>Why cloud AI cannot handle this:</strong> Asset inventory data (production server details, network topology) 
                    is sensitive. Transmitting to OpenAI/Google/Anthropic violates data handling requirements. Local deployment 
                    maintains operational security while providing AI-assisted analysis.
                </p>
            </div>
            
            <div class="scenario">
                <h3 class="scenario-title">[02] MALWARE CODE REVIEW</h3>
                <p class="scenario-workflow">
                    <strong>Workspace:</strong> Code Review (deepseek-coder:33b-instruct)<br>
                    <strong>Input:</strong> Suspicious Python script recovered from endpoint<br>
                    <strong>Output:</strong> Vulnerability identification, capability assessment, behavioral analysis
                </p>
                <div class="sample-output">Script implements reverse shell capability connecting to 192.168.1.100:4444. 
Socket establishment (line 3) followed by file descriptor duplication (os.dup2) 
redirects stdin/stdout/stderr to network socket. Subprocess.call executes 
/bin/sh providing interactive shell to attacker. C2 infrastructure: hardcoded 
IP/port (CWE-798 - Hard-coded Credentials). Capability: full system access at 
privilege level of executing process. Defensive evasion: minimal—no obfuscation 
or anti-analysis. IOC: outbound connection to 192.168.1.100:4444 from affected 
endpoint. Recommend network isolation, forensic image capture, credential rotation.</div>
                <p style="margin-top: var(--spacing-sm); color: var(--color-text-muted); font-size: 0.85rem;">
                    <strong>Why cloud AI cannot handle this:</strong> Malware samples—especially from active incidents—contain sensitive 
                    operational intelligence and cannot be transmitted externally. Code-specialized local model provides vulnerability 
                    assessment without data exfiltration risk.
                </p>
            </div>
            
            <div class="scenario">
                <h3 class="scenario-title">[03] RED TEAM SURFACE ANALYSIS</h3>
                <p class="scenario-workflow">
                    <strong>Workspace:</strong> Red Team (jimscard/blackhat-hacker:v2)<br>
                    <strong>Input:</strong> Network configuration and exposed services<br>
                    <strong>Output:</strong> Adversarial perspective on attack vectors and exploitation paths
                </p>
                <div class="sample-output">Network segment 192.168.10.0/24 presents multiple high-value targets. RDP (3389) 
and SMB (445) exposed—immediate credential brute force vectors. HTTP (80) likely 
hosting internal applications—probe for authentication bypass, SQLi, LFI. SSH (22) 
indicates Linux systems—enumerate for CVEs, weak keys, password reuse. Domain-joined 
architecture + 30-day patch lag = exploitable Kerberoasting, GPP passwords, known 
CVEs (PrintNightmare, PetitPotam candidates). Attack priority: SMB enumeration → 
credential capture → lateral movement to high-value targets → privilege escalation 
via unpatched systems. Network segmentation absent—complete lateral movement path 
likely available post-initial access.</div>
                <p style="margin-top: var(--spacing-sm); color: var(--color-text-muted); font-size: 0.85rem;">
                    <strong>Why cloud AI cannot handle this:</strong> Internal network architecture, system configurations, and security 
                    posture details are operationally sensitive. Local adversarial analysis maintains OPSEC for red team engagements 
                    and security assessments.
                </p>
            </div>
            
            <div class="scenario">
                <h3 class="scenario-title">[04] ATTACK CHAIN RECONSTRUCTION</h3>
                <p class="scenario-workflow">
                    <strong>Workspace:</strong> Attack Chain (deepseek-r1:32b)<br>
                    <strong>Input:</strong> Timeline of security alerts over 48-hour period<br>
                    <strong>Output:</strong> Multi-stage campaign analysis with MITRE ATT&CK mapping and reasoning transparency
                </p>
                <div class="sample-output">Event timeline maps to complete attack lifecycle: T+00:00 phishing (T1566 Initial 
Access) → T+02:15 PowerShell execution (T1059.001 Execution) → T+04:30 LSASS memory 
access (T1003.001 Credential Dumping) → T+06:00 lateral movement via SMB (T1021.002) 
→ T+18:00 scheduled task persistence (T1053.005) → T+24:00 C2 establishment (T1071.001) 
→ T+48:00 data exfiltration (T1041). Chain-of-thought: Initial access via phishing 
suggests targeted campaign, not opportunistic. 2-hour delay before PowerShell execution 
indicates manual operator involvement. Credential dumping followed immediately by lateral 
movement confirms compromised credentials used. Domain controller scheduled task = 
high-privilege persistence achieved. Exfiltration volume suggests pre-staging—data 
collection occurred between T+18:00 and T+48:00. Assessment: sophisticated APT-style 
operation, not commodity malware. Recommend full incident response, assume domain 
compromise, credential reset across environment.</div>
                <p style="margin-top: var(--spacing-sm); color: var(--color-text-muted); font-size: 0.85rem;">
                    <strong>Why cloud AI cannot handle this:</strong> Incident timelines contain operational details about security controls, 
                    detection capabilities, and response timelines—all sensitive intelligence that must remain within controlled systems.
                </p>
            </div>
        </section>

        <!-- Hardware Specifications Section -->
        <section id="hardware">
            <h2>// HARDWARE SPECIFICATIONS</h2>
            <p>
                Production deployment built on high-end gaming/workstation hardware. No upgrades needed—existing specs 
                were sufficient for the 32B-33B model class. RTX 4080 16GB VRAM is the practical sweet spot for 
                capability/cost tradeoff.
            </p>
            
            <div class="specs-grid">
                <div class="spec-card">
                    <h4>PROCESSING</h4>
                    <div class="spec-item">
                        <span class="spec-label">CPU</span>
                        <span class="spec-value">AMD Ryzen 9 7900X</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Cores/Threads</span>
                        <span class="spec-value">12C / 24T</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Clock Speed</span>
                        <span class="spec-value">5.30GHz (stable)</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Cooling</span>
                        <span class="spec-value">Custom Water Loop</span>
                    </div>
                </div>
                
                <div class="spec-card">
                    <h4>GRAPHICS</h4>
                    <div class="spec-item">
                        <span class="spec-label">GPU</span>
                        <span class="spec-value">Zotac RTX 4080</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">VRAM</span>
                        <span class="spec-value">16GB GDDR6X</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Cooling</span>
                        <span class="spec-value">Air (Stock)</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Max Model Size</span>
                        <span class="spec-value">~32B (full VRAM)</span>
                    </div>
                </div>
                
                <div class="spec-card">
                    <h4>MEMORY</h4>
                    <div class="spec-item">
                        <span class="spec-label">System RAM</span>
                        <span class="spec-value">64GB DDR5-5600</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Cooling</span>
                        <span class="spec-value">Air</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Offload Capacity</span>
                        <span class="spec-value">~42GB available</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">70B Model Support</span>
                        <span class="spec-value">Yes (partial offload)</span>
                    </div>
                </div>
                
                <div class="spec-card">
                    <h4>PLATFORM</h4>
                    <div class="spec-item">
                        <span class="spec-label">Motherboard</span>
                        <span class="spec-value">ASUS ROG X670E Hero</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Operating System</span>
                        <span class="spec-value">Windows 11 Pro</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Build</span>
                        <span class="spec-value">26200.7623</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Power Supply</span>
                        <span class="spec-value">850W+ Certified</span>
                    </div>
                </div>
                
                <div class="spec-card">
                    <h4>SOFTWARE STACK</h4>
                    <div class="spec-item">
                        <span class="spec-label">Model Runtime</span>
                        <span class="spec-value">Ollama v0.14.0</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Interface Layer</span>
                        <span class="spec-value">AnythingLLM v1.8.4</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Deployment Type</span>
                        <span class="spec-value">Native Windows</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">External Dependencies</span>
                        <span class="spec-value">ZERO</span>
                    </div>
                </div>
                
                <div class="spec-card">
                    <h4>STORAGE</h4>
                    <div class="spec-item">
                        <span class="spec-label">Type</span>
                        <span class="spec-value">NVMe M.2 SSD</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Model Library Size</span>
                        <span class="spec-value">~150GB</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Model Count</span>
                        <span class="spec-value">8 Deployed</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Documentation</span>
                        <span class="spec-value">101+ pages</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Performance Metrics Section -->
        <section id="performance">
            <h2>// PERFORMANCE METRICS: CLOUD VS LOCAL COMPARISON</h2>
            <p>
                Direct testing conducted January 24, 2026 comparing Gemini 2.5 Flash, Claude 3.5, ChatGPT 3.5, and 
                local Qwen3:32B across identical prompts. Key finding: local quality matched or exceeded cloud on 
                structured analytical tasks.
            </p>
            
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Cloud AI (Average)</th>
                        <th>Local Qwen3:32B</th>
                        <th>Tradeoff</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td data-label="Metric">Response Time (Simple Query)</td>
                        <td data-label="Cloud AI">2-3 seconds</td>
                        <td data-label="Local Qwen3:32B">1m 45s - 2m 15s</td>
                        <td data-label="Tradeoff">Speed vs Sovereignty</td>
                    </tr>
                    <tr>
                        <td data-label="Metric">Response Time (Complex Analysis)</td>
                        <td data-label="Cloud AI">5-6 seconds</td>
                        <td data-label="Local Qwen3:32B">3m 20s - 4m 45s</td>
                        <td data-label="Tradeoff">Speed vs Sovereignty</td>
                    </tr>
                    <tr>
                        <td data-label="Metric">Inference Speed</td>
                        <td data-label="Cloud AI">N/A (server-side)</td>
                        <td data-label="Local Qwen3:32B">3-5 tokens/second</td>
                        <td data-label="Tradeoff">Hardware-dependent</td>
                    </tr>
                    <tr>
                        <td data-label="Metric">Output Quality (Structured Tasks)</td>
                        <td data-label="Cloud AI">Excellent</td>
                        <td data-label="Local Qwen3:32B">Matched or Exceeded</td>
                        <td data-label="Tradeoff">Equivalent Quality</td>
                    </tr>
                    <tr>
                        <td data-label="Metric">Data Sovereignty</td>
                        <td data-label="Cloud AI">ZERO (corporate retention)</td>
                        <td data-label="Local Qwen3:32B">COMPLETE (no transmission)</td>
                        <td data-label="Tradeoff">Critical for Federal Use</td>
                    </tr>
                    <tr>
                        <td data-label="Metric">Operational Security</td>
                        <td data-label="Cloud AI">External processing risk</td>
                        <td data-label="Local Qwen3:32B">Air-gap capable</td>
                        <td data-label="Tradeoff">Local = Classification-Ready</td>
                    </tr>
                    <tr>
                        <td data-label="Metric">Government Data Requests</td>
                        <td data-label="Cloud AI">Vulnerable (subpoena risk)</td>
                        <td data-label="Local Qwen3:32B">Immune (no remote data)</td>
                        <td data-label="Tradeoff">Local = Protected</td>
                    </tr>
                    <tr>
                        <td data-label="Metric">Cost (After Hardware)</td>
                        <td data-label="Cloud AI">Subscription fees</td>
                        <td data-label="Local Qwen3:32B">Zero recurring cost</td>
                        <td data-label="Tradeoff">Upfront vs Ongoing</td>
                    </tr>
                </tbody>
            </table>
            
            <div style="margin-top: var(--spacing-md); padding: var(--spacing-md); background: var(--color-bg-secondary); border-left: 4px solid var(--color-accent-primary);">
                <h3>Interpretation</h3>
                <p>
                    <strong>Speed:</strong> Cloud models respond 20-50x faster on simple queries. For rapid prototyping and general use, 
                    cloud wins. But for federal cybersecurity analytical work, a 4-minute local response analyzing a threat report 
                    is faster than a human analyst doing the same work manually—and the data never left the machine.
                </p>
                <p>
                    <strong>Quality:</strong> On structured analytical tasks (threat assessments, code review, technical documentation), 
                    local Qwen3:32B matched or exceeded cloud model output quality. Domain-specific fine-tuned models (cybersecurity 
                    specialist, code specialist) outperformed general cloud models on their specific domains.
                </p>
                <p>
                    <strong>Operational Decision:</strong> Use local for any task involving sensitive data, internal systems, or 
                    classified-adjacent workflows. Use cloud only for public research using already-public information. When in doubt, 
                    assume any cloud query could be retained, analyzed, or subpoenaed—run it locally.
                </p>
            </div>
        </section>

        <!-- Documentation Section -->
        <section id="documentation">
            <h2>// PROJECT DOCUMENTATION</h2>
            <p>
                Complete technical documentation, architecture decisions, and lessons learned. All files available in 
                GitHub repository.
            </p>
            
            <div class="specs-grid">
                <div class="spec-card">
                    <h4>PLANNING DOCUMENTS</h4>
                    <div class="spec-item">
                        <span class="spec-label">PRD.md</span>
                        <span class="spec-value">Product Requirements</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Project Ideation</span>
                        <span class="spec-value">3 Initial Concepts</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Selected Approach</span>
                        <span class="spec-value">Infrastructure Demo</span>
                    </div>
                </div>
                
                <div class="spec-card">
                    <h4>DEVELOPMENT LOGS</h4>
                    <div class="spec-item">
                        <span class="spec-label">PROTOTYPE_TESTING.md</span>
                        <span class="spec-value">AI Tool Comparison</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">ITERATION_LOG.md</span>
                        <span class="spec-value">10 Iterations Documented</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Development Time</span>
                        <span class="spec-value">~6 hours over 3 days</span>
                    </div>
                </div>
                
                <div class="spec-card">
                    <h4>TECHNICAL DOCUMENTATION</h4>
                    <div class="spec-item">
                        <span class="spec-label">Full Infrastructure Docs</span>
                        <span class="spec-value">101+ pages</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Windows Guide</span>
                        <span class="spec-value">21 pages</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Linux Guide</span>
                        <span class="spec-value">80 pages</span>
                    </div>
                </div>
                
                <div class="spec-card">
                    <h4>GITHUB WORKFLOW</h4>
                    <div class="spec-item">
                        <span class="spec-label">Issues Tracked</span>
                        <span class="spec-value">PRD, Implementation</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Pull Requests</span>
                        <span class="spec-value">All features reviewed</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Deployment</span>
                        <span class="spec-value">GitHub Pages Active</span>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div>
                    <p>&copy; 2026 William Edward Beckham III | CSC-113-0901 Final Project</p>
                    <p style="font-size: 0.85rem; color: var(--color-text-muted);">
                        U.S. Army Veteran | Systems Security & Analysis | Fayetteville Technical Community College
                    </p>
                </div>
                <ul class="footer-links">
                    <li><a href="https://github.com/BECKHAMW3233/CSC-113" target="_blank" rel="noopener">[GitHub Repo]</a></li>
                    <li><a href="https://linkedin.com/in/WilliamBeckham" target="_blank" rel="noopener">[LinkedIn]</a></li>
                    <li><a href="mailto:williamedwardbeckhamiii@gmail.com">[Contact]</a></li>
                </ul>
            </div>
        </div>
    </footer>

    <!-- JavaScript -->
    <script>
        // Model Library Data
        const models = [
            {
                name: 'qwen3:32b',
                size: '20GB',
                role: 'Primary analysis and documentation — daily workhorse',
                parameters: '32B',
                quantization: 'Q4',
                speed: '3-5 tokens/second',
                useCase: 'General analysis, documentation, report drafting, summarization',
                rationale: 'Best balance of output quality and response speed for interactive use. Default model for non-specialized tasks.'
            },
            {
                name: 'llama3.1:70b-instruct-q4_K_M',
                size: '42GB',
                role: 'Advanced reasoning and complex analysis',
                parameters: '70B',
                quantization: 'Q4_K_M',
                speed: 'Slower (partial VRAM offload)',
                useCase: 'Complex multi-step reasoning, lengthy document synthesis, high-stakes analysis',
                rationale: 'Largest model in library. Reserved for tasks where depth matters more than latency. Produces qualitatively better output on sustained reasoning chains.'
            },
            {
                name: 'deepseek-r1:32b',
                size: '19GB',
                role: 'Specialized reasoning and attack chain analysis',
                parameters: '32B',
                quantization: 'Q4',
                speed: '3-5 tokens/second',
                useCase: 'Attack chain reconstruction, threat impact assessment, traceable multi-step logic',
                rationale: 'Chain-of-thought reasoning model. Shows its work step-by-step. Critical for security analysis where reasoning process must be auditable.'
            },
            {
                name: 'deepseek-coder:33b-instruct',
                size: '18GB',
                role: 'Code analysis and vulnerability assessment',
                parameters: '33B',
                quantization: 'Q4',
                speed: '3-5 tokens/second',
                useCase: 'Code review, vulnerability identification, malware analysis, secure coding guidance',
                rationale: 'Code-specialized training produces significantly better vulnerability assessments than general models. Handles multi-language analysis and provides detailed CVE/CWE references.'
            },
            {
                name: 'qwen3-coder:30b',
                size: '18GB',
                role: 'Code analysis and secure development',
                parameters: '30B',
                quantization: 'Q4',
                speed: '3-5 tokens/second',
                useCase: 'Code generation and review, Python-specific work, cross-validation with deepseek-coder',
                rationale: 'Second code model enables cross-validation. Vulnerabilities missed by one model may be caught by another. Strong Python performance.'
            },
            {
                name: 'phi4-reasoning:14b',
                size: '11GB',
                role: 'Fast reasoning and rapid triage',
                parameters: '14B',
                quantization: 'Q4',
                speed: 'Faster than 32B class',
                useCase: 'Quick threat triage, rapid screening, fast reasoned responses, sanity checks',
                rationale: 'Compact reasoning model for speed-critical tasks. Fits entirely in VRAM for maximum performance. Middle ground between fast shallow models and slow deep models.'
            },
            {
                name: 'ALIENTELLIGENCE/cybersecuritythreatanalysisv2',
                size: '4.7GB',
                role: 'Threat intelligence and security analysis',
                parameters: '~7B (estimated)',
                quantization: 'Unknown',
                speed: 'Fast (small model)',
                useCase: 'CISA alert triage, CVE assessment, threat pattern analysis, MITRE ATT&CK mapping',
                rationale: 'Purpose-trained cybersecurity model. Domain-specific fine-tuning produces operationally structured output that general models cannot replicate without extensive prompting.'
            },
            {
                name: 'jimscard/blackhat-hacker:v2',
                size: '9.2GB',
                role: 'Red team and adversarial perspective',
                parameters: '~13B (estimated)',
                quantization: 'Unknown',
                speed: 'Fast (small model)',
                useCase: 'Red team exercises, attack surface analysis, penetration testing planning',
                rationale: 'Fine-tuned for adversarial perspective. Approaches systems from attacker viewpoint consistently. Both offensive and defensive perspectives necessary for complete security analysis.'
            }
        ];

        // Generate Model Cards
        const modelGrid = document.getElementById('modelGrid');
        models.forEach((model, index) => {
            const card = document.createElement('div');
            card.className = 'model-card';
            card.setAttribute('role', 'button');
            card.setAttribute('tabindex', '0');
            card.setAttribute('aria-expanded', 'false');
            
            card.innerHTML = `
                <div class="model-header">
                    <h3 class="model-name">${model.name}</h3>
                    <div class="model-size">${model.size}</div>
                </div>
                <p class="model-role">${model.role}</p>
                <div class="model-details">
                    <div class="model-specs">
                        <div class="spec-line">
                            <span class="spec-label">Parameters:</span>
                            <span class="spec-value">${model.parameters}</span>
                        </div>
                        <div class="spec-line">
                            <span class="spec-label">Quantization:</span>
                            <span class="spec-value">${model.quantization}</span>
                        </div>
                        <div class="spec-line">
                            <span class="spec-label">Speed:</span>
                            <span class="spec-value">${model.speed}</span>
                        </div>
                    </div>
                    <p><strong>Use Case:</strong> ${model.useCase}</p>
                    <p><strong>Selection Rationale:</strong> ${model.rationale}</p>
                </div>
            `;
            
            // Add click event
            card.addEventListener('click', () => toggleCard(card));
            // Add keyboard event
            card.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    toggleCard(card);
                }
            });
            
            modelGrid.appendChild(card);
        });

        // Toggle Card Expansion
        function toggleCard(card) {
            const isExpanded = card.classList.contains('expanded');
            card.classList.toggle('expanded');
            card.setAttribute('aria-expanded', !isExpanded);
        }

        // Smooth Scroll Navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Animate bars on scroll (simple implementation)
        const observerOptions = {
            threshold: 0.3,
            rootMargin: '0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const bars = entry.target.querySelectorAll('.bar-fill');
                    bars.forEach(bar => {
                        const width = bar.style.width;
                        bar.style.width = '0';
                        setTimeout(() => {
                            bar.style.width = width;
                        }, 100);
                    });
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.architecture-card').forEach(card => {
            observer.observe(card);
        });
    </script>
</body>
</html>
