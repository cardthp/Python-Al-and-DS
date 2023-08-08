# 20. Valid Parentheses (Easy)
# Input: s = "()[]{}" Output: true
# Input: s = "(]" Output: false
# >> append ค่าด้านหลังเข้าไป จากนั้น pop ออกเพื่อเทียบว่าเท่ากันไหม ถ้าเท่าแสดงว่าเรียงมาถูกต้อง

def isValid(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(')')
        elif i == '[':
            stack.append(']')
        elif i == '{':
            stack.append('}')
        elif not stack or stack.pop() != i: # not stack = empty stack
            return False
    if stack == []:
        return True