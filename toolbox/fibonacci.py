from math import sqrt
import functools

@functools.lru_cache()
def fibonacci(n):
    '''Returns the n-th fibonaci number'''
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n % 2 == 0:
        m = n // 2
        return fibonacci(m)*(2*fibonacci(m-1)+fibonacci(m))
    else:
        m = -(-n // 2) # ceil division
        return fibonacci(m-1)**2 + fibonacci(m) ** 2
