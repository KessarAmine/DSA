#peaks[[indexP1, valueP2], [...]]
def get_highest(peaks):
    size = len(peaks)
    maxPeak = peaks[0]
    i = 1
    while i < size:
        if peaks[i][1] > maxPeak[1]:
            maxPeak = peaks[i]
        i = i + 1
    return maxPeak

def get_start(peaks, peakValue, size, array, peakIndex):
    i = 0
    if size == 1:
        j = peakIndex
        while j > 0:
            if array[j] <= array[j - 1]:
                return j - 1
            j = j - 1
        return j - 1
    else:
        while i < size:
            if peaks[i][1] == peakValue:
                return peaks[i - 1][0]
            i = i + 1

def get_end(array, peakIndex, size):
    i = peakIndex
    while i < size - 1:
        if array[i + 1] > array[i]:
            return i
        i = i + 1
    return i
    
def longestPeak(array):
    if len(array) > 0:
        size = len(array)
        start_points = []
        peaks = []
        i = 0
        for i in range(size):
            if i == 0:
            #at start we start either from bot or top or same level
            #start from top
                if array[i] >= array[i + 1] and array[i - 1] is None:
                    continue;
            # elif array[i] < array[i - 1]:
            #     start_points.append(i)
            elif i < size - 1 and array[i + 1] < array[i] and array[i] > array[i - 1]:
                peaks.append([i, array[i]])
        if len(peaks) == 0:
            return 0
        maxPeak = get_highest(peaks)
        start = get_start(peaks, maxPeak[1], len(peaks), array, maxPeak[0])
        end = get_end(array, maxPeak[0], size)
        [print(i) for i in peaks]
        print("start point is {}/ End point is {}".format(start, end))
        if start == 0:
            result = end - start + 1
        else:
            result = end - start
        print("result is {}".format(result))
        return result 
    return 0