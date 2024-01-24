# I want to create a game where the user has to guess a randomly generated number within a specified range.

import random


rng = random.randint(1,11)

unum = int(input("Guess the number between 1 and 10: "))

x = True
while x == True:
    print("The correct guess was "+str(rng))
    print("You guessed "+str(unum))
    if unum == rng:
        print("You guessed the right number")
        break
    else:
        print("You guessed the wrong number!")
        break
    
