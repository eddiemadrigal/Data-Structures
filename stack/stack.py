"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# 1 solution:
# Implement the Stack class using an array as the underlying storage structure.
# Make sure the Stack tests pass.

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.items = []
#         # self.storage = ?

#     def isEmpty(self):
#         return self.items == []

#     def __len__(self):
#         return len(self.items)

#     def push(self, value):
#         self.items.append(value)

#     def pop(self):
#         if self.items == []:
#             return None
#         else:
#             return self.items.pop()

# Re-implement the Stack class, this time using the linked list implementation as the underlying storage structure.
# Make sure the Stack tests pass.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False        

    def __len__(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            oldnode = self.head
            self.head = self.head.next
            oldnode.next = None
            return oldnode.data