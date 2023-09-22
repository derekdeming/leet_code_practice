# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

from typing import List


# SOLUTION 1:
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         #  initialize pointers for each list 
#         for j in range(n): # 1 
#             nums1[m+j] = nums2[j]  # 1
#         nums1.sort()  # 2

# 1. iterate through each element in nums2, it assigns it to the corresponding position in nums 1 starting from 'm'. This effectively adds the elements from nums2 to the end of nums1. This part of the code is responsible for copying the elements from nums2 to nums1.
# 2. after copying the elements from nums2 to nums1, we sort the array. This adds on a time complexity of O(m log m) where m is the total number of elements in nums1 after merging  


# SOLUTION 2:
class Solution:
        def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            p1, p2 = m -1, n - 1   # 1. 

            # initialize the pointer for the merged list 
            p = m + n - 1   # 1

            #  merge the lists from end to the beginning 
            while p1 >= 0 and p2 >= 0: 
                if nums1[p1] >= nums2[p2]: # 2 
                    nums1[p] = nums1[p1] # 2 
                    p1 -= 1  # 2
                else: 
                    nums1[p] = nums2[p2] 
                    p2 -= 1 
                p -= 1 

            # if there are any remaining elements in nums2, copy them to nums 1 
            while p2 >= 0: # 4 
                nums1[p] = nums2[p2] # 4 
                p2 -= 1  # 4 
                p -= 1   # 4 

# 1. We initialize two pointers, p1 and p2, to keep track of the current positions in nums1 and nums2, respectively. We set p1 to m - 1 and p2 to n - 1 initially, which positions them at the last elements of their respective lists. We initialize a third pointer, p, which will be used to update nums1 in-place while merging. We set p to m + n - 1, which positions it at the end of the merged list.

# 2.  We compare the elements at the current positions p1 in nums1 and p2 in nums2. If the element in nums1 is greater than or equal to the element in nums2, we want to place it in the merged list. If the element in nums1 is greater, we copy it to the p position in nums1, and then we decrement both p1 (to move it towards the beginning of nums1) and p (to move the pointer in the merged list).

# 3. If the element in nums2 is greater, we copy it to the p position in nums1, and then we decrement both p2 (to move it towards the beginning of nums2) and p (to move the pointer in the merged list). In both cases (whether we copied from nums1 or nums2), we decrement p to move it towards the beginning of the merged list.

# 4 After the loop above finishes, we check if there are any remaining elements in nums2 that were not copied into nums1. If there are remaining elements in nums2, we copy them into nums1 starting from the end of nums1 (at position p) and decrement both p2 and p accordingly.

solution = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)
print(nums1)




# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?