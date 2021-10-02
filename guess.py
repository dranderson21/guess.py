import random

rnjesus = (random.randrange(1, 100, 1))

def correct_answer():
    if int(guess) == (rnjesus):
        print("Correct! " + str(rnjesus) + " is the number!")

guess = int(input("Guess a number 1-100: "))

while int(guess) != (rnjesus):
    if int(guess) > (rnjesus):
        guess = int(input("Lower: "))
    elif int(guess) < (rnjesus):
        guess = int(input("Higher: "))

correct_answer()
