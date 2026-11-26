# Three atoms and a geometric mixture

Take counting measure on three atoms A, B and C. The target density is s = (1/3, 1/3, 1/3) and the tolerance is δ = 1/4. Use a sampling law P = (1/16, 1/64, 59/64). The first candidate lowers atom A to 1/6, the second lowers B to 1/6, and all other entries of those candidates equal the target. For n ≥ 3 the candidate lowers C by 2^(−n−1) and keeps A and B unchanged.

The good-entry threshold is (1−δ)s = 1/4 on every atom. Only the first row is bad at A, only the second is bad at B, and every row is good at C. The bad probabilities satisfy the proof's budgets and the expected last bad index is 3/32. Weighting by 2^(−n) yields the density (1/4, 7/24, 31/96). The pointwise floors from the proof are (1/8, 1/16, 1/4). These floors use only weights after the last bad row. Earlier contributions can make the true mixture larger.

The viewer groups all rows n ≥ 3 into a weighted average with total weight 1/4 and row density (1/3, 1/3, 7/24). Each of those rows individually meets the threshold. [Finite replay](../verification/results/replay.txt) · [Offline explorer](../visualization/geometric-mixture-explorer.zip)
