import re
data1 = open('aa.txt','r').readlines()
#find1 = re.findall("\d+.\d+ USD",data1)
for i in data1: 
    sum = 0
    find1 = re.findall("[0-9]+.[0-9]+ USD",i)
    for j in find1:
        find2 = j.split(" USD")[0]
        sum += float(find2)
    print(sum,"USD")

