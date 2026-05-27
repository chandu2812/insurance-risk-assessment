import math
from math import comb



def binomial_probability(n, k, p):
    # Exact probability of exactly k claims
    if k < 0 or k > n:
        return 0

    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def cumulative_probability(n, max_k, p):
    # P(X <= max_k)
    total = 0

    for i in range(max_k + 1):
        total += binomial_probability(n, i, p)

    return total


def expected_claims(n, p):
    # E(X) = np
    return n * p


def variance_claims(n, p):
    # Var(X) = np(1-p)
    return n * p * (1 - p)


def standard_deviation(n, p):
    return math.sqrt(variance_claims(n, p))