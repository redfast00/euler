import math

def factorize(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return [i] + factorize(number // i)
    else:
        return [number]

def divisors(number):
    found = {1}
    for factor in factorize(number):
        found.update({x*factor for x in found})
    return found

def is_prime(number):
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True

def all_primes_below(number):
    assert number >= 2
    primes = []
    candidate = 2
    while candidate < number:
        breakpoint = int(math.sqrt(candidate))
        for prime in primes:
            if candidate % prime == 0:
                break
            if prime > breakpoint:
                primes.append(candidate)
                break
        else:
            primes.append(candidate)
        candidate += 1
    return primes
