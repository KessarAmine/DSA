def spiralTraverse(array):
    sol = []
    while array:
        sol += array.pop(0)
        array = list(zip(*array))[::-1]
    return sol