
# Dictionary built in Method

myDict = {'name': 'Edy', 'age':26, 'address': 'London', 'education':'master'}

newDict = myDict.copy()
print(myDict)
print(newDict)

# fromkeys()



newDict2 = {}.fromkeys([1,2,3], 0)
print(newDict2)

# get() method to fetch a value according to its key

newDict1 = myDict.copy()
print(myDict.get('karim', 22))
# here in get() method there are two parameter first one is key 
# and the 2nd one is optional which is value, which will be shown 
# if the the targeted list does not contain the mentioned key

# ----items() method-------

print(myDict.items())

# items() method will print the tuples (key, value)

# ------keys() method-----
# it prints all the keys in the dict


print(myDict.keys())

# ------setdefault()------
# it returns the value of a key if the key is in the list
# if the value is not in the dict it insert the key and a default value to the dict

print(myDict.setdefault('sur name', 'added'))
print(myDict)

# ----pop()-----
print(myDict.pop('name1', 'key does not exist'))


# ----values()----
# displays a all values of the dict

print(myDict.values())

# -----update()----
# dictionary.update(other_dictionary)


newDict3 =  {'a':1, 'b':2, 'c':3}
myDict.update(newDict3)
print(myDict)