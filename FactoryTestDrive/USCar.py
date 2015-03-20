from Car import Car


class USCar(Car):
    def __init__(self):
        super(USCar, self).__init__()

        self.name = "USCar"
        self.parts.append("heavy Metal")
        self.parts.append("good Engine")