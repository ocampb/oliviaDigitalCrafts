import random

print ("Let's roll a dice!")

pretzel = ( int(input ("How many sides should it have? (2-20).")))

def dice (answer1, answer2):
    return random.randint(answer1, answer2)


print ("It's rolling...")

print ("It's a " + str(dice(1,pretzel)) + "!")


### Step 1
# Write a function named dice that takes two numbers as arguments

### Step 2
# The function should RETURN a random number between the 2 arguements

### Step 3 
# Ask the user to select a number between 2 and 20

### Step 4 
# Save the user's answer above to a variable called result

### Step 5
# invoke the dice function with the following parameters: 1 & result

