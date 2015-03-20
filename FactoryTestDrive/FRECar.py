from Car import Car


class FRECar(Car):
    def __init__(self):
        super(FRECar, self).__init__()

        self.name = "FRECar"
        self.parts.append("good Engine")
        self.parts.append("good Sound")
