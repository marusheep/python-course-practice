# del
planets = ["pluto","venus","mars","earth"]
del planets[0] #delete pluto
print(planets)

# .remove()
planets.remove("venus") #removed venus
print(planets)

colour = ["blue","orange","green","blue","yellow","blue"]
colour.remove("blue") #only the first blue will be removed if using remove()
print(colour)

# del vs .remove()

# .append()
pets = ["dog","cat","bunny"]
pets.append("fish") # add more item on the end of the list
print(pets)

# .insert()
pets.insert(1,"turtle") # add item on the index you want of the list
print(pets)

# .sort()
num_list = [1.34,1,0,58,-2,-23]
print(num_list)
num_list.sort() #sort the list accs
print(num_list)

name = ["John","Bill","Daniel","Sasha"]
print(name)
name.sort() #sort the list accs
print(name)
name.sort(reverse=True) #sort the list desc
print(name)
# we cannot sort the list with different data type, 
# but can sort with number and boloon (true =1, false =0)
mixed = [False,-1,32]
mixed.sort()
print(mixed)

# ASCIIbetical Order
# Which means the orders are sorted by case sensible
ASCIIbetical = ["Andy","karen","aaron","Rita","Gina"]
ASCIIbetical.sort() # aaron will be left behind
print(ASCIIbetical) 
ASCIIbetical.sort(key=str.lower) # will be case insensible
print(ASCIIbetical)

# .index()
drink = ["cola","juice","beer","rum"]
print(drink.index("cola")) # index =0

# .pop()
band = ["radio head","coldplay","oasis","take that"]
end = band.pop() #it will remove the last item from list and assign it as a variable
print(band)
print(end)

fruit = ["orange","banana","papaya","apple"]
pop = fruit.pop(2) #removed the index 2 and assign it to the variable
print(fruit)
print(pop)