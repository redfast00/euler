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
