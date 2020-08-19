class pascal:
    def __init__(self,row):
        self.row = row

    def calcu (self):
        if self.row <= 0:
            return [1]

        elif self.row == 1:
            return [1,1]

        elif self.row >= 2:
            self.needrow = self.row - 1
            self.lastrow = [1,1]
            for i in range (0,self.needrow):
                self.newrow = [1]
                for j in range (1,len(self.lastrow)):
                    self.newrow.append(self.lastrow[j-1] + self.lastrow[j]) 
                self.newrow.append(1)
                self.lastrow = self.newrow
            return self.lastrow

a = pascal(5)
print(a.calcu())