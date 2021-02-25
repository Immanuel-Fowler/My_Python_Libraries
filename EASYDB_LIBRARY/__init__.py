import os

class DoublyLinkedList:
    
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

    def printList(node):
        last = None
        print("Traversal in forward direction ")
        while (node != None):
            print(node.data, end=" ")
            last = node
            node = node.next
    
        print("\nTraversal in reverse direction ")
        while (last != None):
            print(last.data, end=" ")
            last = last.prev

    def traverse(node, name):
        while(node != None):
            if node == name:
                return node
        pass

class Node:
    
    def __init__(self, next=None, prev=None, data=None):
        self.next = next # reference to next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = data
        self.file = DoublyLinkedList()
        self.dirs = DoublyLinkedList()

global databases
databases = DoublyLinkedList()
        
def mkDatabase(path, database_name):

    if path == "":
        path = os.path.dirname(os.path.abspath(__file__))
    
    os.chdir(path)

    os.mkdir(database_name)
    databases.append(path + "/" + database_name)

def mkData(database_name, file_name):
    path = databases.traverse(database_name)
    os.chdir(path)

    open(path + "/" + file_name, 'a').close()
    databases.file.append(path + "/" + file_name)

def mkDir(database_name, dir_name, parent_dir):
    
    if parent_dir == "" or parent_dir == None:
        path = databases.traverse(database_name)
        os.chdir(path)

        os.mkdir(dir_name)
        databases.dir.append(path + "/" + dir_name)
    else:
        path = databases.traverse(database_name).dirs.traverse(parent_dir)
        os.chdir(path)

        os.mkdir(dir_name)
        databases.dir.append(path + "/" + dir_name)

def writeData(database_name, file_name, input):
    path = databases.traverse(database_name).file.traverse(file_name)

    f = open(path, 'w')
    f.write(input)
    f.close()

def accessData(database_name, file_name):
    path = databases.traverse(database_name).file.traverse(file_name)
    
    f = open(path, 'r')
    output = f.read()
    f.close()

    return output


#Resurces I used to code this :)
#https://www.geeksforgeeks.org/doubly-linked-list/
#https://www.geeksforgeeks.org/python-library-for-linked-list/
#https://www.geeksforgeeks.org/python-library-for-linked-list/
#https://www.geeksforgeeks.org/linked-list-set-1-introduction/
#
#
#
#



