from toolbox import stream_primes
from itertools import takewhile

def is_n_pandigital(number):
    string = str(number)
    for i in '123456789'[:len(string)]:
        if i not in string:
            return False
    return True

for i in takewhile(lambda x: x <= 7654321, stream_primes()): # math: 7 + 6 + ... + 1 % 3 != 0
    if is_n_pandigital(str(i)):
        print(i)
