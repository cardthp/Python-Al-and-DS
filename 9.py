n = int(input("Enter:"))

a = [['.']*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j]="*"
        elif j == n // 2 or i == n // 2:
            a[i][j]="*"
        elif j == n-1-i:
            a[i][j]="*"
        print(a[i][j],end=" ")
    print()
        