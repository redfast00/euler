import math
import itertools

class NumberGenerator(object):
    def __init__(self):
        self.index = 1
        self.last_generated = 0

    def is_in_sequence(self, value):
        while self.last_generated < value:
            self.last_generated = self.generate_next()
            self.index += 1
        return self.last_generated == value

    def generate_next(self):
        raise NotImplementedError

class Triangular(NumberGenerator):
    def generate_next(self):
        return self.index * (self.index + 1) // 2

class Pentagonal(NumberGenerator):
    def generate_next(self):
        return self.index * (3 * self.index - 1) // 2

triangular = Triangular()
pentagonal = Pentagonal()

# 143 because that's the first number, we need to find the second
for i in (n*(2*n - 1) for n in itertools.count(143 + 1)):
    if pentagonal.is_in_sequence(i) and triangular.is_in_sequence(i):
        print(i)
        break
