import time
import random
import ctypes

rnjesus = (random.randrange(1, 1000, 1))

def correct_answer():
    if int(guess) == (rnjesus):
        ctypes.windll.user32.MessageBoxW(0, str(rnjesus) + " is correct, " + str(counter) + " attempts in " + str(time.perf_counter()) + " seconds" "", "David's Guessing Game", 1)

guess = int(input("Guess a number 1-1000: "))
counter = 1

while int(guess) != (rnjesus):
    if int(guess) > (rnjesus):
        guess = int(input("Lower: "))
        counter = counter + 1
    elif int(guess) < (rnjesus):
        guess = int(input("Higher: "))
        counter = counter + 1

correct_answer()
