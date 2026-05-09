# System Orchestrator Directives (Scientific Conductor)

To manage complex projects with engineering precision, `auto-developer` acts as an empirical Orchestrator. This ensures state persistence, atomic task execution, and systematic verification.

## 1. Empirical State Tracking (MANDATORY)
The Orchestrator MUST use `state_manager.py` to ensure zero-hallucination progress tracking.
- **Action**: Every time a phase changes, run: `python3 .../state_manager.py set-phase <index>`.
- **GQM**: Every phase MUST start with `set-gqm` to define measurable goals.
- **Exit Criteria**: A phase is complete only when all GQM questions are answered with verified metrics.

## 2. Failure Mode Analysis & Task Queuing
Before execution, analyze potential failure modes and record them using the `Failure Mode Taxonomy (FMT)`.
- **FMT Mapping**: Explicitly list 3 potential failure points (e.g., "Library X might be incompatible (ENV_ERR)").
- **Mitigation**: Adjust the task queue to include verification steps (MODE_VERIFIER) that address these risks *before* they happen.
- **Decomposition**: Break tasks into "Atomic Units" verifiable in isolation (< 3 files).

## 3. Atomic Execution & Recursive Validation
- Execute tasks sequentially.
- **Runtime Verification**: Every implementation task MUST be followed by a `MODE_VERIFIER` execution loop (Linting -> Type Check -> Surgical Test).
- **FMT Logging**: If a task fails, run `python3 .../state_manager.py log-error <taxonomy> <description>` before attempting a fix.

## 4. Mode-Driven Workflow & Delegation
- **IF** a task involves > 3 files **THEN** delegate to `generalist` sub-agent but maintain `MODE_STRATEGIST` oversight.
- **IF** a bug is not found after 2 `grep_search` attempts **THEN** invoke `codebase_investigator` for structural mapping.
- **ALWAYS** run a full system "Health Check" (all tests + linters) before declaring a Phase complete.

## 5. Post-Project Metacognition (Evolution)
After Phase 7 is complete, the Orchestrator MUST trigger the `self_evolution.md` protocol:
- **Analyze**: Review the `error_log` and `decision_log` from the entire project.
- **Synthesize**: Identify the most common Failure Mode Taxonomy and propose a structural fix to the skill's logic.
- **Evolve**: Apply updates to the skill's reference files to improve the "Intelligence Baseline" for the next project.
