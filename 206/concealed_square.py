from math import sqrt, floor, ceil

fmt = '1_2_3_4_5_6_7_8_9_0'
# Since the number ends in a zero, we know that two factors of the number have to be 2 and 5
# Since the number is a square, it will contain 2 and 5 two times, so the original number should
#  contain 2 and 5 in it's prime factors and so should be divisible by 10.

def is_solution(candidate):
    # Only multiples of 10 should come in here, so no need to check last two digits
    number = (candidate//10)**2
    for i in range(9, 0, -1):
        if number % 10 != i:
            return False
        number = number // 100
    return True

minimum = floor(sqrt(int(fmt.replace('_', '0'))))
maximum = ceil(sqrt(int(fmt.replace('_', '9'))))
# Since the minimum has to a multiple of 10, remove the last digit.
minimum = (minimum//10)*10

print(f'Now doing {(maximum - minimum)//10} calculations')

for candidate in range(minimum, maximum, 10):
    if is_solution(candidate):
        print(candidate)
        break
