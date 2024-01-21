# Quiz Game

>This is my attempt to describe and explain the Quiz Game made in my 12 Hour Course journey.

This *quiz* involved four questions with four possible answers each.

The code read each user guess and generated a score based on it in percentage(%).

#### Q&A
---

```python
questions = {
    "Who created Python?: ": "B",
    "What year was Python created?: ": "C",
    "Python is tributed to which comedy group?: ": "B",
    "Is the Earth round?: ": "A"
}

options = [["A. Elon Musk", "B. Guido van Rossum", "C. Bill Gates", "D. Mark Zuckerburg"], # 0
          ["A. 1964", "B. 2004", "C. 1991", "D. 2011"], # 1
          ["A. Lonely Island", "B. Monty Python", "C. PyZue", "D. Queton"], # 2
          ["A. True", "B. False", "C. Sometimes", "D. Earth isn't a planet"]] # 3
```
I created a list called `questions` and a `2D List` called `options`.

In the list `questions`, I listed four questions, each with its own `key` representing the correct answer for that question.

In the **2D list**, I wrote four lists, each containing four answers separated by commas. Each list represented a different question in the quiz.

### Main
---

```python
new_game()
while play_again():
    new_game()

print("bye bye")
```
The **new_game()** function was called, and if the game was finished, it would ask the user if they wanted to play again.

This was simply done using a **while** loop in which I called the `play_again` function that returned a boolean value (`True` or `False`). Within the loop, I called the `new_game` function to restart the code.

If the value is false, proceed and end with _"bye bye"._

### Functions (new_game)
---

I first defined the function `new_game()`.

```python
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Enter (A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)
```
First, I declared an empty list called `guesses` to store the user's guesses. I also declared a variable called `correct_guesses` that initially held a value of 0, indicating that the user had not made any correct guesses yet.

I further set a variable called `question_num` to 1 to represent the first question.

---

I used a `for` loop to print all questions with the `print(key)` statement.

I also had to display all options. I did that with a `nested for loop`.

```python
for i in options[question_num-1]:
            print(i)
```
I then called the `options` list and used the `question_num` variable as a counter to iterate through each option for each question separately. Since `question_num` was initialized to 1, I simply set the starting index to -1 to ensure the loop started at the beginning of the list.

To progress through all options for all questions, I incremented `question_num` by 1 within the loop. This allowed me to access all options for each question in sequence.

This is the incrementation:
```python
question_num += 1
```
---

I also had to get the users "guess".
```python
guess = input("Enter (A,B,C or D): ")
```
I created a variable called `guess`. I then asked the user to enter one of the following options: `A`, `B`, `C`, or `D`. 

Since strings are case-sensitive, I ensured that the input would be received in uppercase.
```python
guess = guess.upper()
```
---
To display the user's guesses at the end of the game, I accessed the empty list `guesses` that was created earlier.

```python
guesses.append(guess)
```
---
Next, I tried to check if the user's answer was right.
```python
correct_guesses += check_answer(questions.get(key),guess)
```
Here i used `correct_guesses` to add and assign the function `check_answer`. 
> If answer is correct, it will add +1 to the score from the `check_answer` function.

The `check_answer` function passes in the correct answer (`questions.get(key)`) and the user's guess (`guess`).

**Those 2 arguments will be later used in the corresponding function.**


---
>Since all of this is still in the inner `for` loop, it will automatically iterate thru each question/answer.

---
I ended the outer `for` loop with:
```python
display_score(correct_guesses, guesses)
```
I called the `display_score` function and passed in both correct "answers" and the users guesses.

#### Functions (check_answer)
---
```python
def check_answer(answer,guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("Wrong!")
        return 0
```

I used the arguments from earlier
> (questions.get(key)) == answer

> guess == guess

Furthermore, I set an `if` statement to determine if the `answer` was equal to the user's `guess`.

If the `answer` matched the `guess`, a "correct" message was displayed, and the value `1` was returned. This value was then utilized to increase the `correct_guesses` score.

In the opposite case, a value of `0` was returned, and the message "Wrong!" was printed.

#### Functions (display_score)
---

```python
def display_score(correct_guesses, guesses):
    print("-----------------")
    print("RESULTS")
    print("-----------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
```

Here i defined the `display_score` function and recalled the 2 arguments `correct_guesses` and `guesses` into my parameter.

Furthermore, I decided to display both the answers and the user's guesses separately. I started by printing "Answers: " and added the parameter `(,end= "")` to prevent a new line break.

Next, I used a `for` loop to iterate through all the keys in the `questions` and `guesses` lists, assigning each key to the variable `i`. To get the corresponding value for each key, I used `questions.get(i)`, which returns the value associated with the key `i` in the `questions` dictionary. *This allowed me to print both the question keys (answers) and the user's guesses for each question.*

#### Functions (play_again)
---

```python
def play_again():
    
    response = input("Do you want to play again? (y/n): ").upper()
    if response == "Y":
        return True
    else:
        return False
```

To allow users to play the quiz again, I created a function called `play_again()`. This function asked the user if they would like to play again by prompting them with the message "Would you like to play again? (Y/N)". I appended `.upper()` to the `input` to ensure the user's response would be converted to uppercase letters.

Next, I incorporated an `if` statement to evaluate whether the user's response (`response`) was equal to "Y". If it was, the function returned `True`, indicating the user's desire to play again. Otherwise, it returned `False`, indicating the user's decision to end the game.

---
