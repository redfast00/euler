from toolbox import is_prime, all_primes_below

def is_left_truncatable(number_string):
    for i in range(1, len(number_string)):
        if not is_prime(int(number_string[i:])):
            return False
    return True

def is_right_truncatable(number_string):
    for i in range(1, len(number_string)):
        if not is_prime(int(number_string[:-i])):
            return False
    return True

def is_truncatable(number):
    number_string = str(number)
    return len(number_string) > 1 and is_left_truncatable(number_string) and is_right_truncatable(number_string)

def truncatable_primes_below(number):
    for i in all_primes_below(number):
        if is_truncatable(i):
            yield i

print(sum(truncatable_primes_below(1000000)))
