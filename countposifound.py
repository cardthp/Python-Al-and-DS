class indposist:
    def __init__(self,s,l):
        self.s = s
        self.l = l

    def ind(self):
        self.a = []
        for i in range (len(self.l)-len(self.s)+1):
            if self.l[i:len(self.s)+i] == self.s:
                self.a.append(i)
        return print(self.a)

a = indposist ("abc","abcasgadfgabc")
a.ind()
