def reverse_string(x):
  return x[::-1]

def semordnilap(words):
    result = []
    setWords = {""}
    for currentWord in words:
        setWords.add(currentWord)
        for compareWord in words:
            if compareWord not in setWords and reverse_string(compareWord) == currentWord:
                result.append([currentWord, compareWord])
    return result