# Scientific Research & Hypothesis Validation

To achieve elite-level intelligence, `auto-developer` replaces "searching" with "Scientific Investigation."

## 1. Hypothesis-Based Problem Solving
Instead of jumping to a solution, follow this loop:
- **Hypothesis**: "I believe library X is the best because of Y."
- **Falsification**: Actively look for 3 reasons why library X might FAIL or be sub-optimal (e.g., bundle size, memory leaks, community abandonment).
- **Benchmarking**: Compare library X against 2 alternatives using a scoring matrix (Performance, Security, DX).

## 2. Evidence-Based Decision Making
Every choice in `DECISION_LOG.md` must be backed by empirical evidence (e.g., "I ran a quick test script and library X was 20% faster than library Z").

## 4. Large-Scale Context Mapping (MANDATORY)
For projects with > 5 files, the agent MUST run the context compressor to get a structural map without wasting tokens:
- **Command**: `python3 /data/data/com.termux/files/home/.gemini/skills/auto-developer/scripts/context_compressor.py <directory>`
- **Usage**: Use this map to understand system-wide dependencies before proposing any structural changes.
