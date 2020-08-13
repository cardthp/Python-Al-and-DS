def findstring(string,sub_string):
    a = 0
    for i in range (len(string)-len(sub_string)+1):
        if string[i:len(sub_string)+i] == sub_string:
            a += 1
    return a

b = findstring('ABACABA','ABA')
print(b)
