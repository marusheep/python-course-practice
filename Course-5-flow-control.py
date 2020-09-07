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