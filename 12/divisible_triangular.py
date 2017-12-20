import math

def factor(number):
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return factor(number // i) + [i]
    else:
        return [number]

def number_of_divisors(factors):
    total = 1
    for number in set(factors):
        total *= factors.count(number) + 1
    return total

def triangular():
    result = 0
    now = 0
    while True:
        result += now
        now += 1
        yield result

for idx, triangle in enumerate(triangular()):
    divisors = number_of_divisors(factor(triangle))
    if divisors > 500:
        print(triangle)
        break
