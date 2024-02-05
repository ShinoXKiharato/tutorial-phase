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
      upref = str(input("Enter a password you like to strenghen: ")) # input

# count lenght of user string and use lenght to create a random number int from 1 to x(how long the userstring is)
# manipulate string couple times by using random number inbetween user-string to add characters and therefore create a "better password"
      
# string slice into different parts, modify and add back together??
      
def again(): # play again
    x = input("Again (Y/N)?: ").upper()
    if x == 'Y':
        return None
    else:
        quit()

print("")

def spc(**we): # s
     rslt =  ""
     for r in we.values():
         rslt += r
         print(rslt)
     return rslt
    
s = spc
g = True
p = True
rslt = 0
bepe = ""
# if int(len(rslt)) != 10:

while p == True:

    if len(user_pref.upref) <= 3 or user_pref.upref[1] == user_pref.upref[2:3]: # <----------
        s(k='------------')
        while len(bepe) < 9:
            x = random.choice(string.ascii_letters)
            print(x,end="")

            bepe += x
        again()


    if len(user_pref.upref) >= 1:
        s(k='------------')
        while len(bepe) < 9:
                
            zin = random.choice(string.ascii_letters)
            op = random.randint(1, 3)
            slc = user_pref.upref[::op]

            li = [zin, zin, zin, slc, slc]
            pri = random.choice(li)
            bep = str(pri + zin)
            
            print(str(bep), end="")
            bepe += bep
        s(k="")
        s(k='------------')
        again()


'''
    if len(user_pref.upref) >= 1:
        for i in range(1, 5):
            
            zin = random.choice(string.ascii_letters)
            op = random.randint(1, 3)
            slc = user_pref.upref[::op]

            li = [zin, zin, zin, slc, slc]
            pri = random.choice(li)
            bep = str(pri + zin)
            #rslt = len(pri+zin)

            rslt = len(bep)
            print(str(bep), end="")
    elif (rslt == 10):
            break'''
