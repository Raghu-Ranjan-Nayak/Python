#Claculate the area and parametr of a circle
class Circle:
    def __init__(self,rad):
        self.rad = rad
    def area(self):
        print("area of a circle is",3.14*self.rad*self.rad)
    def perimeter(self):
        print("perimeter of a circle is",2*3.14*self.rad)

c1 = Circle(2)
c1.area()

c1 = Circle(5)
c1.perimeter()