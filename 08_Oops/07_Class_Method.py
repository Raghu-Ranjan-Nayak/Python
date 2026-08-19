#Acess the class by using classs method
class Person:
    name = "Raghu"
    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Person()
p1.changename("Raja")
print(p1.name)
print(Person.name)