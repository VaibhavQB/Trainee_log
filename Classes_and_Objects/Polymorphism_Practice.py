# A Simple code to show Pollymorphism

'''class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self) :
        print("Drive!!!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self) :
        print("Sail!!!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self) :
        print("fly!!!")

c = Car("Dodge", "Challanger")
b = Boat("Sea Ray", "Sundancer 320")
p  = Plane("Airbus","A380")

for x in (c,b,p):
    x.move()'''


# Polymorphism in All Child class from sma e Parent Class

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
    # pass
    def move(self) :
        print("Drive!!!")

class Boat(Vehicle):
    
    def move(self) :
        print("Sail!!!")

class Plane(Vehicle):
    
    def move(self) :
        print("fly!!!")

c = Car("Dodge", "Challanger")
b = Boat("Sea Ray", "Sundancer 320")
p  = Plane("Airbus","A380")

# for x in (c,b,p):
#     x.move()
[x.move() for x in (c,b,p)]