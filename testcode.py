class Node:
    
    def __init__(self, next=None, prev=None, data=None):
        self.next = next # reference to next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = data

class DoubliyLinkedList:
    
    def __init__(self, data):
        self.head = None

    def push(self, new_data):
        new_node = Node(data = new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = None

        self.head = new_node  

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("This Node doesn't exist")
            return

        new_node = Node(data = new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(data = new_data)
        last = self.head

        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while (last.next is not None):
            last = last.next

        last.next = new_node
        new_node.prev = last














