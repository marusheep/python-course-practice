# function with 1 parameter exercise
# Do all of this in a .py file in Pycharm
# 1. Create a function called name_printer which takes 1 parameter and prints it
# 2. Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
# 3. Call name_printer() with the variable "name" as its argument.

def name_printer(varName):
    print(varName)

name = input("please enter your name")
name_printer(name)