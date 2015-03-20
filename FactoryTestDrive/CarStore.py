class CarStore(object):
    def __init__(self, factory):
        self._factory = factory

    def orderCar(self, type):
        car = self._factory.createCar(type)
        print(car)
        car.construct()
        car.wash()
        car.dry()
        car.ship()
        return car
