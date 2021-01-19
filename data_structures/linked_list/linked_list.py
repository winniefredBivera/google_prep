# linked list implementation

class LinkedList:
    """interface for linked list"""

    first_nod = None

    def __init__(self):
        self.first_node = None

    def is_empty(self):
        """return True if not empty"""
        output = True if self.first_node is None else False
        return output

    def insert_first(self, node_element):
        """insert a node in the link list"""
        node_element.next = self.first_node
        self.first_node = node_element

    def search(self, value):
        """find first instance of a value in linked list"""
        current_element = self.first_node

        # edge case
        if current_element is None:
            print("No element is in the link list to search")
            output = None

        # elements are present in the list
        else:
            output = self._search_when_list_is_not_empty(value)
        return output

    def _search_when_list_is_not_empty(self, value):
        """search when we know that the list is not empty"""
        current_element = self.first_node

        while current_element.next is not None and current_element.element != value:
            current_element = current_element.next

        if current_element.next is None:
            print("reached end of the list")
            output = None

        if current_element.element == value:
            print("found element in list")
            output = current_element

        else:
            print("element not found in list")
            output = None

        return output

    def delete_first(self):
        """delete first node"""
        if self.first_node is None:
            print("nothing left to delete")
        else:
            first_node = self.first_node
            second_node = first_node.next
            self.first_node = second_node
            print("deleted first element")
            print("first element was: " + str(first_node.element))

    def delete(self, value):
        """delete first occurance from linked list"""
        current_node = previous_node = self.first_node

        # edge case: empty list
        if self.first_node is None:
            print("nothing is left to delete")
        else:
            self._delete_element_when_list_is_not_empty(value)

    def _delete_element_when_list_is_not_empty(self, value):
        """special case when list is not empty"""
        current_node = previous_node = self.first_node

        while current_node.next is not None and current_node.element != value:
            previous_node = current_node
            current_node = current_node.next

        if current_node.next is None and current_node.element != value:
            print("reached end of the list")
            print("element is not present in list")

        elif self.first_node.element == current_node.element == previous_node.element == value:
            # edge case first node
            self.delete_first()

        elif current_node.element == value:
            print("element is found")
            next_node = current_node.next
            previous_node.next = next_node
        else:
            print("element is not present in linked list")

    def parse_print(self):
        current_node = self.first_node
        self.parse_recursively(current_node)

    def parse_recursively(self, node):
        if node is not None:
            print(node.element)
            self.parse_recursively(node.next)

    def get_middle_node(self):
        if self.first_node is None:
            output = None
        else:
            current_node = pointer_2 = self.first_node
            node_count = 0

            while current_node.next is not None:
                current_node = current_node.next
                node_count = node_count+1
                if node_count % 2 == 0:
                    pointer_2 = pointer_2.next
        return pointer_2

    def no_of_nodes(self):
        count = 0
        current_element = self.first_node
        while current_element.next is not None:
            current_element = current_element.next
            count = count + 1
        return count

    def get_n_nodes_before_last_node(self, n):
        pointer_2 = current_element = self.first_node
        record_count = 0

        # get nth node first
        for i in range(n):
            current_element = current_element.next

        while current_element.next is not None:
            current_element = current_element.next
            pointer_2 = pointer_2.next

        return pointer_2

