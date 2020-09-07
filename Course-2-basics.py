print("Hello, world")

# Anything after the hash will be a comment

# Variable & Assignment, it's reassignable
ex_var = 5

# Float vs Integers vs Booleans
float_1 = 1.23
int_1 = 5
bool_1 = True

# reassign variable
float_1 = 2.25
int_1 = 2
bool_1 = False



# exponentiation
exponentiation = 4 ** 4 # it will be 256
print(exponentiation)
# floor division
floor_division = 16 // 5 # it should be 3, which is integer
print(floor_division)
# modulo
modulo = 7 % 3 # the result is 1 which is the remain after 7 divide by 3
print(modulo)

# assignment operator
add_assign = 5
add_assign += 7 # now add_assign is reassigned as 12
print(add_assign)
# more cases of assignment operator # Precedence: () > ** > %,*,/,// > +,-
sub = 10
sub -= 3 # 7
print(sub)
mult = 9
mult *= 5 # 45
print(mult)
div = 6
div /= 2 # 3
print(div)
exp = 2
exp **=3 # 8 (2*2*2)
print(exp)
floor = 10
floor //= 3 # 3
print(floor)
mod = 7
mod %= 2 # 1
print(mod)




# Print Exercise
excer_var = 9.257
print(excer_var)
print(34)
print(round(3**3/(5+4))) # Round() avoid decimal or generate more decimals



# Grocery Store Purchase 💪
# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
#
# Penne 16 oz Pack of 12 - $16.68
# Arrabiata Pasta Sauce 24 oz - $6.98
# Bag of 20 Organic Garlic Cloves - $16.78
# Italian Seasoning 1.5 oz Bottle - $15.26
# Artisan Baguettes Twin Pack - $3.00
# 12 oz Bag of Meatballs - $4.39
#
# In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.
# The subtotal is just the sum of all of their prices.
# Use print() to display the result of the expression.

varPenne = 16.68
varPastaSauce = 6.98
varGarlic = 16.78
varSeasoning = 15.26
varBaguettes = 3
varMeatballs = 4.39

varTotal = (varPenne+varPastaSauce+varGarlic+varSeasoning+varBaguettes+varMeatballs)

print(round(varTotal,2))