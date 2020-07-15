class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None # if empty list, the head node is none

    def append(self, data):
        if self.head is None: # if the head node is none (there are no elements in the list)
            new_node = Node(data) # we'll create a new node based on the data passed into the append function
            new_node.prev = None # make sure that prev point of this new node points to none
            self.head = new_node # update status of the head pointer, ie., the head is now the new node that we just put on to that new list
        else:                    # if there is at least one element in the list
            new_node = Node(data) # create the new node
            cur = self.head # set cur to first node (self.head)
            while cur.next: # while not none, cur = the current node
                cur = cur.next  # update the current pointer to keep going down the list
            cur.next = new_node # next pointer of that node points to the new node
            new_node.prev = cur # the new node's previous pointer points to the cur(rent) node (the last one on the list)
            new_node.next = None # new node's next is now None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data) # create a new node based on the data fed in
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data) # new_node = Node of data
            self.head.prev = new_node # we want the previous pointer of the current head to point to the new node that we just created
            new_node.next = self.head # new_node.next = head of the list
            self.head = new_node # make the new_node the head
            new_node.prev = None # make sure the new_node's prev points to None

    def print_list(self):
        cur = self.head # current is set to the head of the list
        while cur:
            print(cur.data)
            cur = cur.next # move that pointer right along the list

dllist = DoublyLinkedList() # we've created a doubly linked list
dllist.prepend(0)
dllist.append(1) # append elements 1 - 4
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(-1)

dllist.print_list() # print the list out to the screen