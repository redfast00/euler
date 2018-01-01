from itertools import permutations

def substring_property(number_string):
    dividers = [2, 3, 5, 7, 11, 13, 17]
    for i, divider in zip(range(7), dividers):
        if int(number_string[i+1:i+4]) % divider != 0:
            return False
    return True

def finder():
    for number_tuple in permutations('0123465789'):
        number_string = ''.join(number_tuple)
        if substring_property(number_string):
            print(number_string)
            yield int(number_string)

print(f'Sum = {sum(finder())}')
