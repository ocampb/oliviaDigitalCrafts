# Inheritance 

class Employee:
    def __init__(self, name, department, role):
        self.name = name 
        self. department = department
        self.role = role 

# 3 classes >> parent, child and sibling


class Parent:
    def __init__(self,lastName,eyeColor,height):
        self.lastName = lastName
        self.eyeColor = eyeColor
        self.height = height
    def eating(self):
        print("I'm going to eat dinner.'")

class Child(Parent):
    def __init__(self,lastName,eyeColor,height,favoriteGame):
        super().__init__(lastName,eyeColor,height)
        self.favoriteGame = favoriteGame
    def gaming (self):
        print ("I'm going to play Settlers of Catan.")

class Sibling(Parent):
    def __init__(self,lastName,eyeColor,height,favoriteCandy):
        super().__init__(lastName,eyeColor,height)
        self.favoriteCandy = favoriteCandy
    def eatingCandy (self):
        print ("I'm going to eat a Snickers Bar.")

 
JamesPotter = Parent("Potter", "Brown", "5.10")
HarryPotter = Child("Potter", "Green", "5.7", "Quidditch")
SiriusPotter = Sibling("Black", "Blue", "6.1", "Chocolate Frogs")

JamesPotter.eating()
