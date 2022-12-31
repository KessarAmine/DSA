def multiply(array, index):
    result = 1
    size = len(array)
    for i in range(size):
        if i != index:
            result = (result * array[i])
    return result
    
def arrayOfProducts(array):
    output = []
    size = len(array)
    for i in range(size):
        output.append(multiply(array, i))
    [print(i) for i in output]
    return output