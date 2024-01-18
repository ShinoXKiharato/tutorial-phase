''' [temperature = input("")
# temperature = float(temperature)
if (temperature) > 30: 
    print("It's a hot day")
    print("Drink water")
elif (temperature) > 20:
    print("It's a nice day") # U stinky mf
elif (temperature) > 10:
    print("It's a bit cold") # (10, 20)
else:
    print("it's cold")
print("Done") '''

# Weight Converter program
'''
user_weight = float(input("How much do you weight? "))


messwert = input("(K)g or (L)bs: ")

if messwert.lower() == "k":
    cnv = user_weight * 2.205
    print('Your weight is ', int(cnv) , ' lbs')
elif messwert.lower() == "l":
    cnv = user_weight / 2.205
    print('Your weight is ' , int(cnv) , ' Kg')
else:
    print("Please enter a valid input")
'''
# the float(input) at the variable user_weight automatically removes the need of conversing any other data

# While loops
'''
i = 1
while i < 10:
    print(i * '*')
    i = i + 1
'''


# lists
'''
names = ["Bob", "John", "Mosh"]
names[0] = "Boobs"
print(names[0:2])
print(names)
'''
# list methods
''' numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(0, -1) # = [-1, 1, 2, 3, 4, 5]
# numbers.remove(3) # = [1, 2, 4, 5]
# numbers.clear() # empty list

print(numbers)
# print(1 in numbers) # Checks if 1 is in the List and returns "True" (Boolean Value)
print(len(numbers)) # Returns the number of "elements" in the list
'''

# For Loops
'''
numbers = [1, 2, 3, 4 ,5]
for item in numbers:
    print(item) # makes each item seperate on the list, also able to make in a while loop, but is longer.
'''
# The Range() function, generates a sequence of numbers
'''
numbers = range(20, 100, 15) # first number, starting point, second -end point and third number by how much it jumps, fx 2,4,6,8 instead of 1, 2, 3 ,4 ...
for number in numbers:
    print(number)
'''
'''
for number in range(6):
    print(number) # Shorter vers
'''

# Tuples, kinda like lists but Immuteable

# numbers = (1, 2, 3) # We use []to define a list and () to define a touple.

# Weight converter
'''
u_weight = float(input("How much do you weight? "))
measure = input("(K)g's or (L)bs:")

if measure.lower() == 'k':
    cnv = u_weight * 2.205
    print("Your total weight is ", int(cnv), "lbs.")
elif measure.lower() == "l":
    cnv = u_weight / 2.205
    print("Your total weight is " + str(int(cnv)) + "kg's.")
else:
    print("Error: Type in Valid Input.")
'''


# Weight Converter
'''
user_weight = float(input("How much do you weight?: "))
measure = input("In (K)gs or (L)bs?: ")

if measure.lower() == ('k'):
    rslt = user_weight * 2.205
    print("You weight " + str(int(rslt)) + "lbs.")
elif measure.lower() == ('l'):
    rslt = user_weight / 2.205
    print("You weight " + str(int(rslt)) + "kg.")
else:
    print("Invalid input.")
    '''
# ----
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
# ---
'''
user_weight = float(input("Enter ur weight: "))
measure = input("In (L)bs or (K)g's?: ")

if measure.lower() == ('l'):
    rslt = user_weight / 2.2
    print("U weight"+str(rslt))
elif measure.lower() == ('k'):
    rslt = user_weight * 2.2
    print("U weight "+str(rslt))
else:
    print("invalid") '''

