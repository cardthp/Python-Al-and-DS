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
        return self.stack[-1]

abc = minst()

abc.push(-2)
abc.push(0)
abc.push(-3)
print(abc.getMin()) # return -3
abc.pop()
print(abc.top())    # return 0
print(abc.getMin()) # return -2