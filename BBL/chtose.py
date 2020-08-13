def chtose(a,b):
    res = ""
    if len(a)<=len(b):
        for i in range(len(a)):
            if a[i].isupper() and b[i].isupper():
                res += a[i]
            elif a[i].islower() and b[i].islower():
                res += b[i]
            elif (a[i].islower() and b[i].isupper()) or (a[i].isupper() and b[i].islower()):
                res += "$"
            else:
                res += "#"
        return print(res)

    elif len(a)>len(b):
        for i in range(len(b)):
            if a[i].isupper() and b[i].isupper():
                res += a[i]
            elif a[i].islower() and b[i].islower():
                res += b[i]
            elif (a[i].islower() and b[i].isupper()) or (a[i].isupper() and b[i].islower()):
                res += "$"
            else:
                res += "#"
        return print(res)

a=input("Enter Target : ")
b=input("Enter Mask : ")
if len(a) > 50:
    print("Target not more than 50 character")
elif len(b) > 50:
    print("Mask not more than 50 character")
else:
    chtose(a,b)

#a="Micro Computer"
#b="C Programming"
#a="SCAAT.th.edu"
#b="IT Exhibition"