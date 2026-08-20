#Engineer class is inheritant the employee class
class Employee:
    def __init__(self,roll,department,salary):
        self.role = roll
        self.department = department
        self.salary = salary
    def showDetails(self):
        print("Roll is",self.role)
        print("Department is",self.department)
        print("Salary is",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("devloper","software","12 LPA")


e1 = Engineer("Raghu",19)
e1.showDetails()