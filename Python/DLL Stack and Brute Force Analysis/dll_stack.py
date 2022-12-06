# https://www.geeksforgeeks.org/python-stack-using-doubly-linked-list/
# Class to create a new node
class Node:

    def __init__(self, data):
        # Assign data
        self.data = data
        # Initialize next node as null
        self.next = None
        # Initialize previous node as null
        self.prev = None


# Class to create and handle the stack of nodes
class Stack:

    def __init__(self):
        # Initialize head as null
        self.head = None

    # Function to add node to the stack
    def push(self, data):
        # If the stack is empty, create a starting node
        if self.head is None:
            self.head = Node(data)
        # If the stack is not empty, create a new node
        else:
            # Create a new node
            new_node = Node(data)
            # Set the new node's next to the current head
            new_node.next = self.head
            # Set the previous to null
            new_node.prev = None
            # Set the current head's previous to the new node
            self.head.prev = new_node
            # Set the new node as the head
            self.head = new_node

    # Function to remove node from the stack
    def pop(self):
        # If the stack is empty, return null
        if self.head is None:
            return None
        # If the next node is null, set the head to null
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        # If the stack is not empty, remove the head
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    # Function to return the top of the stack
    def top(self):
        return self.head.data

    # Function to return the size of the stack
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    # Function to return whether the stack is empty or not
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Prints all nodes of the stack separated by a "-> "
    def print_stack(self):
        print("Cryptex lock secret stack:")
        temp = self.head
        while temp:
            # https://stackoverflow.com/questions/39432063/can-i-include-a-for-loop-inside-my-print-statement
            # https://www.tutorialspoint.com/How-to-write-inline-if-statement-for-print-in-Python
            print("{}".format(temp.data + ("-> " if temp.next else "\n")), end="")
            temp = temp.next
