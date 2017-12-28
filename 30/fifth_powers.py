def power_sum(number, power):
    return sum((int(digit)**power for digit in str(number)))

def writeable_as_power(power):
    _max = 9
    while _max < power_sum(_max, power):
        _max = 10 * _max + 9
    for i in range(2, _max):
        if power_sum(i, power) == i:
            print(f'found: {i}')
            yield i

print(sum(writeable_as_power(5)))
