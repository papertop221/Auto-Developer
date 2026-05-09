# Chaotic Quality Assurance

We don't just "test" for success; we "hunt" for failure.

## 1. Chaos Testing (Stress Test)
After implementation, the agent must perform "Chaos Tasks":
- **Fuzzing**: Provide extremely long, empty, or weirdly formatted inputs to every function.
- **Boundary Hunt**: Test the exact limits (e.g., maximum integer values, empty arrays).
- **Simulated Failure**: Ask: "What happens to the UI if the API returns a 500 error?" and implement the fix before it happens.

## 2. Automated Regression & Security
- Every fix must be accompanied by a test case that "locks" the fix in place.
- **Secret Scanning**: Mandatory check for hardcoded keys.
- **Dependency Audit**: Continuous scan for vulnerable packages.

## 3. Documentation Standard
Every project MUST include:
- `README.md`: Technical setup and developer notes.
- `USER_GUIDE.md`: Simple, non-technical instructions for the end-user on how to use the app.
- `MAINTENANCE.md`: Instructions on how to update dependencies and back up data.

## 4. Final Delivery Checklist
1. Full build succeeds.
2. All tests pass (100% success rate).
3. Documentation exists and is clear.
4. Security audit passed.
