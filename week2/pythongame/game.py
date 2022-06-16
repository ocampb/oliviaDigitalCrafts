from time import sleep
import os 


class Dog:
    def __init__(self, name, energy, attention, profile):
        self.name = name
        self.energy = energy
        self.attention = attention
        self.profile = profile
    def updateEnergy(self, updateAmount):
        self.energy = self.energy + updateAmount
    def listAttentionSpan(self):
        print ("Attention Span = " + str(self.attention))
    def listEnergy(self):
        print("Energy = " + str(self.energy))
    def listProfile(self):
        print (self.profile)

Winnie = Dog("Winnie", 10, 3, "Winnie is an energetic puppy who loves chewing on bones, digging holes and playing with friends. Winnie has never met a stranger - she's friendly to all new dogs and humans. Her birthday is on August 8th and she'll be one year old! She has a high energy level but a low attention span for completing tasks. ")
Buddee = Dog("Buddee", 5, 7, "")
Rusty = Dog("Rusty", 3, 10, "")

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
    "\n"
    "Winnie is a high energy puppy and she LOVES playing with her friend Moose who lives next door."
    "\n"
    "Winnie and Moose play together at night when their parents are done working, but Winnie wants to play with Moose in the mornings too!"
    "\n")
    print(dog_ascii_4)
    print( "Help Winnie dig a hole in the fence so that she can visit Moose whenever she wants."
    "\n"
    "To accomplish this task, you'll need to spend a lot of time digging which requires a lot of energy." 
    "\n"
    "To acquire more energy, you'll need to eat food (treats, meals, stuff you find in the backyard, etc.)"
    "\n"
    "The future of Winnie's play dates with Moose depend on your success. Good luck.  "
    )


def measureHoleInitial():
    print("Using your paw, you estimate that the hole will need to be 12 paws deep in order for you to fit through and enter Moose's backyard.""\n"
    "Measuring that hole took a lot of mental energy, you lose 1 energy point.")
    Dog.updateEnergy(Winnie, -1)
    Dog.listEnergy(Winnie)
    #created as separate function to not mix class functions between Hole and Dog. 

# ASCII IMAGES:

dog_ascii_1 = """
           __
      (___()'`;
      /,    /`
      \\"--\\
"""
# print(dog_ascii_1)

dog_ascii_2= """
   / \__
  (    @\___
  /         O
 /   (_____/
/_____/   U
"""
# print(dog_ascii_2)

dog_ascii_3= """

         __
        /  \\
       / ..|\\
      (_\  |_)
      /  \@'
     /     \\
 _  /  `   |
\\/  \  | _\\
 \   /_ || \\_
  \____)|_) \_)

"""
# print(dog_ascii_3)

dog_ascii_4= """

    ___
 __/_  `.  .-\"\"\"-.
 \_,` | \-'  /   )`-')
  "") `"`    \  ((`"`
 ___Y  ,    .'7 /|
(_,___/...-` (_/_/ 
"""

# print(dog_ascii_4)

dog_ascii_5= """

          "",_o
!       ( (  _)
`\ ,,,,_'),)=~
 (          )
  ,   ,,,,  ,
  ) ,)   < (
 < <      ",\\
  ",)      "_)

"""
# print(dog_ascii_5)



## game play begins

def mainMenu ():
    print(dog_ascii_2)    
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

os.system("clear")
os.system("say \"let's play untitled dog game\"")

playgame = mainMenu()

if playgame == "1": 
    print(
        "Welcome!" "\n"
        "You'll be playing as Winnie today.""\n"
        )
if playgame == "2": 
    print(
        "Bummer!" "\n"
        "Buddee is taking a nap right now and can't play.""\n"
        )
if playgame == "3": 
        "Bummer!" "\n"
        "Rusty is taking a nap right now and can't play.""\n"
if playgame == "4": 
    os._exit(0)

os.system("clear")
print(
        "Welcome!" "\n"
        "You'll be playing as Winnie today.""\n"
        )


print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
"\n"
"\n")

print(dog_ascii_3)

############## MOVE 1 ###################

move1 = ""
def startGame():
    sleep(1)
    print ("\n"
    "Let's learn about Winnie!""\n"
     "\n")
    move1 = input( "Select an option below:""\n"
    "1 View Winnie's Character Profile""\n"
    "2 View Winnie's Attention Span""\n"
    "3 View Winnie's Energy Stats""\n"
    "4 View Winnie's Objective for Today""\n"
    "5 Let's Play!""\n"
    "\n"
    "\n"
    )
    return move1
move1 = startGame()
while move1 != "5":
    if move1 == "1":
        Dog.listProfile(Winnie)
        sleep(2)
    if move1 == "2": 
        Dog.listAttentionSpan(Winnie)
        sleep(2)
    if move1 == "3": 
        Dog.listEnergy(Winnie)
        sleep(2)
    if move1 == "4":
        os.system("clear")
        objective()
        sleep(4)
    # list1 = ["1" "2", "3", "4", "5"]
    # for number in list1: 
    #     if move1 != number:
    #         print ("Please enter your answer as a numeric value, either 1, 2, 3, 4 or 5")
    
    move1 = startGame()
    os.system("clear")

    # fix this ^ by using an array with answers and using index to indicate answer


############# MOVE 2 ##################

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
"\n")

print(dog_ascii_1)

move2 = ""
def breakfast (): 
    print("Good Morning Winnie! Your human just let you out of your crate and it's time for breakfast." "\n") 
    sleep(1)
    move2 = input (
    "What would you like to do?" "\n"
    "1 Eat the food in my bowl." "\n"
    "2 Wait and hope my human mixes in treats for extra energy.")
    return move2

move2 = breakfast()
if move2 == "1":
    Dog.updateEnergy(Winnie, 2)
    print(
       "\n""\n""Yummy breakfast, your energy increased by 3 points!")
    Dog.listEnergy(Winnie)
if move2 == "2":
    print("Uh oh. Your human reacted to your stubbornness by rolling their eyes and putting your bowl on the kitchen table.")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
"\n"
"\n"
"\n"
"\n")

print(dog_ascii_5)

move3 = ""
def backyard (): 
    move3 = input ("Your human let you out back for your morning play session. You see Moose in his backyard through the fence but can't play with him." "\n"
    "What would you like to do?" "\n"
    "1 Use your paws to measure how deep of a hole you need to dig." "\n"
    "2 Start digging your hole.""\n"
    "3 Bark at Moose through the fence. You miss your friend!""\n"
    "4 Hunt for treats in the backyard.""\n"
    "5 Leave the backyard for my nap.""\n"
    )
    return move3


while move3 != "5":
#while less than 6 inputs and when they click 5 break the loop 
    if move3 == "1": measureHoleInitial()
    if move3 == "2": 
          Hole.dig(Hole1, 3)
          Hole.measureHole(Hole1)
          Dog.updateEnergy(Winnie, -3)
    if move3 == "3":
        print ("You and Moose start barking at each other through the fence and it's SO FUN you get the zoomies. Lose 1 energy. ")
        Dog.updateEnergy(Winnie, -1)
    if move3 == "4":    
        print ("You begin your hunt near the hammock and immediately find something! You gobble it down quickly, but you suddenly feel sick which costs you energy.")
        Dog.updateEnergy(Winnie, -3)
    move3 = backyard()

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n")

move4 = ""
def lunch ():
    Dog.updateEnergy(Winnie, 3)
    print("\n""It's time for lunch and you sure are hungry! You immediately eat all of the food in your food bowl.""\n")
    Dog.listEnergy(Winnie)
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
    print("Success! You got a treat which increased your energy levels by 2 points!")
    Dog.updateEnergy(Winnie, 2)
if move4 == "2":
    print ("You missed out on a tasty treat. You're now in the backyard, ready to dig your hole.")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n")

####### MOVE 5 #########

move5 = ""
def backyard2 (): 
    move5 = input ("Your human lets you back outside for your afternoon play session." "\n"
    "What would you like to do?" "\n"
    "1 Dig as much as you can." "\n"
    "2 Hunt for treats in the backyard.""\n"
    "3 Take a nap under the hammock.""\n"
    )
    return move5

move5treats = ["1 - grass" , "2 - a stick", "3 - a treat"]

numberOfTurns = 0
while numberOfTurns < 5: 

    move5 = backyard2()

    if move5 == "1": 
        Hole.dig(Hole1, 3)
        Hole.measureHole(Hole1)
        Dog.updateEnergy(Winnie, -3)
    if move5 == "2": 
        print ("hunt for treats")
        for treat in move5treats:
            print(treat)
        treat1 = input("Which would you like to eat?")
        if treat1 == "1": 
            print("Bummer, that didn't give you any energy!")
        if treat1 == "2": 
            print("Bummer, that didn't give you any energy!")
        if treat1 == "3":
            print("Success! That treat gave you more energy.")
            Dog.updateEnergy(Winnie, 3)
    if move5 == "3":
        print ("Nap ")
        Dog.updateEnergy(Winnie, -1)
    numberOfTurns = numberOfTurns + 1

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n")

####### 

if Hole1.depth > 12: 
    print ("You win!")

if Hole1.depth == 12: 
    print ("You win!")

if Hole1.depth < 12:
    print("The sun is starting to set and your human comes outside to play." 
    "Your day is over and you're out of time to dig your hole. Your human quickly notices the hole and grabs a wheelbarrow full of dirt to fill in your progress." 
    "While you failed today, there's always tomorrow to try again!")

playgame = mainMenu()