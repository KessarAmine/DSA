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
    
def threeNumberSum(array, targetSum):
    tuples = []
    sort_array_inc(array)
    i =  0
    size = len(array)
    while i < size:
        j = i + 1
        while j < size:
            z = j + 1
            while z < size:
                if array[i] +  array[j] +  array[z] == targetSum:
                    print("hm")
                    tuple = [array[i], array[j], array[z]]
                    tuples.append(tuple)
                z = z +1
            j = j + 1
        i = i + 1
    return(tuples)
    