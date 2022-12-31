def binarySearch(array, target):
    i = int(len(array) / 2)
    while i >= 0 and i < len(array):
        if array[i] == target:
            print(i)
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