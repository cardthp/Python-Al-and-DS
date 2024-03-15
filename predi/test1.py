import re
data1 = open('predi/aa.txt','r')

# for n in data1:
    # a = n.strip()
    # print(a)
    # print('with')
    # print(a.split())

for i in data1:
    #curren = ['USD']
    #list_out = i.split(' ')
    list_out = i.strip().split(' ')
    list_out_conv = []
    list_out_type = []
    location_float = []
    dict_collect = {}
    list_new = []
    for i in list_out:
        #i.strip()
        try:
            i = float(i)
            list_out_conv.append(i)
            list_out_type.append(type(i))
        
        except:
            list_out_conv.append(i)
            list_out_type.append(type(i))

    #list_out_conv
    # ['abc', 100.0, 'USD.', 'sdfgsdf', '\n']
    # ['safgasgaga', 200.0, 'USD.', 500.0, 'USD.', '\n']
    # ['asdsdad', 300.56, 'USD', 'asdadasd', '\n']
    # ['400.asd', 'USD']
    #list_out_type
    # [<class 'str'>, <class 'float'>, <class 'str'>, <class 'str'>, <class 'str'>]
    # [<class 'str'>, <class 'float'>, <class 'str'>, <class 'float'>, <class 'str'>, <class 'str'>]
    # [<class 'str'>, <class 'float'>, <class 'str'>, <class 'str'>, <class 'str'>]
    # [<class 'str'>, <class 'str'>]

    for k in range(len(list_out_type)):
        if list_out_type[k] == float:
            location_float.append(k)

    #len(list_out_type)
    # 5
    # 6
    # 5
    # 2
    #location_float
    # [1]
    # [1, 3]
    # [1]
    # []

    for j in location_float:
        key=list_out_conv[j+1].strip('').strip('\n').replace('.','').upper()
        if key in dict_collect:
            #dict_collect[list_out_conv[j+1].strip('').strip('\n').replace('.','').upper()] += list_out_conv[j]
            dict_collect[key] += list_out_conv[j]
        else:
            #dict_collect[list_out_conv[j+1].strip('').strip('\n').replace('.','').upper()] = list_out_conv[j]
            dict_collect[key] = list_out_conv[j]

    # for cur in curren: #USD in USD
    #     if cur in dict_collect: #100,700,300.56
    #         print(dict_collect[cur],cur)

    #if key in curren:
            
    #dict_collect
    # {'USD': 100.0}
    # {'USD': 700.0}
    # {'USD': 300.56}

    for key,value in dict_collect.items():
        print(value,key)