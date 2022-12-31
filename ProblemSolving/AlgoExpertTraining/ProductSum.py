#O(N) time | O(level) space
def productSum(array, level = 1):
    sum = 0
    for index in range(0, len(array)):
        if isinstance(array[index], list):
            sum += productSum(array[index], level + 1)
        elif isinstance(array[index], int):
            sum += array[index]
    return sum * level