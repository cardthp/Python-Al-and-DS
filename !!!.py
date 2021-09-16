import re
data1 = open('aa.txt','r').read()
find1 = re.findall("\d+\.\d+ USD",data1)
#re.findall("\d+\.*\d* USD", text)
for i in find1:
    print(i)
