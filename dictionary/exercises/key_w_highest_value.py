
# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output:

# b

# hackjob solution
def max_value_key(my_dict):
    max_value = 0
    max_key = None
    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
        
# print(max_value_key(my_dict))


# actual solution 

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

print(max_value_key(my_dict))

# Time Complexity: O(n) where n is the number of key-value pairs in the dictionary
# Space Complexity: O(1) - constant space used in the function