class Node:
    # Constructor
    def __init__(self):
        self.data = None
        self.next = None
    # method for setting the data field of the node
    def setData(self,data):
        self.data = data
    # method for getting the data field of the node
    def getData(self):
        return self.data
    # Method for setting the next field of the node
    def setNext(self,next):
        self.next = next
    # method for getting the next field of the data
    def getNext(self):
        return  self.next
    def hasNext(self):
        return self.next is not None

class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    # method for inserting new node at the beginning of the Linked list
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.listLength() == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    # method for inserting new node at the ending of the Linked list
    def insertAtEnding(self,data):
        newNode = Node()
        newNode.setData(data)

        current = self.head
        while current.getNext is not None:
            current = current.getNext
        current.setNext(newNode)

    # Method for inserting a new node at any position in a linked list
    def insetAtPos(self,pos,data):
        if pos > self.listLength() or pos < 0:
            return
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.listLength():
                    self.insertAtEnding(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count = 0
                    current = self.head
                    while count < pos-1:
                        count += 1
                        current = current.getNext()
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)

    # Add element in the linked list
    def addElement(self,data):
        new_node = Node()
        new_node.setData(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)

    # method for deleting the first node of the linked list
    def deleteFirstNode(self):
        if self.head is None:
            print('The list is empty')
        else:
            current = self.head
            # self.head = self.head.getNext()
            self.head = current.getNext()
            current.setNext(None)

    # Deleting the last node in single linked list
    def deleteLastNode(self):
        if self.listLength() == 0:
            print('The list is empty')
        else:
            current_node = self.head
            prev_node = None
            while current_node.getNext() is not None:
                prev_node = current_node
                current_node = current_node.getNext()
            if prev_node is None:
                self.head = None
            else:
                prev_node.setNext(None)

    # Deleting an intermidate Node is single linked list
    def deleteFromLinkedListWithNode(self,node):
        if self.listLength() == 0:
            print('The list is empty')
        else:
            current = self.head
            prev = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    print('Node is not found in the list')
                else:
                    prev = current
                    current = current.getNext()
            if prev is None:
                self.head = current.getNext()
            else:
                prev.setNext(current.getNext())
    # Delete with data fromlnked list
    def deleteValue(self,value):
        if self.listLength() == 0:
            print('The list is empty')
        else:
            current_node = self.head
            prev_node = self.head
            while current_node.getNext() is not None or current_node.getValue() is not value:
                if current_node.getValue() is value:
                    prev_node.setNext(current_node.getNext())
                    return
                else:
                    prev_node = current_node
                    current_node = current_node.getNext()





