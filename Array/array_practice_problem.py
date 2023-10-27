

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
# 2. Access individual elements through indexes

def accessArrayElement(array, index):
    print(array[index])

accessArrayElement(arr1, 3)

print('\n')

# 3. Append any value to the array using append() method

print('Append any value to the array using append() method')
arr1.append(7)
print('Array elements after append operation')
print(arr1)

# 4. Insert value in an array using inset() method
print('Insert value in an array using insert() method')

def InsertValueArray(index, value):
    arr1.insert(index, value)

InsertValueArray(0,11)
print('Array after insetion at 0 index')
print(arr1)

# 5. Extend python array using extend() method

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

# 8. Remove last array element using pop() method

print('Remove last array element using pop() method\n')

arr1.pop()
print(arr1)

# Fetch any element through its index using index() method

print("\nFetch any element from array using index \n")

def accessArrayElement(array, index):
    print(array[index])

accessArrayElement(arr1, 3)

print('\n')
#  10. Reverse a python array using reverse() method

print('Reversing an array using reverse() method\n')

arr1.reverse()
print(arr1)

# 11. Get array buffer information through buffer_info() method

print('Get array buffer information through buffer_info() method\n')

print(arr1.buffer_info())

#  12, Check for number of occurrence of an element using count() method

print('Check for number of occurrences of an element using count() method\n')
arr1.append(6)
print(arr1.count(6))

# 13. Convert array to string using tostring() method

print('\n Convert array to string using tostring() method\n')

# create an array (list) of elements with different data types
arr2 = arr1
arr2 = [str(element) for element in arr2]

# here[....] is used to define a new list

# covert the array to a string, using a space as a separator

my_string = ' '.join(arr2)

print(my_string)

# 14. Convert array to a python list with same elements using tolist() method

arr3 = arr1
print('Convert array to a python list using tolist()\n')

print(arr3.tolist())

# 15. Slice Elements from an array

print('Slice elements from an array\n')

print(arr1[5:10])

