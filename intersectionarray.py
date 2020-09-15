def inter(num1,num2):
    a = {}
    res = []
    for i in num1:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    for j in num2:
        if j in a:
            if a[j] != 0:
                res.append(j)
                a[j] -= 1

    return res

#num1 = (int(i) for i in input("Enter1:").split())
#num2 = (int(i) for i in input("Enter2:").split())
num1 = [4,9,5] 
num2 = [9,4,9,8,4]
print(inter(num1,num2))
