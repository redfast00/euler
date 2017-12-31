from math import sqrt
from collections import Counter



def find_max(limit):
    seen = Counter()
    for a in range(1, limit):
        for b in range(1, a+1):
            c = sqrt(a**2 + b**2)
            if a + b + c > limit:
                break
            if c.is_integer():
                c = int(c)
                print(f'Found triplet: {a},{b},{c}')
                seen[a+b+c] += 1
    return seen

result = find_max(1000)
print(result.most_common(1))
