def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j] < array[j - 1] and j > 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1
    return array