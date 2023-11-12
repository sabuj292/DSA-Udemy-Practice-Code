
# mainly follow 3 steps
# create 'head' and 'tail' node and intialize the reference will null
# create a node, assign a value and put null in reference section
# put reference of the previously created node with head and tail


#  here in below '__init__' is a constructor, that is automatically called when an object is created from a class or when a class is called


# 'self' is a way for each instance of a class to refer to itself.
#  It's like a placeholder that gets replaced with the actual 
# instance when a method is called. It helps to keep track of data 
# specific to each instance and allows methods to operate on that instance's data.

class Node:
    def __init__(self, value= None):
        self.value = value # the value add in the node

        self.next = None # reference of the next node


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLindedList.head.next = node2
singlyLinkedList.tail = node2
