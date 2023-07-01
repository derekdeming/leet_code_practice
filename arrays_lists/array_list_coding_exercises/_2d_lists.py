# given 2D list calculate the sum of diagonal elements

# example: 

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# diagonal_sum(my_list)  # 15

def diagonal_sum(my_list):
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i][i]
    return sum

print(diagonal_sum(my_list))

# explanation: 
'''
1.loop should iterate the length of the matrix (number of rows) and add the element at the ith row and ith column to the sum.
2. using sum += my_list[i][i] to add the value of the diagonal element at the current index to the sum. The diagonal
element is the one where the row and column indices are the same (i.e. row 0, column 0; row 1, column 1; row 2, column 2, etc.).
or in this case my_list[0][0], my_list[1][1], my_list[2][2]

time complexity: O(n) for this solution
- where n in the number of rows (or columns) in the matrix. The function iterates through the rows once 

space complexity: O(1) for this solution
- the function only uses a single variable to store the sum 
'''