# Diagonal
# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

# Example

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# output_tuple = get_diagonal(input_tuple)
# print(output_tuple)  # Expected output: (1, 5, 9)

def get_diagonal(tup):
    row = len(tup)
    col = len(tup[0])
    diag = []
    for i in range(row):
        for j in range(col):
            if i == j: 
                diag.append(tup[i][j])
    return tuple(diag)

# print(get_diagonal(input_tuple))


# other solution -- better solution for time and space complexity 

def diagonal(tup):
    return tuple(tup[i][i] for i in range(len(tup)))

print(diagonal(input_tuple))

'''
def get_diagonal(input_tuple): - Define a function called "get_diagonal" that takes a tuple of tuples
 "input_tuple" as an argument. No time or space complexity associated with this line as it is just a 
 function definition.

return tuple(input_tuple[i][i] for i in range(len(input_tuple))) - This line uses a generator expression 
to iterate through the indices i from 0 to the length of the input tuple minus one, and select the diagonal 
elements by indexing the inner tuples with the same index i. The time complexity is O(n), where n is the 
length of the input tuple because it iterates through the indices once. The space complexity is O(n) 
because it creates a new tuple containing the diagonal elements, which has a length equal to the length of the 
input tuple.

'''