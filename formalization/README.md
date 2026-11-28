# Geometric mixture lower envelope

For finite lists of rational pointwise density values, a nonnegative initial segment of length N followed by terms and a terminal remainder of height at least c gives a geometric mixture of height at least c/2ᴺ.

The terminal remainder takes the unallocated geometric weight. Choosing approximants, taking the countable mixture, integrating the log loss and comparing the extended suprema remain in the manuscript.

[Lean source](Q760Envelope.lean) · [Mathematical source](../paper/manuscript.tex) · [Expected axiom report](expected-axioms.txt)

Replay from this directory with Lean 4.30.0 and its standard library.

```sh
lean -DwarningAsError=true Q760Envelope.lean > axioms.actual
diff -u expected-axioms.txt axioms.actual
```
