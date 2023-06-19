class Vehical:
    speed=0
    def drive(self, speed):
        self.speed=speed
        print('Driving')

        def stop(self):
            self.speed=speed
            print("Stopped")

        def display(self):
            print(f"Driving at {self.speed}  speed")


#Freezer class

class Freezer:
    temp=0
    def freeze(self, temp):
        self.temp=temp
        print("Freezing")

    def display(self):
        print( "Freezing at {self.temp} temp")


#Freezer Truck class

class FreezerTruck(Freezer, Vehical):
  def display(self):
      print(f:Is a freezer)
t=FreezerTruck()
t.drive(58)
t.freeze(-30)
print('  -   ' *20)

t.display()