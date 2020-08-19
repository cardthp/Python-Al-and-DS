def test(InputValue,WinLotto):
    res = ""
    count = 0
    for i in InputValue:
        if i in WinLotto:
            if i != res:
                res += i
            count += 1

    if count > 1:
        return print("Number of win =",res,"It's winner number more than one time it's win =",count,"times")
    else:
        return print("Number of win =",res,"Win 1 time")

a = input("Enter Value want to find : ").split()
b = input("Enter Value win lotto : ")
test(a,b)