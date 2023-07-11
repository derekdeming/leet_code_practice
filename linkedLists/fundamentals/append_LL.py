# insert an element at the end of singly linked list - append method 

#  pointing at 10       tail (pointing at 40)
#  HEAD --> 10 --> 20 --> 30 --> 40 --> None 
#  We will update 40 --> None to point at 50 --> None and then update Tail to point at 50 

# edge cases: if the linked list is None then making sure each pointer will point to a newly appended node 
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


        
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
# print(new_linked_list.head.value)
# print(new_linked_list.tail.value)

# Time complexity for append method is O(1)
# Space complexity for append method is O(1)