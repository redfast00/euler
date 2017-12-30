import math

def is_digit_factorial_sum(number):
    return number == sum((math.factorial(int(i)) for i in str(number)))

def find_digit_factorials_below(number):
    for i in range(10, number):
        if is_digit_factorial_sum(i):
            yield(i)

print(sum(find_digit_factorials_below(10**7)))
