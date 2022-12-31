def bubbleSort(array):
    length = len(array)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            j = j + 1
        i = i + 1
    return array