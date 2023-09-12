#This Question have one stack that have 10 element
#pushFirst is push to left side / pushSecond is push to right side
#Stack is FILO
class StackWithTwo:
    def __init__(self, CAPACITY): #CAPACITY is 10 element
        self.CAPACITY = CAPACITY
        self.arr = []

    def pushFirst(self, n):
        if len(self.arr) < self.CAPACITY // 2:
            self.arr.insert(0, n) #insert to left side and move already array to right+1 (normally insert to right side)
        else:
            print("Stack overflow")

    def popFirst(self):
        if self.arr:
            return self.arr.pop(0)
        else:
            print("Stack underflow")
            return None

    def pushSecond(self, n):
        if len(self.arr) < self.CAPACITY // 2:
            self.arr.append(n)
        else:
            print("Stack overflow")

    def popSecond(self):
        if self.arr:
            return self.arr.pop()
        else:
            print("Stack underflow")
            return None

def main():
    s = StackWithTwo(10)
    s.pushFirst(1)  #left side  [1 x x x x x x x x x]
    s.pushFirst(2)  #left side  [2 1 x x x x x x x x]
    s.pushSecond(3) #right side [2 1 x x x x x x x 3]
    print(s.popFirst())  # 2
    print(s.popSecond()) # 3
    print(s.popFirst())  # 1

if __name__ == "__main__":
    main()