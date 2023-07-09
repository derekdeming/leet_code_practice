
# Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.

# Example

input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24

def sum_product(input_tuple):
    # TODO
    sum_result = 0 
    product_result = 1
    for i in range(len(input_tuple)):
        sum_result += input_tuple[i] 
        product_result *= input_tuple[i]
    return sum_result, product_result

sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)

'''
Time and Space Complexity

sum_result = 0 - Constant time complexity O(1) because it's a single assignment operation. 
Constant space complexity O(1) because it stores a single integer.

product_result = 1 - Constant time complexity O(1) because it's a single assignment operation. 
Constant space complexity O(1) because it stores a single integer.

for num in t: - Linear time complexity O(n) for the loop, where n is the number of elements in the tuple. 
This is because the loop iterates through each element in the tuple once. No additional space is used in the loop.

sum_result += num - Constant time complexity O(1) for each addition operation inside the loop.

product_result *= num - Constant time complexity O(1) for each multiplication operation inside the loop.

return sum_result, product_result - Constant time complexity O(1) because it returns a tuple with two integers. 
Constant space complexity O(1) because it creates a tuple with two integers.

Time complexity = O(n)
Space complexity = O(1)
'''