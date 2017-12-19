from functools import reduce
from math import gcd

def lcm(m, n):
    return int(m * n / gcd(m, n))

product = reduce(lcm, range(1, 21))
print(product)
