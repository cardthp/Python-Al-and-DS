#1
# Write a function, which checks that provided string is palindrome.

# AABBAA - true
# AAA - true
# AA - true
# A - true
# ABB - false (BAA)
# BAA - false (AAB)
# AAABBA - false
# AAABBB false

# 12345, reverse = 54321 - not same string, false
# 12321, reverse = 12321 - same string, true


#def res1(a):
#    rev = a[::-1] # 123 -> 321 , 123 != 321

#    if a == rev:
#        return print("true")
#        return True
#    else:
#        return print("false")
#        return False
    

#print(res1("AABBAA"))   



#2
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
    #return print("true") 
        
print(res2("ABBA"))
#a = input("Enter:")
#print(res2(a))
        

            
