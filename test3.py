class StackWithTwo:  
    def __init__(self, n):
        self.size = n 
        self.arr = [''] * n 
        self.top1 = -1
        self.top2 = self.size         
    def pushFirst(self, x): 
        if self.top1 < self.top2 - 1 : 
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x 
        else: 
            print("Stack is full") 
    def pushSecond(self, x): 
        if self.top1 < self.top2 - 1: 
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x 
        else : 
           print("Stack is full") 
    def popFirst(self): 
        if self.top1 >= 0: 
            x = self.arr[self.top1] 
            self.top1 = self.top1 -1
            return x 
        else: 
            print("Stack is empty") 
    def popSecond(self): 
        if self.top2 < self.size: 
            x = self.arr[self.top2] 
            self.top2 = self.top2 + 1
            return x 
        else: 
            print("Stack is empty") 

if __name__ == "__main__":
    st = StackWithTwo(10)
    st.pushFirst(1) 
    st.pushFirst(2) 
    st.pushSecond(3) 
    print("Pop value in Stack First is" ,st.popFirst()) 
    print("Pop value in Stack Second is",st.popSecond())
    print("Pop value in Stack First is",st.popFirst()) 