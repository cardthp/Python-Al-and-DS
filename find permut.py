def permut(alist, current=0):
    if current == len(alist) - 1:
        print(''.join(alist))
        #print(alist) -> 'A','B','C'


    for i in range(current, len(alist)):
        alist[current],alist[i] = alist[i],alist[current]
        permut(alist, current + 1)
        alist[current],alist[i] = alist[i],alist[current]

permut(list("ABC"))
#permutations('ABC')