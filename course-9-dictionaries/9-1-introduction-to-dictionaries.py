# To create a dictionary, type {} then type key value pairs, separated by : 
console = {"Nintendo": "WII", "Microsoft": "Xbox", "Sony": "Playstation"}

# accessing by key
print (console["Microsoft"]) # it will display "Xbox"
val = console["Sony"]
print(val)
# key values can be mixed data type

# dictionaries are unordered
print([2, 4, 6] == [2, 4, 6]) #true
print([2, 4, 6] == [6, 4, 2]) #false
first = {0: 2.2, 1: 3.5, 2: 4.8}
second = {1: 3.5, 2: 4.8, 0: 2.2}
print(first == second) #true

# in ot not in
print(0 in first) #True
print(1 not in first) #False