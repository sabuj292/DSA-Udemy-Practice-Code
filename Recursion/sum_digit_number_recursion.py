# Finding the sum of digits of a positive number using recursion

def sumofDigits(n):
   # assert n>= 0 and int(n) ==n, 'The number has to be a positive integer'
    # here n == 0 is the base case| the stopping criterion
     # Handle negative numbers by taking the absolute value
     # n = abs(n) handle negative number by considering absolute value 
    n = abs(n)
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

# num = input("Enter a number for finding out the sum of digits : ")

print(sumofDigits(-4554))
  