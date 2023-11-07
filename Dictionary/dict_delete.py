
# deleting an element from a dictionary

myDict = {'name' : 'Edy', 'age': 26, 'address': 'London', 'education':'masters'}

# deletion using pop() method

myDict.pop('name')

print(myDict)

# deletion using popitem() method
# it deletes an element randomly

myDict1 = {'name' : 'Edy', 'age': 26, 'address': 'London', 'education':'masters'}

print(myDict1.popitem())

print(myDict1)

myDict2 = {'name' : 'Edy', 'age': 26, 'address': 'London', 'education':'masters'}

myDict2.clear()
print(myDict2)

# using del
myDict3 = {'name' : 'Edy', 'age': 26, 'address': 'London', 'education':'masters'}

del myDict3['name']
print(myDict3)
# deleting entire dictionary
del myDict3
# print(myDict3)