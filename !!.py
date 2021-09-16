data1 = open('aa.txt','r')

# for n in data1:
#     a = n.strip()
#     print(a)
#     print('with')
#     print(a.split())

for i in data1:
    curren = ['USD']
    list_out = i.split(' ')
    list_out_conv = []
    list_out_type = []
    list_float_num = []
    dict_collect = dict()
    for i in list_out:
        i.strip()

        try:
            i = float(i)
            list_out_conv.append(i)
            list_out_type.append(type(i))
        
        except:
            list_out_conv.append(i)
            list_out_type.append(type(i))

    # ['abc', 100.0, 'USD.', 'sdfgsdf', '\n']
    # ['safgasgaga', 200.0, 'USD.', 500.0, 'USD.', '\n']
    # ['asdsdad', 300.56, 'USD', 'asdadasd', '\n']
    # ['400.asd', 'USD']
    # [<class 'str'>, <class 'float'>, <class 'str'>, <class 'str'>, <class 'str'>]
    # [<class 'str'>, <class 'float'>, <class 'str'>, <class 'float'>, <class 'str'>, <class 'str'>]
    # [<class 'str'>, <class 'float'>, <class 'str'>, <class 'str'>, <class 'str'>]
    # [<class 'str'>, <class 'str'>]

    for k in range(len(list_out_type)):
        if list_out_type[k] == float:
            list_float_num.append(k)
    # 5
    # 6
    # 5
    # 2
    # [1]
    # [1, 3]
    # [1]
    # []

    for j in list_float_num:
        key=list_out_conv[j+1].strip('').strip('\n').replace('.','').upper() #USD #ใช้ regex ดีกว่า
        if key in dict_collect:
            dict_collect[list_out_conv[j+1].strip('').strip('\n').replace('.','').upper()] += list_out_conv[j]
        else:
            dict_collect[list_out_conv[j+1].strip('').strip('\n').replace('.','').upper()] = list_out_conv[j]

    print(dict_collect)
    # for cur in curren: #USD in USD
    #     if cur in dict_collect: #100,700,300.56
    #         print(dict_collect[cur],cur)
    #         #200,USD