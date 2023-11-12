

class Node:
    def __init__(self, value= None):
        self.value = value # the value add in the node

        self.next = None # reference of the next node


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: # insert at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == -1: # insert at the ending
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:                  # insert at a particular location
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next =  newNode
                newNode.next = nextNode
                if tempNode == self.tail:   # updating the tail if need to insert at the end of the list
                    self.tail = newNode

singlyLinkedList = SLinkedList()

singlyLinkedList.insertSLL(1,1)   
singlyLinkedList.insertSLL(2,1)   
singlyLinkedList.insertSLL(3,1)   
singlyLinkedList.insertSLL(4,1)   
singlyLinkedList.insertSLL(5,1)   
singlyLinkedList.insertSLL(6,1)   
singlyLinkedList.insertSLL(100,0)  
print([node.value for node in singlyLinkedList])

# here in the above code
# If you don't implement __iter__ in your class, 
# instances of that class won't be directly iterable, 
# and attempting to use them in a for loop will result in an error.
#  Implementing __iter__ allows you to define the iteration behavior 
# for your custom objects.


# purpose of using 'yield'
# Purpose: The yield statement is used in the context of a generator function. 
# It turns a function into a generator, allowing it to produce a sequence of values 
# over multiple calls without losing its state. When yield is encountered, 
# the function's state is saved, and the yielded value is returned to the caller.


# difference between 'yield' vs 'return'
# A regular function with return is executed entirely, and it returns a single result to the caller.
# A generator function with yield is executed incrementally. Each time it yields a value, it is paused,
#  and the state is saved. The next time it is called, it resumes execution from where it left off.


# Use return when you want to return a single result and terminate the function.
# Use yield when you want to produce a sequence of values over multiple calls and maintain the function's state.
        


