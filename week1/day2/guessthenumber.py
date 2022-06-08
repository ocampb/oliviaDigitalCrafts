import random
my_random_number = random.randint(1, 10)
print   ("I am thinking of a number between 1 and 10.")

guess1 = ( int(input ("What's the number?")))



# def gameBot(guess1):
if guess1 == my_random_number: 
    print ("Yes! You win!")

if guess1 != my_random_number:
    print ("Nope, try again.")

