
# Insert at the Beginning
# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the 
# beginning of the original tuple.

# Example

input_tuple = (2, 3, 4)
value_to_insert = 1
# output_tuple = insert_value_front(input_tuple, value_to_insert)
# print(output_tuple)  # Expected output: (1, 2, 3, 4)

def insert_value_front(input_tuple, value_to_insert):
    lst = list(input_tuple)
    lst.insert(0, value_to_insert)
    return tuple(lst)

print(insert_value_front(input_tuple, value_to_insert))




# second solution:
def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

'''
return (value_to_insert,) + input_tuple - Create a new tuple with the given value as the first element and 
concatenate the original tuple "input_tuple" to it. The comma after the value is necessary to 
create a single-element tuple. Return the new tuple.


Overall time complexity = O(n)
Space complexity = O(n) because it creates a new tuple with n+1 elements.
'''