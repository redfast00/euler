def is_palindrome(string):
    return string == string[::-1]

def palindromes_below(_max):
    for i in range(1, _max):
        if is_palindrome(str(i)) and is_palindrome("{0:b}".format(i)):
            yield i

print(sum(palindromes_below(1000000)))
