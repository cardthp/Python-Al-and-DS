# 125. Valid Palindrome (Easy)
# Input: s = "A man, a plan, a canal: Panama" Output: true
# Input: s = " " Output: true

def isPalindrome(s: str) -> bool:
    a = ''.join([i for i in s if i.isalnum()]).lower()
    # b = a[::-1]

    # if a == b:
    #     return True
    # else:
    #     return False

    left = 0
    right = len(a)-1
    while left < right:
        if a[left] == a[right]:
            left+=1
            right-=1
        else:
            return False
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))