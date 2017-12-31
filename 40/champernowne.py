from toolbox import nth

def stream_digits(limit):
    current = 0
    yielded = 0
    while yielded <= limit:
        for i in str(current):
            yield i
            yielded += 1
        current += 1

def get_digit(n):
    return nth(stream_digits(n), n, default=None)

product = 1
for i in range(6):
    product *= int(get_digit(10**i))
print(product)
