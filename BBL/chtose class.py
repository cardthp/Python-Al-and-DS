class Chtose:
    def __init__(self, a, b): 
        self.a = a
        self.b = b
    def chtose1(self, a, b):
        self.res = ""
        if len(self.a)<=len(self.b):
            for i in range (len(self.a)):
                if self.a[i].isupper() and self.b[i].isupper():
                    self.res += self.a[i]
                elif self.a[i].islower() and self.b[i].islower():
                    self.res += self.b[i]
                elif (self.a[i].islower() and self.b[i].isupper()) or (self.a[i].isupper() and self.b[i].islower()):
                    self.res += "$"
                else:
                    self.res += "#"
            return print(self.res) 
        elif len(self.a)>len(self.b):
            for i in range (len(self.b)):
                if self.a[i].isupper() and self.b[i].isupper():
                    self.res += self.a[i]
                elif self.a[i].islower() and self.b[i].islower():
                    self.res += self.b[i]
                elif (self.a[i].islower() and self.b[i].isupper()) or (self.a[i].isupper() and self.b[i].islower()):
                    self.res += "$"
                else:
                    self.res += "#"
            return print(self.res) 


a=input("Enter Target : ")
b=input("Enter Mask : ")

if len(a) > 50:
    print("Target not more than 50 character")
elif len(b) > 50:
    print("Mask not more than 50 character")
else:
    ch = Chtose(a,b)
    ch.chtose1(a,b)