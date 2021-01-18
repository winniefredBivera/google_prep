# linked list implementation

class linked_list:
    """interface for linked list"""

    first_node = None

    def is_empty(self):
        """return True if not empty"""
        output = True if self.first_node is None else False
        return output

    def insert(self, node_element):
        """insert a node in the link list"""
        node_element.next = self.first_node
        self.first_node = node_element

    def search_element(self, value):
        """find first instance of a value in linked list"""
        current_element = self.first_node
        output = None

        # edge case
        if current_element is None:
            print("No element is in the link list to search")

        # elements are present in the list
        else:

            while current_element.next is not None and current_element.element != value:
                current_element = current_element.next

            if current_element.next is None:
                print("reached end of the list")

            if current_element.element == value:
                print("found element in list")
                output = value
            else:
                print("element not found in list")

        return output

    def delete_first_node(self):
        """delete first node"""
        if self.first_node is None:
            print("nothing left to delete")
        else:
            first_node = self.first_node
            second_node = first_node.next
            self.first_node = second_node
            print("deleted first element")
            print("first element was: " + str(first_node.element))

    def delete_element(self, value):
        """delete first occurance from linked list"""
        current_node = self.first_node
        previous_node = None

        # edge case: empty list
        if self.first_node is None:
            print("nothing is left to delete")

        elif self.first_node.element == value:
            # edge case: first element to be deleted
            self.delete_first_node() 

        else:

            while current_node.next is not None and current_node.element != value:
                
                previous_node = current_node
                current_node = current_node.next

            if current_node.next is None and current_node.element != value:
                print("reached end of the list")
                print("element is not present in list")
            
            elif current_node.element == value:
                print("element is found")
                next_node = current_node.next
                previous_node.next = next_node
            else:
                print("element is not present in linked list")
