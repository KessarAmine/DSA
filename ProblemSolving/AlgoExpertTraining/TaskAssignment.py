def getMax(array, indexes):
    max = [array[0], 0]
    i = 1
    while i < len(array):
        if array[i] >= max[0] and i not in indexes:
            max = [array[i], i]
        i += 1
    if max[1] in indexes:
        #make max the last element left
        max = getLast(array, indexes)
    return max
    
def getMin(array, indexes):
    min = [array[0], 0]
    i = 1
    while i < len(array):
        if array[i] <= min[0] and i not in indexes:
            min = [array[i], i]
        i += 1
    if min[1] in indexes:
        #make min the last element left
        min = getLast(array, indexes)
    return min
    
def getLast(array, indexes):
    for i in range(0, len(array)):
        if i not in indexes:
            return [array[i], i]

def taskAssignment(k, tasks):
    indexes = []
    result = []
    for i in range(0, k):
        max = getMax(tasks, indexes)
        indexes.append(max[1])
        min = getMin(tasks, indexes)
        indexes.append(min[1])
        result.append([max[1], min[1]])
    return result
