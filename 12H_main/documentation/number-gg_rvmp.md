# NGG Doc

> Documentation (revamp) about my number guessing game.



```python
import random

tries = 1
pre_tries = 0
highest_tries = 0

def play_againQ():
    play_again = input("Would you like to play again? (y/n): ").upper()
    if play_again == "N":
        quit()
    else:
        return False

x = True
```
- Importing random module
- assign values to 3 variables.
- define function play_againQ()
    - Function asks if player would like to play again + sets it uppercase
- Assign True to `x`

---

#### Actual Code
```python
while x == True:
    rng = random.randint(1,10)
    unum = None
    try:
        unum = int(input("Guess the number between 1 and 10: "))
        
        print("The correct guess was: "+str(rng))
        print("You guessed: "+str(unum))
        if unum == rng:
            if tries == 1:
                print("You guessed it on your first try!")
            else:
                print("You guessed the right number")
                print("It took you "+str(tries)+" times to figure the correct number!")
            print("")
            if tries >= highest_tries:
                highest_tries = tries
            print("Current Amount: "+str(tries))
            print("Previous Amount: "+str(pre_tries))
            print("Highest Amount: "+str(highest_tries))
            pre_tries = tries
            print("")
            while play_againQ():
                break
            tries = 1
        else:
            print("You guessed the wrong number!")
            print("")
            tries += 1

    except ValueError as e:
        print("Error:")
        print("")
        print("Please enter a Number / (Integer)")
        print(e)
    finally:
        pass
```

---

### Breakdown
#### While
[
- The `while` loop works as long `x` is equal to `True`.
- Set random integer from 1 to 10 to `rng`.
- Set `unum` to nothing
---
> ### Try
> - Ask for integer user input "Guess a number .. 1-10" in `unum`
> - Print Correct guess
> - Print Users guess 
>> - `If` `unum` is equal to `rng`
>>> - `If` `Tries` is equal to **1** 
>>>      - prints message
>>> - `else` prints message + amount of tries
>> ---
>>> - `If` current `tries` is bigger than or equal to highest amount of `tries`
>>>      - Set highest `tries` to current `tries`
>>> - Print all variations of `tries` as string.
>>> - set `pre_tries` to current `tries`-
>> ---
>>> - Call `play_againQ()` function in `while` loop.
>>>      - break out of `while` loop
>>> - Reset `Tries` to 1
>> - `else` if user guessed wrong number print message +
>> - add + 1 to `tries`
> - `Exception ValueError as e` to print several messages.
> - End `Try` with `Finally`+`pass`.

]

---
<img src="https://media.discordapp.net/stickers/1014098155702325288.webp?size=240" width="300" height="300">
