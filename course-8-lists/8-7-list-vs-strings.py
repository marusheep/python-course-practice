# List is mutable but String is immutable

# reference
orginal = [1,2,3,4,5]
new = orginal
new[2] = 4
print(orginal)
print(new)  
# because Python uses reference so all variables, including original & new will be changed


# copy module and deepcopy()
import copy
ex_1 = [1,2,3,4,5]
ex_2 = copy.deepcopy(ex_1) #need to import copy module like Ln13 to copy the list
ex_2[2] = 4 #since the list's copied, we can change the list without affecting ex_1
print(ex_1)
print(ex_2)


# list line continuation
# list can be in multiple lines
ex_3 = ["tree",
        "flower",
        "nuts"]
print(ex_3)

# \line continuation
ex_4 =  1 +\
        2 +\
        3
print(ex_4)
