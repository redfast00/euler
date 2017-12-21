from math import factorial

def choose(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k))

size = 20

print(choose(2*size, size))
