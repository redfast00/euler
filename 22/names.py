import sys
import csv
import string

filename = sys.argv[1]

def word_value(word):
    return sum((string.ascii_uppercase.index(letter)+1 for letter in word))

def value_names(names):
    for idx, name in enumerate(sorted(names)):
        yield (idx+1) * word_value(name)

with open(filename) as namefile:
    csv_reader = csv.reader(namefile.readlines())
    # This is a bit of a hack
    names = csv_reader.__next__()
    print(sum(value_names(names)))
