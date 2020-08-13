def mergeSort(alist):
    if len(alist) > 1 :
        mid = len(alist)//2
        L = alist[:mid]
        R = alist[mid:]

        mergeSort(L)
        mergeSort(R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                alist[k] = L[i]
                i += 1
            else:
                alist[k] = R[j]
                j += 1 
            k += 1
        while i < len(L):
            alist[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            alist[k] = R[j]
            j += 1
            k += 1
    return alist

alist = [3,8,7,4,5,1,9,2,6]
mergeSort(alist)
print(alist)