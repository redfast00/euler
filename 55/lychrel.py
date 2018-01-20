def is_palindrome(number):
    string = str(number)
    number_of_digits = len(string)
    for i in range(number_of_digits//2):
        if string[i] != string[number_of_digits - i - 1]:
            return False
    return True

def is_lichrel_number(number, limit=50):
    for i in range(limit):
        number = number + int(str(number)[::-1])
        if is_palindrome(number):
            return False
    return True

count = 0
for i in range(1, 10_000):
    count += is_lichrel_number(i)
print(count)
