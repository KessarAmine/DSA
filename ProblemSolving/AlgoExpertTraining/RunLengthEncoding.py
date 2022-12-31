def runLengthEncoding(string):
    result = ""
    count = 1
    for i in range(0, len(string)):
        
        if i == len(string) - 1:
            if string[i] == string[i - 1]:
                result += str(count) + string[i]
            else:
                result += str(1) + string[i]
            break
            
        if string[i] == string[i + 1]:
            if count == 9:
                result += str(count) + string[i]
                count = 0
            count += 1
        else:
            result += str(count) + string[i]
            count = 1
    return result