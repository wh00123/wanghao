class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Insert at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    # Delete a node from the list
    def delete(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = current.next

    # Print the list
    def print_list(self):
        if self.head is None:
            return
        current = self.head
        while current.next != self.head:
            print(current.data, end=' ')
            current = current.next


# Create a new linked list
my_list = CircularLinkedList()

# Add some nodes to the list
my_list.insert_at_end(3)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(1)

# Delete a node from the list
my_list.delete(2)

# Print the contents of the list
my_list.print_list()
