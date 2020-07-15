"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev 
        self.value = value # creates a node object based on the value that's passed in
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = self.tail = node # if we have an empty list, the head node is none
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it as the new head of the list. 
    Don't forget to handle the old head node's previous pointer accordingly.
    PREPEND.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)                  # create a new node based on the value passed into the 'add_to_head' function
        self.length += 1                            # increase the count of nodes by 1
        if not self.head and not self.tail:         # if list is empty
            self.head = self.tail = new_node        # the new_node is both the head and tail
        else:                                       # else, more than 1 node exists
            new_node = ListNode(value)              # create a new node based on the value passed into the 'add_to_head'
            cur = self.head                         # set cur to first node (self.head)
            while cur.next:                         # while not None, cur equals the current node
                cur = cur.next                      # update the current pointer to keep going down the list
            cur.next = new_node                     # next pointer of that node points to the new node
            new_node.prev = cur                     # the new node's previous pointer points to the cur(rent) node (the last one on the list)
            new_node.next = None                    # new node's next is now None
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value                     # store the head's value in value
        self.delete(self.head)                      # delete the head
        return value                                # return the value stored in value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)                  # create a new node based on the value passed into 'add_to_tail'
        self.length += 1                            # increase the length of the list by 1
        if not self.head and not self.tail:         # if the list is empty
            self.head = self.tail = new_node        # new_node is both the head and tail of the list
        else:                                       # list is not empty
            new_node.prev = self.tail               # the new node's previous pointer is points to the tail of the list
            self.tail.next = new_node               # the tail's next points to the new_node
            self.tail = new_node                    # the tail node pointer points to the new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value                     # store the tail node's value in value
        self.delete(self.tail)                      # delete the tail node
        return value                                # return the value stored in value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:                       # if single head node exists
            return                                  # exit, it's the only one, so alread in the front
        self.add_to_head(node.value)                # add value to head of list
        self.delete(node)                           # delete the node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:                       # if single tail node exists
            return                                  # exit, it's the only one there
        self.add_to_tail(node.value)                # add value to tail of list
        self.delete(node)                           # delete the node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1                            # reduce the list count by 1
        
        if self.head is self.tail:                  # only 1 node exists
            self.head = self.tail = None            # set head and tail nodes to None        
        elif node is self.head:                     # if node is the head
            self.head = node.next                   # point head to the node's next
            node.delete()                           # delete the node        
        elif node is self.tail:                     # if the node is the tail
            self.tail = node.prev                   # tail points to the node's previous
            node.delete()                           # delete the node        
        else:                                       # the node is between the head and tail
            node.delete()                           # delete the node

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head                         # set current to the head node
        max = self.head.value                       # set max to the value of head
        while(current is not None):                 # go through all nodes
            if current.value > max:                 # sort through each value looking for the max value
                max = current.value                 # replace max with the current value
            current = current.next                  # check the next value
        return max                                  # return max after filtering for a max value