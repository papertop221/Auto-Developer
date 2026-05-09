# Autonomous Self-Correction Directives

`auto-developer` is designed to be resilient. When errors occur, follow these protocols to recover autonomously.

## Error Detection
Monitor all shell command outputs for:
- Non-zero exit codes.
- "Error", "Exception", "Failed", "Warning" (if relevant) in stdout/stderr.
- Linting or Type-check failures.

## Recovery Protocol
Do not immediately ask the user for help. Follow these steps first:

1. **Analyze**: Read the full error log. Identify the file and line number causing the issue.
2. **Hypothesize**: Determine the likely cause (e.g., missing dependency, syntax error, type mismatch, logic error).
3. **Isolate**: If it's a logic error, create a minimal reproduction test case.
4. **Fix**: Apply the correction using surgical tools (e.g., `replace`).
5. **Verify**: Re-run the command that failed.
6. **Iterate**: Repeat up to 3 times.

## When to Involve the User
Only use `ask_user` if:
- You have failed to fix the same error 3 times.
- The error is due to missing external credentials/API keys that you cannot generate.
- The error requires a fundamental change to the project's scope or requirements.

## Precision Standards
- Never use "hacks" (e.g., `any` in TypeScript, suppressing warnings).
- Ensure all fixes follow the patterns established in `tech_stack.md`.
