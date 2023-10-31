
import numpy as np

twoDArray = np.array([[11, 15, 10, 6],
                        [10, 14, 11, 5],
                        [12, 17, 12, 8],
                        [15, 18, 14, 9]]
                        )

print(twoDArray)

# insertion in 2D array

# newTwoDArray = np.insert(twoDArray, 2, [[1,2,3, 4]], axis = 1)
# print(newTwoDArray)

#  Access an element in 2D array

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray, 3, 3)

print('\n \n')

# Traversal 2D array

def traverse2DArray(array):
    for i in range(len(array)): # here len(array) return the length of the row 
        for j in range(len(array[0])): # here len(array[0]) return the length of the coloum of the array
            print(array[i][j])

traverse2DArray(twoDArray)
print('\n \n')

# Searching Two Dimensional Array

def search2DArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index ' +str(i)+" "+str(j)
    return 'The element is not found'

print(search2DArray(twoDArray, 80))

print('\n \n')

# Deleting a row or a column in 2D array

newTarray = np.delete(twoDArray, 0, axis = 1)
print(newTarray)

 