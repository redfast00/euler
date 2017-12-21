# From https://stackoverflow.com/a/32640407/5431090
import string
from num2letter import int_to_en

def number_of_letters(number):
    word = int_to_en(number)
    return sum([letter.lower() in string.ascii_lowercase for letter in word])


# for i in range(1, 1001):
#     print(number_of_letters(i), int_to_en(i))

total = sum(map(number_of_letters, range(1,1001)))
print(total)
