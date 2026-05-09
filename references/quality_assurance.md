# Scientific Validation & Runtime Verification

Precision is maintained through continuous execution and systematic failure analysis.

## 1. Runtime Verification Loop
Every code change must survive the **Execution Loop**:
- **Step 1: Linting**: Run project-specific linters. `LINT_ERRORS` must be 0.
- **Step 2: Type Checking**: Run `tsc`, `mypy`, or equivalent. No implicit `any` or suppressed warnings.
- **Step 3: Surgical Testing**: Execute a focused test case targeting the specific change.
- **Step 4: Regression Testing**: Run the full test suite.

## 2. Failure Mode Taxonomy (FMT)
When a task fails, categorize the error using the `state_manager.py log-error` command:
- `SPEC_ERR`: Requirements were ambiguous or incorrect.
- `ALIGN_ERR`: Coordination or context mismatch between agent steps.
- `VERIF_ERR`: Verification logic (tests/linters) was incomplete or failed to catch a bug.
- `ENV_ERR`: Tooling, environment, or dependency failure.

## 3. Root Cause Analysis (RCA)
For any `VERIF_ERR`, the agent MUST perform an RCA:
- Why did the test fail to catch the bug?
- What property was missing from the test suite?
- Update the test suite before re-attempting the fix.

## 4. Stability Metrics
- **Pass@1 Rate**: Percentage of tasks completed successfully on the first attempt.
- **Containment Rate**: Percentage of errors caught by the Runtime Verification Loop before user interaction.
