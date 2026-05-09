# Recursive Learning & Knowledge Synthesis

To achieve super-precision, `auto-developer` must treat every error and success as a data point for evolution.

## 1. Mandatory Post-Mortem Analysis
After completing any implementation task or fixing a bug, the agent MUST perform a self-audit:
- **What went wrong?** (Analyze the root cause of any errors encountered).
- **Was the solution optimal?** (Could it be done with fewer lines, better performance, or cleaner types?).
- **What is the "Golden Rule"?** (Formulate a one-sentence rule to prevent this specific mistake in the future).

## 2. Knowledge Base Update
Save the "Golden Rule" to `/data/data/com.termux/files/home/.gemini/tmp/home/memory/auto-developer/KNOWLEDGE_BASE.md`.
- **Structure**: `[Category] | [Problem] -> [Golden Rule]`.
- **Example**: `[TypeScript] | Null pointer in API response -> Always use optional chaining and provide a default fallback object.`

## 3. Pre-Task Knowledge Recall
Before starting any new task, the agent MUST search the `KNOWLEDGE_BASE.md` for relevant rules to ensure past mistakes are NEVER repeated. This is the foundation of "Super Precision."
