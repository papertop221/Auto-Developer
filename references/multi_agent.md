# Functional Sub-Agent Orchestration

To maximize precision, `auto-developer` utilizes a **Functional Decomposition** model. Instead of roleplay, we define execution modes with specific constraints and verification duties.

## 1. Functional Roles (Execution Modes)

### MODE_STRATEGIST (The Conductor)
- **Responsibility**: GQM management, Task Serialization, and High-Level Logic.
- **Tools**: `state_manager.py`, `grep_search`, `glob`.
- **Exit Criteria**: All atomic tasks for the phase are queued and match the ARCHITECTURE.md.

### MODE_IMPLEMENTER (The Surgeon)
- **Responsibility**: Atomic code generation, linting, and structural integrity.
- **Tools**: `replace`, `write_file`, `run_shell_command` (linters).
- **Exit Criteria**: `LINT_ERRORS=0` and code passes the "Surgical Test" plan.

### MODE_VERIFIER (The Inquisitor)
- **Responsibility**: Adversarial testing, Benchmarking, and Failure Mode Analysis (FMT).
- **Tools**: `run_shell_command` (test runners), `web_fetch`, `read_file`.
- **Exit Criteria**: `TEST_PASS_RATE=100%` and any failure is logged in `error_log` with taxonomy.

## 2. Adversarial Verification Protocol (AVP)
Every major architectural change or implementation must survive a verification loop:
- **Phase A (Proposal)**: `MODE_STRATEGIST` proposes the change based on requirements.
- **Phase B (Challenge)**: `MODE_VERIFIER` must attempt to break the proposal (edge cases, security, performance).
- **Phase C (Refactor)**: `MODE_IMPLEMENTER` applies the change, incorporating feedback from the challenge.
- **Outcome**: A verified state change that has been challenged and hardened.

## 3. Data Integrity & Sync
- `MODE_STRATEGIST` MUST update `PROJECT_STATE.md` and `.auto-dev-state.json` after every role transition.
- `MODE_VERIFIER` MUST audit the state file for consistency before Phase completion.

