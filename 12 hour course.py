# Variable
'''
first_name = "bitch"
last_name = "you"
fullname = first_name + " "+ last_name
print(fullname)'''

# Int datatype (Integer) / A whole number
'''
age = int(input("What's your age? "))
if age <= 11:
    print("Great, you're Gen Alpha kid, go fuck yourself")
elif age <= 26:
    print("Oh wow a Zoomer")
elif age <= 44:
    print("Bro's dust")
else:
    print("a realistic number")
'''
# print(age)
# print(type(age))
'''
age = 21
print("Y ", int(age)) 
'''
# Comma (,)	Separates elements in a sequence
# Plus Sign (+)	Performs arithmetic operations (addition, concatenation, string formatting)

# FLOAT datatype (floating point number / decimal number / .1)
'''
height = 250.5
print("blabla "+ str(height)+"cm")
'''
# Boolean (True or False / 1/0) useful in If statements
'''
human = True
print("stfu "+ str(human)) #prints stfu True
'''
# Multiple assignments = allows us to assign multiple variables at once in one line of code❤

# name, age, attractive = "Bro", 19, True | This is 3 Variables in one line of code. Each defined in order.

# Spongebob = 30
# Patrick = 30
# yo_mam = 30

# Spongebob = Patrick = yo_mom = 30 | This multiple assigned variable assigns the number 30 to all three(3) variables

#----------------------------------------------------------- 20M
# String Methods

#name = "tobi"

#print(len(name)) # Returns lenght of name (6)
#print(name.find("T")) #Finds charcter within string
#print(name.capitalize()) # Make the first character have upper case and the rest lower case.
#print(name.upper()) #Makes string all uppercase
#print(name.lower()) #Makes string all lowercase
#print(name.isdigit()) #Returns Boolean value (True/False)if string is only digits.
#print(name.isalpha()) #Check to see if string contains only Alphabetical Letters
#print(name.count("o")) Counts how many "o" there is in the string
#print(name.replace("T","a")) replaces all "T"'s to "a"'s
#print(name*3) #prints the string 3 times.

#----------------------------------------------------------- 25M

# Type Cast - Convert the data type of value to another data type.
'''
x = 1 #int
y = 2.0 #float
z = "3" #str

# x = float(x) Manually
y = str(y)
z = int(z)

print("X is "+str(x)) In Line
print(str(y))
print(z*3)
'''

#----------------------------------------------------------- 30M

# User Input 
'''
# name = input("What's your name?: ") #User Input is always from the STring Datatype
age = int(input("How old are you?: ")) # Input will automatically convert into Integer data type, this way can be used in math line 89
height = float(input("How tall are you?: ")) # Same shit as above but Float datatype, registers decimels.

print("You are "+ str(age+2)) # Coverts age into a string, while it is still an integer in the brackets and therefore used in math
print("You are "+ str(height)+ "cm. tall")
# print("Hello "+name) prints Hello Name
'''
#----------------------------------------------------------- 37M

# Math Functions
'''
import math

pi = 3.14
x = 1
y = 2
z = 3

# print(round(pi)) Rounds number / variable
#print(math.ceil(pi)) Rounds number up to the nearest Integer
#print(math.floor(pi)) rounds number down to the nearest Integer
#print(abs(pi)) Absolute Value, tells me how far number is from 0
#print(pow(pi, 2)) pow will rase a base number to a power, raised pi to the power of 2 = 9.8596
#print(math.sqrt(420)) gives me the square root of the number 420 = 20.49~

print(max(x,y,z)) gives me the largest value out of different variables / values
print(min(x,y,z)) gives me the lowest value out of different variables / values
'''
#------------------------------------------------------------ 41M

# String Slicing

# Slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step] for slice it's , instead : 

#name = "Shino Kiharato"
# First Index/[start] "S" in this case, is INCLUSIVE. The stopping index [:stop] is exclusive. 
'''
first_name = name[0:5] # Can be written as [:5] ¬ prints "Shino" 0-4 / :5
last_name = name[6:14] # prints 'Kiharato' 6-13 but exclusive => 6:14 '''
# Can be written as [6:] => prints out everything after index '6' till end.

#Step 
'''funky_name = name[0:14:2]''' #Can be written as [::2] | "Step" only displays every second character, if value is ::3 only every third character.
'''
reversed_name = name[::-1] #Displays variable reversed
print(first_name)
print(last_name+ " " + funky_name + " "+ reversed_name)
'''
             #Slice() creates slice object
'''
website1 = "http://google.com"
website2 = "http://wikipedia.com"
#Exclusive
sliceobj = slice(7, -4) # removes the https:// and .com portion

print(website1[sliceobj])# only prints out "google"
print(website2[sliceobj])# only prints out "wikipedia"
'''
#------------------------------------------------------------ 52M

#If Statement

# if statement = a block of code that will execute if it's condition is true
'''
age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age >= 12:
    print("You are a teenager!")
elif age >= 6:
    print("You are a child!")
else:
    print("Invalid Input!")
'''
# Order of IF Statement matters!

#------------------------------------------------------------ 58M

# Logical Operators 

# logical operators(and,or,(not)) = used to check if two or more conditional statements are true.
'''
temp = int(input("What's the temperature outside?: "))
#celsius
if not(temp >= 0 and temp <= 30): #In order to meet the conditions, both must be true. The "Not" logical operator flips the outcome from true, to false.
    print("The temperature is good today!")
elif temp < 0 or temp >30: 
    print("The temperature is bad today") # checks if temp is below 0 or above 30. If one of them is true, entire Statement is true.
'''
# The "Not" logical operator flips the outcome from true, to false.
# In this case, if i apply "not" to both if lin 176 and elif line 178, i would need to switch out both print statements in order to function just aswell as it was without the "not" operators.

#------------------------------------------------------------ 1:04 H or 64 M

# While loops

# while loop = a statement that will execute it's block of code,
#              as long as it's conditions remains true.

#while 1==1:
#    print("Help, I'm stuck in a loop!") <- Infinite Loop

# In this while loop, we ask the User for their name, if nothing is entered the loop continues and asks the user again until loop is false.
'''
name = ""                               name = None
while len(name) == 0:                   while not name:
    name = input("Enter your name: ")       name = input("Enter your name: ")

print("Hello "+name)                    print("Hello "+name)
'''
# Those are 2 different ways to write the loop/code, both do the exact same thing.

#------------------------------------------------------------ 1:07 H or 67 M

# For loops

# for loops = a statement that will execute it's block of code
#             a limited amount of times

#            while loop = unlimited
#            for loop = limited

#for i in range(10): # i for index, in, set a range of 10
    #print(i+1)

 #for i in range(50, 100+1,2): #(include, exclusive, step)
    #print(i) # Prints everything from 50-100 with a step of 2

#for i in "Shino Kiharato":
    #print(i) prints every letter of the string seperately

#Countdown that counts down from 10 to 0 with a sleep time of 1 second inbetween and prints "Happy New Year" at the end.
'''
import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year")
'''
#------------------------------------------------------------ 1:13 H or 73 M

 # Nested Loops = The "inner loop" will finish all of it's iterations before
#                 finishing one iteration of the "outer loop"
'''
rows = int(input("How many rows?: ")) #charge of outer loop
columns = int(input("How many columns?: ")) #charge for inner loop
symbol = input("Enter a Symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #end="" prevents the print statement to seperate with the next print statement,
    print()                   #       prevents the next print statement to enter a new line.
    '''

#------------------------------------------------------------ 1:17 H or 77 M

# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder
'''
while True:
    name = input("Enter ur name: ")
    if name != "":
        break '''
# As long as no input happens, it will continously ask for the users input(name). If input occurs, loop will stop.

'''
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":        # checks for - character.
        continue        # skips every - character / continues over every - character
    print(i, end="")    # end="" prevents the next print statement to enter a new line.
''' 
# In this we create a phone number which will be displayed. But we use continue to skip over the - characters to only print the whole number instead.

'''
for i in range(1, 21): # iterates from 1 to 20 because the second digit is exclusive
    
    if i == 13:
        pass
    else:
        print(i)
'''
# Creates variabl I to count thru a range from 1-20. Asks if i, is equal to 13. If true, it will "pass" over it / Skip 13 when printed.

#------------------------------------------------------------ 1:21 H or 81 M

# lists = used to store multiple items/values in a single variable
'''
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"] # creates a list instead of a variable if added []

food[0] = "sushi" #Updates element 0 / pizza to sushi '''
#print(food[0])

#food.append("ice cream") # Adds element to the list at the end. 
#food.remove("hotdog") #removes "hotdog" from the list
#food.pop() removes last element
#food.insert(0, "cake") inserts itself as new element and pushes the others further up. Element 0 is now cake while sushi is now 1.
#food.sort() sorts list alphabetically
#food.clear() cleares entire list.
'''
for x in food:
    print(x) 
    '''
#prints all elements in list.

#------------------------------------------------------------ 1:27 H or 87 M

# 2D Lists = a list of lists 
# also called multi dimensional list
'''
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger"]
dessert = ["cake", "ice-cream"]

food = [drinks,dinner,dessert] #2D list

print(food[0][2]) ''' # displays Tea from the first list. 0 == drinks, 2 == tea

#------------------------------------------------------------ 1:30 H or 90 M

# tuple = collection which is ordered and unchangeable
#         used to group together releated data
# similar to list but ordered and unchangable
'''
student = ("yuon", 19, "undefined") # created tuple with ()

print(student.count("yuon")) # counts how many times "yuon exists in the tuple"
print(student.index("undefined")) # indexes where in the list "undefined" appears. This case 0 is yuon, 1 is 19 so, 2 is undefined.

for x in student: #prints the tuple
    print(x)

if "yuon" in student: #if "yuon" in student is true, then-
    print("Yu is here")
'''
#------------------------------------------------------------ 1:33 H or 93 M

# set = collection which is unordered, unindexed. No duplicate values allowed
'''
utensils = {"fork", "knife", "spoon"}
dishes = {"bowl", "cup", "plate", "knife"}
'''
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes) #Updates utensils with the values in dishes.
#dinner_table = utensils.union(dishes) # Joins utensils and dishes into new set called dinner_table
'''
for x in dinner_table:
    print(x)'''

# print(utensils.difference(dishes)) #compares what utensils have what dishes doesn't
#print(utensils.intersection(dishes)) #returns element which they have in common. 

#------------------------------------------------------------ 1:40 H or 100 M

# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly
'''
capitals = {'USA': 'Washington DC', 
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}
'''

#capitals.update({'Germany': 'Berlin'}) #update with adding new key
#capitals.update({'USA': 'Las Vegas'}) # updates key USA with new Value 'Las Vegas'
#capitals.pop('China') # removes key 'China'
#capitals.clear() # Clears entire dictionary

#print(capitals['Russia']) #prints the key russia, so "Moscow"
#print(capitals.get('Germany')) safe to check if there is a key called germany
#print(capitals.keys()) prints only the keys
#print(capitals.values) prints only values
#print(capitals.items()) prints entire dictionary
'''
for key,value in capitals.items():
    print(key, value) # prints entire dictionary
    '''
#------------------------------------------------------------ 1:47 H or 107 M

# index operator [] = gives access to a sequence's element that includes but are not limited to : (str, list, tuples)

 #name = "yuon Ki!"

#if(name[0].islower()): #returns a ooolean value
#    name = name.capitalize() #capitalize the ffirst character of name

#creat substring
'''
first_name = name[:4].upper() # Specified range 0-4 and turn them uppercase
last_name = name[5:].lower() #range 5-end and turn lowercase
last_character = name[-1] 
print(first_name, last_name)
print(last_character) # prints !.
'''
#------------------------------------------------------------ 1:53 H or 113 M

# ❤️Functions = a block of code which is executed only when it is called.
'''
def hello(first_name, last_name, age):
    print("hello "+first_name+" "+last_name)
    print("You're "+str(age)+" years old!")
    print("Have a nice day!")
'''

#hello("Yuon")
#hello("dude")

#my_name = "Yuon"
#hello(my_name)

#hello("Yu", "Ki", 19) 
# I can create a call, and give it a number of arguments. Those arguments (yu, ki, 19) need a matching number of parameters in the function (first_name,last_name,age)
#------------------------------------------------------------ 2:02 H or 122 M

# Return statement = Functions send python values/objects back to the caller.
#                    These values/objects are known as the function's return value
'''
def multiply(nr1, nr2):
    return nr1 * nr2

x = multiply(6,8)
print(x) / print(multiply(6,8))'''
#------------------------------------------------------------ 2:05 H or 125 M

# Keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguemnts that our function recieves
'''
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Ki",middle="-",first="Yuu") '''# Gave each argument a unique identifier to the parameter in the function.
#------------------------------------------------------------ 2:07 H or 127 M

# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")
#num = float() create a floating point numer out of the string
#num = abs() find the absolute value
#num = round() round it to the nearest whole number
#print(num) print number

'''print(round(abs(float(input("Enter a whole positive number: "))))) '''
#does the same shit but in one line of code
#------------------------------------------------------------ 2:10 H or 130 M NR. 25