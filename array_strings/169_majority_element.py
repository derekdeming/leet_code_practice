# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# SOLUTION 
from typing import List
#  Boyer-Moore Voting Algorithm - 

class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        candidate = None
        count = 0

        for num in nums: 
            if count == 0: 
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1 
        return candidate

# Explanation:

# The algorithm starts by assuming the first element as the majority candidate and sets the count to 1.
# As it iterates through the array, it compares each element with the candidate:
# a. If the current element matches the candidate, it suggests that it reinforces the majority element because it appears again. Therefore, the count is incremented by 1.
# b. If the current element is different from the candidate, it suggests that there might be an equal number of occurrences of the majority element and other elements. Therefore, the count is decremented by 1.
# Note that decrementing the count doesn't change the fact that the majority element occurs more than n/2 times.
# If the count becomes 0, it means that the current candidate is no longer a potential majority element. In this case, a new candidate is chosen from the remaining elements.
# The algorithm continues this process until it has traversed the entire array.
# The final value of the candidate variable will hold the majority element.
# Explanation of Correctness:
# The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the array. This assumption guarantees that even if the count is reset to 0 by other elements, the majority element will eventually regain the lead.

# Moore's Voting Algorithm is O(n) time complexity because it traverses the array once 


# SOLUTION 2
class Solution: 
    def majorityElement(self, nums: List[int]) -> int: 
        nums.sort()
        n = len(nums)
        return nums[n//2]
    

# Explanation of the above solution 2 
# Once the array is sorted, the majority element will always be present at index n/2, where n is the size of the array.
# This is because the majority element occurs more than n/2 times, and when the array is sorted, it will occupy the middle position.
# The code returns the element at index n/2 as the majority element.
# The time complexity of this approach is O(n log n) since sorting an array of size n takes O(n log n) time.

solution = Solution()
# print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([2,2,1,1,1,1,1,2,2]))

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109