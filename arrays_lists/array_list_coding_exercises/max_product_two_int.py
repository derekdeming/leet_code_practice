# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) # Output: 63 (9*7)

def max_prod(arr): 
    max_prod = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]*arr[j] > max_prod:
                max_prod = arr[i]*arr[j]
    return max_prod
print(max_prod(arr))

#  time complexity: O(n^2) for this solution 


def max_prod2(arr):
    max1, max2 = 0, 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1*max2
print(max_prod2(arr))

# time complexity: O(n) for this solution

# Solution with time complexity explanation 
def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization
 
    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment
 
    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication
 
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)