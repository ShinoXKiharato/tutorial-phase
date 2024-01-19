import math
'''
print("Calculator V1")
user_input1 = float(input("Enter first number: "))
operator = input("Enter what operator you would like to use: ")
user_input2 = float(input("Enter second number: "))

if operator == '+':
    result = user_input1 + user_input2
    print(str(result))
elif operator == '-':
    result = user_input1 - user_input2
    print(str(result))
elif operator == '/':
    result = user_input1 / user_input2
    print(str(result))
elif operator == '*':
    result = user_input1 * user_input2
    print(str(result))
else:
    print("Invalid operator")
'''
print("Calculator V1.1")

def add(nr1:str, nr2:str):
    if nr1.isdecimal() and nr2.isdecimal():
        return (float(nr1) + float(nr2))
    else:
        raise ValueError("Invalid Input")

def subtract(nr1:str, nr2:str):
    if nr1.isdecimal() and nr2.isdecimal():
        return (float(nr1) - float(nr2))
    else:
        raise ValueError("Invalid Input")
    

def divide(nr1:str, nr2:str):
    if nr2 == 0:
        raise ZeroDivisionError("Division by 0 is invalid")
    elif nr1.isdecimal() and nr2.isdecimal():
        return (float(nr1) * float(nr2))
    
def multiply(nr1:str, nr2:str):
    if nr1.isdecimal() and nr2.isdecimal():
        return (float(nr1) * float(nr2))
    else:
        raise ValueError("Invalid Input")

def isOPRT(oprt):
    '''
    Returns true if equals to +, -, * or /
    '''
    return oprt == '+' or oprt =='-' or oprt =='*' or oprt == '/'


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