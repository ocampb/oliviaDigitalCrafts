
def flipCoin():
     print("You flipped a coin!")

flipCoin()

import random
def one_or_zero():
    return random.randint(0, 1)

one_or_zero()
result = one_or_zero()

def naming():
    if result == 1:
        return 'It is heads.'
    if result == 0:
        return "It is tails."

print(naming())