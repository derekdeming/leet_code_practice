# Common Keys
# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

# Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
# merge_dicts(dict1, dict2)
# Output:

# {'a': 1, 'b': 5, 'c': 7, 'd': 5}

def merge_dicts(dict1, dict2): 
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
        else:
            result[key] = dict1[key]
    for key in dict2:
        if key not in result:
            result[key] = dict2[key]
    return result


# other solution: 

def merge_dicts2(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

print(merge_dicts(dict1, dict2))
# print(merge_dicts2(dict1, dict2))

# Time Complexity: O(n+m) where n is the number of elements in dict1 and m is the number of elements in dict2. 
# the copy method takes O(n) time and the loop iterates m times with O(1) operations inside the loop.