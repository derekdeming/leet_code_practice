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


'''


# ------------------ Time and Space Complexity Explanation ------------------
'''


'''