# Universal SDLC Workflow (Scientific GQM)

`auto-developer` follows a Goal-Question-Metric (GQM) driven lifecycle to ensure technical rigor and empirical verification.

## Phase 0: Initialization & Recall
*   **Goal**: Establish system state and load empirical memory.
*   **Questions**: Is the `PROJECT_STATE.md` initialized? Have past `KNOWLEDGE_BASE.md` rules been applied?
*   **Metrics**: `STATE_SYNC=1`, `RULES_LOADED >= 1`.

## Phase 1: Research & Evidence Gathering
*   **Goal**: Validate technical feasibility and library selection.
*   **Questions**: Are there at least 2 alternatives for each major library? Is the benchmark score > 0.7?
*   **Metrics**: `ALTS_IDENTIFIED >= 2`, `BENCHMARK_SCORE`.
*   **Reference**: [references/research.md](references/research.md).

## Phase 2: Requirements & Formalization
*   **Goal**: Define unambiguous, falsifiable requirements.
*   **Questions**: Is every requirement measurable? Have failure conditions been identified?
*   **Metrics**: `MEASURABLE_REQS_COUNT`, `FAILURE_MODES_DEFINED`.

## Phase 3: System Design & Task Serialization
*   **Goal**: Create a modular, verifiable architecture.
*   **Questions**: Is the cyclomatic complexity minimized? Are tasks atomic (< 3 files)?
*   **Metrics**: `ATOMIC_TASKS_COUNT`, `SECURITY_AUDIT_PASS=1`.

## Phase 4: Atomic Implementation (Surgical)
*   **Goal**: Implement features with zero regressions.
*   **Questions**: Does the code pass linting? Does it match the architectural pattern?
*   **Metrics**: `LINT_ERRORS=0`, `TYPE_CHECK_PASS=1`.

## Phase 5: Validation & Runtime Verification
*   **Goal**: Prove correctness through execution.
*   **Questions**: Do all unit tests pass? Is the coverage sufficient?
*   **Metrics**: `TEST_PASS_RATE=100%`, `COVERAGE_PCT`.
*   **Reference**: [references/quality_assurance.md](references/quality_assurance.md).

## Phase 6: Infrastructure & Observability
*   **Goal**: Ensure reproducible deployment and monitoring.
*   **Questions**: Is the Dockerfile optimized? Are health checks implemented?
*   **Metrics**: `BUILD_SUCCESS=1`, `HEALTH_CHECK_PASS=1`.

## Phase 7: Sustainability & Error Modeling
*   **Goal**: Long-term reliability and automated recovery.
*   **Questions**: Are backups verified? Is the Failure Mode Analysis complete?
*   **Metrics**: `BACKUP_VERIFIED=1`, `FMT_LOG_COUNT`.

## Phase 8: Metacognitive Evolution
*   **Goal**: Improve the agent's internal logic based on project data.
*   **Questions**: Which failure mode was most common? How can the skill be updated?
*   **Metrics**: `SKILL_UPDATES_PROPOSED`, `KNOWLEDGE_BASE_ENTRIES`.


