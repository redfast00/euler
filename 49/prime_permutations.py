from itertools import permutations
from toolbox import is_prime

def contains_sequence(numbers):
    numberset = set(numbers)
    for idx, first in enumerate(numbers):
        for second in numbers[idx+1:]:
            if 2 * second - first in numberset:
                return [first, second, 2 * second - first]
            elif 2 * second - first > numbers[-1]:
                break

seen = set()

for candidate in range(1000, 9999):
    # check if smallest is prime
    if not is_prime(candidate):
        continue
    smallest = ''.join(sorted(str(candidate)))
    if smallest in seen:
        continue
    else:
        found = set()
        for permutation in permutations(str(smallest)):
            number = int(''.join(permutation))
            if not(1000 <= number < 10000):
                continue
            if is_prime(number):
                found.add(number)
        if len(found) < 3:
            continue
        found = sorted(found)
        sequence = contains_sequence(found)
        if sequence is not None:
            print(sequence)
            print(''.join([str(i) for i in sequence]))
        seen.add(smallest)
