
# searching an element in tuple

newTuple = ('a', 'b', 'c', 'd')

print('dd' in newTuple)

def searchTuple(stuple, element):
    for i in stuple:
        if i == element:
            return stuple.index(i)
    return 'The element does not exist'

print(searchTuple(newTuple, 'f'))