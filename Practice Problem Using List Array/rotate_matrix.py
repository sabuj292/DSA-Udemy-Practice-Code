
# Given an image represented by an N*N 
# matrix write a method to rotate the image
#  by 90 degree

# import numpy as np

# myArray = np.array([[1,2,3], [4,5,6], [7,8,9]])

# for j in range(len(myArray[0]) -1, -1):
#     for i in range(len(myArray)-1):
#         print(myArray[j][j])

# PseudoCode for solving this porblem
# only for corner number
# for i = 0 to n:
#     temp = top[i]
#     top[i] = left[i]
#     left[i] = bottom[i]
#     bottom[i] = right[i]
#     right[i] = temp


# import numpy as np

# myArray = np.array([[1,2,3], [4,5,6], [7,8,9]])

# print(myArray)

# def rotateMartix(matrix):
#     n = len(myArray)
#     for layer in range(n//2):
#         first = layer
#         last = n - layer -1
#         for i in range (first, last):
#             # save top element
#             top = matrix[layer][i]
#             # move left element to top
#             matrix[layer][i] = matrix[-i-1][layer]
#             # move bottom element to left
#             matrix[-i-1][layer] = matrix[-layer-1][-i-1]
#             # move right to bottom
#             matrix[-layer-1][-i-1] = matrix[i][-layer-1]
#             # move top to right
#             matrix[i][-layer-1] = top
#         return matrix

# print(rotateMartix(myArray))


# Define the 2x2 matrix
# matrix = [[1, 2], [3, 4]]

# matrix = [[1,2,3], [4,5,6], [7,8,9]]

# # Print the original matrix
# print("Original Matrix:")
# for row in matrix:
#     print(row)

# # Rotate the matrix by 90 degrees using a for loop
# n = len(matrix)
# rotated_matrix = [[0 for _ in range(n)] for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         rotated_matrix[i][j] = matrix[n - j - 1][i]

# # Print the rotated matrix
# print("Rotated Matrix:")
# for row in rotated_matrix:
#     print(row)

# here matrix is a 2D list
matrix = [[1,2,3], [4,5,6], [7,8,9]]

print('Original Matrix: ')
for row in matrix:
    print(row)

# for row in matrix: - This line initiates a for loop 
# that iterates through each element in the matrix list. 
# The variable row represents each element in the matrix,
#  which is actually a list itself.
# here row is a list itself


# Rotate the matrix by 90 degree using a for loop

n = len(matrix)

rotated_matrix = [[0 for _ in range(n)] for _ in range(n)]

# [0 for _ in range(n)] creates a list with n zeros.
# '_' is often used as a throwaway variable when you don't need 
# to use the values from the loop. So, it creates a list of n zeros.


for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n - j - 1][i]

print("Rotated Matrix")

for row in rotated_matrix:
    print(row)