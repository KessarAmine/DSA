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

def fourNumberSum(array, targetSum):
    slopes = []
    sort_array_inc(array)
    size = len(array)
    first = 0
    while first < size - 3:
        second = first + 1
        while second < size - 2:
            third = second + 1
            while third < size - 1:
                fourth = third + 1
                while fourth < size:
                    sum =  array[first] + array[second] + array[third] + array[fourth]
                    if sum > targetSum:
                        break
                    if sum ==  targetSum:
                        slopes.append([array[first], array[second], array[third], array[fourth]])
                    fourth = fourth + 1
                third = third + 1
            second = second + 1
        first = first + 1
    return slopes
