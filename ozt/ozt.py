"""
ex.n=5 a=19 b=2 d=12
a = จำนวนแถวทั้งหมด,b = ระยะห่างระหว่างช่อง or b = n - ( n//2 +1 )
0-4 range n
5-6 ระยะห่าง n,n+b
7-11 range n+b,2*n+b
12-13 ระยะห่าง 2*n + b, 2*n + 2*b
14-18 range 2*n + 2*b,a
"""

n = int(input("Enter : "))
a = (n*3) + (n-1) #Total of Column
b = n//2 #Length for free space
d = 2*n+b #Length that end at z char

for i in range (n):
    for j in range (a):
        if j in range(n):
            if (i + j == n//2 or i + j == n-1+(n//2) or j == i+(n//2) or i == j+(n//2)) :
                print("O",end = "")
            else:
                print(end=" ")

        elif j in range (n,n+b):
            print(end = " ")

        elif j in range(n+b,d):
            if i == 0 or i == n-1:
                print("Z",end = "")
            elif i+j == d-1:
                print("Z",end = "")
            else:
                print(end=" ")  

        elif j in range (d,d+b):
            print(end = " ")

        elif j in range (d+b,a):
            if i == 0:
                print("T",end = "")
            elif j == a-b-1:
                print("T",end = "")
            else:
                print(end=" ")
    print()