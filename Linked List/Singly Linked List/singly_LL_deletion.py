
# Singly Linked List Deletion
# -Deleting the first Node
# -Deleting any given Node
# -Deleting the last Node




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

    # Search in SLL
    def searchSLL(self, nodeValue):
        if self.head is None:
            print("The LL is not exist")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value,' is present in the SLL.'
                node = node.next
            return 'The value does not exist in the SLL'




     # deleting a Node
    def deleteNode(self, location):
         if self.head is None:
            print('The LL is not exist')
         else:
            if location == 0:
                if self.head == self.tail:  # checking if there is ony one node
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node

            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1 
                nextNode = tempNode.next
                tempNode.next = nextNode.next



singlyLinkedList = SLinkedList()

singlyLinkedList.insertSLL(1,1)   
singlyLinkedList.insertSLL(2,1)   
singlyLinkedList.insertSLL(3,1)   
singlyLinkedList.insertSLL(4,1)   
singlyLinkedList.insertSLL(5,1)   
singlyLinkedList.insertSLL(6,1)   
singlyLinkedList.insertSLL(100,0)  
print([node.value for node in singlyLinkedList])
# singlyLinkedList.traversalSLL()

# search
print('Search Operation')
searchValue = singlyLinkedList.searchSLL(5)
print(searchValue)

# deletion of a Node
print('Deletion Operation')
deleNode = singlyLinkedList.deleteNode(0)
print([node.value for node in singlyLinkedList])