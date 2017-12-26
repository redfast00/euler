def divisors(number):
    for divisor in range(1, (number//2)+1):
        if number % divisor == 0:
            yield divisor

def paired_number(number):
    '''Returns the sum of divisors of a number'''
    return sum(divisors(number))

def amicable_numbers_below(upperbound):
    for i in range(1, upperbound):
        other_number = paired_number(i)
        if i != other_number and other_number < upperbound:
            if paired_number(other_number) == i:
                yield i

print(sum(amicable_numbers_below(10000)))
