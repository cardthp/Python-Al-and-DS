def insectionSort(alist):
    for i in range(1,len(alist)):
        CurrentV = alist[i]
        posi = i
        while posi > 0 and alist[posi-1] > CurrentV:
            alist[posi] = alist[posi-1]
            posi = posi - 1
        alist[posi] = CurrentV

alist = [3,8,7,4,5,1]
insectionSort(alist)
print(alist)