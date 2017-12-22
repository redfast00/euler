import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'input.txt')

# Algorithm works as follows: look at the penultimate layer of the tree. Then, for
#  each node that layer, look at the possible choices below the node, pick the best one
#  and add it to the node we are looking at. Then discard the last layer. Repeat
#  this until we are at the top layer:

def choose_best(cellidx, levelidx, levels):
    level_below = levels[levelidx+1]
    return max(level_below[cellidx], level_below[cellidx + 1])

with open(filename) as pyramidfile:
    levels = [[int(number) for number in line.split(' ')] for line in pyramidfile.readlines()]
    for level in levels[len(levels)::-1][1:]:
        # We will not remove or add items in the list, so this is fine
        for cellidx, value in enumerate(level):
            level[cellidx] += choose_best(cellidx, len(level) - 1, levels)
    print(levels[0][0])
