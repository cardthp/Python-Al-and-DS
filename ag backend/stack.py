#Stack is FILO
class minst:
    def __init__(self):
        self.stack = []
    
    def push(self,x):
        self.stack.append(x)

    def getMin(self):
        return min(self.stack)
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1] #the last element of the array

abc = minst()

abc.push(-2) #-2
abc.push(0)  #-2 0
abc.push(-3) #-2 0 -3
print(abc.getMin())  # return -3  #-2 0 -3
abc.pop()            # return -3  #-2 0
print(abc.top())     # return 0   #-2 0
print(abc.getMin())  # return -2  #-2 0


    # StackWithTwo s = new StackWithTwo(10);
    # s.pushFirst(1);
    # s.pushFirst(2);
    # s.pushSecond(3);
    # s.popFirst(); //2
    # s.popSecond(); //3
    # s.popFirst(); //1    