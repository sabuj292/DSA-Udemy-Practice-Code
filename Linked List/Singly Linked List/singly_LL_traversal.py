


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
    
    # Traversal Singly Linked List
    def traversalSLL(self):
        if self.head is None:
            print("The SLL is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


singlyLinkedList = SLinkedList()

singlyLinkedList.insertSLL(1,1)   
singlyLinkedList.insertSLL(2,1)   
singlyLinkedList.insertSLL(3,1)   
singlyLinkedList.insertSLL(4,1)   
singlyLinkedList.insertSLL(5,1)   
singlyLinkedList.insertSLL(6,1)   
singlyLinkedList.insertSLL(100,0)  
print([node.value for node in singlyLinkedList])
singlyLinkedList.traversalSLL()