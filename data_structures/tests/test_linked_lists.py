# unit test cases for linked lists
import unittest
from linked_list.linked_list import LinkedList as ll
from linked_list.node import Node


class LinkedListTesting(unittest.TestCase):

    def test_is_empty_empty(self):
        test_ll = ll()
        output = test_ll.is_empty()
        expected_output = True
        self.assertEqual(output, expected_output)

    def test_is_empty_not_empty(self):
        test_ll = ll()
        test_node = Node(1)
        test_ll.insert_first(test_node)
        output = test_ll.is_empty()
        expected_output = False
        self.assertEqual(output, expected_output)

    def test_search_empty(self):
        test_ll = ll()
        output = test_ll.search(1)
        expected_output = None
        self.assertEqual(output, expected_output)

    def test_search_true_not_empty(self):
        test_ll = ll()
        test_node = Node(1)
        test_ll.insert_first(test_node)
        output = test_ll.search(1)
        self.assertEqual(output.element, test_node.element)

    def test_search_false_not_empty(self):
        test_ll = ll()
        test_node = Node(1)
        test_ll.insert_first(test_node)
        output = test_ll.search(2)
        expected_output = None
        self.assertEqual(output, None)

    def test_delete_first_empty(self):
        test_ll = ll()
        test_node_1 = Node(1)
        test_ll.insert_first(test_node_1)
        test_ll.delete_first()
        output = test_ll.is_empty()
        expected_output = True
        self.assertEqual(output, expected_output)

    def test_delete_first_not_empty(self):
        test_ll = ll()
        test_node_1 = Node(1)
        test_node_2 = Node(2)
        test_ll.insert_first(test_node_1)
        test_ll.insert_first(test_node_2)
        test_ll.delete_first()
        first_node = test_ll.first_node
        expected_output = 1
        self.assertEqual(first_node.element, expected_output)

    def test_delete_element_first(self):
        test_ll = ll()
        for i in range(0, 5):
            test_ll.insert_first(Node(i))
        test_ll.delete(4)
        first_element = test_ll.first_node.element
        expected_first_element = 3
        self.assertEqual(first_element, expected_first_element)

    def test_delete_element(self):
        test_ll = ll()
        for i in range(0, 5):
            test_ll.insert_first(Node(i))
        test_ll.delete(2)
        search_output = test_ll.search(2)
        expected_output = None
        self.assertEqual(search_output, expected_output)
