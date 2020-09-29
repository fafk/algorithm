"""
Find into how many distinct partitions a natural positive number can be partitioned into.
Do not count the number itself as a valid partition.

https://en.wikipedia.org/wiki/Partition_(number_theory)

Solution found by using generating functions.
"""


def polMultByPower(pol, exp):  # multiple a polynomial by x^exp
    return [0] * exp + pol


def addPolynomials(a, b):
    return [
        ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0))
        for i in range(max(len(a), len(b)))
    ]


def getPolyOfOrder(n):
    return [1] + ([0] * (n - 1)) + [1]


def solution(n):
    base = [1, 1]  # (1 + x)
    for i in range(1, n):
        base = addPolynomials(base, polMultByPower(base, i + 1))
    return base[n] - 1  # ^n member of the series


solution(200) == 487067745
