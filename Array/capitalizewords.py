def capitalizewords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizewords(arr[1:])

words = ['i', 'am', 'learning', 'data', 'structure']
print(capitalizewords(words))

# In this line, result is a list that stores the 
# capitalized words, and arr[1:] is a slice of the 
# original list arr starting from the second element 
# (index 1) to the end.
