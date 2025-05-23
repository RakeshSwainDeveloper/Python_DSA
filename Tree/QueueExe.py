class Queue(object):
    def __init__(self,limit = 5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    def isEmpty(self):
        return self.size <= 0
    def enQueue(self,item):
        if self.size >= self.limit:
            print("Queue Overflow")
            return
        else:self.que = item
        if self.front is None:
            self.front = self.rear= 0
        else:
            self.rear = self.size
        self.size += 1
        print('Queue after enQueue ',self.que)
    def deQueue(self):
        if self.size <= 0:
            print('Queue Underflow')
            return 0
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.front = 0
                self.rear = self.size - 1
            print('Queue after dequeue : ',self.que)
    def queueRear(self):
        if self.rear is None:
            print('sorry the queue is empty')
            raise IndexError
        return self.que[self.rear]

    def queueFront(self):
         if self.front is None:
             print('Sorry the queue is empty')
             raise IndexError
         return self.que[self.front]
