def isinstring(str1):
    a = "card"
    #a = list("card")
    ind = 0
    for i in str1:
        if ind == len(a):
            break
        if i == a[ind]:
            ind += 1
    if ind == len(a):
        return print("YES")
    else:
        return print("NO")

isinstring("cegahrld")