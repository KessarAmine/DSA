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

def sort_array_dec(coins):
    length = len(coins)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if coins[i] < coins[j]:
                temp = coins[i]
                coins[i] = coins[j]
                coins[j] = temp
            j = j + 1
        i = i + 1

def get_max(sums):
    max = sums[0]
    i = 1
    for i in range(len(sums)):
        if sums[i] > max:
            max = sums[i]
    return max

def get_min(sums):
    min = sums[0]
    i = 1
    for i in range(len(sums)):
        if sums[i] < min:
            min = sums[i]
    return min

def swap_toend(array, start, end, toMove):
    while array[end] == toMove and end > start:
        end = end - 1
    temp = array[start]
    array[start] = array[end]
    array[end] = temp
    
def moveElementToEnd(array, toMove):
    if not array:
        return (array)
    if get_min(array) == toMove:
        sort_array_dec(array)
        return(array)
    if get_max(array) == toMove:
        sort_array_inc(array)
        return(array)
    size = len(array)
    j = size - 1
    i = 0
    while i < size:
        if array[i] == toMove:
            swap_toend(array, i, j, toMove)
        i = i + 1
    return(array)
