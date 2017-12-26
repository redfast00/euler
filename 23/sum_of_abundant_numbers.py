from toolbox import divisors
from itertools import combinations_with_replacement

def is_abundant(number):
    d = divisors(number)
    d.remove(number)
    return sum(d) > number

limit = 28123
abundant_numbers = [value for value in range(1, limit) if is_abundant(value)]

# This algorithm could be optimized

writeable_numbers = set()
for first, second in combinations_with_replacement(abundant_numbers, 2):
    _sum = first + second
    if _sum <= limit:
        writeable_numbers.add(_sum)
print(sum(set(range(limit+1)).difference(writeable_numbers)))
