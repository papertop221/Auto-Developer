# Quality Assurance & Security Gates

To ensure every project is "production-ready," `auto-developer` must pass these quality gates before final delivery.

## 1. Security Audit
- **Secret Scanning**: Ensure NO secrets (API keys, passwords, `.env` content) are hardcoded in the source code.
- **Dependency Check**: Run `npm audit` or `pip audit` to identify vulnerable packages.
- **Input Validation**: Verify that all user inputs are sanitized to prevent SQL Injection and XSS.

## 2. Performance & Clean Code
- **Linter Compliance**: Zero ESLint or Ruff warnings.
- **Dead Code Removal**: Remove unused imports, variables, and console logs.
- **Optimization**: For web, ensure images are optimized and large dependencies are lazy-loaded where possible.

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
