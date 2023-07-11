# insert an element at the beginning of a singly linked list - prepend method 
class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None
        
class LinkedList:
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None: 
            result += str(temp_node.value)
            if temp_node.next is not None: 
                result += ' -> ' 
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)  # O(1)
        if self.head is None:   # O(1)
            self.head = new_node   # O(1)
            self.tail = new_node   # O(1)
        else: 
            self.tail.next = new_node   # O(1)
            self.tail = new_node   # O(1)
        self.length += 1   # O(1)
# *****************************************************
    def prepend(self, value):
        new_node = Node(value)   # O(1)
        if self.head is None:   # O(1)
            self.head = new_node  # O(1)
            self.tail = new_node  # O(1)
        else: 
            new_node.next = self.head   # O(1)
            self.head = new_node  # O(1)
        self.length += 1  # O(1)
# *****************************************************
        
new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.prepend(5)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)

# Time complexity for append method is O(1)
# Space complexity for append method is O(1)