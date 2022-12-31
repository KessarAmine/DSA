def generateDocument(characters, document):
    visited = []
    found = False
    for char in document:
        for i in range(0, len(characters)):
            if characters[i] ==  char and i not in visited:
                visited.append(i)
                found = True
                break
        if found == False:
            return False
        found = False
    return True
