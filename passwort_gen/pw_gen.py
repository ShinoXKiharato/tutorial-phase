# Build a program that generates strong and secure passwords based on user-provided preferences.

import random

class user_pref:
    upref = str(input("Enter a password you like to strenghen: "))
    upref = upref.lower()

class strmnpl(user_pref): #string manipulation
    uprefrnd = random.randint(0,15)
    
    print(uprefrnd)


def again(): # play again
    pass

print(user_pref())