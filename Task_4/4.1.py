import sys


class Counter:
    def __init__(self, start = 0, stop = sys.maxint):
        self.start_value = start
        self.stop_value = stop

    def increment(self):
        if self.start_value == self.stop_value:
            print("Maximal value is reached")
        else: self.start_value += 1
    def get(self):
        print(self.start_value)


c = Counter()
c.increment()
c.get()
d = Counter(21,22)
d.increment()
d.get()
d.increment()
d.get()