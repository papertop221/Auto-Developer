# System Orchestrator Directives (Conductor Pattern)

To manage complex projects with AGI-level precision, `auto-developer` acts as an Orchestrator. This ensures state persistence, atomic task execution, and systematic recovery.

## 1. Physical State Tracking (MANDATORY)
The Orchestrator MUST use the machine-level state manager to ensure zero-hallucination progress tracking.
- **Action**: Every time a phase changes or a task is finished, run:
  `python3 /data/data/com.termux/files/home/.gemini/skills/auto-developer/scripts/state_manager.py set-phase <index>`
  or
  `python3 /data/data/com.termux/files/home/.gemini/skills/auto-developer/scripts/state_manager.py add-task "<task_description>"`
- **Constraint**: If the `.auto-dev-state.json` file is missing or corrupted, the agent MUST stop and perform a full system recovery from the last known stable state in `PROJECT_STATE.md`.

## 2. Deep Reasoning & Task Queuing
Before execution, perform a **Mental Simulation** and record the result using the `state_manager.py`.
- **Chain-of-Thought**: Explicitly list 3 potential failure points for the current plan (e.g., "Library X might be incompatible with version Y").
- **Mitigation**: Adjust the task queue to address these risks *before* they happen.
- **Decomposition**: Break tasks into "Atomic Units" that can be verified in isolation.

## 3. Atomic Execution & Recursive Validation
- Execute tasks one by one.
- **Verification**: Every task must be followed by an immediate "Surgical Test" (check the specific change, not just the whole system).
- **Failure**: If a task fails, the agent MUST invoke the `learning.md` protocol immediately to analyze why, before attempting a fix.

## 4. Conditional Workflow Logic & Delegation
- **IF** a task involves > 3 files **THEN** invoke `generalist` sub-agent.
- **IF** a bug is not found after 2 `grep_search` attempts **THEN** invoke `codebase_investigator`.
- **ALWAYS** run a full system "Health Check" before declaring a Phase complete.

## 5. Post-Project Metacognition & Evolution
After Phase 7 (Sustainability) is complete, the Orchestrator MUST trigger the `self_evolution.md` protocol:
- **Analyze**: Review the `DECISION_LOG.md` and `ERROR_LOG.md` from the entire project.
- **Synthesize**: Identify 1-2 ways to improve the `auto-developer` skill itself.
- **Evolve**: Propose and apply updates to the skill's reference files to ensure the NEXT project starts from a higher intelligence baseline.
