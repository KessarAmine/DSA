def mergeOverlappingIntervals(intervals):
    output= []
    if intervals is None or len(intervals) == 0:
        return [[]]
    output.append(intervals[0])
    size = len(intervals)
    for i in range(size):
        if output[len(output) - 1][1] > intervals[i][0]:
            if output[len(output) - 1][1] < intervals[i][1]:
                output[len(output) - 1][1] = intervals[i][1]
            if intervals[i][0] < output[len(output) - 1][0]:
                output[len(output) - 1][0] = intervals[i][0]
        else:
            output.append(intervals[i])
        [print("[Debug] {}".format(i)) for i in output]
    return output
