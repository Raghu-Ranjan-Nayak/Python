#Use properties and methods of a car class by inheritance
#This inheritance is called single inheritance
class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")
class Toyotacar(Car):
    def __init__(self,name):
        self.name = name
car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.start())