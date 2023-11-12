def simple_return():
    print("This is executed first.")
    return 42
    print("This is not executed.")

def simple_yield():
    print("This is executed first.")
    yield 42
    print("This is executed when the generator is resumed.")
    yield 43

# Using the simple_return function
result = simple_return()
print(result)  # Output: 42

# Using the simple_yield generator
gen = simple_yield()
print(next(gen))  # Output: 42
print(next(gen))  # Output: 43


def generate_numbers(n):
    for i in range(n):
        yield i

gen_num = generate_numbers(10)
print(next(gen_num))
print(next(gen_num))
print(next(gen_num))
print(next(gen_num))

# The next() function is used to retrieve the next item from an iterator. 
'''
Each call to next() advances the generator to the next yield statement and returns the yielded value. 
If there are no more values to yield, it raises a StopIteration exception. This is how the for loop 
internally works when iterating over a generator or any iterable.
'''


'''
gen = simple_yield(): This line creates a generator object gen by calling the simple_yield generator function. 
At this point, the function's code is not executed yet; it is just ready to be executed when the generator is iterated.

print(next(gen)): The first call to next(gen) starts the execution of the generator function until the first yield statement 
is encountered. The function prints "This is executed first." and then yields the value 42. The state of the function is saved. 
The output of this line is 42.

print(next(gen)): The second call to next(gen) resumes the execution of the generator function from where it left off. 
It prints "This is executed when the generator is resumed." and then yields the value 43. The state of the function is saved again.
 The output of this line is 43.

If you were to call next(gen) again, it would resume execution from where it left off and continue the pattern.

This example illustrates the incremental execution of a generator function, allowing you to produce a sequence of values 
one at a time while maintaining the function's state between calls.


'''
