from FactoryTestDrive.CarStore import CarStore
from FactoryTestDrive.SimpleCarFactory import SimpleCarFactory

__author__ = 'Desmo'


class FactoryTestDrive(object):
    def main():
        factory = SimpleCarFactory()
        store = CarStore(factory)
        car = store.orderCar("US")
        print("Here is your " + car.name + "\n")
        car = store.orderCar("JP")
        print("Here is your " + car.name + "\n")
        car = store.orderCar("FRE")
        print("Here is your " + car.name + "\n")



    main = staticmethod(main)


if __name__ == '__main__':
    FactoryTestDrive.main()