def phoneNumberMnemonics(phoneNumber):
    table = {1: "1",    2: "abc", 3: "def",
             4: "ghi",  5: "jkl", 6: "mno",
             7: "pqrs", 8: "tuv", 9: "wxyz",
             0: "0"}
    inputs = []
    for char in phoneNumber:
        possibleRepresentation = table.get(int(char))
        inputs.append(possibleRepresentation)
    results = combinationsHelper(inputs,  [[]])
    return results

def combinationsHelper(inputs, results):
    print("======================================================================")
    print("[Data]...")
    if len(inputs) == 0:
        output = []
        for res in results:
            newStr = ""
            for char in res:
                newStr = newStr + char
            output.append(str(newStr))
        print("[Output...]\nResults = {}".format(output))
        return output
    currentInput = inputs[0]
    newResults = []
    # run throught results per array
    print("results {}\ncurrentInput: {}".format(results, currentInput))
    for result in results:
        # run through current input per character append each element to result array
        for char in currentInput:
            # append new results
            newResults.append(result + [char])
    print("[Results]\nresults at {}:\n {}".format(currentInput, newResults))
    # remove the currentInput from the inputs
    newInputs = inputs[:0] + inputs[1:]
    # recursion call with newInputs and newResults
    results = combinationsHelper(newInputs, newResults)
    # at the end of the call stack we return outputs which is the result but to get the result to our real output on the main thread
    # we have to save the result of the call then return it
    return results