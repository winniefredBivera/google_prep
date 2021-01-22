"""
STACKS
winniefred bivera
"""

from node import Node
from linked_list import LinkedList

class Stack:
    ll = None
    
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        item_node = Node(item)
        self.ll.insert_first(item_node)

    def pop(self):
       top_of_the_stack = self.ll.delete_first()
       return top_of_the_stack 
