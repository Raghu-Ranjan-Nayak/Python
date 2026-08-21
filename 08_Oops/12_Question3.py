#print order1>order2 if price of order1>order2
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,ord2):
        return self.price > ord2.price
        
ord1 = Order("chips",200)
ord2 = Order("food",100)
print(ord1>ord2)