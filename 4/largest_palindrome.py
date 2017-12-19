from itertools import combinations_with_replacement

def ndigits(digits):
    multiplier = 10**(digits-1)
    for i in range(1,10):
        for j in range(multiplier):
            yield i*multiplier + j


def is_palindrome(digits):
    return str(digits) == str(digits)[::-1]

def palindromes(digits):
    for a, b in combinations_with_replacement(ndigits(digits), 2):
        if is_palindrome(a * b):
            yield(a*b)

print(max(palindromes(3)))
