def finddis(alist):
    a = set(range(1,max(alist)+1))
    b = list(a - set(alist))
    return b

def missingNumber(nums):
    n = len(nums);
    return int(n*(n+1)/2 - sum(nums))   

print(finddis([1,2,3,7,8]))
print(missingNumber([3,0,1]))
