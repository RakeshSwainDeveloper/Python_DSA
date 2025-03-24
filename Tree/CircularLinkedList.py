from itertools import count

from networkx.algorithms.flow.utils import CurrentEdge


class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next(self,next_node):
        self.next = next_node
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next is not None

class CircularLinkedList:
    def __init__(self,head):
        self.head = head
    def circular_list_length(self):
        current_node = self.head
        if current_node is None:
            return 0
        count = 1
        current_node = current_node.get_next()
        while current_node is not self.head:
            current_node = current_node.get_next()
            count +=1
        return count

    # print circular linked list
    def print_circular_linked_list(self):
        current_node = self.head
        if current_node is None:return 0
        print(current_node.get_data())
        current_node = current_node.get_next()
        while current_node is not self.head:
            print(current_node.get_data())
            current_node = current_node.get_next()

    # Inserting element at end of the linked list
    def insert_at_end(self,data):
        current = self.head
        new_node = Node()
        new_node.set_data(data)
        while current.get_next() is not self.head:
            current = current.get_next()
        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            current.set_next(new_node)
    # Inserting elemetn at begining of the linked list
    def inset_at_beg(self,data):
        current = self.head
        new_node = Node()
        new_node.set_data(data)
        while current is not self.head:
            current = current.get_next()
        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            current.set_next(new_node)
            self.head = new_node

    # deleting the last node
    def delete_last_node(self):
        current = self.head
        temp = self.head
        if self.head is None:
            print('List is empty')
            return
        while current.get_next() is not self.head:
            temp = current
            current = current.get_next()
        temp.set_next(current.get_next())
        current.set_next(None)
        current = None

