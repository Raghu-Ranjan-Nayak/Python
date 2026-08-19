#Property decorator
class Student:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math
    @property
    def percentage(self):
        return str((self.phy+self.che+self.math)/3)+"%"

s1 = Student(90,95,98)
print(s1.percentage)

s1.phy = 92
print(s1.percentage)
