# Programming Challenge: Roman Numeral Equivalent
# 
# For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.
# Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.
# For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output.

from random import randint
varInt = randint(1,10)

if varInt == 1:
    print("The roman numberal equivalent of 1 is I.")
elif varInt == 2:
    print("The roman numberal equivalent of 1 is II.")
elif varInt == 3:
    print("The roman numberal equivalent of 1 is III.")
elif varInt == 4:
    print("The roman numberal equivalent of 1 is IV.")
elif varInt == 5:
    print("The roman numberal equivalent of 1 is V.")
elif varInt == 6:
    print("The roman numberal equivalent of 1 is VI.")
elif varInt == 7:
    print("The roman numberal equivalent of 1 is VII.")
elif varInt == 8:
    print("The roman numberal equivalent of 1 is VIII.")
elif varInt == 9:
    print("The roman numberal equivalent of 1 is IX.")
else:
    print("The roman numberal equivalent of 1 is X.")

#bool function

print(bool(0)) # false as 0 is falsthy