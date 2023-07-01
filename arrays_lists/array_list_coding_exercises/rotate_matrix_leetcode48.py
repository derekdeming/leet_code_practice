# Rotate Matrix/ Image - LeetCode 48
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.

# Example:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix): 
    # transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for row in range(len(matrix)):
        matrix[row].reverse()
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

# explanation: 
'''
transpose the matrix: 
1. for i in range(n): - start a loop that iterates over the rows 
2. for j in range(i, n): - start a nested loop that iterates over the columns starting from the current row index
- this ensures we only swap elements in the upper triangle of the matrix avoiding double swaps 
3. matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] - swap the elements at the current indices (i,j) and (j,i)
4. reverse each row:

'''

# Time Complexity: O(n^2)
#  because both the transpose and reverse steps involve nested loops that iterate over all the elements in the matrix 

# Space Complexity: O(1) - in-place rotation without allocating any additional data structures 