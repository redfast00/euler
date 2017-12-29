from toolbox import all_primes_below, is_prime
from itertools import permutations

def is_circular_prime(number):
    numberstring = str(number)
    for i in range(1, len(numberstring)):
        candidate = int(f'{numberstring[i:]}{numberstring[:i]}')
        if not is_prime(candidate):
            return False
    return True

def find_circular_primes_below(number):
    all_primes = all_primes_below(number)
    print("Done finding primes, now looking for circular primes")
    for number in all_primes:
        if is_circular_prime(number):
            yield number

print(sum(1 for i in find_circular_primes_below(1000 * 1000)))
