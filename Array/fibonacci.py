def fibonacci(n):
    assert n>=0 and int(n) == n, 'Fibonacci number cannot be negative or non integer.'

    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Number of terms in the Fibonacci series


n = input("Enter a number of which you want ot print the fibonacci series : ")
n_terms = int(n)
print("Fibonacci Series:")
for i in range(n_terms):
    print(fibonacci(i))




