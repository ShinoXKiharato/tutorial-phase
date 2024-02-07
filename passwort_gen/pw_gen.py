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

<<<<<<< Updated upstream
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
=======

def space(strings):
     for string in strings:
         print(string, end="")
     print()

display=("")

def again(): # play again
    play_again = input("Again (Y/N)?: ").upper()
    if play_again == 'Y':
        display("")
>>>>>>> Stashed changes
    else:
        quit()

print("")

def spc(**we):
     rslt =  ""
     for r in we.values():
         rslt += r
         print(rslt)
     return rslt
    
s = spc
p = True
rslt = 0
# if int(len(rslt)) != 10:
while p == True:
<<<<<<< Updated upstream
    s(k='------------')
    for i in range(1, 10):
=======
    gen_pw = ""
    pw_lenght = int(input("Set new passwort lenght: "))
    u_input = input("Enter a password you like to strenghen: ")
    len_u_input = len(u_input)

    display('-' * 10)
>>>>>>> Stashed changes

        zin = random.choice(string.ascii_letters)
        op = random.randint(1, 3)
        slc = user_pref.upref[::op]

        li = [zin, zin, zin, slc]
        pri = random.choice(li)
        #rslt = len(pri+zin)
        print(pri,end="")
    if int(len(user_pref.upref)) <= 3 or user_pref.upref[1] == user_pref.upref[2:3]: # <----------
        for i in range(1, 4):
            x = random.choice(string.ascii_letters)
            #y = random.randint(1,15)
            print(x,end="")
<<<<<<< Updated upstream
            x += x
    s(k="")
    s(k='------------')
=======

            gen_pw += x'''


    if len(u_input) >= 1:
        while len(gen_pw) < pw_lenght:

            rng_letter = random.choice(string.ascii_letters) 
            rng_int_input = random.randint(1, 3 or 4)
            rng_int_input2 = lambda rng_int_input:random.randint(1, 6) if len_u_input >= 5 else False
            rng_char_input = u_input[::rng_int_input or rng_int_input2]

            li_st = [rng_letter, rng_char_input, rng_letter, rng_letter, rng_char_input]
            rng_list_letter = random.choice(li_st)
            result_str = "" + rng_list_letter


            
            
            
            print(str(result_str), end="")

            gen_pw += result_str

    display('')
    display([len(gen_pw), "Characters"])
    display('-'*10)
>>>>>>> Stashed changes
    again()