class Node:
    # id data is not given by user, its taken as None
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next(self,next):
        self.next = next
    def get_next(self):
        return self.next
    def set_prev(self,prev):
        self.prev = prev
    def get_prev(self):
        return self.prev
    def has_next(self):
        return self.next is not None
    def has_prev(self):
        return self.prev is not None
    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    # insert at begining
    def inse_at_begning(self,data):
        new_node = Node(data,None,None)
        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node