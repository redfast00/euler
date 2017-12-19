class fibonaci:
    def __init__(self, limit):
        self.prev = 0
        self.cur = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        nextval = self.prev + self.cur
        if nextval < self.limit:
            self.prev = self.cur
            self.cur = nextval
            return nextval
        else:
            raise StopIteration()

sum = 0
for i in fibonaci(4 * 1000 * 1000):
    if i % 2 == 0:
        sum += i

print(sum)
