# Evidence-Based Research & Decision Protocol (EBDP)

To achieve high-precision engineering, `auto-developer` replaces "searching" with empirical investigation and benchmarking.

## 1. Decision Scoring Matrix
Every major technical choice (libraries, frameworks, patterns) MUST be evaluated using a weighted scoring matrix:
- **Performance (40%)**: Latency, memory footprint, bundle size.
- **Security (30%)**: CVE history, active maintenance, supply chain trust.
- **Maintainability (30%)**: Documentation quality, community size, type safety.

## 2. Hypothesis & Falsification
Instead of looking for confirmation, follow the **Falsification Protocol**:
1. **Hypothesis**: "Library X is optimal for task Y."
2. **Stress Test**: Find 3 specific scenarios where Library X fails (e.g., "breaks on large datasets", "lacks TS support for X").
3. **Alternative Comparison**: Benchmark Library X against at least one alternative using the Scoring Matrix.

## 3. Empirical Benchmarking
- Whenever possible, run a micro-benchmark script to verify performance claims.
- Log the results in `DECISION_LOG.md` using the `state_manager.py log-decision` command.

## 4. Large-Scale Context Mapping
- Use `context_compressor.py` to map the codebase structure before proposing any structural changes.
- Ensure the map includes dependency directions to avoid circular imports.
