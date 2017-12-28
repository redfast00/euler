def leftover(amount, possible_sizes):
    if amount == 0 or len(possible_sizes) <= 1:
        return 1
    else:
        return sum(map(lambda x: leftover(amount - x, possible_sizes[1:]), range(0, amount+1, possible_sizes[0])))

print(leftover(200, [200, 100, 50, 20, 10, 5, 2, 1]))
