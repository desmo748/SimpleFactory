from Car import Car

class ITACar(Car):
    def __init__(self):
        super(ITACar, self).__init__()

        self.name = "ITACar"
        self.parts.append("good Looking")
        self.parts.append("good Engine")