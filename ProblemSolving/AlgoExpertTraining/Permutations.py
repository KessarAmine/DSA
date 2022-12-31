# Space O(N*N!)
# Time O(N*N!)
# Swaping positions 
def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations

def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:]) #array[:] make a copy view
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i] #swap
            permutationsHelper(i + 1, array, permutations)
            array[i], array[j] = array[j], array[i] #swap

# Space O(N*N!)
# Time O(N^2*N!)
# Creating new arrays by slicing eacch time
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, perm, perms):
    # if the array is empty perm becomes empty and will be appended to perms which is not right, so we check for len(perm)
    if not len(array) and len(perm):
        perms.append(perm) #O(N!)
    else:
        for i in range(len(array)):
            # the way er remove the i element is by slicing for the start - > i and then from i + 1 -> the end of the array (skip i)
            newArray = array[:i] + array[i + 1:] #O(N)
            # we create a list that will be the concat of the currentPerm and our Current elem which is Int not list so we do [int]
            newPerm = perm + [array[i]] #O(N)
            permutationsHelper(newArray, newPerm, perms)

# Arrays can store data very compactly and are more efficient for storing large amounts of data.
# import numpy as np

# def getPermutations(array):
#     permutations = np.array([])
#     permutationsHelper(array, np.array([]), permutations)
#     return permutations

# def permutationsHelper(array, perm, perms):
#     # if the array is empty perm becomes empty and will be appended to perms which is not right, so we check for len(perm)
#     if not len(array) and len(perm):
#         np.append(perms, perm)#O(N!)
#     else:
#         for i in range(len(array)):
#             # the way er remove the i element is by slicing for the start - > i and then from i + 1 -> the end of the array (skip i)
#             newArray = np.array(array[:i] + array[i + 1:])#O(N)
#             # we create a list that will be the concat of the currentPerm and our Current elem which is Int not list so we do [int]
#             newPerm = np.array(perm + [array[i]])#O(N)
#             permutationsHelper(newArray, newPerm, perms)