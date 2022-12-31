#Average O(log(n)) | time, O(1) space
#Worst O(N) time | O(1) space

def smallest_backward(array, i):
    j = i - 1
    while j >= 0:
        if array[i] <= array[j]:
            return False
        j = j - 1
    return True

def smallest_forward(array, i):
    j = i + 1
    while j < len(array):
        if array[i] == array[j] and i == j + 1:
            continue
        if array[i] > array[j]:
            return False
        j = j + 1
    return True

def subarraySort(array):
    start = -1
    end = -1
    for i in range(len(array)):
        if smallest_forward(array, i) == False and start == -1:
            start = i
            break
    i = len(array)
    while i > 0:
        if smallest_backward(array, i - 1) == False and start != -1:
            end = i - 1
            break
        i = i - 1
    return [start, end]
#==================================================================================================================================
#smallest forward gets the start
#smallest bakward gets the end 
def get_end(array, i):
    last = -1
    j = i + 1
    while j < len(array):
        if array[i] == array[j] and i == j + 1:
            continue
        if array[i] >= array[j]:
            last = j
        j = j + 1
    return last

def smallest_forward(array, i):
    j = i + 1
    while j < len(array):
        if array[i] == array[j] and i == j + 1:
            continue
        if array[i] > array[j]:
            return False
        j = j + 1
    return True
    
def subarraySort(array):
    start = -1
    end = -1
    for i in range(len(array)):
        if smallest_forward(array, i) == False:
            start = i
            end = get_end(array, i)
            break
    return [start, end]
