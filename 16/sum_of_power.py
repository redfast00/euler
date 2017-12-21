from functools import reduce

number = 2**1000

print(reduce((lambda x,y: x+y), map((lambda x:int(x)), str(number))))
