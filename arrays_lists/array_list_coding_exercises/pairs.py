# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. 
# Do not consider commutative pairs.

# Example

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']


# Note:

# 4+3 comes from second and third elements from the main list.

# 3+4 comes from third and seventh elements from the main list.

def pair_sum(myList, sum): 
    # Create an empty hash set 
    result = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(f'{myList[i]}+{myList[j]}')
    return result

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],6))
# ['2+5', '4+3', '3+4', '-2+9']

# Time Complexity: O(n^2)
# - the time complexity of the nested for loop is O(n^2) where n is the length of the input array (myList)
# - for each element in the array, it checks every other element in the array for possible pairs 

# Space complexity: O(n)
# where n is the length of the input array. Additional space used in this function is in the result list, 
# which stores the pairs that add up to the sum. In the worst case, the number of pairs that sum up to the target sum is 
# proportional to the size of the input array 