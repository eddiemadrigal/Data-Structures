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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):                            
        if value < self.value:                      # if value is less than self.value                        
            if self.left is None:                   # no left child exists
                self.left = BSTNode(value)          # make the left child node be an instance of BSTNode with value
            else:                                   # a left child exists
                self.left.insert(value)             # recurse until there are no left childs exist
        elif value >= self.value:                   # else if the value coming in is greater than existing self.value
            if self.right is None:                  # if self.right (right child) does not exist
                self.right = BSTNode(value)         # run the value through BSTNode class and assign it to self's right child
            else:                                   # a self.right child node exists
                self.right = insert(value)          # retry the insert(value) function until there are no child nodes left

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):                     # target is the value we're searching for 
        if self.value == target:                    # if the self.value equals target
            return True                             # return True
        if target < self.value:                     # if the target we're searching for is less than self.value
            if self.left is None:                   # no left child exists
                return False                        # return false
            else:                                   # a left child exists
                return self.left.contains(target)   # try again, only start the search from here    
            

    # Return the maximum value found in the tree
    def get_max(self):                              # get_max function definition
        if self.value < self.right:                 # if self.value is less than the right child tree node
            self.value = self.right                 # set the self.value to check for equal the right child tree node
            return self.right.get_max(self.value)   # re-run the function, only this time, start with the current self.value
        else:                                       # there is no right value
            return self.value                       # return the self.value (the self.value is the max value by default)
        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):                         # for_each node found, run a function called fn on the value i.e., fn(self.value)
        fn(self.value)                              # fn(self.value) is run on each node's value 

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        print()
        if self.value is not None:
            print('In order: ')
            self.value.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


r = BSTNode(50)
r.insert(10)
r.in_order_print()