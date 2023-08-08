# 242. Valid Anagram (Easy)
# Input: s = "anagram", t = "nagaram"
# Output: true
# เก็บข้อมูลใน dict แล้วเทียบ

def isAnagram(s, t):
    a = {}
    b = {}
    for i in s:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    for j in t:
        if j in b:
            b[j] += 1
        else:
            b[j] = 1
    
    if a == b:
        return True
    else:
        return False


print(isAnagram('anagram','nagaram'))