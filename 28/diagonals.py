
def diagonal(width):
    yield 1 # middle cell
    for level in range(1, (width + 1)//2 ):
        first = (2*level+1)**2
        for i in range(4):
            yield(first - i * (2*level))


print(sum(diagonal(1001)))
