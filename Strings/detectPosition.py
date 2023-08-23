#detect position of string when found
def detectPosition(l,s):
    position = []
    for i in range (len(l)-len(s)+1): #ลบกันบวก 1 เพื่อให้วนครบจนหมด
        if l[i:len(s)+i] == s:        #ขยับค่า i ไปเรื่อยๆจนกว่าจะเจอ
            position.append(i)
    return print(position)

detectPosition('abcasgadfgabc','abc')


#Optinal : Find String
def findstring(string,sub_string):
    cnt = 0
    for i in range (len(string)-len(sub_string)+1):   #ลบกันบวก 1 เพื่อให้วนครบจนหมด
        if string[i:len(sub_string)+i] == sub_string: #ขยับค่า i ไปเรื่อยๆจนกว่าจะเจอ
            cnt += 1
    return print(cnt)

findstring('ABACABA','ABA')