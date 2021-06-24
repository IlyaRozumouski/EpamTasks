instances = 0


class Singleton:

    def __init__(self):
        global instances
        if instances == 0:
            instances += 1
        else:
            print("Object of this class is already existing")


c = Singleton()
f = Singleton()
