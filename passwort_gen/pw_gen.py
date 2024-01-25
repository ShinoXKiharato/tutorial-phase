# Build a program that generates strong and secure passwords based on user-provided preferences.

'''info
>>>def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

>>>print (random_char(5))
>>>fxkea
'''

import random
import string

string.ascii_letters

class user_pref:
      upref = str(input("Enter a password you like to strenghen: ")).lower()
class strmnpl(user_pref): #string manipulation
    uprefrnd = random.choice(string.ascii_letters)
    print(uprefrnd)
    for i in range(1, 4):
        x = random.randint(1,15)
        y = random.randint(1,15)
        print(x,y)
def again(): # play again
    pass