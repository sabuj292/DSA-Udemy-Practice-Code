
from array import *

arr1 = array('i', [1,2,3,4,5,6])

def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The Element does not exits in this array"

print(searchInArray(arr1, 6))
print(searchInArray(arr1, 10))