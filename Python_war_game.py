
import random

#Game variables:
deck=10

class Player:
    
    def __init__(self, name):
        self.name=name
        self.points=0
        self.cards=list(range(1, deck+1, 1))
        random.shuffle(self.cards)
        
    def pick_card(self, ):
        picked_card=self.cards[0]
        self.cards.remove(picked_card)
        print(f"{self.name} card is {picked_card}")
        return picked_card
    
    def add_point(self):
        self.points +=1
        print(f"A point has been added to {self.name}")
p=Player(name="Player 1")

p2=Player(name="Player 2")

print("\t\t\t\tGame Starts ....")
while True:
    input("\t\t\tPress enter to pick a card!")
    p_card=p.pick_card()
    p2_card= p2.pick_card()
    
    if p_card>p2.card:
       p.add_point()
       
    elif p2_card>p_card:
       p2.add_point()
    else:
        print("Tie")
   
    







""""
p.pick_card()
p2.pick_card()
print(len(p.cards))
print(len(p2.cards))

"""