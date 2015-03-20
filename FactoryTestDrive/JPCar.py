from Car import Car


class JPCar(Car):
    def __init__(self):
        super(JPCar, self).__init__()

        self.name = "JPCar"
        self.parts.append("light Metal")
        self.parts.append("good Tires")