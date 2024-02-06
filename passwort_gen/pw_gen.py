# Build a program that generates strong and secure passwords based on user-provided preferences.

# imp note join()
# imp note lstrip() to remove smth from string
# imp note replace() to replace a substring
# imp note swapcase() swaps all case letters big to low, low to big
# imp lookup .sample() ¦ isalpnum()
import random
import string

string.ascii_letters   


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

            rng_letter = random.choice(string.ascii_letters) 
            rng_int_input = random.randint(1, 3 or 4)
            rng_int_input2 = lambda rng_int_input:random.randint(1, 6) if len(u_input) >= 5 else None
            rng_char_input = u_input[::rng_int_input or rng_int_input2]

            li_st = [rng_letter, rng_char_input, rng_letter, rng_letter, rng_char_input]
            rng_list_letter = random.choice(li_st)
            result_str = "" + rng_list_letter

            if rng_list_letter == result_str[-1 or -2::2 and 3 and 4]: 
                result_str = str(rng_letter)
            else:
                result_str = str(rng_list_letter) 
            
            print(str(result_str), end="")

            gen_pw += result_str

    display(k="")
    print(len(gen_pw), "Characters")
    display(k='------------')
    again()