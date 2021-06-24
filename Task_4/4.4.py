class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(self.name, "bird can fly")

    def walk(self):
        print(self.name, "bird can walk")


class FlyingBird(Bird):
    def __init__(self, name, ration="seeds"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(self.name, "eats", self.ration)


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(self.name, "eats", self.ration)

    def fly(self):
        raise AttributeError(self.name, "cannot fly")

    def swim(self):
        print(self.name, "can swim")


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name, ration="everything"):
        super().__init__(name)
        self.ration = ration

    def fly(self):
        print(self.name, "can fly")


nonf = NonFlyingBird("penguin")
nonf.eat()
superb = SuperBird("pelican")
superb.eat()
superb.fly()
superb.walk()
