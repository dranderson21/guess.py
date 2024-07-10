import time
import random
import ctypes

def main():
    rnjesus = random.randrange(1, 1001)  # generate random number between 1 and 1000
    guess = int(input("Guess a number 1-1000: "))
    counter = 1
    start_time = time.perf_counter()  # Start the timer at the first guess

    while guess != rnjesus:
        if guess > rnjesus:
            guess = int(input("Lower: "))
        elif guess < rnjesus:
            guess = int(input("Higher: "))
        counter += 1

    end_time = time.perf_counter()  # Stop the timer when the correct number is guessed
    elapsed_time = end_time - start_time  # Calculate elapsed time
    correct_answer(rnjesus, counter, elapsed_time)

def correct_answer(number, attempts, elapsed_time):
    message = f"{number} is correct, {attempts} attempts in {elapsed_time:.2f} seconds."
    ctypes.windll.user32.MessageBoxW(0, message, "David's Guessing Game", 1)

if __name__ == "__main__":
    main()
