from math import sqrt
from itertools import combinations_with_replacement

def pythagorean_streamer(limit):
    for a, b in combinations_with_replacement(range(1, limit), 2):
        c = sqrt(a**2 + b**2)
        if c.is_integer():
            yield a, b, int(c)

for a, b, c in pythagorean_streamer(1000 // 2):
    if a + b + c == 1000:
        print(a*b*c)
