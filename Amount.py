def amount_helper(A, start, result, remainder, combo):
    combo_copy = combo.copy()
    if(remainder == 0):
        result.append(combo_copy)
        return
    elif(remainder <0):
        return
    for i in range(start, len(A)):
        if i > start and A[i] == A[i-1]:
            continue
        amount_helper(A, i+1, result, remainder - A[i], combo_copy + [A[i]])

def amount(A, S):
    A.sort()
    result = []
    amount_helper(A, 0, result, S, [])
    result = result[::-1]
    return(result)

