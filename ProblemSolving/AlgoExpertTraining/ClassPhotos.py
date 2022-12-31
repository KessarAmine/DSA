def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j] < array[j - 1] and j > 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1
    return array
    
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights = insertionSort(redShirtHeights)
    blueShirtHeights = insertionSort(blueShirtHeights)
    redInFront = -1
    for i in range(0, len(redShirtHeights)):
        if (redShirtHeights[i] < blueShirtHeights[i]):
            if redInFront == 1:
                return False
            else:
                redInFront = 0
        elif (redShirtHeights[i] > blueShirtHeights[i]):
            if redInFront == 0:
                return False
            else:
                redInFront = 1
        else:
            return False
    return True
