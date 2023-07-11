# inserting an element into a specific location in a singly linked list 
'''
new_node = Node(50)
temp_node = self.head
for _ in range(index - 1):
    temp_node = temp_node.next
new_node.next = temp_node.next
temp_node.next = new_node
'''

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
    def insert(self, index, value): 
        new_node = Node(value)   # O(1)
        if index < 0 or index > self.length:   # O(1)
            return False
        if self.length ==0: 
            self.head = new_node   # O(1)
            self.tail = new_node   # O(1)
        elif index == 0: 
            new_node.next = self.head   # O(1)
            self.head = new_node
        else: 
            temp_node = self.head   # O(1)
            for _ in range(index-1):    # O(n)
                temp_node = temp_node.next   # O(1)
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length  += 1   # O(1)
        return True
# *****************************************************
    
        
new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.prepend(5)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
new_linked_list.insert(3, 50)
print(new_linked_list)

# Time complexity = O(n)
# Space complexity = O(1)