

class Travel:
    def __init__(self, country, month, type):
        self.country=country
        self.month=int(month) 
        self.type=type
        self.price=0
        
    def trip_infor(self):
        if self.month >= 10 and self.month <= 3:
            print("You are goinng to {self.country} in the winter! This is a {self.type} trip")
        elif self.month > 3 and self.month < 10:
            print(f"You are going to {self.county} in the Summer! This is a {self.type} trip!") 
        else:
            print("Invalid Input")
            
    def calc_cost(self, cost):
        costs=[]
        while cost !=0:
            self.price +=cost 
            costs.append(cost)
            cost=int(input("Enter another cost: "))
            
    
    def advice(self, num):
        if num < 500:
            print("Low budget")
        elif num >= 500 and num < 1500:
            print("Take a flight to anywhere...")
        else:
            print("Luxury Trip!") 
            
            
    def list_inspect(self, costs):
        less_than_ten=0
        for i in costs:
            if i >= 10:
                less_than_ten +=1
        
        
        
                
                   
        