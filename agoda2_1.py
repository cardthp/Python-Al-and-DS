def capi(a):
    n = len(a)
    if n % 2 != 0:
        res = a[:n-1] + a[n-1].upper()
    else:
        res = a.title()
        #res = a.capitalize()
    return res

print(capi("card"))
print(capi("cardz"))