
# Searching for an element in the List

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# using IN operator for searching

if 100 in mylist:
    print(mylist.index(100))

else: 
    print('The value does not exist in the list')


# Linear Search Method



def searchinList(list, value):  # Time Complexity O(n)
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(mylist, 60))