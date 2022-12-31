def sort_array_inc(coins):
    length = len(coins)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if coins[i] > coins[j]:
                temp = coins[i]
                coins[i] = coins[j]
                coins[j] = temp
            j = j + 1
        i = i + 1
        
def get_max(array, largestIndexes, largestValues):
    max = float('-inf')
    index = 0
    i = 0
    while i < len(array):
        if array[i] >= max and i not in largestIndexes:
            max = array[i]
            index = i
        i = i + 1
    largestIndexes.append(index)
    largestValues.append(max)
        
def findThreeLargestNumbers(array):
    largestIndexes = []
    largestValues = []
    while len(largestIndexes) < 3:
        get_max(array, largestIndexes, largestValues)
    sort_array_inc(largestValues)
    return largestValues