

# Various List Operations

# + operator: Concatenate Lists

a = [1,2,3,4]
b = [5,6,7,8]

c = a + b
print(c)

# * operator for repeating a particular pattern

x = [0,1]
x= x * 4

print(x)


# len() : returns count of elements in the List

a = [0, 1,2,3,4,5,6,7]
print(len(a))

# max() : returns the items with the highest value in the List\

print(max(a))


# min() : returns the items with the lowest value in the List

print(min(a))

# sum(): returns the sum of all items in the List

print(sum(a))

# Finding average of a list

print(sum(a) / len(a))


# finding average

total = 0
count = 0

while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count +1
    average = total / count

print('Average of the numbers: ', average)

# Finding Average of elements of a list

mylist = list()
while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    mylist.append(value)

average = sum(mylist) / len(mylist)

print('Average of elements of the list: ', average)
