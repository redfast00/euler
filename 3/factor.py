import math

def factor(number):
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return factor(number // i) + [i]
    else:
        return [number]

print(max(factor(600851475143)))
