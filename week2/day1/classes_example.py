class User:
    def __init__(self, name, height, weight, siblings, greeting):
        self.name = name
        self.height = height
        self.weight = weight
        self.siblings = siblings
        self.greeting = greeting

Olivia = User("Olivia", "5.4", "150 pounds", ["Mary Ellen", "Jake", "Taylor"], "Hi")

if Olivia.greeting == "Hi":
    print("yes")

for sibling in Olivia.siblings:
    print(sibling)

