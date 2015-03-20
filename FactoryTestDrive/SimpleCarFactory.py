from GERCar import GERCar
from USCar import USCar
from JPCar import JPCar
from ITACar import ITACar
from FRECar import FRECar


class SimpleCarFactory(object):
    def createCar(self, type):
        if type == "GER":
            car = GERCar()
        elif type == "US":
            car = USCar()
        elif type == "JP":
            car = JPCar()
        elif type == "ITA":
            car = ITACar()
        elif type == "FRE":
            car = FRECar()
        else:
            raise TypeError("No such car type: " + type)
        return car