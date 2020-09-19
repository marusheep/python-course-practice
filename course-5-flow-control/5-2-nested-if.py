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