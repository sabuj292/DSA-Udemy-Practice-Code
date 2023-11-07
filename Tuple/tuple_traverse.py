
# traversing a tuple

newTuple = ('a', 'b', 'c', 'd')

for i in newTuple:
    print(i)

# another method
print('\n range() method for traversing')

for i in range(len(newTuple)):
    print(newTuple[i])
# here this loop will return index, then using newTuple[i] we can print the value
