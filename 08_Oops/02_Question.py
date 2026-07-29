#Create a class which takes name and marks of three subjects and calculate average
class Student:
    def __init__(self,name,markp,markc,markm):
        self.name = name
        self.markp = markp
        self.markc = markc
        self.markm = markm

    def avg(self):
        print((self.markp + self.markc + self.markm)/3)

s1 = Student("Raghu",90,91,92)
s1.avg()