# Empirical Memory & Recursive Learning

To achieve super-precision, `auto-developer` treats every error as a scientific data point for systemic evolution.

## 1. Post-Mortem Analysis (FMT-Driven)
After completing a task or fixing a bug, perform a self-audit using the **Failure Mode Taxonomy (FMT)**:
- **Taxonomy**: `SPEC_ERR | ALIGN_ERR | VERIF_ERR | ENV_ERR`.
- **Root Cause**: Identify exactly why the error occurred (e.g., "Misinterpreted a prompt instruction" -> `ALIGN_ERR`).
- **Optimal Solution**: Determine if there's a more efficient or safer way to achieve the result.

## 2. The Golden Rule Protocol
Formulate a "Golden Rule" to prevent the specific failure mode from recurring.
- **Format**: `[TAXONOMY] | [Category] | [Problem] -> [Golden Rule]`.
- **Storage**: Save to `/data/data/com.termux/files/home/.gemini/tmp/home/memory/auto-developer/KNOWLEDGE_BASE.md`.

## 3. Systematic Knowledge Recall
Before starting any new task, the agent MUST search the `KNOWLEDGE_BASE.md` for rules relevant to the current task's tools and domain.
- **Example**: If using `replace`, check for `[VERIF_ERR]` rules related to regex or context selection.

## 4. Stability Score Tracking
- **Failure Density**: Number of FMT logs per 100 tasks.
- **Recovery Efficiency**: Success rate of autonomous fixes after an FMT log.
- **Goal**: Continuously reduce `VERIF_ERR` density through improved testing protocols.
