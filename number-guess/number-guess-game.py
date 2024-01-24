# I want to create a game where the user has to guess a randomly generated number within a specified range.
# add leaderboard, high-score system
# add condition if first try print different message,

import random

counter = 0
x = True

while x == True:
    rng = random.randint(1,10)
    unum = None
    try:
        unum = (input("Guess the number between 1 and 10: "))

        if unum == int:
            print("The correct guess was "+str(rng))
            print("You guessed "+str(unum))
            if unum == rng:
                if counter == 0:
                    print("You guessed it on your first try!")
                else:
                    print("You guessed the right number")
                    print("It took you "+str(counter)+" times to figure the correct number!")
                x = False
            else:
                print("You guessed the wrong number!")
                counter += 1
        else:
            print("Error:")
            print("")
            print("Please enter a Number / (Integer)")
            print("")
    finally:
        pass