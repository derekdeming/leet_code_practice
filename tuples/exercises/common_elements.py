
# Common Elements
# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

# Example

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
# output_tuple = common_elements(tuple1, tuple2)
# print(output_tuple)  # Expected output: (4, 5)

def common_elements_(tuple1, tuple2): 
    common = []
    for i in tuple1: 
        for j in tuple2: 
            if i == j: 
                common.append(i)
    return tuple(common)

print(common_elements_(tuple1, tuple2))


#  another solution
def comm_elements(tuple1, tuple2):
    return tuple([x for x in tuple1 if x in tuple2])

print(comm_elements(tuple1, tuple2))


#  another and better solution 
def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

print(common_elements(tuple1, tuple2))


'''
return tuple(set(tuple1) & set(tuple2)) - This line creates two sets from the input tuples using the set() constructor, 
and then computes the set intersection using the & operator. 

The time complexity of creating each set is O(n), where n is the length of the input tuple.
 The time complexity of computing the set intersection is O(min(n,m)), where m is the length of the second input tuple. 
 Since the two input tuples are of equal length, the overall time complexity of the function is O(n). 
 
 The space complexity is also O(n) because the size of the resulting set will be no larger than the size of the 
 smaller of the two input tuples.
'''
