mylist = [1,1,2,5]
result = []
for i in mylist:
    if i in result:
        result.remove(i)
    else:
        result.append(i)

print(result)
print(result.pop())
    
