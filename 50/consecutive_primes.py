from toolbox import all_primes_below

def longest_prime_below(upperbound):
    chain_length = 2
    primes = all_primes_below(upperbound)
    primeset = set(primes)
    max_ = 0
    tried_at_least_one = True
    while tried_at_least_one:
        if chain_length % 2 == 0:
            # we have an even number of primes, so we should only consider a sequence
            #  starting with 2 ... or the sum of the sequence will be even and so not a prime
            candidate = sum(primes[:chain_length])
            if candidate in primeset:
                # Found a prime! set the current maximum to this prime,
                # increase chain lenght and restart
                max_ = candidate
                print(f"Found {max_} at chain lenght {chain_length}")
            chain_length += 1
        else:
            tried_at_least_one = False
            for cur_idx in range(0, len(primes) - chain_length):
                candidate = sum(primes[cur_idx:cur_idx+chain_length])
                if candidate >= upperbound:
                    # exceeded maximum, increase chain length and restart
                    chain_length += 1
                    break
                else:
                    tried_at_least_one = True
                if candidate in primeset:
                    # Found a prime! set the current maximum to this prime,
                    # increase chain lenght and restart
                    max_ = candidate
                    print(f"Found {max_} at chain lenght {chain_length}")
                    chain_length += 1
                    break
    return max_

print(longest_prime_below(1000*1000))
