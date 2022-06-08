import random

def one_or_zero():
    return random.randint(0, 1)

result = one_or_zero()

if result == 1:
    print("1")

if result == 0:
    print("2")