class Car(object):
    def __init__(self):
        self.parts = []
        self.name = ""

    def construct(self):
        print("Constructing your " + self.name)

    def wash(self):
        print("Washing your " + self.name)

    def dry(self):
        print("Drying your " + self.name)

    def ship(self):
        print("Shipping your " + self.name)

    def __repr__(self):
        display = ("---- " + self.name + " ----\n")
        for part in self.parts:
            display += part + '\n'

        return display
