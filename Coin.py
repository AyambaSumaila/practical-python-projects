import random
class flipped:
    def __init__(self):
        self.sideup='Head'
    def toss(self):
        if random.randint(0, 1)==0:
            self.sideup='Heads'
        else:
            self.sideup='Tails'
    def get_sideup(self):
        return self.sidup
    