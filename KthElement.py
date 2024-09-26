
def kthElement(Arr1, Arr2, k):
    sorted_arr=[0]*(len(Arr1) + len(Arr2))
    p=0
    i=0
    j=0

    while (i<len(Arr1) and j<len(Arr2)):
        if Arr1[i]<Arr2[j]:
            sorted_arr[p] = Arr1[i]
            i=i+1
        else:
            sorted_arr[p] = Arr2[j]
            j=j+1
        p=p+1

    while (i<len(Arr1)):
        sorted_arr[p] = Arr1[i]
        p=p+1
        i=i+16

    while (j<len(Arr2)):
        sorted_arr[p] = Arr2[j]
        p=p+1
        j=j+1

    return sorted_arr[k-1]

