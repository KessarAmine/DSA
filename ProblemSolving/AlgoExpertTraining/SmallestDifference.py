def smallestDifference(arrayOne, arrayTwo):
    size_one =  len(arrayOne)
    size_two =  len(arrayTwo)
    result = []
    min = arrayOne[0] - arrayTwo[0]
    i = 0
    j = 1
    while i < size_one:
        current = arrayOne[i]
        while j < size_two:
            compare = arrayTwo[j]
            differance = current - compare 
            if differance < 0:
                differance = -differance
            if differance == 0:
                result.append(current)
                result.append(compare)
                return (result)
            if differance > min and min < 0:
                left = current
                right = compare
                min = differance
            if differance < min and min > 0:
                left = current
                right = compare
                min = differance
            j = j + 1
        j = 0
        i = i + 1
    result.append(left)
    result.append(right)
    return (result)

#===================================================================================================
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

def smallestDifference(arrayOne, arrayTwo):
    sort_array_inc(arrayOne)
    sort_array_inc(arrayTwo)
    pass
