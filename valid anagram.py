def validana(a,b):
    if len(a) != len(b):
        return False    
    res = {}
    for i in a:
        if i in res:
            res[i] +=1
        else:
            res[i] = 1

    for j in b:
        if j in res:
            res[j] -= 1
        else:
            return False

    for key,value in res.items():
        if value != 0:
            return False

    return True

def validana2(a,b):
    return sorted(a) == sorted(b)

print(validana('cat','act'))
print(validana2('cat','act'))