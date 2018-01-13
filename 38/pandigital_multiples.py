from toolbox import number_of_digits, is_pandigital

def concat(number):
    places_left = 9
    result = []
    current = 1
    while places_left > 0:
        to_add = str(current * number)
        result.extend(to_add)
        places_left -= len(to_add)
        current += 1
    if places_left == 0:
        return ''.join(result)

max_ = 0
# 10000 because if i is 4 digits, then 2*i might be 5 digits and form 9 digits that way
for i in range(1, 10000):
    result = concat(i)
    if result:
        number = int(result)
        if number > max_ and is_pandigital(result):
            print(f'New maximum: {number}')
            max_ = number

print(max_)
