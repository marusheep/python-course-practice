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