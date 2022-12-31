def twoNumberSum(array, targetSum):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if i != j and array[i] + array[j] == targetSum:
                return [array[i], array[j]]         
    return []
