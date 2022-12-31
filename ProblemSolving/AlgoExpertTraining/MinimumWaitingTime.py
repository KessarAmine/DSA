def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j] < array[j - 1] and j > 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1
    return array

def minimumWaitingTime(queries):
    queries = insertionSort(queries)
    sum = waitTime = 0
    for time in queries:
        sum += waitTime
        waitTime += time
    return sum
