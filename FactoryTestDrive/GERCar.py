from Car import Car

class GERCar(Car):
    def __init__(self):
        super(GERCar, self).__init__()

        self.name = "GERCar"
        self.parts.append("good Engine")
        self.parts.append("good Sound")
