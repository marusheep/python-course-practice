# format()

name = input("what's the job applicatant's name?")
degree = input("what did they major in at college?")
job = input("what is their current occupation?")
experience = input("how many years have they been working in their field?")

print(name + " major in " + degree + " works as a " + job + ", and has " + experience + " years of experience.")

print("{} major in {} works as a {}, and has {} years of experience.".format(name,degree,job,experience))