# Here is an implementation of a doubly linked list in Python:

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.next


# ${INSERT_HERE}
# create a new doubly linked list
my_list = DoublyLinkedList()

# append some data
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_list()
# prepend some data
my_list.prepend(0)
my_list.print_list()
# delete some data
my_list.delete(2)
# print the list
my_list.print_list()
