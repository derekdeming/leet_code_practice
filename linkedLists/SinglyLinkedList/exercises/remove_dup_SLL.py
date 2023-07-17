class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None: 
            result += f'{temp_node.value} -> '
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

# ---------- ANOTHER SOLUTION ----------
    def remove_duplicates(self):
        if not self.head: 
            return "Linked list is empty."
        node_values = set()
        current_node = self.head
        prev_node = None
        while current_node: 
            if current_node.value in node_values:
                prev_node.next = current_node.next
                if current_node.next is None:
                    self.tail = prev_node
            else: 
                node_values.add(current_node.value)
                prev_node = current_node
            current_node = current_node.next
            return f"Duplicates removed. The list now has {len(node_values)} unique values: {node_values}"

# ---------- ONE SOLUTION ----------
    def remove_duplicates(self): 
        if self.head is None: 
            return None
        if self.head.next is None:
            return self.head
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            if next_node is None:
                break
            if current_node.value == next_node.value:
                current_node.next = next_node.next
                self.length -= 1
            else:
                current_node = next_node
        return self.head
    
# ---------- SECOND SOLUTION ----------
    def remove_duplicates(self):
        if self.head is None: 
            return None 
        node_values = set() # Sets are used here because they only allow unique values and have O(1) lookup time.
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next: 
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node



# ------------------ Code Explanation ------------------
'''
if current_node.next.value in node_values -- Checks if the value of the next node is in the 
node_values set, which would mean it's a duplicate.

current_node.next = current_node.next.next -- If the value is a duplicate, this line "skips" 
the next node, effectively removing it from the linked list by adjusting the next pointer of the 
current node to point to the node after the next one.

'''


# ------------------ Time and Space Complexity Explanation ------------------
'''
Time Complexity - O(n) -- The algorithm traverses the linked list once, so the time complexity
Overall, the time complexity of the remove_duplicates method is O(n), where n is the number 
of nodes in the linked list. This is because the while loop iterates through the list once, 
performing constant-time operations in each iteration.

Space Complexity - O(1) -- may depend on which solution you take 
The space complexity of the remove_duplicates method is O(1), as the space used does not grow 
with the size of the input. It only requires a constant amount of extra space to store the 
set node_values.

'''