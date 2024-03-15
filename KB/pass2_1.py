# You are given strings S and C. String S represents a table in CSV (comma-separated values) format, 
# where rows are separated by new line characters (An) and each row consists of one or more fields separated by commas (';). 
# The first row contains the names of the columns. The following rows contain values. 

# For example, the table below is presented by the following string: S = "id,name,age,act,room,depAnl,Jack,68,T,13,8 \n17,Betty,28,F,15,7". 
# id I name  I age I act I room I dep
#  1 I Jack  I 68  1  I  I   13 I   8
# 17 I Betty I 28  I  F  I   15 I   7

# String C is the name of a column in the table described by S that contains only integers. 
# Your task is to find the maximum value in that column. In the example above, for C = "age, the maximum value is 68. 
# Write a function: def solution(S, C) which, given two strings S and C consisting of N and M characters, 
# respectively, returns the maximum value in column C of the table described by S. 

# Examples: 1. Given S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7" and C = "age, 
# your function should return 68 since 68 is the maximum of 68 and 28. 
# id I name  I age I act I room I dep
#  1 I  Jack I 68  1  I  I   13 I   8
# 17 I Betty I 28  I  F  I   15 I   7

# Examples: 2. Given S = "area,land \n3722,CN \n6612,RU \n3855,CA\ n3797,USA" and C = "area", 
# your function should return 6612. 
# area I land
# 3722 I   CN
# 6612 I   RU 
# 3855 I   CA
# 3797 I   USA

# Examples: 3. Given S = 'city,temp2,temp\nParis,7,-3\nDubai,4,-4\nPorto,-1,-2.- and C = "temp", 
# your function should return -2.
# city  I temp2 I temp
# Paris I     7 I   -3
# Dubai I     4 I   -4
# Porto I    -1 I   -2


# S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7"

def solution(a,b):
    sp = a.split("\n")
    split_row = sp[0].split(",")
    index = 0
    for i in split_row:
        if b == i:
            index = split_row.index(i)
    print(index) # 2

    res = []
    for j in range (1,len(sp)):
        res.append(sp[j]) 
    print(res) # ['1,Jack,68,T,13,8', '17,Betty,28,F,15,7']

    res2 = []
    for k in res:
        sp2 = k.split(",")
        res2.append(sp2)
    print(res2) # [['1', 'Jack', '68', 'T', '13', '8'], ['17', 'Betty', '28', 'F', '15', '7']]

    res3 = []
    for l in res2:
        for m in range(len(l)):
            if m == index:
                res3.append(l[m])
    print(res3) # ['68', '28']

    print(max(res3)) # 68

solution("id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7","age")
solution("area,land \n3722,CN \n6612,RU \n3855,CA\ n3797,USA","area")
solution("city,temp2,temp\nParis,7,-3\nDubai,4,-4\nPorto,-1,-2","temp")