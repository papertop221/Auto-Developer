# Visual Feedback & UI Design Review

To ensure "pixel-perfect" delivery, `auto-developer` uses visual cues and design audits.

## 1. Visual Scaffolding
- Use established Design Systems (e.g., Tailwind, Shadcn).
- Enforce "Visual Hierarchy": Proper spacing (8pt grid), typography scales, and color theory.

## 2. Vision Audit (Simulation/Real)
- **If Image Input is supported**: Take a screenshot of the local build (via terminal-based tools or user provided) and analyze for:
    - Alignment issues.
    - Color contrast.
    - Component responsiveness.
- **If Text-only**: Perform a "Mental Model Audit" of the JSX/HTML structure to ensure accessibility and responsive classes (e.g., `sm:`, `md:`, `lg:` in Tailwind).

## 3. UI/UX Refinement
- Always implement "Interactive Feedback": Loading states, Hover effects, and Toast notifications for every action.
