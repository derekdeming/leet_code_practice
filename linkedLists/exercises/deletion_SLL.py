class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None

class Linkedlist(self): 
    def __init(self):
        self.head = self.tail = None 
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
        new_node = Node(value)
        if self.head is None: 
            self.head = self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node 
        self.length += 1 

    def remove(self, index): 
        if index < 0 or index >= self.length:
            return None 
        # if node to be removed is the head node 
        elif index == 0: 
            popped_node = self.head
            if self.length == 1: 
                self.head = self.tail = None 
            else: 
                self.head = self.head.next
            popped_node.next = None 
            self.length -= 1
            return popped_node
        else: 
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            popped_node = temp.next

            # if node to be removed is the tail node 
            if popped_node.next is None: 
                self.tail = temp 
            temp.next = temp.next.next
            popped_node.next = None
            self.length -= 1 
            return popped_node

# time complexity = O(n)
# space complexity = O(1)

# Code explanation: 
'''
1. def remove(self, index):: This line defines the remove method, which is going to take an instance of the LinkedList class (self) and an index as arguments.

2. if index < 0 or index >= self.length:: This conditional checks whether the provided index is out of the range of valid indices for the linked list (less than 0 or greater than or equal to the number of nodes in the list).

3. return None: If the above condition is met (the index is out of range), the function returns None and exits.

4. elif index == 0:: This conditional checks whether the provided index is 0, meaning that the head of the list should be removed.

5. popped_node = self.head: If the head is to be removed, the method saves a reference to it in the popped_node variable.

6. if self.length == 1:: This conditional checks whether the list only contains one node.

7. self.head = None: If there is only one node, it removes the node by setting the head of the list to None.

8. self.tail = None: Similarly, it sets the tail of the list to None, effectively removing the single node in the list.

9. else:: This is the alternative case where the list contains more than one node.

10. self.head = self.head.next: It removes the head by setting the head of the list to the next node in the list.

11. popped_node.next = None: It disconnects the original head node from the list by setting its next reference to None.

12. self.length -= 1: It decreases the length of the list by 1 to account for the removed node.

13. return popped_node: It returns the removed node.

14. else:: This is the alternative case where the node to be removed is not the head.

temp = self.head: It sets temp to the head of the list to start a traversal.

for _ in range(index - 1):: It starts a loop to reach the node preceding the one to be removed.

temp = temp.next: Inside the loop, it advances temp to the next node in each iteration.

popped_node = temp.next: After reaching the node preceding the one to be removed, it saves a reference to the node to be removed in popped_node.

if popped_node.next is None:: This checks if the popped_node is the last node (its next attribute is None).

self.tail = temp: If popped_node is the last node, it updates the tail of the list to temp, which is the new last node after the removal.

temp.next = temp.next.next: It removes popped_node by skipping it in the linked list. It sets the next reference of the node preceding popped_node to the node following popped_node.

popped_node.next = None: It disconnects popped_node from the list by setting its next reference to None.

self.length -= 1: It decreases the length of the list by 1 to account for the removed node.

return popped_node: It returns the removed node.
'''