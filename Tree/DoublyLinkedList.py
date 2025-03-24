from tempfile import tempdir
from typing import NewType


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
        self.tail = None
    # insert at begining
    def inse_at_begning(self,data):
        new_node = Node(data,None,None)
        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    # insert at end
    def inse_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(Node(data,None,current))
            self.tail = current.get_next()

    # get Node
    def get_node(self,index):
        current_node = self.head
        if current_node is None:
            return None
        i = 0
        while i< index and current_node.get_next() is not None:
                current_node = current_node.get_next()
                if current_node is None:
                    break
                i += 1
        return current_node

    # insert at given position
    def insert_pos(self,index,data):
        new_node = Node(data)
        if self.head is None or index == 0 :
            self.inse_at_begning(data)
        elif index > 0:
            temp = self.get_node(index)
            if temp is None or temp.get_next() is None:
                self.inse_at_end(data)
            else:
                new_node.set_next(temp.get_next())
                new_node.set_prev(temp)
                temp.get_next().set_prev(new_node)
                temp.set_next(new_node)



# delete elment
























