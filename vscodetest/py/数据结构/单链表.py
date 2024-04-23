# Define a Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node to the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to add a new node at the beginning of the linked list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to insert a new node after a specified node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Method to print the linked list
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


# Create a new linked list
my_list = LinkedList()

# Add some nodes to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)


# Print the contents of the list
my_list.print_list()
