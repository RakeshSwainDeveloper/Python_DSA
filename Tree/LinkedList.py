# Single linked list
class singleNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

Head = singleNode(1)
A = singleNode(3)
B = singleNode(5)
C = singleNode(6)
Head.next = A
A.next = B
B.next = C
# print(Head)

# Trverse the list - O(n)
# curr = Head
# while curr:
#     print(curr)
#     curr = curr.next

# Display the linked list - O(n)
def display(head):
    curr = head
    element = []
    while curr:
        # element.append(str(curr))
        element.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(element))
# display(Head)

# Search for node value -> O(n)
def search(head,val):
    curr = head
    while curr:
        if val == curr.val:
            return  True
        curr = curr.next
    return False
# print(search(Head,3))


# Doubly linked list
class DoublyNode:
    def __init__(self,val,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)

head = tail = DoublyNode(1)
# print(tail)

# Despaly - O(n)
def display(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(element))
# display(head)

# Insert at beginning - O(1)
def insert_at_beginning(head,tail,val):
    new_node = DoublyNode(val,next = head)
    head.prev = new_node
    return new_node,tail
# head,tail = insert_at_beginning(head,tail,3)
# display(head)

# Insert at end - O(n)
def insert_at_end(head,tail,val):
    new_node = DoublyNode(val,prev=tail)
    tail.next = new_node
    return head,new_node
head,tail = insert_at_end(head,tail,7)
display(head)