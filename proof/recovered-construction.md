# Q760: arbitrary mixing preserves maximum description gain

## Source and exact target

Lardy, Grünwald and Harremoës, *Reverse Information Projections and Optimal E-statistics*, Appendix C, final paragraph, printed p. 23 (PDF p. 23), state the conjectured equality “D(P∥Q ⇝ C) = D(P∥Q ⇝ C′)” under the requirement that the measures have “densities with respect to a common σ-finite measure.”

[Exact page, CWI's final-version copy (dated July 30, 2024, arXiv v3)](https://ir.cwi.nl/pub/34397/2306.16646v3-4-.pdf#page=23) · [IEEE publication DOI](https://doi.org/10.1109/TIT.2024.3444458) · [Institutional final-version record](https://ir.cwi.nl/pub/34397/) · [2025 thesis, Appendix A.3, printed p. 216 / PDF p. 231](https://ir.cwi.nl/pub/35219/ThesisLardy.pdf#page=231).

Precisely, C is a σ-convex class of subprobability measures and C′ its Choquet-convex hull, allowing measurable barycentric mixtures in the source's Polish/Borel model. P,Q and every R∈C share one σ-finite dominating measure λ. With lowercase densities, define

    g(R) = ∫ log(r/q) dP − R(Ω) + Q(Ω).

An undefined value counts as −∞ in the supremum. The target is sup(C) g = sup(C′) g, including infinite values, without assuming existence of an optimal measure, finite KL divergence, or a finite-value member of C.

## Proof

Work in the real space L¹(λ). Let B be the norm closure of the densities of C; it is convex because C is σ-convex. If C is empty the assertion is immediate, so assume otherwise. The nonnegative unit ball describing subprobabilities is closed, so B still consists of subprobability densities.

**1. The closed class B contains all measurable barycenters.** A barycenter S of any family of measures with densities in B is λ-dominated, as every λ-null set has mass zero under each component. If s were outside B, Hahn–Banach would strictly separate it from B via some bounded measurable function h, using (L¹(λ))*=L∞(λ). The defining weak integration identity of a barycenter gives ∫h dS equal to the mixture average of the component values, all bounded above by sup over B. This contradicts strict separation. Representatives of h can be taken bounded and measurable everywhere, and the identity for bounded h follows from that for indicators. This does not require choosing jointly measurable density versions for the component family. Thus B is Choquet-closed, and C′ has densities in B, even if a hull definition takes repeated mixtures.

**2. Countable convexity repairs the logarithmic lower tail.** Fix a density s in B and 0<δ<1. For n≥1 choose Rₙ∈C such that

    ‖rₙ−s‖₁ ≤ δ,
    P(Bₙ) ≤ δ·2^(−n)/n, where Bₙ={s>0 and rₙ<(1−δ)s}.

Such choices are possible: take an L¹-approximating sequence in C and a subsequence converging λ-almost everywhere. Because P≪λ, the indicators of Bₙ for candidates along that subsequence tend to zero P-almost surely, and dominated convergence yields the desired arbitrarily small bound. Set R=Σₙ≥1 2^(−n)Rₙ. This is in C, its density is the corresponding nonnegative series λ-almost everywhere, and ‖r−s‖₁≤δ.

From summability, N=sup({0}∪{n:x∈Bₙ}) is finite P-almost surely and ∫N dP≤Σₙ nP(Bₙ)≤δ. For x with s(x)>0, all terms with n>N have rₙ(x)≥(1−δ)s(x). Their mixture weights add up to 2^(−N). Hence, P-almost surely,

    r ≥ (1−δ) 2^(−N) s.

This holds also where s=0, trivially. The nonnegative loss bound H=−log(1−δ)+N log 2 satisfies

    ∫H dP ≤ −P(Ω)log(1−δ)+δ log 2.

**3. Compare the extended gains.** Fix s with g(S)>−∞, so the negative part of the target log ratio is integrable. By the lower bound on r, log(r/q) ≥ log(s/q)−H wherever the target log ratio is defined. For q=0<s both ratios are +∞ almost surely because r>0; a place with s=0<q has zero P-mass if g(S)>−∞. If 0/0 is regarded as undefined such a point cannot carry P-mass for this S; under the usual fixed 0/0 convention an r=0 retains the same value and an r>0 raises it to +∞. Thus the negative part of the new log ratio is integrable as well. The inequality can be integrated without subtracting two infinities; in particular if the target gain is +∞ the new gain is +∞. Also |R(Ω)−S(Ω)|≤δ. Consequently

    g(R) ≥ g(S) − δ + P(Ω)log(1−δ) − δ log 2.

Let δ decrease to zero. Every candidate S in C′ with value greater than −∞ is matched arbitrarily closely from below by candidates in C (and +∞ is preserved). If none exists, the suprema are already both −∞. This proves the desired equality. In fact sup over C equals sup over the entire L¹-closed convex class B.

### Why the domination hypothesis matters

If one weakens the source to allow only P and Q to be dominated together, the conclusion need not hold. Take P=Q uniform on [0,1] and C all countably supported probability measures there. This class is σ-convex. With an individual common dominating measure for each R, its density is zero P-almost surely, so every R∈C gives −∞. But the measurable uniform mixture of Dirac masses belongs to the Choquet hull and is P itself, with gain zero. There is no common σ-finite measure dominating C and P in this example; every singleton would need positive mass, impossible for uncountably many points in a σ-finite space. The theorem above uses exactly the stronger domination in the paper, not just domination of P,Q alone.

## Source and easy-corollary audit, 2026-11-26

- Compared the [IEEE-linked final institutional copy](https://ir.cwi.nl/pub/34397/2306.16646v3-4-.pdf#page=23), the [arXiv version history](https://arxiv.org/abs/2306.16646), and the later [thesis, p. 216](https://ir.cwi.nl/pub/35219/ThesisLardy.pdf#page=231). All accessible full versions retain the conjecture. The linked IEEE landing itself was not retrievable; page numbering refers to the authors' institutional final-version copy, not to a guessed IEEE typeset page.
- Their Corollary 1 treats an already attained reverse projection. Appendix C's Lemma 4 and Theorem 7 handle countable mixtures with a finite starting description or near-optimal sequences under their stated premises. That does not give an approximant of an arbitrary measurable mixture with controlled log loss when C has no known anchor. Weak or L¹ closure alone is insufficient for a lower bound on log gain: uniform densities truncated on a shrinking positive-P set converge in L¹ to the uniform density, while each truncated gain against uniform is −∞. The geometric-mixture lower-tail bound above handles exactly that gap.
- [Ram, Larsson, Ruf and Ramdas, *Strong duality for the GROW criterion*, v2](https://arxiv.org/abs/2606.24768v2) proves minimax log-betting and weak-* closed entropy results. The bounded-e-variable duality does not compare the extended description-gain suprema here for arbitrary q, including the case of infinite KL, or construct the needed individual countable mixture. The finite-KL identity relating description gain to a difference of KL divergences is not available when both are infinite.
- Searched exact paper and conjecture wording, countable versus Choquet convexification, description-gain and log-density closure variants, and later reverse-projection work. No exact solution or immediate scope-matching corollary located. Hahn–Banach, dominated convergence and the geometric-tail summation are standard ingredients; the bounded check does not certify priority.
