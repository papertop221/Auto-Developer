# Scientific Engineering Standards

To ensure maximum reliability and maintainability, all code produced by `auto-developer` MUST adhere to these engineering standards.

## 1. Type Safety & Determinism
- **Strict Typing**: No `any`, `unknown` (without narrowing), or implicit types. Use interfaces and exhaustive types.
- **Deterministic State**: Favor functional programming patterns and immutable state where applicable.
- **Error Handling**: Use explicit error types (e.g., Result/Either patterns). Never swallow errors.

## 2. Structural Integrity
- **Modular Design**: Every component must have a single responsibility.
- **Dependency Injection**: Use DI to make components testable in isolation.
- **Clean Abstractions**: Prefer composition over inheritance.

## 3. International Technical Compliance
- **Internationalization (i18n)**: Never hardcode user-facing strings. Use standardized localization libraries.
- **Accessibility (a11y)**: WCAG 2.1 compliance. Use semantic HTML and ARIA attributes for screen reader support.
- **Privacy (GDPR/CCPA)**: Implement secure data handling and privacy-by-design principles.

## 4. Verification Standards
- **LINT_ERRORS = 0**: Code must pass all static analysis without suppressions.
- **TEST_COVERAGE >= 80%**: Critical logic must be fully covered by unit tests.
- **SECURITY_AUDIT = PASS**: No high-severity vulnerabilities.

## 5. Performance Budgets
- **Binary/Bundle Size**: Monitor and log regressions.
- **Execution Latency**: Meet defined SLOs for critical execution paths.
