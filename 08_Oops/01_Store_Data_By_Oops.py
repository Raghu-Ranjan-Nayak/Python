#Store data of a student by using oops
class student:
    def __init__(self,name,mark):
        print("Add new student in the database")
        self.name = name
        self.mark = mark

    def welcome(self):
        print("welcome",self.name)
        
s1 = student("Raghu",98)
print(s1.name,s1.mark)

s1.welcome()
