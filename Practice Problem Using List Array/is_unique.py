
# Is Unique: check if a list has all unique characters, using python list

myList = [1, 20, 30, 44, 20, 56,57,8,9,10,31,12,13,14,35,16,27,58, 19,21]




def isUnique(list):
    a = []
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(isUnique(myList))