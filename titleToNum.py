def titleToNumber(str1):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = {}
    for i in range(26):
        a[LETTERS[i]] = i + 1 #maps = {'A': 1, 'B': 2, 'C': 3 -- > 'X': 24, 'Y': 25, 'Z': 26}  
            
    col = 0 
    for j in str1:
        col = 26*col + a[j]
        
    return col

print(titleToNumber('AB'))
print(titleToNumber('BB'))