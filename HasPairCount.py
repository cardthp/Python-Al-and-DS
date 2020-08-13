def me(alist):
    keys = set(alist) 
    answer = 0 
    for i in keys: 
        if alist.count(i) > len(alist) / 2: 
            answer = i 
            #break 
    return answer

alist = [2,2,1,1,1,2,2]
print(me(alist))
