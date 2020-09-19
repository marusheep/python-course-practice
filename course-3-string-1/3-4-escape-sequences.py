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