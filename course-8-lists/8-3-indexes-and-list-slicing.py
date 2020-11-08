# accessing by index
example_1 = ["brocoli","peas","carrot"]
print(example_1[0]) #brocoli
print(example_1[1]) #peas
print(example_1[1][1]) #e

example_2 = [2,3,4],[4,5,6],[7,8,9]
print(example_2[1][2]) #6

# negative indexes
negative_example = [1,2,3,4,5]
print(negative_example[-1]) #5
print(negative_example[-2]) #4

# list slicing
sliced = [1,2,3,4,5,6,7,8,9]
print(sliced[:4]) #sliced from the begginer until the index 4-1
print(sliced[3:8]) #select index 3 to index 8-1
print(sliced[2:]) #select index 2 to the end

# reassigning a list's items
example = [3, 4, 6, 9]
print(example)

example[3] = 7 #9 changed to 7
print(example)

example[1:3] = [2,4] #4,6 changed to 2,4
print(example)

