def test(InputValue,WinLotto):
    res = []
    for i in InputValue:
        if i in WinLotto:
            res.append(i)
    return res

def bonus(alist): 
    res2 = {} 
    for j in alist: 
        if j in res2: 
            res2[j] += 1
        else: 
            res2[j] = 1
  
    #print (res2.items()) #dict_items([(222, 2), (333, 2)])
    for key, value in res2.items(): 
        print ("Number of win = {} Count of win = {}".format(key, value))

InputValue = [111,222,222,333,333]
WinLotto = [222,333] 
c = test(InputValue,WinLotto)
bonus(c) 

#a = input("Enter Value want to find : ").split()
#b = input("Enter Value win lotto : ")


