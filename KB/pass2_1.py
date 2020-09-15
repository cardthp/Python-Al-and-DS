def solution(a,b):
    sp = a.split("\n")
    fir = sp[0].split(",")
    index = 0
    for i in fir:
        if b == i:
            index = fir.index(i)
    print(index)

    res = []
    for j in range (1,len(sp)):
        res.append(sp[j]) 
    print(res)

    res2 = []
    for k in res:
        sp2 = k.split(",")
        res2.append(sp2)
    print(res2)

    res3 = []
    for l in res2:
        for m in range(len(l)):
            if m == index:
                res3.append(l[m])
    print(res3)

    print(max(res3))

solution("id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7","age")    