# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.

# Example

# remove_duplicates([1, 1, 2, 2, 3, 4, 5])
arr = [1, 1, 2, 2, 3, 4, 5]
# Output : [1, 2, 3, 4, 5]

def remove_duplicates(arr):
    new_list = []
    for num in arr:
        # if the number is not in the new list, append the number to the new list
        if num not in new_list:
            new_list.append(num)
    return new_list

print(remove_duplicates(arr))


def remove_dups(arr): 
    unique_list = []
    seen = set()
    for item in arr: 
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

print(remove_dups(arr))

# time complexity analysis: 
'''
- creating an empty list takes constant time, O(1)
- creating an empty set takes constant time, O(1)
- looping through the array takes O(n) time, where n is the length of the array
- checking if an item is in a set takes O(1) time
- adding an item to a set takes O(1) time
- appending an item to a list takes O(1) time
- so the total time complexity is O(n) for this solution
'''


#  space complexity: O(n) since we use additional data structures (list and set) to store the unique elements