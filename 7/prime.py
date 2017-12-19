from math import sqrt

def stream_primes(num):
    primes = []
    candidate = 2
    for i in range(num):
        prime = next_prime(primes, candidate)
        primes.append(prime)
        candidate = prime + 1
        yield prime

def next_prime(primes, candidate):
    while True:
        for prime in primes:
            if candidate % prime == 0:
                break
            elif prime > sqrt(candidate):
                return candidate
        else:
            return candidate
        candidate += 1

for prime in stream_primes(10001):
    print(prime)
