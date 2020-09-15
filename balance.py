def check(myStr): 
    a = []
    openlist = ["[","{","("] 
    closelist = ["]","}",")"]  
    for i in myStr: 
        if i in openlist: 
            a.append(i) 
        elif i in closelist: 
            pos = closelist.index(i) 
            if len(a) > 0 and openlist[pos] == a[len(a)-1]: 
                a.pop() 
            else: 
                return "Unbalanced"
    if len(a) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
  
print(check("{()}"))
print(check("{[]{()}}"))
print(check("[{}{})(]"))
print(check("()"))