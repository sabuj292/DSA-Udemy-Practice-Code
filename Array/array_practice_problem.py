

from array import *

# 1. Create an array and traverse

print('Create an array and traverse')
arr1 = array('i', [1,2,3,4,5,6])

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)
print("\n")
print('Access individual elements through index')
# Access individual elements through indexes

def accessArrayElement(array, index):
    print(array[index])

accessArrayElement(arr1, 3)

print('\n')

# Append any value to the array using append() method

print('Append any value to the array using append() method')
arr1.append(7)
print('Array elements after append operation')
print(arr1)

# Insert value in an array using inset() method
print('Insert value in an array using insert() method')

def InsertValueArray(index, value):
    arr1.insert(index, value)

InsertValueArray(0,11)
print('Array after insetion at 0 index')
print(arr1)

# Extend python array using extend() method

print('Extend python array using extend() method')

arr2 = array('i', [10, 11, 12, 13])
arr1.extend(arr2)
print('Extended array \n')
print(arr1)

# 6. Add items  from list into array using fromlist() method
print('\n Add items from list into array using fromlist() method\n')

tempList = [20, 21, 22]
arr1.fromlist(tempList)
print(arr1,'\n')

# 7. Remove any array element using remove() method
print('Remove any array element using remove() method')

def RemoveElement(array, value):
    for i in array:
        if i == value:
            array.remove(value)
    # if value in array:
    #     array.remove(value)
    # else:
    #     print('\n There is no such element in this array\n')

RemoveElement(arr1, 11)
print('\n', arr1, '\n')
