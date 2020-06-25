# -*- coding: utf-8 -*-
"""

"""

'''
Queue Methods and Attributes
Before we begin implementing our own queue, let's review the attribute and methods it will have:

Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the queue. It needs no parameters and returns an integer.
'''

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        return self.items.append(item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    
q = Queue()
q.size()
q.isEmpty()
q.enqueue(1)
q.dequeue()
        
# Jose;s solution
    
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
''' Implementation of deque '''

'''

Implementation of Deque
In this lecture we will implement our own Deque class!

Methods and Attributes
Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the deque. It needs no parameters and returns an integer.

'''


class Deque:
    def __init__(self):
        self.items = []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0,item)   # Need to understand why addRead is insert to the first value look at the video!
    def removeFront(self):
        self.items.pop()
    def removeRear(self):
        self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

# Jose's answer 

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
