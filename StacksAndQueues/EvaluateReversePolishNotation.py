# 150. Evaluate Reverse Polish Notation (Medium)
# Input: tokens = ["2","1","+","3","*"] Output: 9 Explanation: ((2 + 1) * 3) = 9
# Input: tokens = ["4","13","5","/","+"] Output: 6 Explanation: (4 + (13 / 5)) = 6
# The valid operators are '+', '-', '*', and '/'
# >> เก็บตัวเลขไปก่อนถ้าเจอแล้วค่อยทำตาม symbols (เน้นเรื่องการใส่ int)

def evalRPN(tokens):
    symbols = ['+','-','*','/']
    stacktokens = []
    for i in tokens:
        if i not in symbols:
            stacktokens.append(int(i))
        else:
            b = int(stacktokens.pop())
            a = int(stacktokens.pop())
            if i == '+':
                result = a+b
            elif i == '-':
                result = a-b
            elif i == '*':
                result = a*b
            else:
                result = int(a/b)
            stacktokens.append(result)
        
    return stacktokens[0]

print(evalRPN(["2","1","+","3","*"]))
#print(evalRPN(["18"]))