class Laptop:
    discount=10 #class variable
    def __init__(self, name, price):
        self.name=name
        self.price=price
        
    @classmethod
    def from_string(clr, string):
        import re
        item=re.findall('is \w*', string)
        name=item[0][3:]
        price=item[1][3:]
        return clr(name, int(price))
    
    
    def applydicount(self):#Intance Method
        discountAmount=(self.price/100) * self.discount
        final_amount =self.price - discountAmount
        return int(final_amount)
    
    
laptop=Laptop('9329', 100)
print(laptop.__dict__)

print(laptop.applydiscount())