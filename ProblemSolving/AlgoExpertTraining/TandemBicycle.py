def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j] < array[j - 1] and j > 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1
    return array
    
def insertionSortDec(array):
    for i in range(1, len(array)):
        j = i
        while array[j] > array[j - 1] and j > 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        i += 1
    return array
        
def getMax(redShirtSpeeds, blueShirtSpeeds):
    maximum = 0
    size = len(redShirtSpeeds)
    i = 0
    print(redShirtSpeeds)
    print(blueShirtSpeeds)
    while i < size:
        tandemSpeed = max(redShirtSpeeds[i], blueShirtSpeeds[i])
        maximum += tandemSpeed
        i += 1
    return maximum
    
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds = insertionSort(redShirtSpeeds)
    if fastest == True:
        blueShirtSpeeds = insertionSortDec(blueShirtSpeeds)
        return getMax(redShirtSpeeds, blueShirtSpeeds)
    blueShirtSpeeds = insertionSort(blueShirtSpeeds)
    return getMax(redShirtSpeeds, blueShirtSpeeds)
