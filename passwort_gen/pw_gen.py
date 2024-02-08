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
    user_input_punc = input("Would you like to add punctuations? (Y/N): ")
    user_input_num = input("Would you like to add numbers? (Y/N): ")
    len_u_input = len(user_input)

    display('-' * 10)

    char_counts = {}

    while len(generated_password) < password_lenght:
        # change so next_char will only have punctuation if Y same for digits. Probably outside of line 38? maybe if statement.

        if user_input_punc.upper() == 'Y' and user_input_num.upper() == 'Y':
            next_char = random.choice(
            [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.punctuation), random.choice(string.digits)])
        elif user_input_punc.upper() == 'Y':
            next_char = random.choice(
            [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.punctuation)])
        elif user_input_num.upper() == 'Y':
            next_char = random.choice(
            [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.digits)])
        else:
            next_char = random.choice(
            [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]])
            


        if (
            (user_input in generated_password + next_char and len(user_input) > 2)
            or (next_char.upper() in char_counts and char_counts[next_char.upper()] >= 5)
        ):
            continue

        char_counts[next_char.upper()] = char_counts.get(next_char.upper(), 0) + 1

        generated_password += next_char
        print(next_char, end="")

    display('')
    display([len(generated_password), " Characters"])
    display('-'*10)
    again()