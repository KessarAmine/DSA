def get_max(sums):
    max = sums[0]
    i = 1
    for i in range(len(sums)):
        if sums[i] > max:
            max = sums[i]
    return max
	
def get_sum(coins):
    sum = 0
    for i in coins:
        sum += i
    return sum

def nonConstructibleChange(coins):
    sums = []
    i = 0
    max_input = get_sum(coins)
    length = len(coins)
    for i in range(length):
        if coins[i] not in sums:
            sums.append(coins[i])
            sums.append(coins[i] * 2)
        if i == 0:
            j = i + 1
            while j < length:
                subsum = coins[i] + coins[j]
                if subsum not in sums and subsum < max_input:
                    sums.append(subsum)
                j = j + 1
        else:
            for indexSums in range(len(sums)):
                x = i + 1
                while x < length:
                    subsum = sums[x] + coins[x]
                    if subsum not in sums and subsum < max_input:
                        sums.append(subsum)
                    x  = x + 1
    print(sums)
    i = 1
    max = get_max(sums)
    for index in range(max):
        if i not in sums:
            print("the min change is {}".format(i))
            return i
        i = i +1
    return 1
