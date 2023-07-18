class Node: 
    def __init__(self, value=None): 
        self.value = value
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        node = self.head
        while node: 
            yield node
            if node.next == self.head:
                break
            node = node.next

    def create_circular_sll(self, node_value): # O(1) time | O(1) space
        node = Node(node_value)  # O(1) time | O(1) space
        node.next = node   # O(1) time | O(1) space
        self.head = self.tail = node   # O(1) time | O(1) space
        return "The circular singly linked list has been created"
    
CircularSLL_ = CircularSLL()
CircularSLL_.create_circular_sll(1)    # O(1) time | O(1) space

print([node.value for node in CircularSLL_])


'''
Time Complexity: 0(1)

Space Complexity: 0(1)

'''