"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)                            
        if not self.value: 
            self.value = value        
        elif value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)             

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):                     # target is the value we're searching for 
        if self.value == target:                    # if the self.value equals target
            return True                             # return True
        if target < self.value:                     # if the target we're searching for is less than self.value
            if not self.left:                   # no left child exists
                return False                        # return false
            else:                                   # a left child exists
                return self.left.contains(target)   # try again, only start the search from here    
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
            

    # Return the maximum value found in the tree
    def get_max(self):                              # get_max function definition
        if not self.right:                 # if self.value is less than the right child tree node
            return self.value
        else:                                       # there is no right value
            return self.right.get_max()                     # return the self.value (the self.value is the max value by default)
        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):                         # for_each node found, run a function called fn on the value i.e., fn(self.value)
        fn(self.value)                              # fn(self.value) is run on each node's value 
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = queue.Queue()
        queue.put(node)

        while queue.qsize() > 0:
            current_node = queue.get()
            print(current_node.value)
            if current_node.left:
                queue.put(current_node.left)
            if current_node.right:
                queue.put(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = stack.Stack()
        stack.push(node)
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
