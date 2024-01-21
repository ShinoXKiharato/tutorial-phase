# Quiz Game

>This is my attempt to describe and explain the Quiz Game made in my 12 Hour Course journey.

This *quiz* Involves 4 questions with 4 possible answers each.

The code reads each user guess and generates a score based on it in %.

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

In the list `questions` i list 4 questions that each has it's own `key` which represents the answer for each question.

In the `2D List` i write 4 lists that each has 4 "answers seperated with `,`.

### Main
---

```python
new_game()
while play_again():
    new_game()

print("bye bye")
```
The function `new_game()` is being called and if the game is finished it will ask the user if they want to play again. 

This is simply done with a `while` loop where i call the function `play_again` that will return a boolean value(`True/False`), in the while loop i call `new_game` again to start the code *again*.

If not, proceed and end with _"bye bye"._

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

First i declare a empty list called `guesses`. Furtheron i declare a variable called `correct_guesses` which will be eqal to 0 because we haven't guessed yet.

I also set a variable called `question_num` to 1 which represents the first question.

---

I use a `for` loop to print all questions with the `print(key)` statement.

I also had to display all options. I do that with a `nested for loop`.

```python
for i in options[question_num-1]:
            print(i)
```

Here i called `options` and use the `question_num` as a count to go thru each option for each question seperately. 

Since `question_num` is equal to 1 i simply had to write **-1** to start it in index 0. 

I now have to increment `question_num` by 1 to go thru all options for all questions when they are being pulled, i do that while it's still in the `for` loop.

This is the incrementation:
```python
question_num += 1
```
---

I also have to get the users "guess".
```python
guess = input("Enter (A,B,C or D): ")
```
I created a variable called `guess`.

`Guess` is asking the user to Enter one of the following: `A,B,C,D`.

Strings are case-sensitive so i make sure that the input will be recieved in upper-case. 
```python
guess = guess.upper()
```
Furtheron, 
I will display the users guesses at the end of the game. I did that by using the empty list earlier created called `guesses`.

```python
guesses.append(guess)
```

Next i want to check if the users input is the correct answer or not.
```python
correct_guesses += check_answer(questions.get(key),guess)
```
Here i use `correct_guesses` to add and assign the function `check_answer`. 
> If answer is correct, it will add +1 to the score from the `check_answer` function.

`check_answer` is going to pass in answer and guess with `(questions.get(key), guess)`.

Those 2 arguments will be later used in the corresponding function.


---
>Since all of this is still in the inner `for` loop, it will automatically iterate for each question/answer.

---
I end the outer `for` loop with:
```python
display_score(correct_guesses, guesses)
```
I called the `display_score` function and pass in both correct "answers" and the users guesses.

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

Furtheron use an `if` statement to ask if `answer` is equal to the users `guess`.

If that is the case it will then print a "correct" message and return the value `1` which will then be used to increment the score `correct_guesses`.

It else will return 0 and print the message "Wrong!"
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

Here i define `display_score` and recall the 2 arguments `correct_guesses` and `guesses` into my parameter.


Furthermore, i state that i want to print the answers and the user-guesses seperately. I do this by printing "Answers: " and to make sure i don't end on a new line, i write `(,end= "")` at the end of the print statement.

I then use a `for` loop to iterate thru all answer `key`'s and all user-`guesses`.

I do this by using `i` in `questions`/`guesses` to iterate thru them and print `i`. Though i have to tell `i` with `questions.get(i)` to return me the value of the item with the specified key, which in this case is all the `key`'s in `questions` / all the answers.

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
With the function `play_again()`, i ask the user if they would like to run the quiz again.

This is done by creating a user_input called `response`, this asks the user specificly if they would like to play again. I add `.upper()` at the end of the `input` to make sure the answer will be set in upper-case letters.

I then write an `if` statement to check `if` the `response` is equal to "Y". If so, return `True`, else return `False`.

---
