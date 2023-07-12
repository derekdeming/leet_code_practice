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
    
    def traversal(self): 
        current = self.head   # O(1)
        while current:     # O(n)
            print(current.value)
            current = current.next   # O(1)

    def search(self, target_value):
        current = self.head   # O(1)
        index = 0 
        while current:      # O(n)
            if current.value == target_value:  # O(1)
                return True
            current = current.next  # O(1)
            index += 1
        return -1 
    
    def get(self, index): 
        if index == -1:   # O(1)
            return self.tail
        if index < -1 or index >= self.length:  # O(1)
            return None
        current = self.head
        for _ in range(index): # O(n)
            current = current.next
        return current

    def set_value(self, index, value): 
        temp = self.get(index)  # O(n)
        if temp: 
            temp.value = value  # O(1)
            return True
        return False 

# *****************************************************
    def pop_first(self):
        if self.length == 0:   # O(1)
            return None
        popped_node = self.head  # O(1)
        if self.length == 1: 
            self.head = None  # O(1)
            self.tail = None
        else:
            self.head = self.head.next  # O(1)
            popped_node.next = None
        self.length -= 1
        return popped_node.value  # O(1)


new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.prepend(5)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.insert(3, 50)
new_linked_list.traversal()
print(new_linked_list.search(50))
print(new_linked_list.get(-1))
print(new_linked_list)
print(new_linked_list.set_value(2, 45))
print(new_linked_list)
print(new_linked_list.pop_first())





# Time complexity = O(1)
# Space complexity = O(1) - uses a fixed amount of space 