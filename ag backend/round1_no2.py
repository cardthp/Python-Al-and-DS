# Solution 1
def capi1(a):
    n = len(a)
    if n % 2 != 0:    #Odd number
        res = a[:n-1] + a[n-1].upper()
    else:             #Even number
        res = a.title()
        #res = a.capitalize()
    return print(res)

capi1("hello")
capi1("helloz")

# Solution 2 >> Recommand
def capi2(str1):
    if len(str1) % 2 != 0:   #Odd number
        re = str1[-1].upper()
        re1 = str1[:len(str1)-1]
        re2 = re1+re
    elif len(str1) % 2 == 0: #Even number
        re2 = str1.title()
    return print(re2)

# str1 = input("Enter:").strip()
# capi(str1)
capi2("hey")
capi2("heyz")