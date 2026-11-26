"""Exact finite checks of the geometric envelope and worked subprobabilities."""

from fractions import Fraction as F
from itertools import product


def check_geometric_envelope():
    checked = 0
    for length in range(1, 12):
        weights = [F(1, 2**i) for i in range(1, length+1)]
        tail = F(1, 2**length)  # Treat all subsequent indices as good.
        for bad in product((False, True), repeat=length):
            bad_indices = [i for i, flag in enumerate(bad, 1) if flag]
            last = max(bad_indices, default=0)
            good_weight = tail+sum(w for flag, w in zip(bad, weights) if not flag)
            assert good_weight >= F(1, 2**last)
            assert last <= sum(bad_indices)
            for target, delta in product((F(0), F(1, 5), F(1)), (F(1, 100), F(1, 5))):
                lowest_mixture = (1-delta)*target*good_weight
                assert lowest_mixture >= (1-delta)*target*F(1, 2**last)
                checked += 1
    assert checked == 24564
    print(f"{checked} exact geometric lower-envelope inequalities")


def check_worked_example():
    s = (F(1, 3),)*3
    p = (F(1, 16), F(1, 64), F(59, 64))
    delta = F(1, 4)
    weights = (F(1, 2), F(1, 4), F(1, 4))
    # The third row is the weighted mean of approximants n >= 3.
    # Their third-coordinate deficit is 2^(-n-1). Summing its weighted
    # geometric series gives a total deficit of 1/96.
    first = (F(1, 6), s[1], s[2])
    second = (s[0], F(1, 6), s[2])
    tail_deficit = F(1, 2**7)/(1-F(1, 4))
    assert tail_deficit == F(1, 96)
    later = (s[0], s[1], s[2]-tail_deficit/weights[2])
    assert later == (F(1, 3), F(1, 3), F(7, 24))
    assert s[2]-F(1, 16) >= (1-delta)*s[2]
    assert all(sum(abs(a-b) for a,b in zip(r,s)) <= delta for r in (first, second, later))
    assert p[0] <= delta/2 and p[1] <= delta/8

    rows = (first, second, later)
    mixture = tuple(sum(weights[i]*rows[i][j] for i in range(3)) for j in range(3))
    assert mixture == (F(1, 4), F(7, 24), F(31, 96))
    last = [max((i for i, r in enumerate(rows, 1) if r[j] < (1-delta)*s[j]), default=0)
            for j in range(3)]
    assert last == [1, 2, 0]
    assert sum(n*w for n,w in zip(last,p)) == F(3, 32) <= delta
    floor = tuple((1-delta)*value/F(2**index) for value,index in zip(s,last))
    assert floor == (F(1, 8), F(1, 16), F(1, 4))
    assert all(a>=b for a,b in zip(mixture,floor))
    print("Exact three-atom mixture, last bad indices, budgets and density floors")


def check_unanchored_truncations():
    for length in range(1, 31):
        masses = [F(1, 2**i) for i in range(1, length+1)]
        missing = F(1, 2**length)
        norm = sum(masses)
        assert norm+missing == 1 and missing>0
        truncated = [value/norm for value in masses]
        assert sum(truncated) == 1
        assert sum(abs(t-m) for t,m in zip(truncated,masses))+missing == 2*missing
    print("30 exact truncation distances and positive missing masses")


if __name__ == "__main__":
    check_geometric_envelope()
    check_worked_example()
    check_unanchored_truncations()
