from itertools import product

def distinct_powers(max_size):
    seen = set()
    for a, b in product(range(2, max_size+1), repeat=2):
        seen.add(a**b)
    return seen

print(len(distinct_powers(100)))
