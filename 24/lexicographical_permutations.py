from itertools import permutations, islice

characters = '0123456789'
index = 1000 * 1000

generator = permutations(characters)

print(''.join(islice(generator, index - 1, index).__next__()))
