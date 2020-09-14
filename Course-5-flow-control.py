# Flow Control - booleans
# Always use == istead of = if compare to the value.

# If Statements / Else Statements
veg = input("Type the name of a vegetable.")
if veg == "corn":
    print("Corn is the best vegetable!")
elif veg !="":
    print(veg + " is good too!")
else:
    print("Type something")

# nested if and else statements

gpa = float(input("Please input your GPA here."))
inst_app = input("Is the student going to be educated at an approved institution?")

if gpa >= 3.7:
    if inst_app == "yes":
        print("You are qualified for low APR loan.")
    else:
        print("You are not qualified for low APR loan.")
else:
    print("You need higher GPA to qualify.")

# Programming Challenge: Grade Determiner
# Professor Fuentes teaches a Python class and uses the following grading scale for all of her exams.
# You work as a teacher's assistant and due to her busy schedule she has requested that you write a program
# which will determine the grades of the class's students.
#
# Her grading scale is as follows:
#
# 1. A score of 90 or above is an A
# 2. A score of 80 or above is a B
# 3. A score of 70 or above is a C
# 4. A score of 60 or above is a D
# 5. A score any lower is an F
#
# For this exercise, start by creating a variable and assigning that variable a student's score as an integer using input().
#
# Then, using nested if and else statements and the following set of rules,
# determine and then display the student's grade along with their score using print().
#
# 1. If the student's score is greater than or equal to 90, then the student will receive an A grade.
# 2. Otherwise, if the student's score is greater than or equal to 80, then the student will receive an B grade.
# 3. Otherwise, if the student's score is greater than or equal to 70, then the student will receive an C grade.
# 4. Otherwise, if the student's score is greater than or equal to 60, then the student will receive an D grade.
# 5. Otherwise, the student will receive an F grade.
#
# Make sure to run your program multiple times and test it with values for each 5 of the different grades
# to make sure that the correct output is displayed for any value entered as a student's score.

verScore = int(input("Please insert the student's scores."))

if verScore >= 90:
    print("Your grade is A")
else:
    if verScore >= 80:
        print("Your grade is B")
    else:
        if verScore >= 70:
            print("Your grade is C")
        else:
            if verScore >= 60:
                print("Your grade is D")
            else:
                print("Your grade is F")


# elif statements
user_num = int(input("please enter an integer."))

if user_num < 0:
    print("The nummber you entered is less than 0.")
elif user_num == 0:
    print("The number you entered is 0.")
elif 0 < user_num <= 100:
    print("The number you entered can be 1, 100, or anything in between.")
else:
    print("The number you entered is greater than 100.")


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