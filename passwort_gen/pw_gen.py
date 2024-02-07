import random
import string

string.ascii_letters   


def space(strings):
     for string in strings:
         print(string, end="")
     print()

display=("")

def again(): # play again
    play_again = input("Again (Y/N)?: ").upper()
    if play_again == 'Y':
        display("")
    else:
        quit()

display = space
p = True

while p == True:
    generated_password = ""
    password_lenght = int(input("Set new passwort lenght: "))
    user_input = input("Enter a password you like to strenghen: ")
    len_u_input = len(user_input)

    display('-' * 10)


    while len(generated_password) < password_lenght:

        rng_letter = random.choice(string.ascii_letters) 
        rng_int_input = random.randint(1, 6) if len_u_input >= 5 else random.randint(1, (3 or 4))
        rng_char_input = user_input[::rng_int_input]

        next_char = random.choice([rng_letter, rng_char_input])
        result_str = '' + next_char

        
        
        
        print(str(result_str), end="")

        generated_password += result_str

    display('')
    display([len(generated_password), " Characters"])
    display('-'*10)
    again()