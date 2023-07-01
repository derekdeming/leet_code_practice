# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

# Input: nums = [1,2,3,1]
# Output: true
# Hint: Use sets

nums = [1,2,3,1]

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# another solution

def contains_duplicate2(nums):
    seen = set()
    for num in nums:
        if num in seen: 
            return True
        seen.add(num)
        # print(seen)
    return False


print(contains_duplicate2(nums))


# time complexity: O(n) since we loop through the array once
# - since the loop runs n times and all operations inside the loops are constant time operations, the time complexity is O(n)

# space complexity: O(n) since we use a set to store the unique elements