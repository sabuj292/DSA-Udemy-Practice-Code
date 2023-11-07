
# operations and Built in Functions

myDict = {'one':'uno', 'two':'dos', 'three':'tres', 'four':'cuarto'}

# in opertor
# it returns True if the key is in the dict
print('one' in myDict)
# for cheaking values in the dict

print('uno' in myDict.values())

# "for" operator
# the following returns all the key of the dict

for key in myDict:
    print(key)

# for returns all the values according to keys

for key in myDict:
    print(myDict[key])

# for printing keys, and values
for key in myDict:
    print(key, myDict[key])

# ----------Built in Function-----

# all()
# need to check this method
dict1 = {0:'True'}
print(all(dict1))

# any() method

dict2 = {0:False, 1:True, 2:False}
print(len(dict2))
# sorted() function
dict3 = {'e':1, 'a':2, 'u':3, 'o':4, 'i':5}
print(sorted(dict3, reverse=False))

# ---------
dict3 = {'ede':1, 'aasd':2, 'ufghd':3, 'odsa':4, 'ii':5}
print(sorted(dict3, key= len))