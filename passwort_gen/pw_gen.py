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
'''
class user_pref:
      upref = str(input("Enter a password you like to strenghen: ")) # input
'''
# count lenght of user string and use lenght to create a random number int from 1 to x(how long the userstring is)
# manipulate string couple times by using random number inbetween user-string to add characters and therefore create a "better password"
      
# string slice into different parts, modify and add back together??
      


def space(**we): # s
     print_rslt =  ""
     for r in we.values():
         print_rslt += r
         print(print_rslt)
     return print_rslt

display=("")

def again(): # play again
    play_again = input("Again (Y/N)?: ").upper()
    if play_again == 'Y':
        return display(e="")
    else:
        quit()

display = space
p = True

while p == True:
    gen_pw = ""
    pw_lenght = int(input("Set new passwort lenght: "))
    u_input = input("Enter a password you like to strenghen: ")
    display(k='------------')
    ''' optional, modify later
    if len(u_input) <= 3 or u_input[1] == u_input[2:3]: # <----------
        while len(gen_pw) < pw_lenght:
            x = random.choice(string.ascii_letters)
            print(x,end="")

            gen_pw += x'''


    if len(u_input) >= 1:
        while len(gen_pw) < pw_lenght:
                
            rng_letter = random.choice(string.ascii_letters) # creates random letter.
            rng_int_input = random.randint(1, 3 or 4) # creates random integer between 1-3
            rng_char_input = u_input[::rng_int_input] # chooses every character from the user input with the step of "rng_int_input" which is between 1-3

            li_st = [rng_letter, rng_char_input, rng_letter, rng_letter, rng_char_input] # creates 60% chance for rng_letter and 40 for rng_char_input 
            rng_list_letter = random.choice(li_st) # chooses with "random.choice" one of the following in that li_st
            result_str = "" + rng_list_letter

            if rng_list_letter == result_str[-1 or -2::2 and 3 and 4]: # maybe add according to input instead of set integers? <-------------
                result_str = str(rng_letter)
            else:
                result_str = str(rng_list_letter) 
            
            print(str(result_str), end="")

            gen_pw += result_str

    display(k="")
    print(len(gen_pw), "Characters")
    display(k='------------')
    again()
    
# Add check where User input will not be visible in password, no duplicates!