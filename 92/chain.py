# Goal: find amount of numbers linking to 89 below 10 million.

seen = {89: 89, 1:1}

UNTIL = 10_000_000
lookup = {str(i): i**2 for i in range(0, 10)}


def next_item_in_chain(number):
    return sum((lookup[i] for i in str(number)))

def end_small_number(number):
    encountered_here = set()
    while True:
        cached = seen.get(number, False)
        if cached:
            for value in encountered_here:
                seen[value] = cached
            return cached
        encountered_here.add(number)
        number = next_item_in_chain(number)

def end(number):
    if number < 1000:
        return end_small_number(number)
    else:
        number = next_item_in_chain(number)
        return seen[number]

print(sum((1 for i in range(1, UNTIL) if end(i) == 89)))
