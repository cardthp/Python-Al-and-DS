data1 = open('aa.txt','r')
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

    for k in range(len(list_out_type)):
        if list_out_type[k] == float:
            list_float_num.append(k)

    for j in list_float_num:
        key=list_out_conv[j+1].strip('').strip('\n').replace('.','')

        if key in dict_collect:
            dict_collect[list_out_conv[j+1].strip('').strip('\n').replace('.','')] += list_out_conv[j]
        else:
            dict_collect[list_out_conv[j+1].strip('').strip('\n').replace('.','')] = list_out_conv[j]

    for cur in curren:
        if cur in dict_collect:
            print(dict_collect[cur],cur)