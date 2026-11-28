# Claims and evidence

| Claim | Evidence |
| --- | --- |
| Arbitrary measurable mixtures and L¹ closure preserve the extended supremum | [Theorem 1](paper/manuscript.pdf) |
| The geometric mixture controls the negative log-loss contribution | [Section 3](paper/manuscript.pdf) and [exact replay](verification/results/replay.txt) |
| Finite convexity suffices with a finite-gain anchor and P ≪ Q | [Proposition 2](paper/manuscript.pdf) |
| Missing anchors and common domination are distinct failure modes | [Section 5](paper/manuscript.pdf) |
| The original question has this exact scope | [Primary sources and comparison](audits/public_safe_reports/LITERATURE.md) |

## Partial Lean verification

For finite lists of rational pointwise density values, a nonnegative initial segment of length N followed by terms and a terminal remainder of height at least c gives a geometric mixture of height at least c/2ᴺ. [Scope, source and replay](formalization/README.md)
