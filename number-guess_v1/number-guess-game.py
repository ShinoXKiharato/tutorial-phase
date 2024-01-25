# I want to create a game where the user has to guess a randomly generated number within a specified range.

import random

tries = 1
pre_tries = 0
highest_tries = 0

def play_againQ():
    play_again = input("Would you like to play again? (y/n): ").upper()
    if play_again == "N":
        quit()
    else:
        return False

x = True

while x == True:
    rng = random.randint(1,10)
    unum = None
    try:
        unum = int(input("Guess the number between 1 and 10: "))
        
        print("The correct guess was: "+str(rng))
        print("You guessed: "+str(unum))
        if unum == rng:
            if tries == 1:
                print("You guessed it on your first try!")
            else:
                print("You guessed the right number")
                print("It took you "+str(tries)+" times to figure the correct number!")
            print("")
            if tries >= highest_tries:
                highest_tries = tries
            print("Current Amount: "+str(tries))
            print("Previous Amount: "+str(pre_tries))
            print("Highest Amount: "+str(highest_tries))
            pre_tries = tries
            print("")
            while play_againQ():
                break
            tries = 1
        else:
            print("You guessed the wrong number!")
            print("")
            tries += 1

    except ValueError as e:
        print("Error:")
        print("")
        print("Please enter a Number / (Integer)")
        print(e)
    finally:
        pass