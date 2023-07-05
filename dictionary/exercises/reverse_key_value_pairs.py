
# Reverse Key-Value Pairs
# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

# Example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
# reverse_dict(my_dict)
# Output:

# {1: 'a', 2: 'b', 3: 'c'}

def reverse_dict(my_dict):
    return {value: key for key, value in my_dict.items()}   

print(reverse_dict(my_dict))

# Time Complexity: O(n) where n is the number of key-value pairs in the dictionary
# Space Complexity: O(n) - space used in the function is proportional to the number of key-value pairs in the dictionary