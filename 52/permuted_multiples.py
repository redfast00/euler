def is_okay(number):
    characters = sorted(str(number))
    for i in range(2, 6 + 1):
        if characters != sorted(str(i * number)):
            return False
    return True

candidate = 1
while not is_okay(candidate):
    candidate += 1
print(candidate)
