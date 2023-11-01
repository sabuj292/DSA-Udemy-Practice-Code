
myList = [1,2,3,4,5,6]

print(myList)

myList.insert(2, 22)
print(myList)

myList.append(555)
print(myList)  

newList = [11,22,33,44,55]

myList.extend(newList)

print(myList)
myList[0:2]= ['x','y']
print(myList[:])
# we can use slice for delete operation
# pop() method of delete operation

myList.pop(1)
print(myList)
# delete() method for delete operation
# del 
del myList[0:3]
print(myList)
# remove method for deletion
print(myList.remove(555))

print(myList)