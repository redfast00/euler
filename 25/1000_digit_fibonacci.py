from toolbox import fibonacci

def length_of_fibonacci(number):
    return len(str(fibonacci(number)))

def find_length(length):
    current_guess = 1
    while length_of_fibonacci(current_guess) < length:
        current_guess *= 2
    for i in range(current_guess // 2, current_guess):
        if length_of_fibonacci(i) >= length:
            return i

print(find_length(1000))
