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

def add(nr1, nr2):
    return (float(nr1) + float(nr2))
def subtract(nr1, nr2):
    return (float(nr1) - float(nr2))
def divide(nr1, nr2):
    return (float(nr1) / float(nr2))
def multiply(nr1, nr2):
    return (float(nr1) * float(nr2))

i = None
while i == None:
    try:
        nr1, nr2, oprt = input("Enter first number: "),input("Enter second number: "), input("Enter operator (+,-,/,*): ")
        if oprt == '+':
            i = add(nr1, nr2)
        elif oprt == '-':
            i = subtract(nr1, nr2)
        elif oprt == '/':
            i = divide(nr1,nr2)
        elif oprt == '*':
            i = multiply(nr1,nr2)
        else:
            print("Error occured ", end="")
        print("= "+ str(i))
    except ZeroDivisionError as e:
        print("Can't divide by 0")
    except nr1 != float:
        print("Error occured ", end="")
    except nr2 != float:
        print("Error occured ", end="")