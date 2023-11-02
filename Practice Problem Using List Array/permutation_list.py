
# check if two list are permutation of one another

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

list1 = ['l', 'k', 'j','c']
list2 = [4,6,3,2,0]

print(permutation(list1, list2))
