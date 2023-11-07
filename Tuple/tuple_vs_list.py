
# list is mutable whereas list is immutable

#  Methods that can Not be used for tuples
# - append()
# -insert()
# -remove()
# -pop()
# -clear()
# -sort()
# -reverse()

# but we can use in case of list


# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types
# Iterating through a tuple is faster than list
# Tuples that contain immutable elements can be used as a key for a dictionary
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected
 


# Tuples can be stored in Lists
# Also Lists can be stored in Tuples

list1 = [(1,2), (9,0), (3,4)]

print(list1)

tuple1 =([1,2], [3,4], [5,6])
print(tuple1)