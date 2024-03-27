class App:
    def __init__(self, users, storage, userName):
        self.users=users
        self.storage=storage 
        self.userName=userName
        
    
    def login(self): 
        if self.userName =="owner" and self.users >=1:
            print("Welcome ", self.userName)
            print("Your storage is : ", self.storage)
        
        else:
            print("You are not a user!")
            
            
    
    def increase_capacity(self, number):
        self.storage +=number 
        print("Updated storage ", self.storage)
        
        
        
        
    def check_update(self):
        if self.users >= self.storage:
            upgrade_amt=int(input("Upgrade amount: "))
            self.storage +=upgrade_amt
        else:
            print("You still have: ", (str(self.storage - self.users), "Spaces open"))
             
            
            
product_one=App(12, 33, "owner")
product_one.login()
product_one.increase_capacity(234)

print()
product_two=App(10, 11, "Kent")
product_two.login()

