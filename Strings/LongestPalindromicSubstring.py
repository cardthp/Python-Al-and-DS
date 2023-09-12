# 5. Longest Palindromic Substring (Medium)
# Input: s = "babad" Output: "bab"
# Explanation: "aba" is also a valid answer.
# Input: s = "cbbd" Output: "bb"
# >> https://www.youtube.com/watch?v=XYQecbcd6_c
# >> ลักษณะการทำ เป็นการไล่ทีละตัว(หลัก) จากนั้นจะขยับออก(ย่อย)พร้อมกันโดยซ้าย-1 ขวา+1 เพื่อเช็คว่าเป็น Palindromic ไหม

def longestPalindrome(s):
    res = ""
    resLength = 0 #กำหนดเพื่อเช็คว่า Palindromic นี้ได้ความยาวเท่าไหร่แล้ว

    for i in range(len(s)):
        #Odd
        left,right = i,i    #เพื่อไล่ทำตัวหลักทีละตัว
        while left >= 0 and right < len(s) and s[left] == s[right]:    #เงื่อนไขตัวสุดท้ายทำเพื่อเช็คตัวย่อยว่าเป็น Palindromic ไหม
            if right-left+1 > resLength:    #เช็คว่าตัวย่อยอันใหม่จำนวนอักษรมันจะมากกว่า Palindromic อันเดิมไหม
                resLength = right-left+1
                res = s[left:right+1]       #เหมือน detectPosition ที่ต้องบวก 1 เพราะจะได้ยึดตามตัวอักษรจริงไม่ใช่ array
            left -= 1       #ขยายขอบเขตไปทางซ้าย
            right += 1      #ขยายขอบเขตไปทางขวา

        #Even
        left,right = i,i+1 #จำนวนคู่ทำเหมือนคี่แต่บวก 1 ไปที่ right
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right-left+1 > resLength:
                resLength = right-left+1
                res = s[left:right+1]
            left -= 1
            right += 1

    return print(res)


longestPalindrome("babad")
longestPalindrome("cbbd")