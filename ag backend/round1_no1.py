# Write a function, which checks that provided string is palindrome.

# Solution 1
# AABBAA - true
# AAA - true
# ABB - false (BAA)
# BAA - false (AAB)
# AAABBA - false
# AAABBB false

def res1(a):
    rev = a[::-1] # 123 -> 321 , 123 != 321

    if a == rev:
        return True
    else:
        return False
    
print(res1("AABBAA"))   


# Solution 2
# AABBAA, [A, A, B, B, A, A]
#          ^              ^
#             ^        ^
#                ^  ^
#          0, 1, 2, 3, 4, 5

def res2(a):
    for i in range (len(a)):
        if a[i] != a[len(a) - i - 1]: # 6 - 0 = 6 > 5
            return False
        else:
            return True
        
print(res2("ABBA"))


# Solution 3 >> Recommand
def res3(a):
    start = 0
    end = len(a)-1
    while start < end:
        if a[start] == a[end] :
            return True
        else:
            return False
        
print(res3("ABBA"))