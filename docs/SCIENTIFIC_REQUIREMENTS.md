# Requirements: Scientific Auto-Developer Evolution

## Objective
Transform the `auto-developer` skill from a persona-based helper into a rigorous, evidence-based autonomous software house using scientific methodologies.

## Core Principles
1. **Empiricism**: Every decision must be backed by data, benchmarks, or verified facts.
2. **Falsifiability**: Plans must include "failure conditions" and active attempts to prove themselves wrong.
3. **Reproducibility**: Tasks must be atomic and verifiable with surgical tests.
4. **Quantifiability**: Use the Goal-Question-Metric (GQM) framework to measure progress and quality.

## Functional Requirements

### 1. Goal-Question-Metric (GQM) Integration
- Each SDLC phase must have defined **Goals**, **Questions** to assess status, and **Metrics** for completion.
- Replace "Phase Complete" vibes with "Metric-Verified Exit Criteria".

### 2. Evidence-Based Decision Protocol (EBDP)
- Mandatory benchmarking for library/architecture selection.
- Scoring matrix: `(Performance * 0.4) + (Security * 0.3) + (Maintainability * 0.3)`.

### 3. Functional Sub-Agent Specialization
- Move away from "Simulated Personas".
- Define functional roles with specific tool access and validation logic:
    - **Strategist**: Handles high-level GQM and Task Queuing.
    - **Implementer**: Focuses on atomic code generation and linting.
    - **Verifier**: Runs tests, performs failure mode analysis, and benchmarks.

### 4. Failure Mode Taxonomy (FMT)
- Categorize all errors according to the taxonomy:
    - `SPEC_ERR`: Ambiguous or incorrect requirements.
    - `ALIGN_ERR`: Coordination/Context mismatch.
    - `VERIF_ERR`: Incomplete or failed verification.
    - `ENV_ERR`: Environment/Tooling issues.

### 5. Runtime Verification Loop
- Automated execution of generated code in a sandbox.
- Capture and analyze tracebacks as first-class citizens in the reasoning loop.

## Success Metrics (Meta-Task)
- **M1**: 100% of `references/*.md` updated with scientific protocols.
- **M2**: `state_manager.py` updated to support GQM tracking.
- **M3**: `PROJECT_STATE.md` template includes Failure Mode Analysis.
