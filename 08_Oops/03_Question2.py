#Creating a object which credit , debit , and check balance of your account
class Account:

    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc


    def credit(self,ammount):
        self.bal += ammount
        print("Rs",ammount,"was credited")
        print("Total ammount is:",self.check_bal())
    def debit(self,ammount):
        self.bal -= ammount
        print("Rs",ammount,"was debited")
        print("Total ammount is:",self.check_bal())
    def check_bal(self):
        return self.bal

A1 = Account(100,2785)
print(A1.bal)
print(A1.acc)
A1.credit(100)
A1.debit(100)