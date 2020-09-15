# while loops

counter = 0

while counter < 5:
    print("something")
    counter += 1

# infinite loops
#####
###inCounter = 1

###while inCounter < 3:
###    print(inCounter)
#####

# While Loops Exercise
#
# For this exercise, 
# you will print 10 descending integers starting from 10 and ending at 1 
# with each integer being 1 less than the last and each integer printed on a new line.
#
# Create a variable and assign it the integer 10.
# 
# Then, print
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# in the output by using a while loop to print numbers while the variable does not equal 0.
# Use the -= operator to reassign descending values to the variable.

exCount = 8

while exCount != 0:
    print(exCount)
    exCount -= 1

# Programming Challenge: Sum of Numbers From A Positive Integer
#
# Write a program which gets a positive integer 
# from a user using input() and assigns it to a variable.
# 
# The program should then use a while loop to get the sum of all of 
# the integers from the integer that was entered by the user down to 1.  
# For example, if the integer entered by the user was 6, 
# the while loop would find the sum of 6, 5, 4, 3, 2, and 1, which is 21.
# 
# At the bottom of your program create two print statements.  
# One will display the user entered integer and the other will display 
# the sum found by the while loop.

posInt = int(input("Please enter a positive integer."))

intInit = posInt

summed = 0

while posInt > 0:
    summed += posInt
    posInt -= 1
print(intInit)
print(summed)

# For loops

word = "house"

for letter in word:
    print(letter)



# For Loops Exercise
# Use a for loop to print each letter from the string "hello world".

exWord = "hello world"

for letter in exWord:
    print(letter)

# Programming Challenge: Find The Number of Characters in A String
#
# In a .py file, write a program which calculates the number of characters in a string.
# The string should be entered using input() and assigned to a variable. 
# Use print() twice at the end of your program.  

# The first print() will print the string that the user entered 
# and the second print() will display the number of characters in the string.  
# For example, if the user entered the string "hello world", 
# the number of characters would be 11.

intStr = str(input("Please type some words here."))

count = 0

for char in intStr:
    count += 1

print(intStr)
print(count)

# range()

# 1. use range() with 1 argument
one_input = range(5)
for num in one_input:
    print(num)


# 2. use range() with 2 arguments
two_input = range(3,10)
for num in two_input:
    print(num)

# 3. use range() with 3 arguments
three_input = range(5,30,2)
for num in three_input:
    print(num)

# Programming Challenge: Fizz Buzz
#
# Write a program that prints the integers 1 through 50 using a loop.
# 
# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.
# For numbers which are multiples of 3 but not 5 print “Fizz” instead of the number 
# and for the numbers that are multiples of 5 but not 3 print “Buzz” instead of the number.
# 
# All of the remaining numbers which are not multiples of 3 or 5 
# should just be printed as themselves.

