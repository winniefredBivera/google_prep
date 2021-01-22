"""
DOUBLE ENDED LINKED LIST
winniefred bivera
"""
from node import Node

class DoubleEndedLinkedList:
    first = None
    last = None

    def __init__(self):
        self.first = None
        self.last = None

    def insert_first(self, new_node):
        if self.first==None:
            self.first = self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node

    def remove_first(self):
        if self.first==None and self.last==None:
            return None
        elif self.first== self.last:
            item = self.first.element
            self.first = self.last = None
            return item
        else:
            item = self.first.element
            self.first = self.first.next
            return item

    def insert_last(self, new_node):
        if self.first==None :
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def parse_print(self):
        current = self.first
        while current is not None:
            print(current.element)
            current = current.next
