myList = [1,1,8,8,4,5,6,6]
mySet = set()
result = []
for i in myList:
    if i in mySet:
        result.append(i)
        #mySet.remove(i) #if not have will be appare i that have pair already
    else:
        mySet.add(i)

print(result)

a = sorted(result)
print(a)
print(a[-2])
