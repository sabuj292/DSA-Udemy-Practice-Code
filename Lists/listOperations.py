

shoppingList = ['milk', 'cheese', 'butter']

print('milks' in shoppingList)

print(shoppingList[1])
print(shoppingList[-1])
# when we use negative index it print the element from right end

print('\n')
# Traversing a List

for i in shoppingList:
    print(i)

print('\n')

for i in range(len(shoppingList)):
    print(shoppingList[i])
    print('\n')


# sorting list elements

mylist = [9,8,7,6,5,4,3,2,1,0]

origl = mylist[:]


mylist.sort()

print(origl)



print(mylist)

# another method of sorting a list
sorted(mylist)