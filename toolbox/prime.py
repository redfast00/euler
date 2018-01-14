import math
import itertools
import bisect

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
    if number < 2:
        return False
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

def stream_primes():
    primes = []
    candidate = 2
    while True:
        breakpoint = int(math.sqrt(candidate))
        for prime in primes:
            if candidate % prime == 0:
                break
            if prime > breakpoint:
                primes.append(candidate)
                yield candidate
                break
        else:
            primes.append(candidate)
            yield candidate
        candidate += 1

class DynamicPrime(object):
    def __init__(self):
        self.primes = [2, 3]

    def __iter__(self):
        for i in itertools.count(0):
            yield self[i]

    def __getitem__(self, key):
        while len(self.primes) <= key:
            self._generate_next()

        return self.primes[key]

    def is_prime(self, number):
        assert number > 1
        if number > self.primes[-1]:
            while number > self.primes[-1]:
                self._generate_next()
            return number == self.primes[-1]
        else:
            # Lookup prime with binary search in already generated primes
            place = bisect.bisect_left(self.primes, number)
            return (place != len(self.primes) and self.primes[place] == number)

    def _generate_next(self):
        candidate = self.primes[-1] + 1
        while True:
            breakpoint = int(math.sqrt(candidate))
            for prime in self.primes:
                if candidate % prime == 0:
                    break
                if prime > breakpoint:
                    self.primes.append(candidate)
                    return candidate
            else:
                self.primes.append(candidate)
                return candidate
            candidate += 1
