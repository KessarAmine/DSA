def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets

# we double everytime the number of the subsets wich is exponantial 2^N
# Time O(2^N * N)
# Space O(2^N * N)
def powerset(array):
    subsets = [[]]
    powerSetsHelper(array, subsets)
    return subsets

def powerSetsHelper(array, subsets):
    if not len(array):
        return subsets
    elif len(array) == 1:
        if array not in subsets:
            subsets.append(array)
        return subsets
    else:
        for i in range(0, len(array)):
            if [array[i]] not in subsets:
                subsets.append([array[i]])
            if len(subsets) > 1:
                for j in range(1, len(subsets)):
                    sub = subsets[j]
                    if array[i] not in sub and array[i] > sub[len(sub) - 1]:
                        newSubset = subsets[j] + [array[i]]
                        if newSubset not in subsets:
                            subsets.append(newSubset)
                newArray = array[:i] + array[i + 1:]
                powerSetsHelper(newArray, subsets)
