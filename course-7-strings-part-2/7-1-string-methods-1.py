# .upper() & .lower()

all_low = "there are no capitals here."
print(all_low)
print(all_low.upper())

all_up = "THIS IS SHOUTING TEXT!"
print(all_up)
print(all_up.lower())

# .title()
title = "this is title."
print(title.title())

# .isupper()

print("Mixed Case".isupper())
print("ALL CAPS".isupper())

# islower()

print("AHHHH".islower())
print("this is all lowercase".islower())

# more syntax
# .isalpha() #only letters
# .isalnum() #only numbers and letters
# .isdecimal() #only numbers
# .isspace() #only spaces
# .istitle() #only titlecase

print("Batman".isalpha())

# .startswith() & .endswith()
print("this is a string".startswith("this"))

# .join()
print("-".join(["one", "two", "three"]))

#split()
print("Eggs, Milk, Waffles, Bacon".split(", "))