# -*- coding: utf-8 -*-

'''
Problem Statement
Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a) 
target_node.value
4

    
'''

# This is the formula


def nth_to_last_node(n, head): # I didn't consider if the n is larger than the linked list length
    count = 0
    stop_head = head
    while head is not None:
        count +=1 
        head = head.nextnode # Get the whole length of the head
    stop_point = count - n 
    for i in range (0,stop_point):
        stop_head = stop_head.nextnode
    return stop_head

# This is Jose's answer 
def nth_to_last_node(n, head):

    left_pointer  = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in range(0, n-1):
        
        # Check for edge case of not having enough nodes!
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.nextnode

    # Move the block down the linked list
    while right_pointer.nextnode:
        left_pointer  = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    # Now return left pointer, its at the nth to last element!
    return left_pointer

# Here is the test
from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(2,a),d)
        print('ALL TEST CASES PASSED')
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node)


















class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        
def reverse(head):
    
    # Set up current,previous, and next nodes
    current = head
    previous = None
    nextnode = None

    # until we have gone through to the end of the list
    while current:
        
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        nextnode = current.nextnode

        # Reverse the pointer ot the next_node
        current.nextnode = previous

        # Go one forward in the list
        previous = current
        current = nextnode

    return previous

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

d.nextnode.value

reverse(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)

print a.nextnode.value # This will give an error since it now points to None