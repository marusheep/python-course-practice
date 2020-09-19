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