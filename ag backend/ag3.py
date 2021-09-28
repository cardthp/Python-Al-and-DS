def dup(l,s):
    res = []
    a = False
    for i in l:
        if i in s:
            res.append(i)
            a = True
    return res,a

l = [1,2,3,4,5,6,7,8,9,0] 
s = [4,10,5,1]
#s = [11,12]

print(dup(l,s))