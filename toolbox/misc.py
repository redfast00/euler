from math import floor, log10

def number_of_digits(number):
    return math.floor(math.log10(number)) + 1

def is_pandigital(string):
    if len(string) != 9:
        return False
    for i in '123465789':
        if i not in string:
            return False
    else:
        return True
