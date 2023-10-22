def product_of_array(arr):
    # Base case: if the array is empty, return 1 (the multiplicative identity)
    if len(arr) == 0:
        return 1
    # Recursive case: multiply the first element by the product of the rest of the elements
    else:
        return arr[0] * product_of_array(arr[1:])

# Example usage:
my_array = [1, 2, 3, 4, 5]
result = product_of_array(my_array)
print("The product of the array is:", result)
