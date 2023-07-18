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

# ------------------ Code Explanation ------------------
'''
class Node: this is the definition of a node class. Each node in the linked list will be an instance of this class.

def __init__(self, value=None): this is the constructor for the node class, it takes a parameter value and sets
the instance variable value to the parameter value. If no value is passed, it defaults to None. It also sets the
instance variable next to None.

self.next = None: this initializes the nodes next attribute to None. The next attribute points to the next node 
in the linked list 

class CircularSLL: this is the definition of the circular singly linked list class. Each instance of this class
will be a circular singly linked list.

def __iter__(self): defines a method which makes an object iterable. Python calls the object's __iter__() method
when a for-loop is used with the object 

while node: begins a while loop that continues as long as node is not None. This means the loop will continue as
long as there is a node to process 

yield node: uses the yield keyword to define a generator. Yield proces a value and suspends the function's execution. 
the function can then be resumed from where it left off, thus allowing it to produce a series of values over time

if node.next == self.head: this checks if the next node is the head of the list. This is a specific condition for 
circular linked lists, where the last node's next attribute points to the head of the list, instead of None. If the
next node is the head of the list, then the loop is broken

'''

