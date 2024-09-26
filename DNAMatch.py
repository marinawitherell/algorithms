
def dna_match_topdown_helper(DNA1, DNA2, m, n, cache):

    if m==0 or n==0:
        return 0
    
    if cache[m][n] != -1:
        return cache[m][n]
    
    if DNA1[m-1] == DNA2[n-1]:
        cache[m][n] = 1 + dna_match_topdown_helper(DNA1, DNA2, m-1, n-1, cache)
        return cache[m][n]
    
    cache[m][n] = max(dna_match_topdown_helper(DNA1, DNA2, m, n-1, cache), dna_match_topdown_helper(DNA1, DNA2, m-1, n, cache))
    return cache[m][n]

def dna_match_topdown(DNA1, DNA2):
    m = len(DNA1)
    n = len(DNA2)
    cache = [[-1 for x in range(n+1)] for x in range(m+1)]

    return dna_match_topdown_helper(DNA1 ,DNA2, m, n, cache)



def dna_match_bottomup(DNA1, DNA2):
    m = len(DNA1)
    n = len(DNA2)
    cache = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                cache[i][j] = 0
            elif DNA1[i-1] == DNA2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])
    
    return cache[m][n]


    

