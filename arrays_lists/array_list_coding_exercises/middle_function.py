# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
#  excluding the first and last elements

# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]

def middle(lst): 
    return lst[1:-1]

myList = [1, 2, 3, 4]
print(middle(myList))  


# Solution with time complexity and space complexity explanation
"""
time complexity: O(n) for this solution
the function has a time complexity of O(n) where n is the length of the list. The reason is that slicing a list takes linear time 
proportional to the length of the slice. In this case, the slice goes from index 1 to the second to last index, 
so the length of the slice is n-2. Therefore, the time complexity is O(n-2) which is equivalent to O(n).

space complexity: O(n) for this solution
the space complexity of the function is also O(n) because it returns a new list that is a slice of the original list. The
new list has n-2 elements which is still in the order of O(n). The memory usage is proportional to the length of the list.
"""