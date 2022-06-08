import random

print ("Let's roll a dice!")

pretzel = ( int(input ("How many sides should it have? (2-20).")))

def dice (answer1, answer2):
    return random.randint(answer1, answer2)


print ("It's rolling...")

print ("It's a " + str(dice(1,pretzel)) + "!")
