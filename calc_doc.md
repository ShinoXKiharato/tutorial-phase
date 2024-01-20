# Calculator v1.1
**Base**
```python
i = None
while i == None:
    try:
        nr1 = input("Enter first number: ")
        oprt = input("Enter operator (+,-,/,*): ")
        if not isOPRT(oprt):
            raise ValueError()
        nr2 = input("Enter second number: ")
        if oprt == '+':
            i = add(nr1, nr2)
        elif oprt == '-':
            i = subtract(nr1, nr2)
        elif oprt == '/':
            i = divide(nr1,nr2)
        elif oprt == '*':
            i = multiply(nr1,nr2)
        elif not isinstance(nr1, float) or not isinstance(nr2, float):
            print("enter number")
        else:
            None
    finally:
        print("= "+ str(i))
```

I created a variable named `i` and set it to `None`. I used this variable to control a `while` loop. 
Inside the loop, I created a `try` block that asked the user for input and performed various checks on the input.

First, I asked the user for the first number. Then, I asked the user for the operator. 
After that, I asked the user for the second number. I also checked `if` the operator was valid using the `isOPRT()` function. 
If the operator was not valid, I **raised an** `ValueError.`

Next, I checked `if` the operator was one of the four valid operators: `+`, `-`, `*`, or `/`. 
If so, I used the corresponding function to perform the calculation and stored the result in the `i` variable.

---
At the end of the `if` statement, I asked `if not isinstance(nr1, float) or not isinstance(nr2, float).` This statement basically checks if the instance of nr1 or nr2 is a floating-point number.

If either `nr1` or `nr2` is a floating-point number, it returns `False` and continues its code. 
If either `nr1` or `nr2` is not a floating-point number, it returns `True` and raises an error with the print 
statement asking the user to enter a number instead.

The `if` statement ends with `else:` to leave the `if` statement and go back into the `try` statement, 
where it calls finally to `print "= "+ str(i).` 
This prints the result as a string to the user. `If` `i` is equal to None, the loop continues again.

## Functions
I first defined all the functions I wanted to have in my calculator like this:
```python
def add(nr1:str, nr2:str):
    if nr1.isdecimal() and nr2.isdecimal():
        return (float(nr1) + float(nr2))
    else:
        raise ValueError("Invalid Input")
```
I first defined a function called `add` that performs addition. I used user input number 1 `(nr1)` and number 2 `(nr2)` 
and converted them into strings to ensure that the user entered a number and define if that would not be the case.

Next, I wrote an `if` statement that checked `if` `nr1` and `nr2` were both decimal numbers. 
If so, it converted them to floating-point numbers and added them together, returning the result.

If the `if` statement was not true, I `raised` an `ValueError` to tell the user that the input was invalid.

I followed the same approach to define functions for subtraction `(subtract)`, multiplication `(multiply)`, and division `(divide)`.

However, I made a slight adjustment to the `divide()` function. 
```python
def divide(nr1:str, nr2:str):
    if nr2 == 0:
        raise ZeroDivisionError("Division by 0 is invalid")
    elif nr1.isdecimal() and nr2.isdecimal():
        return (float(nr1) * float(nr2))
    else:
        raise ValueError("Invalid Input")
```
I added an `if` statement to check `if` the second number `(nr2)` was equal to 0. 
If so, I raised a `ZeroDivisionError` to indicate that division by 0 is invalid.


Furtheron, i defined a function for all operators.
```python
def isOPRT(oprt):
    return oprt == '+' or oprt =='-' or oprt =='*' or oprt == '/'
```

I created a function called `isOPRT()` that checked if the input operator `(oprt)` 
was one of the four valid operators: `+`, `-`, `*`, or `/`. 
If so, it returned `True`; otherwise, it returned `False.`

---

