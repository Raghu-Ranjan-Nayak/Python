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

#This inheritance is called multi-level inheritance
class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")
class Toyotacar(Car):
    def __init__(self,brand):
        self.brand = brand
class fortuner(Toyotacar):
    def __init__(self,type):
        self.type = type
car1 = fortuner("petrol")
car1.stop()

#This inheritance is called multiple inheritance
class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")
class Toyotacar:
    @staticmethod
    def brand():
        print("pulse")
class Fortuner(Car,Toyotacar):
    def __init__(self,type):
        self.type = type
car1 = Fortuner("petrol")
car1.brand()
car1.start()
