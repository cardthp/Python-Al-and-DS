def bubberSort(alist):
    for pname in range(len(alist)-1,0,-1):
        for i in range (pname):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

alist = [3,8,7,4,5,1]
bubberSort(alist)
print(alist)