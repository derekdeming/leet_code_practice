
# Conditional Filter
# Define a function that takes a dictionary as a parameter and returns a dictionary 
# with elements based on a condition.

# new_dict = {new_key:new_value for (key, value) in dict.items() if condition}

# Example:

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
# filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
# Output:

# {'b': 2, 'd': 4}

def filter_dict(my_dict, condition):
    return {key:value for (key, value) in my_dict.items() if condition(key, value)}

print(filter_dict(my_dict, lambda k, v: v % 2 == 0))

# Time Complexity: O(n) where n is the number of key-value pairs in the dictionary
# Space Complexity: O(n) - space used in the function is proportional to the number of key-value pairs in the dictionary