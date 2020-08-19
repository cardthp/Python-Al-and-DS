def solve1(alist):
    a = sorted(set(alist))[::-1]
    return a[1]

def solve2(alist):
    a = set(alist)
    b = list(a)
    b.remove(max(b))
    return max(b)

alist = [5,7,8,3,5]
print (solve1(alist))
print (solve2(alist))

  
#new_list = set(list1) 
#new_list.remove(max(new_list)) 
#print(max(new_list))     