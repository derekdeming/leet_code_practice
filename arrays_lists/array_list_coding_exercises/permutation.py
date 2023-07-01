# permutation 

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    else: 
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False

print(permutation([1,2,3], [3,2,1]))