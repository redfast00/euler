import sys
import csv
import string
import itertools
import math

filename = sys.argv[1]

def is_triangular(value):
    n = math.floor(math.sqrt(2 * value))
    return 2 * value == n * (n + 1)

def is_triangular_word(word):
    return is_triangular(sum((string.ascii_uppercase.index(letter)+1 for letter in word)))

with open(filename) as namefile:
    csv_reader = csv.reader(namefile.readlines())
    # This is a bit of a hack
    words = csv_reader.__next__()
    print(sum((1 for i in filter(is_triangular_word, words))))
