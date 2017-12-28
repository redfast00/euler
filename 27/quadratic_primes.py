from toolbox import is_prime

def len_consecutive_squares(a, b):
    i = 0
    value = i**2 + i*a + b
    while value > 1 and is_prime(value):
        i += 1
        value = i**2 + i*a + b
    return i

_max = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        cur = len_consecutive_squares(a, b)
        if cur > _max:
            _max = cur
            print(f'{a} * {b} = {a * b}')
