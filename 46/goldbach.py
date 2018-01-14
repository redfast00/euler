from toolbox import DynamicPrime, is_prime
from itertools import count
from math import sqrt, ceil

dyn = DynamicPrime()

# all odd numbers, starting with 3
for candidate in count(3, 2):
    if dyn.is_prime(candidate):
        # number is not composite, skip it
        continue
    for doublesquare in (2*(x**2) for x in range(1, ceil(sqrt(candidate / 2)))):
        if dyn.is_prime(candidate - doublesquare):
            # Found a sum that will work, this candidate is not the counterexample
            break
    else:
        print(f'FOUND: {candidate}')
        break
