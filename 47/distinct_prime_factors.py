from toolbox import DynamicPrime
from itertools import count

CONSECUTIVE = 4

def at_least_n_factors(number, n=CONSECUTIVE, dyn=DynamicPrime()):
    return number > 1 and len(set(dyn.factor(number))) >= n

seen = 0
first = 0
for number, has_factors in enumerate(map(at_least_n_factors, count(0))):
    if has_factors:
        seen += 1
    else:
        seen = 0
    if seen == 1:
        first = number
    if seen == CONSECUTIVE:
        print(first)
        break
