class Node: 
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSLL:
    def __init__(self, value=None):
        self.head = self.tail = None

    def __iter__(self):
        node = self.head
        while node: 
            yield node
            if node.next == self.tail.next:
                break

    def create_circular_sll(self, node_value):
        node = Node(node_value)
        node.next = node 
        self.head = self.tail = node
        return "The circular singly linked list has been created"
    

    def insert_circular_sll(self, node_value, loc):
        if self.head is None: 
            return "The head reference is None"
        else:
            new_node = Node(node_value)
            if loc == 0:
                new_node.next = self.head  #  O(1)
                self.head = new_node
                self.tail.next = new_node
            elif loc == 1:
                new_node.next = self.tail.next  #  O(1)
                self.tail.next = new_node
                self.tail = new_node   
            else:
                temp_node = self.head  #  O(1)
                index = 0
                while index < loc - 1: #  O(n)
                    temp_node = temp_node.next  #  O(1)
                    index += 1
                next_node = temp_node.next  #  O(1)
                temp_node.next = new_node  #  O(1)
                new_node.next = next_node  #  O(1)
                return "The node has been successfully inserted"

circularSLL = CircularSLL()
print(circularSLL.create_circular_sll(1))
circularSLL.insert_circular_sll(0, 0)
circularSLL.insert_circular_sll(3, 1)
circularSLL.insert_circular_sll(1, 2)
circularSLL.insert_circular_sll(2, 3)

print([node.value for node in circularSLL])  

# ------------------ Code Explanation ------------------
'''

'''


# ------------------ Time and Space Complexity Explanation ------------------
'''
Time Complexity: O(n)




Space Complexity: O(1)



'''