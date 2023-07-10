
# Concatenate
# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

# Example

input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)  # Expected output: 'Hello World from Python'

def concatenate_strings(input_tuple): 
    return ' '.join(input_tuple)

print(concatenate_strings(input_tuple))

'''
Use the join method on a space character ' ' to concatenate the strings in the input tuple 
input_tuple" with a space as the separator. Return the resulting concatenated string.

The join method has a linear time complexity O(n) because it iterates through each string in the input tuple. 
The space complexity is also O(n) because it creates a new concatenated string with the length equal 
to the sum of the lengths of the strings in the input tuple plus the spaces in between.
'''