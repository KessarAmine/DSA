def firstNonRepeatingCharacter(string):
    charachterFrequencies = {}
    for character in string:
        #create a key if it doesnt exist with 0 as a value, if it does increment its value by one
        charachterFrequencies[character] = charachterFrequencies.get(character, 0) + 1
    for idx in range(len(string)):
        character = string[idx]
        if charachterFrequencies[character] == 1:
            return idx
    return -1
