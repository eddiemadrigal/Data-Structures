"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
sys.path.append('/Lambda/git/Data-Structures/queue_and_stack')
from queue import Queue
from stack import Stack
class Queue:
    def __init__(self):
        self.size = 0
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def __len__(self):
        return len(self.items)

    # to add an element from the rear end of the queue
    def enqueue(self, item):
        self.items.insert(0, item) # insert item at index 0

    # to pop an element from the front end of the queue
    def dequeue(self, myItem=None):
        if myItem != None:
            self.items.remove(myItem)
        else:
            self.items.pop()

