from math import sqrt
def stream_primes(maxprime):
    primes = []
    candidate = 2
    while True:
        prime = next_prime(primes, candidate)
        primes.append(prime)
        candidate = prime + 1
        if prime < maxprime:
            yield prime
        else:
            break

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

below = 1000*1000*2
print(sum(stream_primes(below)))
