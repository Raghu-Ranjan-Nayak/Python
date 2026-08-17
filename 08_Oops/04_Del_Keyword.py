#Use del keyword to delete object properties
class Student:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
S1 = Student("Raghu","CSE")
print(S1.name)
print(S1.branch)
#Delete branch 
del S1.branch
print(S1.branch) 
