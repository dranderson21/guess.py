def main():

    import random

    rnjesus = (random.randrange(1, 1000, 1))

    def correct_answer():
        if int(guess) == (rnjesus):
            print("Correct! " + str(rnjesus) + " is the number!")
            print("It took you " + str(counter) + " attempts.")

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
    
    again = input("Play Again? (y/n): ")
    if again == "y":
        main()
    elif again == "n":
        print("Closing Application...")
    else:
        print("Invalid Entry. Closing Application...")
    
main()
