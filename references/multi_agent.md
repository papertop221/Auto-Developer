# Multi-Agent Orchestration Protocol

To achieve high precision, `auto-developer` simulates a specialized team during the SDLC. Each phase must undergo a "Peer Review" from a different simulated persona.

## 1. Simulated Personas
- **The Architect**: Focuses on scalability, design patterns, and system integrity.
- **The UI/UX Specialist**: Focuses on accessibility, aesthetics, and user flow.
- **The Security Auditor**: Focuses on vulnerabilities, data privacy, and secret protection.
- **The QA Engineer**: Focuses on edge cases, unit tests, and error handling.

## 2. Review Workflow
- **Requirements Review**: The Architect and UX Specialist must "approve" `REQUIREMENTS.md`.
- **Code Review**: After every implementation step, the Security Auditor and QA Engineer must "scan" the code for issues.
- **Conflict Resolution**: If two personas disagree, the **Manager** (Main Agent) makes the final decision based on the user's core goals.

## 3. Review Documentation
- Record review feedback in `CODE_REVIEWS.md`.
- Mark tasks as "Verified" only after simulated approval.
