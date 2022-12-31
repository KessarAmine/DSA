#worst O(N), O(N)
def firstDuplicateValue(array):
    visited = []
    size = len(array)
    for i in range(size):
        if array[i] not in visited:
            visited.append(array[i])
        else:
            return array[i]
    return -1
