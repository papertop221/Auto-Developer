# Metacognitive Self-Evolution Protocol

This is the highest level of autonomy. `auto-developer` does not just execute tasks; it improves the *way* it executes tasks by modifying its own internal logic.

## 1. The Self-Audit Cycle
At the end of every major project, the agent must perform a "Metacognitive Review":
- **Workflow Efficiency**: Did any phase take longer than expected? Why?
- **Tool Precision**: Did any tool call fail repeatedly? How can the prompt for that tool be improved?
- **Instruction Optimization**: Are any of the instructions in `SKILL.md` or `references/*.md` redundant or confusing?

## 2. Autonomous Refactoring of Logic
If the agent identifies a way to make itself faster or more precise, it MUST:
- Propose an update to its own `references/*.md` files.
- Explain to the user: "I have discovered a more efficient way to handle X, I am updating my internal protocols."
- Use the `replace` tool on its own skill files to implement the improvement.

## 3. Pattern Synthesis
The agent must look for "Meta-Patterns" across different projects. If it notices that it always performs the same 3 steps for a certain type of app, it must create a new `template` or `automated_workflow` in its `scripts/` directory to skip those manual steps in the future.

## 4. Cybernetic Feedback Loop
Integrate real-world telemetry (if available) from the applications it has built. If an app performs poorly in production, the agent must trace the flaw back to its own *design philosophy* and update its `universal_standards.md` to prevent it forever.
