# Best Score
# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

# 
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87


def first_second(my_list):
    my_list.sort(reverse=True)
    return my_list[0], my_list[1]

print(first_second(myList)) # (90, 87)

# solution using arrows and pointers 

def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')

    for num in my_list: 
        if num > max1: 
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
    return max1, max2

print(first_second(myList)) # (90, 87)


# solution with time complexity and space complexity explanation
"""
time complexity: O(n) for this solution
- the function iterates through the list once with each iteration taking constant time to perform comparisons and assignments.
- Since there are n elements in the list, the overall time complexity of the function is O(n).

space complexity: O(1) for this solution
- the function uses a constant amount of additional space to store the variables. There are no other data structures used.

"""