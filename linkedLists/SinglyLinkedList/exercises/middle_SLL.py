# Write a function to find and return the middle node of a singly linked list. 
# If the list has an even number of nodes, return the second of the two middle nodes.

# Approach: The approach, often called the "fast and slow pointer" technique or 
# "tortoise and hare" algorithm, allows you to traverse the list only once, instead 
# of first counting the elements and then accessing the middle one

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return self.head
        slow = fast = self.head
        while fast is not None and fast.next is not None: 
            slow = slow.next
            fast = fast.next.next
        return slow


# ------------------ Code Explanation ------------------
'''
def find_middle(self): - This line defines a new method find_middle in the LinkedList class. 
This method will be used to find the middle node of the linked list.

if self.head is None: - This line checks if the head of the linked list is None. 
If it is, that means the list is empty and there is no middle node to find.

return None - If the linked list is empty (i.e., if self.head is None), this line will end 
the function and return None. This is because there is no middle node in an empty list.

slow = self.head - This line initializes the slow pointer at the head of the linked list. 
This pointer will move one node at a time through the list.

fast = self.head - This line initializes the fast pointer also at the head of the linked list. 
This pointer will move two nodes at a time through the list.

while fast and fast.next: - This line starts a while loop that will continue as long as 
both fast and fast.next are not None. This ensures that we do not try to access a None value 
in the next line, which would raise an error.

slow = slow.next - This line moves the slow pointer one node forward in the list.

fast = fast.next.next - This line moves the fast pointer two nodes forward in the list. 
Because fast moves twice as fast as slow, by the time fast reaches the end of the list, 
slow will be at the middle.

return slow - After the while loop, the slow pointer will be at the middle of the linked list. 
This line returns the slow node, which is the middle node of the list.

'''


# ------------------ Time and Space Complexity Explanation ------------------
'''
Time Complexity:

The time complexity is O(n), where n is the number of nodes in the linked list. This is 
because in the worst-case scenario, we have to traverse the whole linked list. Here, the 'fast' 
pointer is moving twice as fast as the 'slow' pointer, but it essentially goes through the entire 
list (or nearly the entire list in the case of an even number of nodes), so the time complexity 
is proportional to the size of the list, i.e., O(n).


Space Complexity:

The space complexity is O(1), which means that the space required does not change with the size 
of the input linked list, hence it's constant. This is because we are only using a fixed amount 
of space to store the 'slow' and 'fast' pointers, and we are not using any additional data structures 
like arrays or other linked lists whose size would scale with the input size. No matter how large 
the input linked list is, we only ever need two nodes ('slow' and 'fast') at any given time, so the 
space complexity is O(1).

'''