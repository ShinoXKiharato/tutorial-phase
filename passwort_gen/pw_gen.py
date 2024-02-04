# Build a program that generates strong and secure passwords based on user-provided preferences.

'''info
>>>def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

>>>print (random_char(5))
>>>fxkea

or

numpy.random.choice to give a unique set if you add replace=False, 

like so: numpy.random.choice(string.ascii_lowercase, size=5, replace=False)
'''
# imp note join()
# imp note lstrip() to remove smth from string
# imp note replace() to replace a substring
# imp note swapcase() swaps all case letters big to low, low to big
# imp lookup .sample() ¦ isalpnum()
import random
import string

string.ascii_letters

class user_pref:
      upref = str(input("Enter a password you like to strenghen: "))
# count lenght of user string and use lenght to create a random number int from 1 to x(how long the userstring is)
# manipulate string couple times by using random number inbetween user-string to add characters and therefore create a "better password"
      
# string slice into different parts, modify and add back together??
'''
class strmnpl(user_pref): #string manipulation
    #uprefrnd = random.choice(string.ascii_letters)
    #print(uprefrnd)
    for i in range(1, 10):
        x = random.choice(string.ascii_letters)
        y = random.randint(1,15)
        print(x, end="")
        x += x
    print(x + user_pref.upref)'''

def again(): # play again
    x = input("Again (Y/N)?: ").upper()
    if x == 'Y':
        return None
    else:
        quit()

print("")
#indexes upref steps thru with random number from 1-3.
def spc(**we):
     rslt =  ""
     for r in we.values():
         rslt += r
         print(rslt)
     return rslt
    
s = spc
p = True

while p == True:
    s(k='------------')
    for i in range(1, 4):
        zin = random.choice(string.ascii_letters)
        op = random.randint(1, 3)
        slc = user_pref.upref[::op]
        li = [zin, slc]
        pri = random.choice(li)
        if int(len(user_pref.upref)) <= 3 or user_pref.upref[1] == user_pref.upref[2:3]: # <----------
            for i in range(1, 4):
                x = random.choice(string.ascii_letters)
                #y = random.randint(1,15)
                print(x,end="")
                x += x
        print(pri, end="")
    s(k="")
    s(k='------------')
    again()
# zin to add string with the step used in slc

