stack1,stack2 = [],[]

def pushFirst(in1):
    if len(stack1) + len(stack2) <= 10:
        stack1.append(in1)
        #print("Stack 1 : ",stack1)
    else:
        print("Stack is full")

def popFirst():
    a = stack1.pop()
    print("Pop value in Stack First is : ",a)

def pushSecond(in2):
    if len(stack1) + len(stack2) <= 10:
        stack2.append(in2)
        #print("Stack 2 : ",stack2)
    else:
        print("Stack is full")

def popSecond():
    b = stack2.pop()
    print("Pop value in Stack Second is : ",b)

pushFirst('1')
pushFirst('2')
pushSecond('3')

popFirst()
popSecond()
popFirst()