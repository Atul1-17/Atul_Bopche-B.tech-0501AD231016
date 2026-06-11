
# Q2

from abc import ABC, abstractmethod

class Vehicle(ABC) :
    @abstractmethod

    def start(self):
        pass

    def stop(self):
        pass

    def fuel_type(self):
        pass

class Car(Vehicle) :
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

    def fuel_type(self):
        print("Car uses petrol")

class Bike(Vehicle) :
    def start(self):
        print("Bike is starting")

    def stop(self):
        print("Bike is stopping")

    def fuel_type(self):
        print("Bike uses petrol")

class Tesla(Vehicle) :
    def start(self):
        print("Tesla is starting")

    def stop(self):
        print("Tesla is stopping")

    def fuel_type(self):
        print("Tesla uses Electric")


c = Car()
c.start()
c.stop()
c.fuel_type()

b = Bike()
b.start()
b.stop()
b.fuel_type()

t = Tesla()
t.start()
t.stop()
t.fuel_type()