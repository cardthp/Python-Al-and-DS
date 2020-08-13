def selectionSort(alist):
    for i in range (len(alist)):
        posiMin = i
        for j in range (i+1,len(alist)):
            if alist[j] < alist[posiMin]:
                posiMin = j
        alist[i],alist[posiMin] = alist[posiMin],alist[i]

alist = [3,8,7,4,5,1]
selectionSort(alist)
print(alist)