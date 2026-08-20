#Adding two complex numbers
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real, "i+",self.img,"j")
    def __add__(self,c2):
        newreal = self.real + c2.real
        newimg = self.img + c2.img
        return Complex(newreal,newimg)
    

c1=Complex(2,5)
c1.shownumber()

c2=Complex(4,7)
c2.shownumber()

#This is possible for polymerphism
c3 = c1 + c2
c3.shownumber()