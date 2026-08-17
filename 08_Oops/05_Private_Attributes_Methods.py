#Write a object to use private and public attributes and methodsgit
class Student:
    #This is private attribute
    __name = "Raghu"
    #This is private method
    def __hello(self):
        print("Hello")
        #This is public method
    def welcome(self):
        self.__hello()
S1 = Student()
print(S1.welcome())
