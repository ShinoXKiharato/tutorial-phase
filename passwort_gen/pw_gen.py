# Build a program that generates strong and secure passwords based on user-provided preferences.

# imp note join()
# imp note lstrip() to remove smth from string
# imp note replace() to replace a substring
# imp note swapcase() swaps all case letters big to low, low to big
# imp lookup .sample() ¦ isalpnum()
import random
import string

string.ascii_letters   

<<<<<<< HEAD
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
=======

def space(**we):
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
>>>>>>> 9754e58741329573fcc36d31e44d284dec64cdf3
    else:
        quit()

display = space
p = True

while p == True:
<<<<<<< HEAD
<<<<<<< Updated upstream
    s(k='------------')
    for i in range(1, 10):
=======
=======
>>>>>>> 9754e58741329573fcc36d31e44d284dec64cdf3
    gen_pw = ""
    pw_lenght = int(input("Set new passwort lenght: "))
    u_input = input("Enter a password you like to strenghen: ")
    len_u_input = len(u_input)
<<<<<<< HEAD

    display('-' * 10)
>>>>>>> Stashed changes
=======
    display(k='------------')
>>>>>>> 9754e58741329573fcc36d31e44d284dec64cdf3

    ''' optional, modify later
    if len(u_input) <= 3 or u_input[1] == u_input[2:3]: # <----------
        while len(gen_pw) < pw_lenght:
            x = random.choice(string.ascii_letters)
            print(x,end="")
<<<<<<< HEAD
<<<<<<< Updated upstream
            x += x
    s(k="")
    s(k='------------')
=======
=======
>>>>>>> 9754e58741329573fcc36d31e44d284dec64cdf3

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


<<<<<<< HEAD
            
=======
            if u_input[::-1].lower() in result_str[-len_u_input::-1].lower() or u_input[-3::-1].lower() in result_str[-3::-1].lower():
                while rng_letter != result_str[-1:]:
                    rng_letter = random.choice(string.ascii_letters)
                    if rng_letter == result_str[-1:]:
                        break
                result_str = str(rng_letter)
                    
            elif rng_list_letter.lower() in result_str[-3::-1].lower() or rng_list_letter.lower() in result_str[-2:].lower(): 
                result_str = str(rng_letter)
            else:
                result_str = str(rng_list_letter) 
>>>>>>> 9754e58741329573fcc36d31e44d284dec64cdf3
            
            
            print(str(result_str), end="")

            gen_pw += result_str

<<<<<<< HEAD
    display('')
    display([len(gen_pw), "Characters"])
    display('-'*10)
>>>>>>> Stashed changes
=======
    display(k="")
    print(len(gen_pw), "Characters")
    display(k='------------')
>>>>>>> 9754e58741329573fcc36d31e44d284dec64cdf3
    again()