from collections import Counter
def test(InputValue,WinLotto):
    res = []
    res2 = {}
    res3 = {}
    for i in InputValue:
        if i in WinLotto:
            res.append(i)

    #a = Counter(res)
    for j in res: 
        if j in res3: 
            res3[j] += 1
        else: 
            res3[j] = 1

    #for key,value in a.items():
    for key,value in res3.items():
        if value > 1:
            res2[key] = value
    
    if res2: #check if res == True
        for key, value in res2.items(): 
            print ("Number of win = {} Count of win = {}".format(key, value))
    else:
        print("no number is won more than once")


InputValue = input("Enter Value want to find : ").split()
WinLotto = input("Enter Value win lotto : ").split()
test(InputValue,WinLotto)