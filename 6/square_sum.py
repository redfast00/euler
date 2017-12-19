def sum_of_squares_until(value):
    return sum(map(lambda x:x**2, range(value+1)))

def sum_until(value):
    return int((value+1)*(value/2)) # That one smart dude Gauss

value = 100
print(sum_until(value)**2 - sum_of_squares_until(value))
