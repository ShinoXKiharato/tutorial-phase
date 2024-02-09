# Password Generator Documentation
Correleated to the Python programm PW_Gen.py

## Checklist

- [x] Manipulate string couple times by using random integers inbetween user-string to add characters and therefore create a "better password"

- [x] Add check where User input will not be visible in password, no duplicates!

- [x] Make Each password look individual af.

- [x] (Optional) Add numbers and punctuation to the generator.

- [x] Add Error handling

- [x] Add percentage chance based on lenght_input (Variation)
    - [x] Added percentage chance.x

- I have no idea what to add.

---

## Raw Code

```python
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

        if user_input_punc.upper() == 'Y' and user_input_num.upper() == 'Y':
            choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.punctuation)
             , random.choice(string.digits)]
            weights = [0.4 if password_lenght >= 12 else 0.5, 0.5 if password_lenght >= 12 else 0.4, 0.25 if password_lenght >= 12 else 0.55, 0.25 if password_lenght >= 12 else 0.55]
            next_char = random.choices(choices, weights=weights)[0]

        elif user_input_punc.upper() == 'Y':
            choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.punctuation)]
            weights = [0.45 if password_lenght >= 12 else 0.5, 0.5 if password_lenght >= 12 else 0.435, 0.3 if password_lenght >= 12 else 0.55]
            next_char = random.choices(choices, weights=weights)[0]
        elif user_input_num.upper() == 'Y':
            choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]
             , random.choice(string.digits)]
            weights = [0.45 if password_lenght >= 12 else 0.58, 0.5 if password_lenght >= 12 else 0.45, 0.3 if password_lenght >= 12 else 0.525]
            next_char = random.choices(choices, weights=weights)[0]
        else:
            choices = [random.choice(string.ascii_letters) if random.choice(string.ascii_letters) != generated_password[-1:] else random.choice(string.ascii_letters)
             , user_input[::random.randint(1, (6 or 8)) if len_u_input >= 5 else random.randint(1, (2 or 3))]]
            weights = [0.65 if password_lenght >= 8 else 0.55, 0.5 if password_lenght >= 8 else 0.6]
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

```
# Breakdown

## Prep-Work
>* Import Libaries `string` and `random`
>* Define function `space()` and `again()`
>    * `space()` is basically print()
>    * `again()` call to be asked to re-iterate thru the loop again or quit
>    * Set address for `display` to `space()` function.

## Main Code

><sub>Top to bottom</sub>
> ## Outer Loop
> * Set `p` equal to `True`
> * Create infinite `while` loop with `p == True`
>> * Variable `generated_password` set to `""`
>> * Variable `password_lenght` set to 0
>> * Variable `valid_input` set to `False`
> ## User Input + Var
>> * `while` `valid_input` is negative (`False`)
>>> * `Try` to ask for integer `password_lenght` if it works continue line and set `valid_input` to `True` (break loop)
>>> * `except` condition for ValueError to ask user for a integer and re-iterate thru the loop.
>>
>> * Asks for a favorable word as input that will be used in the password. (`user_input_**`)
>>
>> * Asks for if the user wants puncuation and or numbers in their password. (Y/N)
>>
>> * Create variable for the lenght of the favorable word. (`user_input`)
>>
>> * Calls `display` (`space()`) to print 10 times `-`
>>
>> * Create list called `char_counts`
> ## Random.Generator
>> * `while` lenght of the `generated_password` is less than `password_lenght`
>>> I have created different variations of the same pattern, which is why i will explain only the one that contains all of them. 
>>> * `if` input.upper() on punctuation is equal to `Y` and numbers.
>>>
>>> Created a list called `choices`
>>>> ---
>>>> #### Choices
>>>> 1. `random.choice(string.ascii_letters)` selects a random ascii letter **`IF`** it is not equal to the last letter appended in the final result `generated_password`, `else` it will try again.
>>>>
>>>> 2. `user_input[::random.randint(1, (6 or 8))]` selects a random character from the users input with a randomised step between 1 and (6 or 8) **`IF`** the lenght of the `user_input` is bigger than 5, `else` the step is random between 1, (2 or 3).
>>>>
>>>> 3. randomly chooses from punctuation list.
>>>> 4. randomly chooses from number list.
>>>  ---
>>>  Created a list called `weights` that will act as percentage giver.
>>>> ---
>>>> #### Weights
>>>> 1. 40% `if` password_lenght is bigger than or equal to 12, `else` 50%
>>>> 2. 50% `if` password_lenght is bigger than or equal to 12, `else` 40%
>>>> 3. 25% `if` password_lenght is bigger than or equal to 12, `else` 55%
>>>> 4. 25% `if` password_lenght is bigger than or equal to 12, `else` 55%
>>>> ---
>>> Create variable called `next_char` to determine the next character for the iteration.
>>>> ---
>>>> * `random.choices` with (`choices`, `weights=weights`)[0] < this will takes 2 arguments to make a weightened random selection.
>>>>
>>>> * [0] This part selects the first element from the result of `random.choices`
>>>> * If no weights applied, all elements have equal chance to be selected.
>>> ---
>>> Note: Numbers vary in each `if` and `elif` statement.
>
> ## No Duplicates
>> `if` statement to make sure that the users input itself doesn't occur in the generated password.
>>> First condition
>>> * `user_input in generated_password + next_char and len(user_input) > 2`
>>> * This checks if the `user_input` string (the password the user wants to strengthen) appears within the already generated password (`generated_password`) combined with the potential next character (`next_char`). 
It also ensures the `user_input` length is greater than 2, allowing up to 2 character matches.
>>>
>>> Second condition
>>> * `next_char.upper() in char_counts and char_counts[next_char.upper()] >= 5:`
>>> * This checks if the uppercase version of the next character (`next_char.upper()`) already exists in the `char_counts` dictionary.
>>> * It also checks if the count for that character in the dictionary is greater than or equal to 5.
>>>
>> If any of these violate the desired limits set, it will use `continue` to skip the rest of the iteration and re-iterate to basically try again.
>>
>> Furthermore
>>> `char_counts[next_char.upper()] = char_counts.get(next_char.upper(), 0) + 1:`
>>>
>>>---
>>> * It retrieves the count for the uppercase version of `next_char` from the dictionary (or 0 if it doesn't exist).
>>> * It then increments the count by 1 and updates the corresponding value in the dictionary.
>>>
>>>This keeps track of how many times each character has appeared in the generated password so far.
>>---
>> Lastly `generated_password `+=` next_char` will append `next_char` to the `generated_password` string.
>> 
>> `print(next_char, end="")`
>> * Prints the character for each iteration on the same line
>
> * Calls `display('')` to continue next line
> * Calls `display([len(generated_password), " Characters"])`
>   * Displays the lenght of the final generated password.
> * Calls `display('-'*10)` to display - 10 times
> * Calls `again()` function
> ---

