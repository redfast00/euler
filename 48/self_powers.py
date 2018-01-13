keep = 10 # number of digits to keep

def last_digits(number, digits=10**keep):
    return pow(number, number, digits)

max_ = 1000
print(sum(map(last_digits, range(1, max_ + 1))) % 10**keep)
