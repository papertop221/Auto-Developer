# Architecture: Scientific Auto-Developer Evolution

## 1. Data Schema (state_manager.py)
The `.auto-dev-state.json` will be expanded to include:
```json
{
  "current_phase": 0,
  "gqm": {
    "goal": "...",
    "questions": ["...", "..."],
    "metrics": {
      "metric_id": "current_value"
    }
  },
  "error_log": [
    {
      "timestamp": "...",
      "taxonomy": "SPEC_ERR | ALIGN_ERR | VERIF_ERR | ENV_ERR",
      "description": "...",
      "recovery_attempt": 1
    }
  ],
  "decision_log": [
    {
      "choice": "...",
      "alternatives": ["...", "..."],
      "benchmark_score": { "choice": 0.8, "alt1": 0.6 }
    }
  ]
}
```

## 2. Functional Roles (multi_agent.md)
Instead of simulated personas, we define functional modes:
- **MODE_STRATEGIST**: Prompted to maximize Goal alignment.
- **MODE_IMPLEMENTER**: Prompted for strict typing, linting, and atomic changes.
- **MODE_VERIFIER**: Prompted for adversarial testing and FMT analysis.

## 3. Evidence-Based Decision Protocol (EBDP)
Workflow for architectural choices:
1. **Identify Options**: List at least 2 alternatives.
2. **Define Criteria**: Use `Performance`, `Security`, `Maintenance`.
3. **Weighting**: Applied per project context.
4. **Empirical Check**: Run `web_fetch` or `google_web_search` for latest benchmarks or run local micro-benchmarks.

## 4. Failure Mode Taxonomy (FMT) Integration
Every failure must be tagged. This allows the `learning.md` protocol to identify systemic weaknesses in the agent's logic (e.g., if 80% of errors are `VERIF_ERR`, the agent needs to prioritize testing earlier).

## 5. Refactoring Sequence
1. **Phase 1**: Update `scripts/state_manager.py`.
2. **Phase 2**: Refactor `references/sdlc_phases.md` and `references/multi_agent.md`.
3. **Phase 3**: Refactor `references/research.md` and `references/quality_assurance.md`.
4. **Phase 4**: Update `references/learning.md` to use FMT data.
