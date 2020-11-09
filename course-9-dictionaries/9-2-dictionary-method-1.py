# .keys()
birth_year = {1984: "Lily", 1985: "Rose", 1986: "Jenny", 1990: "Joanna"}
print(birth_year.keys()) # will show all the keys on the dictionary

# or can use for loop
for key in birth_year.keys():
    print(key) # will show all the keys in different lines


# .values()
print(birth_year.values())
# or for loop
for value in birth_year.values():
    print(value)


# .items()
# it will return keys & values
print(birth_year.items( ))
# use for loop to do so
for key, value in birth_year.items():
    print(key, value)

# make them as list
print(list(birth_year.keys()))
print(list(birth_year.values()))
print(list(birth_year.items()))

# using in and not in on values
print("Jenny" in birth_year.values()) #True
print("Jenny" in birth_year.keys()) #False


# .get()
if 1975 in birth_year:
    print(birth_year[1975])
else:
    print("1975 is not a key in birth_years.")
# or we can use get method
print(birth_year.get(1975, "1975 is not a key in birth_years.")) # 2 arguments


# Dictionary follow reference too!