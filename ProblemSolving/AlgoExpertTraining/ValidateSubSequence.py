def isValidSubsequence(array, sequence):
    visited = []
    for i in sequence:
        if i not in array:
            return False
        for j in range(0, len(array)):
            if array[j] == i and not len(visited):
                visited.append(j)
                break
            elif array[j] == i and j > visited[len(visited) - 1]:
                visited.append(j)
                break
    if len(visited) != len(sequence):
        return False
    return True
