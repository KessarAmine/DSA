def allTraversal(matrix):
    height = len(matrix)
    i = 0
    while i < height:
        if matrix[i][0] != float('inf'):
            return -1
        i = i + 1
    return 1
    
def binarySearch(array, target):
    i = int(len(array) / 2)
    while i >= 0 and i < len(array):
        if array[i] == target:
            return i
        if array[i] < target:
            array[i] = float('inf')
            if i != len(array) - 1:
                i = i + 1
        elif array[i] > target:
            array[i] = float('inf')
            if i != 0:
                i = i - 1        
        if array[i] == float('inf'):
            return -1
    return -1
    
def searchInSortedMatrix(matrix, target):
    height = len(matrix)
    width = len(matrix[0])
    visitedLines = []
    i = int(height / 2)
    visitedLines.append(i)
    while i >= 0 and i < height:
        line = matrix[i]
        if i not in visitedLines:
            visitedLines.append(i)
        result = binarySearch(line, target)
        print("line {} is {}".format(i, line))
        if result != -1:
            return [i, result]
        if line[int(width / 2)] < target:
            if i != height - 1:
                i = i + 1
        elif line[int(width / 2)] > target:
            if i != 0:
                i = i - 1      
        if len(visitedLines) == height:
            return [-1, -1]
    return [-1, -1]
    
#===========================================================================================================================================
def allTraversal(matrix):
    height = len(matrix)
    i = 0
    while i < height:
        if matrix[i][0] != float('inf'):
            return -1
        i = i + 1
    return 1
    
def binarySearch(array, target):
    i = int(len(array) / 2)
    while i >= 0 and i < len(array):
        if array[i] == target:
            return i
        if array[i] < target:
            array[i] = float('inf')
            if i != len(array) - 1:
                i = i + 1
        elif array[i] > target:
            array[i] = float('inf')
            if i != 0:
                i = i - 1        
        if array[i] == float('inf'):
            return -1
    return -1
    
def searchInSortedMatrix(matrix, target):
    height = len(matrix)
    i = 0
    while i < height:
        line = matrix[i]
        result = binarySearch(line, target)
        if result != -1:
            return [i, result]
        i = i + 1
    return [-1, -1]
    