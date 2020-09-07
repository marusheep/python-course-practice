# Strings '',""
ex_1 = 'This is the place we can type string.'
ex_2 = "Or we can type strings with double quote."

# Accessing by index []
ex_3 = "Orange"
print(ex_3[2])
print("Timothy"[3])

# String Slicing [:]
ex_4 = "Mario Cart"
print(ex_4[:2])
print(ex_4[2:7])
print(ex_4[8:])

# Concatenation "" + ""
print("tomato" + " " + "juice")

# String Exercise
# Do all of this in a .py file in Pycharm
# 1. Create a variable and assign it the string "Just do it!"
# 2. Access the "!" from the variable by index and print() it
# 3. Print the slice "do" from the variable
# 4. Get and print the slice "it!" from the variable
# 5. Print the slice "Just" from the variable
# 6. Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string.

varLine = 'Just do it!'
print(varLine[10])
print(varLine[5:7])
print(varLine[8:11])
print(varLine[:5])
varConcate = "Don't"
print(varConcate + " " + varLine[5:])

# type() - use for finding out the data type
var_1 = "I'm hungry"
var_2 = False
var_3 = 2.14159
var_4 = 3
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

# str() - change any types of the data to string
var_5 = str(2.14159)
print(type(var_3))
print(type(var_5))

# Escape Sequences
# 1. tab character \t
print("I\tdon't\tknow\twhat\tit\twill\tlook\tlike\t?")
# 2. new line character \n
print("line1\nline2")
# 3. quote the string with \' and \" depends on what did you use for the strings
print('just to \"emphasis\" this word!')
print("just to \"emphasis\" this word!")
print("just to \'emphasis\' this word!")
# 4. just a slash \\
print("let's see what it will look\\appear like")


# type(), str(), and escape sequences exercises
# Do all of this in a .py file in Pycharm.
# 1. Create a variable and assign it a float
# 2. Use print() and type() to print the data type of the variable in the output
# 3. Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result
# 4. print() the string "Hello, I'm [name], it's nice to meet you!" (you will need to use the \' escape sequence.)

varEx2_1 = 2.13
print(type(varEx2_1))
print(str(varEx2_1) + " " + "is a float.")
print("Hello, I'm Karen, it\'s nice to meet you!")

# Programming Challenge: Asterisk Triangle
# Using your knowledge of escape sequences,
# create a single print() statement with single string inside of it
# that displays this when the program is run:

print("*******\n ***** \n  ***  \n   *   ")

# input() no matter what's type of input, they will all assigned to be a string
varName = input("Please type your name and press enter.")
print("Your name is " + varName + ".")
print(type(varName))

favNum = input("Please type your favourite number")
print("Your favourite number is " + favNum + ".")
print(type(favNum))

# Programming Challenge: Monty Python
# In a .py file, create a program and use input()
# three times to get answers to the following questions from a user.  Store each of the answers in a variable.
#
# 1. What is your name?
# 2. What is your quest?
# 3. What is your favorite color?
# 4. Then, concatenate everything into a string within a print() statement
#    with the form "So your name is [name], your quest is [quest], and your favorite color is [color]."

varGuestName = input("What\'s your name?")
varGuest = input("What\'s your quest?")
varColor = input("What\'s your favorite color?")
print("So your name is " + varGuestName +", your guest is " + varGuest + ", and your favorite color is " + varColor + ".")

# int() and float() - it's allowed you to change the strings to integer or float.
use_int = int(input("please insert an integer."))
print(use_int)
print(type(use_int))

# int() exercise
# In a Python file, use input() to ask the user to enter an integer that 10 will be added to.
# Assign what they type to a variable.
#
# print() the sum of the integer they entered and 10.

varExInt = int(input("Please enter an integer that 10 will added to."))
print(varExInt + 10)