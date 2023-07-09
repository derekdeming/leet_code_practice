
# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

# Example

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

def tuple_elementwise_sum(tuple1, tuple2):
    print(zip(tuple1, tuple2))
    return tuple(map(sum, zip(tuple1, tuple2)))

print(tuple_elementwise_sum(tuple1, tuple2))

# zip(tuple1, tuple2) combines the corresponding elements of tuple1 and tuple2 into pairs. 
# In this case, it produces the pairs (1, 4), (2, 5), and (3, 6).

# map(sum, ...) applies the sum function to each pair of elements obtained from zip. 
# It calculates the sum of each pair, resulting in the values 5, 7, and 9.

'''
return tuple(map(sum, zip(tuple1, tuple2))) - This line has multiple operations: 
a. zip(tuple1, tuple2) - The zip function has a linear time complexity O(n), where n is the length of the input tuples, 
as it iterates through each element in both input tuples to create pairs. The space complexity is also O(n) 
because it creates an iterator containing n pairs. 

b. map(sum, zip(tuple1, tuple2)) - The map function has a linear time complexity O(n), as it applies 
the sum function to each pair created by the zip function. The space complexity is O(n) because it creates 
an iterator containing n element-wise sums. 

c. The tuple(map(sum, zip(tuple1, tuple2))) - The tuple constructor has a linear time complexity O(n) 
because it iterates through the iterator returned by the map function to create a new tuple. 
The space complexity is O(n) because it creates a new tuple with n element-wise sums.

The time complexities of the zip, map, and tuple operations are all linear, O(n), but they are combined in a 
single line, so the overall time complexity for this line is still O(n).
'''



#Second solution
def tuple_elementwise_sum2(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError('Input tuples must have the same length')
    # result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return tuple(a + b for a, b in zip(tuple1, tuple2))
    
print(tuple_elementwise_sum2(tuple1, tuple2))

'''
Overall time complexity of the second function is O(n) because it iterates through each pair of elements 
in the input tuples once. The overall space complexity is O(n) because the function creates a new tuple 
with the same length as the input tuples to store the element-wise sums.
'''