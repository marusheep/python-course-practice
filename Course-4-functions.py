# Defining a function
def function_1():
    print(2+2)

# Calling a function
function_1()

# We can add parameter in the function
def fun_2(parameter):
    print(parameter+2)
fun_2(8)

# Default parameters
def default_example(num1=7, num2=8):
    print(num1*num2)

default_example()
default_example(4,6) #which you can re-define the parameter

# return - use "return" to replace "print" so that you can reuse the variable
def default_example1(num1=7, num2=8):
    return num1 * num2
print(default_example1()+44)

# function with no parameters exercise
# Do all of this in a .py file in Pycharm.
# 1. Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"
# 2. Call the function hello_world_printer()

def hello_world_printer():
    print("hello world")

hello_world_printer()

# function with 1 parameter exercise
# Do all of this in a .py file in Pycharm
# 1. Create a function called name_printer which takes 1 parameter and prints it
# 2. Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
# 3. Call name_printer() with the variable "name" as its argument.

def name_printer(varName):
    print(varName)

name = input("please enter your name")
name_printer(name)


# Programming Challenge: Volume of a Rectangular Prism
# Do all of this in a .py file in Pycharm.
# For this programming challenge, you will be creating a function that calculates the volume of a rectangular prism in feet.
# The formula to find the volume of a rectangular prism is V = l * w * h where l, w, and h are length, width, and height, respectively.
#
# First, create three variables representing length, width, and height.
# Assign each of them an integer as user input using the input() function and int().
#
# Next, create a function to calculate the volume of the rectangular prism.
# It should have 3 parameters representing length, width, and height and return the volume of a rectangular prism
# calculated using those 3 parameters.
#
# Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.
# You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.

length = int(input("Enter an integer that represents length in feet."))
width = int(input("Enter an integer that represents width in feet."))
height = int(input("Enter an integer that represents height in feet."))


def prism_vol(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")



# Programming Challenge: Celsius to Fahrenheit
#
# The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:
# F = 1.8 * C + 32
# Where F is the Fahrenheit temperature and C is the Celsius temperature.
#
# In a .py file, create a variable and assign it an integer representing a celsius temperature
# that is entered as user input().  input()'s message should prompt the user to enter an integer value.
#
# For this programming challenge,
# you will then write a function called fahrenheit that takes in an integer representing a Celsius temperature as its argument.
# The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.
#
# At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:
# "The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".
#
# To make sure that the function works,
# run your program multiple times and call the function on different user entered integer values both negative and positive.

varCelsius = int(input("Please enter your temperature."))

def temperature_convert(celsius):
    return round((1.8 * celsius +32),1)

print("The Fahrenheit equivalent of " + str(varCelsius) + "degrees Celsius is " + str(temperature_convert(varCelsius)) + ".")


# =====Importing Modules=====

# Generic Import
import random
print(random.randint(2, 100))

# Function Import
from random import randint
print(randint(1,20))

# Universal Import
from random import *
print(random())

# Programming Challenge: Miles Per Gallon
# For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.
#
# In a .py file, create two variables, one which will hold a randomly generated integer between 10 and 25
# (inclusive of both 10 and 25), and another which will hold a randomly generated integer between and inclusive of 200 and 400.
# The first variable represents the number of gallons of gas that the car's fuel tank holds.
# The second variable represents the miles that the car can travel on a full tank before needing a refuel.
#
# Using the formula miles per gallon (MPG) = miles driven/gallons used,
# calculate the car's MPG and display it in the output using print().
# Use floor division instead of regular division for this calculation to get an integer instead of a float.
# This will give a realistic approximation of miles per gallon even though floats such as 19.8 round down a large amount
# when using floor division since sometimes, car manufacturers sometimes exaggerate miles per gallon.
# In addition, display the values held in the variables you created for gallons of gas in the car's fuel tank
# and miles it can travel on a full tank with two different print statements.


from random import randint
varFuelTank = randint(10, 25)
varTravelMile = randint(200, 400)

print("The car can travel " + str(varTravelMile // varFuelTank) + "miles per gallen.")
print("The car's fuel tank can hold " + str(varFuelTank) + " gallons.")
print("The car can travel " + str(varTravelMile) + " miles on a full tank.")

# =====variable scope===
# global scope is the variable out of the function and local scope is the variable in the function.

varExample = "hello, world" # global scope

def loc_fun():
    varExample = "this is a string."
    return varExample  # local scope

print(varExample)
print(loc_fun())

# 1. local variables cannot be used by code in the global scope.
# 2. global variables can be accessed by code in the local scope.
# 3. the local scope of one function can't use variables from another function's local scope

# Global Statement
def loc_ex():
    global fruit #which is global statement that makes local function can be used as aglobal variable.
    fruit = "pear"
    print(fruit)

fruit = "apple"
loc_ex()
print(fruit)


