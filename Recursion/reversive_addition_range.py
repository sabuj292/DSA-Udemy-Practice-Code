#  calculates the sum of all positive integers 
# from 1 to the given input number num using recursion.

def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num -1)

print(recursiveRange(6))