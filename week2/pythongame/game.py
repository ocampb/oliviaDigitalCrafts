from time import sleep

class Dog:
    def __init__(self, name, energy, attention):
        self.name = name
        self.energy = energy
        self.attention = attention
    def updateEnergy(self, updateAmount):
        self.energy = self.energy + updateAmount
        print("Energy is now:" + str(self.energy))
    def listStats(self):
        print("Energy = " + str(self.energy)) 
        print ("Attention Span = " + str(self.attention))

Winnie = Dog("Winnie", 10, 3)
Buddee = Dog("Buddee", 5, 7)
Rusty = Dog("Rusty", 3, 10)

class Hole:
    def __init__(self, depth):
        self.depth = depth
    def dig(self, updatedDepth):
        self.depth = self.depth + updatedDepth
    def measureHole(self):
        print("Hole Depth:" + str(self.depth))

Hole1 = Hole(0)


def objective():
    print("Winnie's Objective:"
    "\n"
    "Winnie is a high energy puppy and she LOVES playing with her friend Moose who lives next door."
    "\n"
    "Winnie and Moose play together at night when their parents are done working, but Winnie wants to play with Moose in the mornings too!"
    "\n"
    "Help Winnie dig a hole in the fence so that she can visit Moose whenever she wants."
    "\n"
    "To accomplish this task, you'll need to spend a lot of time digging which requires a lot of energy." 
    "\n"
    "Winnie's energy tank has a high capacity, but she is young and doesn't have a long attention span so you won't be able to dig for very long before she gets distracted."
    "\n"
    "To acquire more energy, you'll need to eat food (treats, meals, stuff you find in the backyard, etc.)"
    "\n"
    "The future of Winnie's play dates with Moose depend on your success. Good luck.  "
    )

def measureHoleInitial():
    print("Using your paw, you estimate that the hole will need to be 12 paws deep in order for you to fit through and enter Moose's backyard."
    "Measuring that hole took a lot of mental energy, you lose 1 energy point.")
    Dog.updateEnergy(Winnie, -1)
    Dog.listStats(Winnie)


## game play begins

def mainMenu ():
    playgame = input( 
        "\n"
        "Let's play Untitled Dog Game!""\n"
        "\n"
        "1 Play as Winnie""\n"
        "2 Play as Buddee""\n"
        "3 Play as Rusty""\n"
        "4 Quit""\n"
        "\n")
    return playgame

playgame = mainMenu()

if playgame == "1": 
    print(
        "Welcome!" "\n"
        "You'll be playing as Winnie today.""\n"
        )

move1 = ""
def startGame():
    move1 = input( 
    "\n"
    "To get started, let's learn about Winnie and the objective:""\n"
     "\n"
     "1 View Winnie's Stats""\n"
     "2 View Winnie's Goal for Today"
      "\n")
    return move1

move1 = startGame()
if move1 == "1":
    print("Winnie Stats:" "\n")
    Dog.listStats(Winnie)
if move1 == "2":
    objective()

move1 = startGame()
if move1 == "1":
    print("Winnie Stats:" "\n")
    Dog.listStats(Winnie)
if move1 == "2":
    objective()

move2 = ""
def breakfast (): 
    print("Good Morning Winnie! Your human just let you out of your crate and it's time for breakfast." "\n") 
    sleep(2)
    move2 = input (
    "What would you like to do?" "\n"
    "1 Eat the food in my bowl." "\n"
    "2 Wait and hope my human mixes in treats for extra energy.")
    return move2

move2 = breakfast()
if move2 == "1":
    Dog.updateEnergy(Winnie, 2)
    print("Yummy breakfast, your energy increased by 3 points!")
    Dog.listStats(Winnie)
if move2 == "2":
    print("Uh oh. Your human reacted to your stubbornness by rolling their eyes and putting your bowl on the kitchen table.")

move3 = ""
def backyard (): 
    move3 = input ("Your human let you out back for your morning play session. You see Moose in his backyard through the fence but can't play with him." "\n"
    "What would you like to do?" "\n"
    "1 Use your paws to measure how deep of a hole you need to dig." "\n"
    "2 Start digging your hole without measuring.""\n"
    "3 Bark at Moose through the fence. You miss your friend!""\n"
    "4 Hunt for treats in the backyard.""\n"
    "5 Leave the backyard for my nap.""\n"
    )
    return move3

move3 = backyard()
# while move3 != "5":
#while less than 6 inputs and when they click 5 break the loop 
if move3 == "1": measureHoleInitial()
if move3 == "2": 
    Hole.dig(Hole1, 2)
    Hole.measureHole(Hole1)
    Dog.updateEnergy(Winnie, -3)
if move3 == "3":
    print ("You and Moose start barking at each other through the fence and it's SO FUN you get the zoomies. Lose 1 energy. ")
    Dog.updateEnergy(Winnie, -1)
if move3 == "4": 
    print ("You begin your hunt near the hammock and immediately find something! You gobble it down quickly, but you suddenly feel sick which costs you energy.")
    Dog.updateEnergy(Winnie, -3)

move4 = ""
def lunch ():
    print("It's time for lunch and you sure are hungry! You immediately eat all of the food in your food bowl.")
    move4 = input( 
    "\n"
    "What are you going to do now?"
    "\n"
    "\n"
    "1 Stand by the container of treats and beg.""\n"
    "2 Stand by the backdoor to go back outside."
      "\n")
    return move4

move4 = lunch()
if move4 == "1": 
    print("Success! You got a treat which increased your energy levels.")
    #insert function to increase energy levels
if move4 == "2":
    print ("You missed out on a tasty treat. You're now in the backyard, ready to dig your hole.")

move5 = ""
def backyard2 (): 
    move5 = input ("Your human lets you back outside for your afternoon play session. It starts raining which softens the dirt near the fence - great conditions to complete your hole!" "\n"
    "What would you like to do?" "\n"
    "1 Dig as much as you can." "\n"
    "2 Hunt for treats in the backyard.""\n"
    "3 Take a nap under the hammock.""\n"
    )
    return move5

move5 = backyard2()

if move5 == "1": 
    Hole.dig(Hole1, 2)
    Hole.measureHole(Hole1)
    Dog.updateEnergy(Winnie, -3)
if move5 == "2": 
    print ("hunt for treats")
if move5 == "3":
    print ("Nap ")
    Dog.updateEnergy(Winnie, -1)

if Hole1.depth > 12: 
    print ("You win!")

if Hole1.depth == 12: 
    print ("You win!")

if Hole1.depth < 12:
    print("The sun is starting to set and your human comes outside to play." 
    "Your day is over and you're out of time to dig your hole. Your human quickly notices the hole and grabs a wheelbarrow full of dirt to fill in your progress." 
    "While you failed today, there's always tomorrow to try again!")

