def capi(str1):
    if len(str1) % 2 != 0:
        re = str1[-1].upper()
        re1 = str1[:len(str1)-1]
        re2 = re1+re
    elif len(str1) % 2 == 0:
        re2 = str1.title()
    return print(re2)

str1 = input("Enter:").strip()
capi(str1)