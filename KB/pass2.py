def solutions(S, C):
    list_column = list()
    list_data = list()
    list_raw = S.split("\n")

    print("1.list_raw : ",list_raw)

    for i in range(0, len(list_raw)):
        if i == 0:
            list_column.append(list_raw[i])
        else:
            list_data.append(list_raw[i])

    print("2.list_column : ",list_column)
    print("2.list_data : ",list_data)

    list_sep_column = list_column[0].split(",")

    print("3.list_sep_column : ",list_sep_column)

    list_sep_data = list()
    
    for data in list_data:
        sep_data = data.split(",")
        list_sep_data.append(sep_data)

    print("3.list_sep_data : ",list_sep_data)
    
    index_of_column = list()
    list_max_age = list()
    
    for k in range(0, len(list_sep_column)):
        if list_sep_column[k] == C:
            index_of_column.append(k)

    print("4.index_of_column : ",index_of_column)
            
    for l in list_sep_data:
        for m in range(0, len(l)):
            if index_of_column[0] == m:
                list_max_age.append(l[m])

    print("4.list_max_age : ",list_max_age)               
    
    res = max(list_max_age)
    return res
          

x="id,age\n1,23\n2,24"
y="age"

print(solutions(x,y))