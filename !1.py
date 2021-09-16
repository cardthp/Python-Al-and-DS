def test(InputValue,WinLotto):

    a=[]
    b={}
    c={}

    for i in InputValue:
        if i in WinLotto:
            a.append(i)
    
    for j in a:
        if j in b:
            b[j] += 1
        else:
            b[j] = 1
    
    for key,value in b.items():
        if value > 1:
            c[key] = value

    if c:
        for key,value in c.items():
            print("no : {} and value : {}".format(key,value))
    else:
        print("NO")

InputValue = [int(item) for item in input("Enter Value want to find : ").split()] 
WinLotto = [int(item) for item in input("Enter Value win lotto : ").split()] 

test(InputValue,WinLotto)
# test([2,3],[3])