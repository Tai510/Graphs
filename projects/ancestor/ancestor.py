
# Clarifications:
# The input will not be empty.
# There are no cycles in the input.
# There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# IDs will always be positive integers.
# A parent may have any number of children.

# from util import Stack, Queue 

# Translate the problem into graph terminology
# Build your graph
# Traverse your graph

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    # Create connection queue
    connection = {}
    
        
    
    

