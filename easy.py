from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

def multiples(n):
    mul_5 = 0
    mul_3 = 0
    mul_15 = 0
    for i in range(1, (n//3) + 1, 1):
        mul_3 += 3*i

    for j in range(1, (n//5), 1):
        mul_5 += 5*j
    for k in range(n//15 + 1):
        mul_15 += 15*k

    total = mul_5 + mul_3 - mul_15

    return total

u = multiples(10)
v = multiples(100)
w = multiples(1000)


import operator as op
from scipy.special import comb as ncr

def wncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom


def mendel(k, m, n):
    total = ncr(k + m + n, 2, exact=True)
    if k == 1:
        if m == 1:
            if n == 1:
                outcome = 2.5
            else:
                outcome = 1 + ncr(n, 1, exact=True) + ncr(n, 1, exact=True)*0.5
        else:
            outcome = ncr(m, 1, exact=True) + ncr(n, 1, exact=True) + ncr(m, 1, exact=True)*ncr(n, 1, exact=True)*0.5 + ncr(m, 2, exact=True)*0.75
    else:
        outcome = ncr(k, 2, exact=True) + ncr(k, 1, exact=True)*ncr(m, 1, exact=True) + ncr(k, 1, exact=True)*ncr(n, 1, exact=True) + ncr(m, 2, exact=True)*0.75 + ncr(m, 1,  exact=True)*ncr(n, 1, exact=True)*0.5

    probablity = outcome/total

    return probablity

v = mendel(2, 2, 2)
ans = mendel(26, 17, 29)

