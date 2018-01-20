from math import factorial
from functools import partial
# 22 C 3 == 22 C (22-3)
# if n C r > q, then n C (n-r) > q and all numbers between r and n - r will be > q

def ncr(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))

def count_ncr_larger_than(n, maximum=None):
    for r in range(1, n//2):
        if ncr(n, r) > maximum:
            return n - 2*r + 1
    return 0

print(sum(map(partial(count_ncr_larger_than, maximum=1_000_000), range(1, 100+1))))
