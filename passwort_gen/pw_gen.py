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
    password_lenght = 0
    valid_input = False

    while not valid_input:
        try:
            password_lenght = int(input("Set new passwort lenght: "))
            valid_input = True
        except ValueError:
            print("Enter a Number")

    user_input = input("Enter a word you would like to use: ")
    user_input_punc = input("Would you like to add punctuations? (Y/N): ")
    user_input_num = input("Would you like to add numbers? (Y/N): ")

    len_u_input = len(user_input)

    display('-' * 10)

    char_counts = {}

    while len(generated_password) < password_lenght:    
        # change so next_char will only have punctuation if Y same for digits. Probably outside of line 38? maybe if statement.

        if user_input_punc.upper() == 'Y' and user_input_num.upper() == 'Y':
            choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.punctuation)
             , random.choice(string.digits)]
            weights = [0.4, 0.5, 0.25, 0.25]
            next_char = random.choices(choices, weights=weights)[0]

        elif user_input_punc.upper() == 'Y':
            choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.punctuation)]
            weights = [0.45, 0.5, 0.3]
            next_char = random.choices(choices, weights=weights)[0]
        elif user_input_num.upper() == 'Y':
            choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.digits)]
            weights = [0.45, 0.5, 0.3]
            next_char = random.choices(choices, weights=weights)[0]
        else:
            choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]]
            weights = [0.65, 0.5]
            next_char = random.choices(choices, weights=weights)[0]

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

    '''
    password_lenght = (input("Set new passwort lenght: "))
        if password_lenght != int(password_lenght):
            raise Exception("")
        while password_lenght != int(password_lenght):
            password_lenght = (input("Set new passwort lenght: "))
            if password_lenght == int(password_lenght):
                break
            '''