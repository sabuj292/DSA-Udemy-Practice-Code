
# A tuple is an immutable sequence of Python objects
# Tuple are also comparable and hashable

# t = 'a','b', 'c'
# t = ('a','b', 'c')

newTuple = ('a', 'b', 'c','d')
print(newTuple)
newTuple1 =('a')
# when using only one element to create a tuple we need to put a comma after that single element
print(newTuple1)
newTuple1 = ('a',)
print(newTuple1)

# tuple() for creating a tuple

tuple1 = tuple('sabuj')
print(tuple1)

# accessing an element in a tuple

print(tuple1[-3])
# slice[:] operator for accessing
print(tuple1[1:3])

# we can't perform update operation because tuples are immutuable


# tuple1[1] = 'o'
# print(tuple1)

