
def powerset_helper(pointer, choices, input, result):
    choices_copy = choices.copy()
    if pointer < 0:
        result.append(choices_copy)
        return 
    
    choices_copy.append(input[pointer])
    powerset_helper(pointer-1, choices_copy, input, result)
    choices_copy.pop()
    powerset_helper(pointer-1, choices_copy, input, result)


def powerset(inputSet):
    result = []
    inputSet = inputSet[::-1]
    powerset_helper(len(inputSet)-1, [], inputSet, result)
    print(result)
    return result
    



powerset([4,6,8])