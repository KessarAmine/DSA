def is_array_inc(coins):
    length = len(coins)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if coins[i] > coins[j]:
                return False
            j = j + 1
        i = i + 1
    return True

def is_array_dec(coins):
    length = len(coins)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if coins[i] < coins[j]:
                return False
            j = j + 1
        i = i + 1
    return True

def isMonotonic(array):
    if len(array) <= 2:
        return True
    if (is_array_dec(array) == False and is_array_inc(array) == False):
        return False
    if (is_array_dec(array) == True or is_array_inc(array) == True):
        return True
    else:
        return True
