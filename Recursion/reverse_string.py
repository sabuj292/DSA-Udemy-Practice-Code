# reverses a given string using recursion

def reverseString(strr):
    if len(strr) <= 1:
        return strr
    return strr[len(strr) -1] + reverseString(strr[0: len(strr)-1])

print(reverseString('Shahriar'))
print(len('Shahriar'))

'''
If we use the code 
return strng[len(strng)] + reverse(strng[0:len(strng) - 1]) 

with len(strng) instead of len(strng) - 1, it will result in 
an "IndexError" in Python.

In Python, string indices start at 0, so the valid indices 
for a string of length n range from 0 to n-1. Attempting to 
access strng[len(strng)] would be trying to access an index 
that is one position beyond the end of the string, which is 
out of bounds and will raise an "IndexError."


'''