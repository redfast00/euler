import functools

# # This would be cool, but Python doesn't support tail call recursion
# @functools.lru_cache(maxsize=128, typed=False)
# def collatz(number):
#     if number == 1:
#         return 1
#     elif number % 2 == 0:
#         return 1 + collatz(number // 2)
#     else:
#         return 1 + collatz(3 * number + 1)

def collatz_no_recursion(number):
    calls = 1
    print(number)
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        calls += 1
    return calls


print(max(range(1, 1000*1000), key=collatz_no_recursion))
