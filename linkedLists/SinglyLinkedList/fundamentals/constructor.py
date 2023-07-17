# node class constructor 

class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None

# new_node = Node(10)
# print(new_node.value)
# Time and space complexity = O(1)




# Linked list constructor - creation of singly linked list 
class LinkedList: 
    def __init__(self, value):
        new_node = Node(value) # O(1)
        self.head = new_node # O(1)
        self.tail = new_node # O(1)
        self.length = 1  # O(1)

new_linked_list = LinkedList(10)
print(new_linked_list)
print(new_linked_list.head)
print(new_linked_list.head.value)

# create linked list without value in it -- simply the creation of a linkedlist with head and tail pointing at None 
class _LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

linked_list_instantiated = _LinkedList()
print(linked_list_instantiated.length)