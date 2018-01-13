from itertools import combinations_with_replacement
from math import log10, floor

def is_pandigital_product(a, b):
    concatenated = f'{a}{b}{a*b}'
    # Bail out fast
    if len(concatenated) != 9:
        return False

    for i in '123456789':
        if i not in concatenated:
            return False
    return True

found = set()

# The length of the final number can be max 9 digits. Let len(a) and len(b) be
#  the length of a and b respectively. Then len(a) + len(b) + len(a*b) = 9.
#  len(a*b) = len(a) + len(b), and so 9 = 2 * len(a) + 2 * len(b). The smallest of
#  len(a) and len(b) will never be bigger than 9 / 4 = 2.
 
for a in range(1, 99):
    if len(str(a)) != len(set(str(a))):
        # if a contains duplicate digits, skip this a
        continue
    else:
        power = 5 - floor(log10(a))
        for b in range(int(10**(power-2)), int(10**(power))):
        # for b in range(a, 10000):
            if is_pandigital_product(a, b):
                found.add(a * b)
                print(a, b, a*b)
print(sum(found))
